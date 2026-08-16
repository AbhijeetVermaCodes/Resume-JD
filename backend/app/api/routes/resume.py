import uuid
from typing import Optional
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.schema_models import ResumeRecord
from app.parsers.resume_parser import ResumeParser
from app.services.ats_checker import ATSChecker
from app.schemas.matcher_schemas import ResumeUploadResponse

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload", response_model=ResumeUploadResponse)
async def upload_resume(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None),
    db: Session = Depends(get_db),
):
    """
    Upload resume via PDF, DOCX, TXT file or paste raw text.
    Extracts text, segments structured sections, and generates preliminary ATS health metrics.
    """
    raw_text = ""
    filename = None
    file_type = "manual"

    if file:
        filename = file.filename
        file_bytes = await file.read()
        if len(file_bytes) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is empty. Please upload a valid PDF, DOCX, or TXT document."
            )
        try:
            raw_text, structured_data = ResumeParser.parse_file(file_bytes, filename=filename or "")
            file_type = (filename or "").split(".")[-1].lower() if "." in (filename or "") else "file"
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Error parsing resume file: {str(e)}"
            )
    elif text and text.strip():
        raw_text = text.strip()
        file_type = "text_paste"
        try:
            structured_data = ResumeParser.parse_raw_text(raw_text)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Error processing resume text: {str(e)}"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please provide a resume file (PDF, DOCX, TXT) or paste resume text."
        )

    if not raw_text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No readable text found in the provided resume."
        )

    # Evaluate preliminary ATS score
    ats_eval = ATSChecker.evaluate(raw_text, structured_data, file_type=file_type)

    # Save to DB
    record_id = str(uuid.uuid4())
    record = ResumeRecord(
        id=record_id,
        filename=filename,
        file_type=file_type,
        raw_text=raw_text,
        structured_data=structured_data.model_dump(),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return ResumeUploadResponse(
        id=record.id,
        filename=filename,
        file_type=file_type,
        raw_text=raw_text,
        structured_data=structured_data,
        ats_preliminary_score=ats_eval.score,
        message="Resume uploaded and structured successfully."
    )


@router.delete("/{resume_id}", status_code=status.HTTP_200_OK)
def delete_resume(resume_id: str, db: Session = Depends(get_db)):
    """
    Privacy compliant resume deletion.
    Permanently removes the resume record and all associated analysis results from the database.
    """
    record = db.query(ResumeRecord).filter(ResumeRecord.id == resume_id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resume record not found.")
    
    db.delete(record)
    db.commit()
    return {"message": f"Resume {resume_id} and all associated data permanently deleted."}
