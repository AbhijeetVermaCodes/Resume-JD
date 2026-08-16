import uuid
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.config import ScoringWeights
from app.models.schema_models import ResumeRecord, JobDescriptionRecord, AnalysisRecord
from app.parsers.resume_parser import ResumeParser
from app.parsers.jd_parser import JDParser
from app.services.ats_checker import ATSChecker
from app.services.llm_service import get_llm_provider
from app.services.scoring_engine import ScoringEngine
from app.schemas.matcher_schemas import (
    AnalysisRequest,
    AnalysisResponse,
    ResumeStructure,
    JDStructure,
)

router = APIRouter(prefix="/analyze", tags=["Analyze"])


@router.post("", response_model=AnalysisResponse)
def analyze_resume_and_jd(
    request: AnalysisRequest,
    db: Session = Depends(get_db),
):
    """
    Core Match & Analysis Endpoint.
    Compares CV against JD using semantic understanding, ATS evaluation,
    transparent weighted scoring, gap analysis, and actionable improvement generation.
    """
    raw_resume = ""
    raw_jd = ""
    resume_struct: Optional[ResumeStructure] = None
    jd_struct: Optional[JDStructure] = None
    resume_id = request.resume_id
    jd_id = request.job_description_id

    # 1. Fetch or parse Resume
    if resume_id:
        resume_record = db.query(ResumeRecord).filter(ResumeRecord.id == resume_id).first()
        if not resume_record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resume {resume_id} not found.")
        raw_resume = resume_record.raw_text
        resume_struct = ResumeStructure(**resume_record.structured_data) if resume_record.structured_data else ResumeParser.parse_raw_text(raw_resume)
    elif request.resume_text and request.resume_text.strip():
        raw_resume = request.resume_text.strip()
        resume_struct = ResumeParser.parse_raw_text(raw_resume)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please provide a valid resume_id or resume_text."
        )

    # 2. Fetch or parse Job Description
    if jd_id:
        jd_record = db.query(JobDescriptionRecord).filter(JobDescriptionRecord.id == jd_id).first()
        if not jd_record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job Description {jd_id} not found.")
        raw_jd = jd_record.raw_text
        jd_struct = JDStructure(**jd_record.structured_data) if jd_record.structured_data else JDParser.parse_raw_text(raw_jd)
    elif request.job_description_text and request.job_description_text.strip():
        raw_jd = request.job_description_text.strip()
        jd_struct = JDParser.parse_raw_text(raw_jd)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please provide a valid job_description_id or job_description_text."
        )

    # 3. Evaluate ATS Quality
    ats_compatibility = ATSChecker.evaluate(raw_resume, resume_struct)

    # 4. Perform Semantic LLM / Heuristic Analysis
    provider = get_llm_provider()
    analysis_raw = provider.analyze(
        resume_data=resume_struct,
        jd_data=jd_struct,
        raw_resume=raw_resume,
        raw_jd=raw_jd,
    )

    skills_result = analysis_raw["skills"]
    experience_gap = analysis_raw["experience_gap"]
    side_by_side = analysis_raw["side_by_side"]
    strengths = analysis_raw["strengths"]
    critical_gaps = analysis_raw["critical_gaps"]
    recommendations = analysis_raw["recommendations"]
    missing_kw_recs = analysis_raw["missing_keyword_recommendations"]

    # 5. Build Configurable Scoring Weights
    custom_weights = None
    if request.custom_weights:
        custom_weights = ScoringWeights(**request.custom_weights.model_dump(exclude_unset=True))

    overall_score, estimated_prob, category_scores, weights_used, final_assessment = ScoringEngine.calculate_scores(
        resume=resume_struct,
        jd=jd_struct,
        skills_result=skills_result,
        ats_result=ats_compatibility,
        critical_gaps=critical_gaps,
        custom_weights=custom_weights,
    )

    # 6. Save Analysis Result to DB
    analysis_id = str(uuid.uuid4())
    record = AnalysisRecord(
        id=analysis_id,
        resume_id=resume_id,
        job_description_id=jd_id,
        overall_score=overall_score,
        estimated_screening_probability=estimated_prob,
        category_scores=category_scores.model_dump(),
        skills_analysis=skills_result.model_dump(),
        experience_gap=[eg.model_dump() for eg in experience_gap],
        ats_compatibility=ats_compatibility.model_dump(),
        strengths=strengths,
        critical_gaps=[cg.model_dump() for cg in critical_gaps],
        recommendations=[r.model_dump() for r in recommendations],
        side_by_side=[s.model_dump() for s in side_by_side],
        final_assessment=final_assessment.model_dump(),
        scoring_weights_used=weights_used,
    )
    db.add(record)
    db.commit()

    return AnalysisResponse(
        id=analysis_id,
        resume_id=resume_id,
        job_description_id=jd_id,
        overall_score=overall_score,
        estimated_screening_probability=estimated_prob,
        category_scores=category_scores,
        scoring_weights_applied=weights_used,
        skills=skills_result,
        experience_gap=experience_gap,
        ats_compatibility=ats_compatibility,
        strengths=strengths,
        critical_gaps=critical_gaps,
        recommendations=recommendations,
        missing_keyword_recommendations=missing_kw_recs,
        side_by_side=side_by_side,
        final_assessment=final_assessment,
        provider_used=type(provider).__name__,
    )


@router.get("/{analysis_id}", response_model=AnalysisResponse)
def get_analysis_by_id(analysis_id: str, db: Session = Depends(get_db)):
    """
    Retrieve previously calculated analysis report by ID.
    """
    record = db.query(AnalysisRecord).filter(AnalysisRecord.id == analysis_id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Analysis record not found.")

    return AnalysisResponse(
        id=record.id,
        resume_id=record.resume_id,
        job_description_id=record.job_description_id,
        overall_score=record.overall_score,
        estimated_screening_probability=record.estimated_screening_probability,
        category_scores=record.category_scores,
        scoring_weights_applied=record.scoring_weights_used,
        skills=record.skills_analysis,
        experience_gap=record.experience_gap,
        ats_compatibility=record.ats_compatibility,
        strengths=record.strengths,
        critical_gaps=record.critical_gaps,
        recommendations=record.recommendations,
        missing_keyword_recommendations=[],
        side_by_side=record.side_by_side,
        final_assessment=record.final_assessment,
        provider_used="Saved Analysis",
    )
