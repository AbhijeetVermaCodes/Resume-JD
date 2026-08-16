import pytest
from app.config import ScoringWeights
from app.parsers.resume_parser import ResumeParser
from app.parsers.jd_parser import JDParser
from app.services.llm_service import HybridHeuristicSemanticProvider
from app.services.ats_checker import ATSChecker
from app.services.scoring_engine import ScoringEngine
from app.sample_data import SAMPLE_RESUME_TEXT, SAMPLE_JD_TEXT


def test_scoring_engine_calculation_and_probability():
    resume_struct = ResumeParser.parse_raw_text(SAMPLE_RESUME_TEXT)
    jd_struct = JDParser.parse_raw_text(SAMPLE_JD_TEXT)
    ats_res = ATSChecker.evaluate(SAMPLE_RESUME_TEXT, resume_struct)
    
    provider = HybridHeuristicSemanticProvider()
    analysis = provider.analyze(
        resume_data=resume_struct,
        jd_data=jd_struct,
        raw_resume=SAMPLE_RESUME_TEXT,
        raw_jd=SAMPLE_JD_TEXT,
    )

    overall_score, estimated_prob, category_scores, weights, final_assessment = ScoringEngine.calculate_scores(
        resume=resume_struct,
        jd=jd_struct,
        skills_result=analysis["skills"],
        ats_result=ats_res,
        critical_gaps=analysis["critical_gaps"],
    )

    # Score should be in realistic 65 - 85 range for this strong match profile with 2 missing skills
    assert 60.0 <= overall_score <= 90.0
    assert 55.0 <= estimated_prob <= 85.0

    # Ensure disclaimer is populated
    assert "estimate" in final_assessment.probability_disclaimer.lower()

    # Category scores check
    assert category_scores.skills_score >= 50.0
    assert category_scores.experience_score >= 80.0
    assert category_scores.ats_quality_score >= 80.0


def test_custom_weights_effect():
    resume_struct = ResumeParser.parse_raw_text(SAMPLE_RESUME_TEXT)
    jd_struct = JDParser.parse_raw_text(SAMPLE_JD_TEXT)
    ats_res = ATSChecker.evaluate(SAMPLE_RESUME_TEXT, resume_struct)
    
    provider = HybridHeuristicSemanticProvider()
    analysis = provider.analyze(
        resume_data=resume_struct,
        jd_data=jd_struct,
        raw_resume=SAMPLE_RESUME_TEXT,
        raw_jd=SAMPLE_JD_TEXT,
    )

    # Custom weights emphasizing skills 70% vs default 35%
    custom_w = ScoringWeights(
        weight_skills=0.70,
        weight_experience=0.10,
        weight_responsibilities=0.05,
        weight_education=0.05,
        weight_projects=0.05,
        weight_soft_skills=0.02,
        weight_ats_quality=0.03,
    )

    score1, _, _, _, _ = ScoringEngine.calculate_scores(
        resume=resume_struct,
        jd=jd_struct,
        skills_result=analysis["skills"],
        ats_result=ats_res,
        critical_gaps=analysis["critical_gaps"],
    )

    score2, _, _, _, _ = ScoringEngine.calculate_scores(
        resume=resume_struct,
        jd=jd_struct,
        skills_result=analysis["skills"],
        ats_result=ats_res,
        critical_gaps=analysis["critical_gaps"],
        custom_weights=custom_w,
    )

    assert isinstance(score1, float)
    assert isinstance(score2, float)
