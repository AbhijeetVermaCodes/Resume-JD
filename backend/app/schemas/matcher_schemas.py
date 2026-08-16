from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


# -------------------------------------------------------------
# Structured Resume & JD Schemas
# -------------------------------------------------------------

class ContactInfo(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None


class ResumeSection(BaseModel):
    title: str
    content: str
    items: List[str] = Field(default_factory=list)


class ResumeStructure(BaseModel):
    candidate_name: Optional[str] = None
    contact_info: ContactInfo = Field(default_factory=ContactInfo)
    professional_summary: Optional[str] = None
    skills: List[str] = Field(default_factory=list)
    work_experience: List[Dict[str, Any]] = Field(default_factory=list)
    projects: List[Dict[str, Any]] = Field(default_factory=list)
    education: List[Dict[str, Any]] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    achievements: List[str] = Field(default_factory=list)
    raw_sections: Dict[str, str] = Field(default_factory=dict)
    detected_hazards: List[str] = Field(default_factory=list)


class JDStructure(BaseModel):
    job_title: Optional[str] = None
    company_name: Optional[str] = None
    required_skills: List[str] = Field(default_factory=list)
    preferred_skills: List[str] = Field(default_factory=list)
    programming_languages: List[str] = Field(default_factory=list)
    frameworks: List[str] = Field(default_factory=list)
    cloud_technologies: List[str] = Field(default_factory=list)
    databases: List[str] = Field(default_factory=list)
    tools_and_devops: List[str] = Field(default_factory=list)
    required_years_experience: Optional[float] = None
    educational_requirements: List[str] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    responsibilities: List[str] = Field(default_factory=list)
    domain_knowledge: List[str] = Field(default_factory=list)
    soft_skills: List[str] = Field(default_factory=list)


# -------------------------------------------------------------
# Upload & Parse Responses
# -------------------------------------------------------------

class ResumeUploadResponse(BaseModel):
    id: str
    filename: Optional[str] = None
    file_type: str
    raw_text: str
    structured_data: ResumeStructure
    ats_preliminary_score: int
    message: str = "Resume processed successfully"


class JDUploadResponse(BaseModel):
    id: str
    raw_text: str
    structured_data: JDStructure
    message: str = "Job description processed successfully"


# -------------------------------------------------------------
# Detailed Matching Schemas
# -------------------------------------------------------------

class SkillMatchItem(BaseModel):
    name: str
    category: str = "General"  # Language, Framework, Cloud, Database, Tool, Soft Skill
    status: str  # strong, partial, missing
    importance: str  # critical, important, nice-to-have
    is_required: bool = True
    reason: str
    resume_evidence: Optional[str] = None


class SkillsAnalysisResult(BaseModel):
    strong_matches: List[SkillMatchItem] = Field(default_factory=list)
    partial_matches: List[SkillMatchItem] = Field(default_factory=list)
    missing: List[SkillMatchItem] = Field(default_factory=list)
    total_required: int = 0
    matched_required: int = 0
    total_preferred: int = 0
    matched_preferred: int = 0
    overall_skill_score: float = 0.0


class ExperienceGapItem(BaseModel):
    jd_requirement: str
    resume_evidence: str
    match_type: str  # Strong, Partial, Missing, Weak
    importance: str  # Critical, Important, Nice-to-have
    notes: Optional[str] = None


class ATSIssueItem(BaseModel):
    severity: str  # high, medium, low
    rule: str
    description: str
    fix_tip: str


class ATSCompatibilityResult(BaseModel):
    score: int
    status: str  # Excellent (85-100), Good (70-84), Warning (50-69), Critical (<50)
    issues: List[ATSIssueItem] = Field(default_factory=list)
    passed_checks: List[str] = Field(default_factory=list)
    formatting_summary: Dict[str, Any] = Field(default_factory=dict)


class ImprovementItem(BaseModel):
    section: str
    original_snippet: str
    recommended_rewrite: str
    why: str
    cautionary_note: str = "Only add this claim if you genuinely performed this work."


class MissingKeywordRecommendation(BaseModel):
    keyword: str
    importance: str
    where_to_add: str
    advice: str
    cautionary_note: str = "Only add a keyword if you genuinely have experience with it."


class SideBySideItem(BaseModel):
    jd_requirement: str
    resume_evidence: str
    match_status: str  # strong, partial, missing
    match_badge: str  # 🟢 Strong, 🟡 Partial, 🔴 Missing
    importance: str
    notes: str


class CriticalGapItem(BaseModel):
    priority: str  # High, Medium, Low
    requirement: str
    gap_description: str
    impact_level: str


class FinalAssessmentResult(BaseModel):
    overall_score: float
    estimated_screening_probability: float
    probability_disclaimer: str = (
        "This is an automated estimate based solely on the provided CV and Job Description. "
        "Actual hiring and ATS results depend on external variables including total applicant volume, "
        "recruiter keyword filters, candidate pool competitiveness, interview performance, work authorization, "
        "and company-specific criteria."
    )
    match_category: str  # 🟢 Strong Match (80–100), 🟡 Moderate Match (60–79), 🟠 Weak Match (40–59), 🔴 Poor Match (0–39)
    recommendation_verdict: str  # "Ready to Apply", "Apply after targeted improvements", "Significant revision needed"
    why_matches_summary: str
    biggest_weaknesses: List[str] = Field(default_factory=list)
    priority_keywords_to_add: List[str] = Field(default_factory=list)
    is_qualified_verdict: str
    what_to_change_before_applying: List[str] = Field(default_factory=list)


# -------------------------------------------------------------
# Overall Analysis Request & Response
# -------------------------------------------------------------

class CustomScoringWeights(BaseModel):
    weight_skills: Optional[float] = None
    weight_experience: Optional[float] = None
    weight_responsibilities: Optional[float] = None
    weight_education: Optional[float] = None
    weight_projects: Optional[float] = None
    weight_soft_skills: Optional[float] = None
    weight_ats_quality: Optional[float] = None


class AnalysisRequest(BaseModel):
    resume_id: Optional[str] = None
    job_description_id: Optional[str] = None
    resume_text: Optional[str] = None
    job_description_text: Optional[str] = None
    custom_weights: Optional[CustomScoringWeights] = None


class CategoryScores(BaseModel):
    skills_score: float
    experience_score: float
    responsibilities_score: float
    education_score: float
    projects_score: float
    soft_skills_score: float
    ats_quality_score: float


class AnalysisResponse(BaseModel):
    id: str
    resume_id: Optional[str] = None
    job_description_id: Optional[str] = None
    overall_score: float
    estimated_screening_probability: float
    category_scores: CategoryScores
    scoring_weights_applied: Dict[str, float]
    skills: SkillsAnalysisResult
    experience_gap: List[ExperienceGapItem]
    ats_compatibility: ATSCompatibilityResult
    strengths: List[str]
    critical_gaps: List[CriticalGapItem]
    recommendations: List[ImprovementItem]
    missing_keyword_recommendations: List[MissingKeywordRecommendation]
    side_by_side: List[SideBySideItem]
    final_assessment: FinalAssessmentResult
    provider_used: str = "Hybrid AI Engine"
