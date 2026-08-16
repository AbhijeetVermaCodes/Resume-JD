import re
from typing import Dict, List, Any, Optional, Tuple
from app.config import ScoringWeights
from app.schemas.matcher_schemas import (
    ResumeStructure,
    JDStructure,
    CategoryScores,
    SkillsAnalysisResult,
    ATSCompatibilityResult,
    FinalAssessmentResult,
    CriticalGapItem,
    SideBySideItem,
)

# Helper type alias
TupleScores = Tuple[float, float, CategoryScores, Dict[str, float], FinalAssessmentResult]


class ScoringEngine:
    """
    Transparent, explainable scoring engine.
    Calculates weighted match score (0-100), estimated ATS shortlist screening probability (0-100%),
    and generates the final assessment verdict.
    """

    @classmethod
    def calculate_scores(
        cls,
        resume: ResumeStructure,
        jd: JDStructure,
        skills_result: SkillsAnalysisResult,
        ats_result: ATSCompatibilityResult,
        critical_gaps: List[CriticalGapItem],
        custom_weights: Optional[ScoringWeights] = None,
    ) -> TupleScores:
        weights = (custom_weights or ScoringWeights()).normalized_dict()

        # 1. Skills Score (0 - 100)
        skills_score = float(skills_result.overall_skill_score)

        # 2. Experience Match Score (0 - 100)
        experience_score = cls._compute_experience_score(resume, jd)

        # 3. Responsibilities Match Score (0 - 100)
        responsibilities_score = cls._compute_responsibilities_score(resume, jd)

        # 4. Education & Certifications Score (0 - 100)
        education_score = cls._compute_education_score(resume, jd)

        # 5. Projects & Achievements Score (0 - 100)
        projects_score = cls._compute_projects_score(resume, jd)

        # 6. Soft Skills Score (0 - 100)
        soft_skills_score = cls._compute_soft_skills_score(resume, jd)

        # 7. ATS Quality Score (0 - 100)
        ats_quality_score = float(ats_result.score)

        # Compute Overall Weighted Match Score
        weighted_sum = (
            (skills_score * weights.get("weight_skills", 0.35)) +
            (experience_score * weights.get("weight_experience", 0.20)) +
            (responsibilities_score * weights.get("weight_responsibilities", 0.15)) +
            (education_score * weights.get("weight_education", 0.10)) +
            (projects_score * weights.get("weight_projects", 0.10)) +
            (soft_skills_score * weights.get("weight_soft_skills", 0.05)) +
            (ats_quality_score * weights.get("weight_ats_quality", 0.05))
        )
        overall_score = round(max(0.0, min(100.0, weighted_sum)), 1)

        # Estimated ATS Shortlist Screening Probability (0 - 100)
        estimated_prob = cls._compute_screening_probability(
            overall_score=overall_score,
            skills_score=skills_score,
            ats_score=ats_quality_score,
            critical_gaps=critical_gaps,
        )

        category_scores = CategoryScores(
            skills_score=skills_score,
            experience_score=experience_score,
            responsibilities_score=responsibilities_score,
            education_score=education_score,
            projects_score=projects_score,
            soft_skills_score=soft_skills_score,
            ats_quality_score=ats_quality_score,
        )

        # Final Assessment
        final_assessment = cls._build_final_assessment(
            overall_score=overall_score,
            estimated_prob=estimated_prob,
            category_scores=category_scores,
            skills_result=skills_result,
            critical_gaps=critical_gaps,
            ats_result=ats_result,
        )

        return overall_score, estimated_prob, category_scores, weights, final_assessment

    @classmethod
    def _compute_experience_score(cls, resume: ResumeStructure, jd: JDStructure) -> float:
        # Check required years
        jd_req_years = jd.required_years_experience or 3.0
        
        # Estimate candidate years from work experience dates
        candidate_years = 0.0
        if resume.work_experience:
            candidate_years = len(resume.work_experience) * 1.5  # Base estimate: ~1.5 yrs per role
            
            # Look for year ranges in duration
            for exp in resume.work_experience:
                dur = exp.get("duration", "")
                years = [int(y) for y in re.findall(r"\b(20\d{2}|19\d{2})\b", dur)]
                if len(years) >= 2:
                    diff = max(years) - min(years)
                    if diff > 0:
                        candidate_years = max(candidate_years, float(diff))

        if candidate_years >= jd_req_years:
            score = 100.0
        else:
            ratio = candidate_years / max(1.0, jd_req_years)
            score = max(50.0, min(95.0, ratio * 100))

        return round(score, 1)

    @classmethod
    def _compute_responsibilities_score(cls, resume: ResumeStructure, jd: JDStructure) -> float:
        if not jd.responsibilities:
            return 85.0

        resume_exp_text = resume.raw_sections.get("experience", "").lower()
        if not resume_exp_text:
            return 50.0

        matched_count = 0
        for resp in jd.responsibilities:
            # Extract key nouns and action verbs
            words = [w.lower() for w in re.findall(r"\b[A-Za-z]{4,}\b", resp) if w.lower() not in ["with", "have", "from", "team", "work", "will", "must"]]
            if words:
                overlap = sum(1 for w in words if w in resume_exp_text)
                if overlap / len(words) >= 0.3:
                    matched_count += 1

        ratio = matched_count / len(jd.responsibilities) if jd.responsibilities else 0.8
        return round(max(40.0, min(100.0, ratio * 100)), 1)

    @classmethod
    def _compute_education_score(cls, resume: ResumeStructure, jd: JDStructure) -> float:
        score = 80.0
        edu_text = resume.raw_sections.get("education", "").lower()
        
        # Degree matching
        has_degree = bool(re.search(r"(bachelor|master|b\.s|m\.s|b\.tech|m\.tech|phd|degree)", edu_text))
        has_cs = bool(re.search(r"(computer|science|software|information|engineering|technology)", edu_text))

        if has_degree and has_cs:
            score = 100.0
        elif has_degree:
            score = 90.0
        elif resume.education:
            score = 85.0
        else:
            score = 65.0

        # Certifications bonus
        if resume.certifications:
            score = min(100.0, score + 5.0)

        return round(score, 1)

    @classmethod
    def _compute_projects_score(cls, resume: ResumeStructure, jd: JDStructure) -> float:
        if resume.projects:
            count = len(resume.projects)
            if count >= 3:
                return 95.0
            elif count >= 1:
                return 88.0
        # If work experience is very strong, substitute projects
        if len(resume.work_experience) >= 2:
            return 82.0
        return 65.0

    @classmethod
    def _compute_soft_skills_score(cls, resume: ResumeStructure, jd: JDStructure) -> float:
        raw_lower = (resume.professional_summary or "" + " " + resume.raw_sections.get("experience", "")).lower()
        if not jd.soft_skills:
            return 85.0
        
        matched = 0
        for s in jd.soft_skills:
            if s.lower() in raw_lower:
                matched += 1

        ratio = matched / max(1, len(jd.soft_skills))
        return round(max(60.0, min(100.0, 70.0 + (ratio * 30.0))), 1)

    @classmethod
    def _compute_screening_probability(
        cls,
        overall_score: float,
        skills_score: float,
        ats_score: float,
        critical_gaps: List[CriticalGapItem],
    ) -> float:
        # Base probability is derived from match score and ATS parseability
        base = (overall_score * 0.75) + (ats_score * 0.25)
        
        # Penalties for critical gaps
        high_gaps = sum(1 for g in critical_gaps if g.priority == "High")
        penalty = min(25.0, high_gaps * 6.0)

        prob = max(10.0, min(95.0, base - penalty))
        return round(prob, 1)

    @classmethod
    def _build_final_assessment(
        cls,
        overall_score: float,
        estimated_prob: float,
        category_scores: CategoryScores,
        skills_result: SkillsAnalysisResult,
        critical_gaps: List[CriticalGapItem],
        ats_result: ATSCompatibilityResult,
    ) -> FinalAssessmentResult:
        if overall_score >= 80:
            category = "🟢 Strong Match (80–100)"
            verdict = "Ready to Apply with Minor Polish"
            qual_verdict = "Strongly Qualified: Candidate profile closely aligns with core role requirements."
        elif overall_score >= 60:
            category = "🟡 Moderate Match (60–79)"
            verdict = "Apply After Making Targeted Improvements"
            qual_verdict = "Generally Qualified: Good foundational overlap with a few notable technical or keyword gaps."
        elif overall_score >= 40:
            category = "🟠 Weak Match (40–59)"
            verdict = "Substantial Revision Recommended Before Applying"
            qual_verdict = "Partially Qualified: Several mandatory technologies or experience requirements are missing."
        else:
            category = "🔴 Poor Match (0–39)"
            verdict = "Significant Skill Gap / Redesign Required"
            qual_verdict = "Under-Qualified for Target Role: Major misalignment in core stack and prerequisites."

        # Summary of why matches
        why_summary = (
            f"Resume achieves an overall match score of {overall_score}/100 and an estimated screening probability of {estimated_prob}%. "
            f"Demonstrates solid proficiency across {len(skills_result.strong_matches)} verified technical domains, "
            f"with an ATS compatibility score of {ats_result.score}/100."
        )

        weaknesses = []
        for g in critical_gaps[:3]:
            weaknesses.append(f"{g.requirement}: {g.gap_description}")
        if ats_result.issues:
            weaknesses.append(f"ATS Formatting: {ats_result.issues[0].description}")

        priority_keywords = [m.name for m in skills_result.missing if m.is_required][:5]
        if not priority_keywords and skills_result.partial_matches:
            priority_keywords = [p.name for p in skills_result.partial_matches][:3]

        checklist = [
            "Incorporate genuine work metrics (e.g. [X% improvement], [X users]) into your experience bullets.",
            "Verify all technical keywords are mentioned in both the Skills section and contextual project bullets.",
            "Ensure linear ATS single-column formatting without nested complex tables.",
            "Tailor your Professional Summary to highlight the job's core technical requirements.",
        ]

        return FinalAssessmentResult(
            overall_score=overall_score,
            estimated_screening_probability=estimated_prob,
            match_category=category,
            recommendation_verdict=verdict,
            why_matches_summary=why_summary,
            biggest_weaknesses=weaknesses or ["No major red flags detected."],
            priority_keywords_to_add=priority_keywords,
            is_qualified_verdict=qual_verdict,
            what_to_change_before_applying=checklist,
        )
