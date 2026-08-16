import os
from typing import Dict
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class ScoringWeights(BaseModel):
    weight_skills: float = Field(default=0.35, ge=0.0, le=1.0, description="Skill & Technical Keyword Match (35%)")
    weight_experience: float = Field(default=0.20, ge=0.0, le=1.0, description="Experience & Seniority Match (20%)")
    weight_responsibilities: float = Field(default=0.15, ge=0.0, le=1.0, description="Responsibilities & Domain Match (15%)")
    weight_education: float = Field(default=0.10, ge=0.0, le=1.0, description="Education & Certifications Match (10%)")
    weight_projects: float = Field(default=0.10, ge=0.0, le=1.0, description="Projects & Achievements Match (10%)")
    weight_soft_skills: float = Field(default=0.05, ge=0.0, le=1.0, description="Soft Skills & Collaboration (5%)")
    weight_ats_quality: float = Field(default=0.05, ge=0.0, le=1.0, description="Resume Quality & ATS Compatibility (5%)")

    def normalized_dict(self) -> Dict[str, float]:
        raw = self.model_dump()
        total = sum(raw.values())
        if total == 0:
            return {k: 1.0 / len(raw) for k in raw}
        return {k: round(v / total, 4) for k, v in raw.items()}


class Settings(BaseSettings):
    app_name: str = "AI Resume & JD Matcher API"
    app_version: str = "1.0.0"
    debug: bool = False
    database_url: str = "sqlite:///./resume_matcher.db"
    
    # LLM configurations
    llm_provider: str = "auto"  # auto, gemini, openai, heuristic
    gemini_api_key: str = ""
    openai_api_key: str = ""
    llm_api_key: str = ""  # Generic fallback
    llm_model: str = "gemini-2.5-flash"

    # Default weights
    default_weights: ScoringWeights = ScoringWeights()

    # Limits
    max_upload_size_bytes: int = 10 * 1024 * 1024  # 10MB

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()

# Sync fallback keys if set
if not settings.gemini_api_key and settings.llm_api_key and "AIza" in settings.llm_api_key:
    settings.gemini_api_key = settings.llm_api_key
if not settings.openai_api_key and settings.llm_api_key and settings.llm_api_key.startswith("sk-"):
    settings.openai_api_key = settings.llm_api_key
