import uuid
from typing import Optional
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.schema_models import JobDescriptionRecord
from app.parsers.jd_parser import JDParser
from app.schemas.matcher_schemas import JDUploadResponse

router = APIRouter(prefix="/job-description", tags=["Job Description"])


@router.post("/upload", response_model=JDUploadResponse)
async def upload_job_description(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None),
    db: Session = Depends(get_db),
):
    """
    Upload Job Description via PDF, DOCX, TXT file or paste raw text.
    Extracts structured requirements: Required vs Preferred skills, Experience years, Education, and Tech entities.
    """
    raw_text = ""
    if file:
        filename = file.filename
        file_bytes = await file.read()
        if len(file_bytes) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded Job Description file is empty."
            )
        try:
            raw_text, structured_data = JDParser.parse_file(file_bytes, filename=filename or "")
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Error parsing Job Description file: {str(e)}"
            )
    elif text and text.strip():
        raw_text = text.strip()
        try:
            structured_data = JDParser.parse_raw_text(raw_text)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Error processing Job Description text: {str(e)}"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please provide a Job Description file or paste the JD text."
        )

    if not raw_text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No readable text found in the provided Job Description."
        )

    # Save to DB
    record_id = str(uuid.uuid4())
    record = JobDescriptionRecord(
        id=record_id,
        title=structured_data.job_title,
        company=structured_data.company_name,
        raw_text=raw_text,
        structured_data=structured_data.model_dump(),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return JDUploadResponse(
        id=record.id,
        raw_text=raw_text,
        structured_data=structured_data,
        message="Job Description parsed and structured successfully."
    )
