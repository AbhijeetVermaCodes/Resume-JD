import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Float, DateTime, JSON, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class ResumeRecord(Base):
    __tablename__ = "resumes"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    filename = Column(String(255), nullable=True)
    file_type = Column(String(50), nullable=True)  # pdf, docx, txt, manual
    raw_text = Column(Text, nullable=False)
    structured_data = Column(JSON, nullable=True)  # sections, contact, ats_hazards
    created_at = Column(DateTime, default=datetime.utcnow)

    analyses = relationship("AnalysisRecord", back_populates="resume", cascade="all, delete-orphan")


class JobDescriptionRecord(Base):
    __tablename__ = "job_descriptions"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=True)
    company = Column(String(255), nullable=True)
    raw_text = Column(Text, nullable=False)
    structured_data = Column(JSON, nullable=True)  # required_skills, preferred_skills, etc.
    created_at = Column(DateTime, default=datetime.utcnow)

    analyses = relationship("AnalysisRecord", back_populates="job_description", cascade="all, delete-orphan")


class AnalysisRecord(Base):
    __tablename__ = "analyses"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    resume_id = Column(String(36), ForeignKey("resumes.id", ondelete="CASCADE"), nullable=True)
    job_description_id = Column(String(36), ForeignKey("job_descriptions.id", ondelete="CASCADE"), nullable=True)
    
    overall_score = Column(Float, nullable=False)
    estimated_screening_probability = Column(Float, nullable=False)
    
    category_scores = Column(JSON, nullable=False)
    skills_analysis = Column(JSON, nullable=False)
    experience_gap = Column(JSON, nullable=False)
    ats_compatibility = Column(JSON, nullable=False)
    strengths = Column(JSON, nullable=False)
    critical_gaps = Column(JSON, nullable=False)
    recommendations = Column(JSON, nullable=False)
    side_by_side = Column(JSON, nullable=False)
    final_assessment = Column(JSON, nullable=False)
    scoring_weights_used = Column(JSON, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    resume = relationship("ResumeRecord", back_populates="analyses")
    job_description = relationship("JobDescriptionRecord", back_populates="analyses")


class WeightConfigRecord(Base):
    __tablename__ = "weight_configs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    weights = Column(JSON, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
