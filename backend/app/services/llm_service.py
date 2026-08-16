import json
import logging
import re
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Tuple

from app.config import settings
from app.parsers.jd_parser import JDParser
from app.schemas.matcher_schemas import (
    ResumeStructure,
    JDStructure,
    SkillMatchItem,
    SkillsAnalysisResult,
    ExperienceGapItem,
    SideBySideItem,
    CriticalGapItem,
    ImprovementItem,
    MissingKeywordRecommendation,
    FinalAssessmentResult,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Technical Taxonomy & Synonym Knowledge Graph
# ---------------------------------------------------------------------------

SYNONYM_MAP = {
    "amazon web services": "aws",
    "aws": "aws",
    "google cloud platform": "gcp",
    "google cloud": "gcp",
    "gcp": "gcp",
    "microsoft azure": "azure",
    "azure": "azure",
    "k8s": "kubernetes",
    "kubernetes": "kubernetes",
    "postgres": "postgresql",
    "postgresql": "postgresql",
    "js": "javascript",
    "javascript": "javascript",
    "ts": "typescript",
    "typescript": "typescript",
    "golang": "go",
    "go": "go",
    "restful apis": "rest apis",
    "rest api": "rest apis",
    "rest apis": "rest apis",
    "ci/cd": "ci/cd",
    "continuous integration": "ci/cd",
    "nextjs": "next.js",
    "next.js": "next.js",
    "nodejs": "node.js",
    "node.js": "node.js",
    "reactjs": "react",
    "react.js": "react",
    "react": "react",
}

# Related technology clusters (category, item -> siblings)
RELATED_TECH_CLUSTERS = {
    "kafka": {
        "siblings": ["rabbitmq", "activemq", "sqs", "pulsar", "eventbridge", "zeromq"],
        "category": "Message Broker / Event Streaming",
        "partial_reason": "Resume demonstrates experience with message queuing systems through {found}, but {target} is not explicitly mentioned.",
    },
    "rabbitmq": {
        "siblings": ["kafka", "activemq", "sqs", "pulsar"],
        "category": "Message Broker",
        "partial_reason": "Resume demonstrates experience with messaging technologies through {found}, but {target} is not explicitly mentioned.",
    },
    "kubernetes": {
        "siblings": ["docker", "docker swarm", "ecs", "nomad", "containerd", "podman", "helm"],
        "category": "Container Orchestration",
        "partial_reason": "Resume shows containerization background ({found}), but production {target} cluster orchestration is not explicitly documented.",
    },
    "docker": {
        "siblings": ["podman", "containerd", "kubernetes"],
        "category": "Containers",
        "partial_reason": "Candidate has container ecosystem exposure with {found}, but explicit {target} usage is not detailed.",
    },
    "terraform": {
        "siblings": ["ansible", "cloudformation", "pulumi", "chef", "puppet"],
        "category": "Infrastructure as Code (IaC)",
        "partial_reason": "Resume indicates cloud infrastructure automation ({found}), but {target} is not explicitly highlighted.",
    },
    "spring boot": {
        "siblings": ["spring", "spring framework", "spring mvc", "micronaut", "quarkus"],
        "category": "Java Framework",
        "partial_reason": "Resume references Spring ecosystem ({found}), but specific {target} microservices experience is not distinctly demonstrated.",
    },
    "aws lambda": {
        "siblings": ["serverless", "cloud functions", "azure functions", "aws", "api gateway"],
        "category": "Serverless Computing",
        "partial_reason": "Candidate has cloud exposure ({found}), but explicit serverless {target} experience is missing.",
    },
    "aws s3": {
        "siblings": ["aws", "cloud storage", "azure blob", "gcs", "minio"],
        "category": "Cloud Object Storage",
        "partial_reason": "Resume demonstrates cloud infrastructure experience ({found}), but {target} object storage is not explicitly named.",
    },
    "redis": {
        "siblings": ["memcached", "hazelcast", "ehcache", "caching"],
        "category": "In-Memory Caching",
        "partial_reason": "Resume indicates caching knowledge via {found}, but {target} is not explicitly cited.",
    },
    "graphql": {
        "siblings": ["rest apis", "grpc", "openapi", "swagger"],
        "category": "API Architecture",
        "partial_reason": "Resume exhibits solid API experience with {found}, but {target} schema/query experience is not mentioned.",
    },
    "postgresql": {
        "siblings": ["mysql", "mariadb", "oracle", "sql server", "sqlite"],
        "category": "Relational Database",
        "partial_reason": "Resume demonstrates SQL database proficiencies ({found}), but {target} specific optimizations are not listed.",
    },
    "mongodb": {
        "siblings": ["dynamodb", "cassandra", "couchbase", "nosql"],
        "category": "NoSQL Database",
        "partial_reason": "Candidate shows NoSQL experience ({found}), but {target} is not explicitly specified.",
    },
    "react": {
        "siblings": ["vue", "angular", "svelte", "javascript", "typescript"],
        "category": "Frontend Framework",
        "partial_reason": "Resume shows web UI development experience ({found}), but {target} is not explicitly listed.",
    },
}


class BaseLLMProvider(ABC):
    @abstractmethod
    def analyze(
        self,
        resume_data: ResumeStructure,
        jd_data: JDStructure,
        raw_resume: str,
        raw_jd: str,
    ) -> Dict[str, Any]:
        pass


# ---------------------------------------------------------------------------
# Heuristic & Knowledge-Graph Semantic Analyzer
# ---------------------------------------------------------------------------

class HybridHeuristicSemanticProvider(BaseLLMProvider):
    """
    High-precision deterministic & semantic analyzer.
    Performs entity normalization, synonym resolution, sibling partial-matching,
    evidence extraction, ATS checks, and anti-hallucination bullet improvements.
    """

    def analyze(
        self,
        resume_data: ResumeStructure,
        jd_data: JDStructure,
        raw_resume: str,
        raw_jd: str,
    ) -> Dict[str, Any]:
        # 1. Normalize resume text & skills
        resume_lower = raw_resume.lower()
        resume_skills_lower = [s.lower().strip() for s in resume_data.skills]
        exp_text_lower = resume_data.raw_sections.get("experience", "").lower()
        proj_text_lower = resume_data.raw_sections.get("projects", "").lower()

        # 2. Extract JD requirements list
        all_jd_skills = []
        for s in jd_data.required_skills:
            all_jd_skills.append((s, True))  # (skill, is_required)
        for s in jd_data.preferred_skills:
            all_jd_skills.append((s, False))

        # Add domain & tech fields if empty
        if not all_jd_skills:
            for s in jd_data.programming_languages + jd_data.frameworks + jd_data.cloud_technologies + jd_data.databases + jd_data.tools_and_devops:
                all_jd_skills.append((s, True))

        # Ensure unique skills
        seen = set()
        deduped_jd_skills = []
        for skill_name, is_req in all_jd_skills:
            norm = skill_name.lower().strip()
            if norm and norm not in seen and len(norm) > 1:
                seen.add(norm)
                deduped_jd_skills.append((skill_name, is_req))

        # 3. Analyze each skill against resume
        strong_matches: List[SkillMatchItem] = []
        partial_matches: List[SkillMatchItem] = []
        missing_skills: List[SkillMatchItem] = []
        side_by_side: List[SideBySideItem] = []
        experience_gaps: List[ExperienceGapItem] = []

        total_req = sum(1 for _, req in deduped_jd_skills if req)
        matched_req = 0
        total_pref = sum(1 for _, req in deduped_jd_skills if not req)
        matched_pref = 0

        for skill_name, is_req in deduped_jd_skills:
            importance = "critical" if is_req else "important"
            norm_target = skill_name.lower().strip()
            synonym_target = SYNONYM_MAP.get(norm_target, norm_target)

            match_found, evidence, match_type, reason = self._evaluate_single_skill(
                skill_name=skill_name,
                norm_target=norm_target,
                synonym_target=synonym_target,
                resume_lower=resume_lower,
                resume_skills_lower=resume_skills_lower,
                exp_text_lower=exp_text_lower,
                proj_text_lower=proj_text_lower,
                raw_resume=raw_resume,
            )

            category = self._categorize_skill(skill_name)

            if match_type == "strong":
                item = SkillMatchItem(
                    name=skill_name,
                    category=category,
                    status="strong",
                    importance=importance,
                    is_required=is_req,
                    reason=reason,
                    resume_evidence=evidence,
                )
                strong_matches.append(item)
                if is_req:
                    matched_req += 1
                else:
                    matched_pref += 1

                side_by_side.append(SideBySideItem(
                    jd_requirement=f"Experience with {skill_name} ({'Required' if is_req else 'Preferred'})",
                    resume_evidence=evidence or f"Explicitly listed in resume skills and demonstrated in work profile.",
                    match_status="strong",
                    match_badge="🟢 Strong Match",
                    importance=importance.title(),
                    notes=f"Direct evidence found in candidate CV for {skill_name}.",
                ))

                experience_gaps.append(ExperienceGapItem(
                    jd_requirement=skill_name,
                    resume_evidence=evidence or "Mentioned in skills & experience",
                    match_type="Strong",
                    importance=importance.title(),
                    notes="Fully satisfied with direct resume evidence."
                ))

            elif match_type == "partial":
                item = SkillMatchItem(
                    name=skill_name,
                    category=category,
                    status="partial",
                    importance=importance,
                    is_required=is_req,
                    reason=reason,
                    resume_evidence=evidence,
                )
                partial_matches.append(item)
                if is_req:
                    matched_req += 0.5
                else:
                    matched_pref += 0.5

                side_by_side.append(SideBySideItem(
                    jd_requirement=f"Experience with {skill_name} ({'Required' if is_req else 'Preferred'})",
                    resume_evidence=evidence or "Related domain technology demonstrated.",
                    match_status="partial",
                    match_badge="🟡 Partial Match",
                    importance=importance.title(),
                    notes=reason,
                ))

                experience_gaps.append(ExperienceGapItem(
                    jd_requirement=skill_name,
                    resume_evidence=evidence or "Related technology listed",
                    match_type="Partial",
                    importance=importance.title(),
                    notes=reason
                ))

            else:  # missing
                # Adjust importance based on JD prominence
                missing_importance = "critical" if is_req else "nice-to-have"
                item = SkillMatchItem(
                    name=skill_name,
                    category=category,
                    status="missing",
                    importance=missing_importance,
                    is_required=is_req,
                    reason=f"Required/preferred by the job description but not explicitly identified anywhere in the candidate's CV.",
                    resume_evidence=None,
                )
                missing_skills.append(item)

                side_by_side.append(SideBySideItem(
                    jd_requirement=f"Experience with {skill_name} ({'Required' if is_req else 'Preferred'})",
                    resume_evidence="Not found in resume",
                    match_status="missing",
                    match_badge="🔴 Missing",
                    importance=missing_importance.title(),
                    notes=f"The JD specifies {skill_name}, but no verifiable evidence or mention was located.",
                ))

                experience_gaps.append(ExperienceGapItem(
                    jd_requirement=skill_name,
                    resume_evidence="Not found in resume",
                    match_type="Missing",
                    importance=missing_importance.title(),
                    notes=f"Missing technical requirement for {skill_name}."
                ))

        # 4. Synthesize Strengths & Critical Gaps
        strengths = self._generate_strengths(strong_matches, resume_data, jd_data)
        critical_gaps = self._generate_critical_gaps(missing_skills, partial_matches, jd_data, resume_data)
        recommendations = self._generate_improvement_suggestions(resume_data, strong_matches, missing_skills, jd_data)
        missing_rec = self._generate_missing_keyword_advice(missing_skills)

        # 5. Skills analysis container
        skill_score = 0.0
        denom = (total_req * 1.0) + (total_pref * 0.5)
        if denom > 0:
            skill_score = round(((matched_req * 1.0) + (matched_pref * 0.5)) / denom * 100, 1)
        else:
            skill_score = 80.0

        skills_analysis = SkillsAnalysisResult(
            strong_matches=strong_matches,
            partial_matches=partial_matches,
            missing=missing_skills,
            total_required=total_req,
            matched_required=int(matched_req),
            total_preferred=total_pref,
            matched_preferred=int(matched_pref),
            overall_skill_score=min(100.0, skill_score),
        )

        return {
            "skills": skills_analysis,
            "experience_gap": experience_gaps,
            "side_by_side": side_by_side,
            "strengths": strengths,
            "critical_gaps": critical_gaps,
            "recommendations": recommendations,
            "missing_keyword_recommendations": missing_rec,
            "raw_matches": {
                "strong": [s.model_dump() for s in strong_matches],
                "partial": [p.model_dump() for p in partial_matches],
                "missing": [m.model_dump() for m in missing_skills],
            }
        }

    def _evaluate_single_skill(
        self,
        skill_name: str,
        norm_target: str,
        synonym_target: str,
        resume_lower: str,
        resume_skills_lower: List[str],
        exp_text_lower: str,
        proj_text_lower: str,
        raw_resume: str,
    ) -> Tuple[bool, Optional[str], str, str]:
        """
        Returns: (match_found, evidence_snippet, match_type: 'strong'|'partial'|'missing', reason)
        """
        # Exact match pattern with word boundary
        pattern_exact = rf"\b{re.escape(norm_target)}\b"
        pattern_synonym = rf"\b{re.escape(synonym_target)}\b"

        # Check 1: Direct in skills or text
        if re.search(pattern_exact, resume_lower) or re.search(pattern_synonym, resume_lower) or any(norm_target in s or synonym_target in s for s in resume_skills_lower):
            evidence = self._find_evidence_snippet(raw_resume, norm_target, synonym_target)
            if re.search(pattern_exact, exp_text_lower) or re.search(pattern_exact, proj_text_lower):
                reason = f"Explicitly mentioned and supported by work experience/project achievements with {skill_name}."
            else:
                reason = f"Explicitly listed in technical proficiencies/skills section."
            return True, evidence, "strong", reason

        # Check 2: Special semantic checks (e.g. AWS S3 vs Amazon S3, REST APIs vs REST)
        if "s3" in norm_target:
            if "s3" in resume_lower or "amazon s3" in resume_lower or "object storage" in resume_lower:
                evidence = self._find_evidence_snippet(raw_resume, "s3", "storage")
                return True, evidence, "strong", "Demonstrated Amazon S3 cloud object storage experience."

        if "rest" in norm_target:
            if "rest" in resume_lower or "restful" in resume_lower:
                evidence = self._find_evidence_snippet(raw_resume, "rest")
                return True, evidence, "strong", "Explicit REST APIs development and integration experience."

        if norm_target == "spring boot":
            if "spring boot" in resume_lower:
                evidence = self._find_evidence_snippet(raw_resume, "spring boot")
                return True, evidence, "strong", "Direct Spring Boot microservices experience."
            elif "spring" in resume_lower:
                evidence = self._find_evidence_snippet(raw_resume, "spring")
                return True, evidence, "partial", "Resume mentions Spring framework, but explicit Spring Boot microservices experience is not clearly specified."

        # Check 3: Check Sibling/Cluster partial matches
        cluster_info = RELATED_TECH_CLUSTERS.get(norm_target)
        if cluster_info:
            for sibling in cluster_info["siblings"]:
                if re.search(rf"\b{re.escape(sibling)}\b", resume_lower):
                    evidence = self._find_evidence_snippet(raw_resume, sibling)
                    reason = cluster_info["partial_reason"].format(found=sibling.title(), target=skill_name)
                    return True, evidence, "partial", reason

        # Check 4: Check if any synonym in dictionary matches
        for term, canonical in SYNONYM_MAP.items():
            if canonical == synonym_target and re.search(rf"\b{re.escape(term)}\b", resume_lower):
                evidence = self._find_evidence_snippet(raw_resume, term)
                return True, evidence, "strong", f"Recognized via synonym '{term}' matching required '{skill_name}'."

        # Check 5: If skill_name is a sentence/clause, check embedded known keywords
        if len(norm_target.split()) > 2:
            all_known = [
                k for k in (
                    JDParser.KNOWN_LANGUAGES + JDParser.KNOWN_FRAMEWORKS +
                    JDParser.KNOWN_CLOUDS + JDParser.KNOWN_DATABASES + JDParser.KNOWN_TOOLS
                ) if len(k) > 1 and k != "c" and k != "r" and k != "go"
            ]
            embedded_found = []
            embedded_missing = []
            for kw in all_known:
                if re.search(rf"\b{re.escape(kw)}\b", norm_target):
                    if re.search(rf"\b{re.escape(kw)}\b", resume_lower) or any(kw in s for s in resume_skills_lower):
                        embedded_found.append(kw)
                    else:
                        embedded_missing.append(kw)

            if embedded_found and not embedded_missing:
                evidence = self._find_evidence_snippet(raw_resume, *embedded_found)
                return True, evidence, "strong", f"Strong alignment demonstrated for embedded technologies: {', '.join(k.title() for k in embedded_found)}."
            elif embedded_found and embedded_missing:
                evidence = self._find_evidence_snippet(raw_resume, *embedded_found)
                return True, evidence, "partial", f"Partially satisfied: Resume shows {', '.join(k.title() for k in embedded_found)}, but lacks {', '.join(m.title() for m in embedded_missing)}."

        return False, None, "missing", f"Not found in candidate resume."

    def _find_evidence_snippet(self, raw_text: str, *keywords: str) -> Optional[str]:
        lines = raw_text.splitlines()
        # Prefer work experience and project bullets
        best_snippet = None
        for line in lines:
            line_str = line.strip()
            if not line_str or len(line_str) < 15:
                continue
            line_lower = line_str.lower()
            for kw in keywords:
                if not kw or len(kw.strip()) <= 1:
                    continue
                if re.search(rf"\b{re.escape(kw.lower().strip())}\b", line_lower):
                    cleaned = re.sub(r"^[•\-*–\d.]+\s*", "", line_str).strip()
                    if len(cleaned) > 160:
                        cleaned = cleaned[:157] + "..."
                    # If this is a bullet point from experience, return immediately
                    if line_str.startswith(("•", "-", "*", "–")) or "engineered" in line_lower or "developed" in line_lower or "built" in line_lower:
                        return cleaned
                    if not best_snippet:
                        best_snippet = cleaned
        return best_snippet

    def _categorize_skill(self, name: str) -> str:
        name_lower = name.lower()
        for lang in JDParser.KNOWN_LANGUAGES:
            if lang in name_lower:
                return "Programming Language"
        for fw in JDParser.KNOWN_FRAMEWORKS:
            if fw in name_lower:
                return "Framework / Library"
        for cl in JDParser.KNOWN_CLOUDS:
            if cl in name_lower:
                return "Cloud & Infrastructure"
        for db in JDParser.KNOWN_DATABASES:
            if db in name_lower:
                return "Database / Storage"
        for t in JDParser.KNOWN_TOOLS:
            if t in name_lower:
                return "DevOps & Tooling"
        for s in JDParser.KNOWN_SOFT_SKILLS:
            if s in name_lower:
                return "Soft Skill & Methodology"
        return "Technical Skill"

    def _generate_strengths(self, strong_matches: List[SkillMatchItem], resume: ResumeStructure, jd: JDStructure) -> List[str]:
        strengths = []
        # Group strong matches by category
        langs = [s.name for s in strong_matches if s.category == "Programming Language"]
        fws = [s.name for s in strong_matches if s.category == "Framework / Library"]
        clouds = [s.name for s in strong_matches if s.category == "Cloud & Infrastructure"]
        dbs = [s.name for s in strong_matches if s.category == "Database / Storage"]
        tools = [s.name for s in strong_matches if s.category == "DevOps & Tooling"]

        if langs:
            strengths.append(f"Strong alignment with core programming language requirements ({', '.join(langs[:3])}).")
        if fws:
            strengths.append(f"Direct experience with required application frameworks ({', '.join(fws[:3])}).")
        if clouds:
            strengths.append(f"Verified cloud computing exposure with {', '.join(clouds[:2])}.")
        if dbs:
            strengths.append(f"Solid database background demonstrated with {', '.join(dbs[:2])}.")
        if tools:
            strengths.append(f"Practical familiarity with modern engineering tools ({', '.join(tools[:3])}).")

        # Check work experience length
        if resume.work_experience:
            strengths.append(f"Demonstrated hands-on industry work experience across {len(resume.work_experience)} distinct roles/projects.")

        return strengths[:5] if strengths else ["Good baseline technical background matching general role profile."]

    def _generate_critical_gaps(
        self,
        missing_skills: List[SkillMatchItem],
        partial_matches: List[SkillMatchItem],
        jd: JDStructure,
        resume: ResumeStructure
    ) -> List[CriticalGapItem]:
        gaps = []
        # High Priority: Missing required skills
        for m in missing_skills:
            if m.is_required:
                gaps.append(CriticalGapItem(
                    priority="High",
                    requirement=m.name,
                    gap_description=f"Explicitly mandatory for the role, but no verifiable mention or evidence is present in the resume.",
                    impact_level="Critical Impact on Screening"
                ))

        # Medium Priority: Partial matches on required skills or missing preferred
        for p in partial_matches:
            if p.is_required:
                gaps.append(CriticalGapItem(
                    priority="Medium",
                    requirement=p.name,
                    gap_description=p.reason,
                    impact_level="Moderate Risk in Technical Screen"
                ))

        for m in missing_skills:
            if not m.is_required:
                gaps.append(CriticalGapItem(
                    priority="Low",
                    requirement=m.name,
                    gap_description=f"Preferred / nice-to-have technology listed in the JD that is absent from the candidate's CV.",
                    impact_level="Minor Score Impact"
                ))

        # Sort High -> Medium -> Low
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        gaps.sort(key=lambda g: priority_order.get(g.priority, 3))
        return gaps[:6]

    def _generate_improvement_suggestions(
        self,
        resume: ResumeStructure,
        strong: List[SkillMatchItem],
        missing: List[SkillMatchItem],
        jd: JDStructure
    ) -> List[ImprovementItem]:
        suggestions = []
        exp_blocks = resume.work_experience

        # Look for vague bullet points in experience and propose measurable rewrites
        if exp_blocks:
            for exp in exp_blocks:
                for b in exp.get("bullets", []):
                    b_clean = b.strip()
                    # Check if bullet lacks metrics or is generic
                    if len(b_clean) > 20 and not re.search(r"(\d+%|\$\d+|\d+\s*ms|\d+\s*users|\d+\s*x)", b_clean):
                        # Generate tailored rewrite incorporating relevant tech
                        strong_names = [s.name for s in strong[:3]]
                        tech_highlight = ", ".join(strong_names) if strong_names else "core technologies"
                        
                        recommended = (
                            f"Engineered and deployed scalable services utilizing {tech_highlight}, "
                            f"serving [X,000+ users/requests] while optimizing latency by [X%] and achieving [X%] test coverage."
                        )

                        suggestions.append(ImprovementItem(
                            section="Work Experience",
                            original_snippet=b_clean,
                            recommended_rewrite=recommended,
                            why="Replaces a passive task description with quantified impact metrics, clear action verbs, and relevant tech keywords.",
                            cautionary_note="Ensure any substituted metrics reflect your actual project contributions."
                        ))
                        if len(suggestions) >= 3:
                            break
                if len(suggestions) >= 3:
                    break

        # If summary is present, suggest enhancement
        if resume.professional_summary:
            summary = resume.professional_summary.strip()
            key_skills = [s.name for s in strong[:4]]
            rec_summary = (
                f"Results-driven Engineer with proven expertise in {', '.join(key_skills) if key_skills else 'software development'}, "
                f"delivering high-reliability distributed systems. Proven track record in optimizing backend services by [X%] and streamlining CI/CD workflows."
            )
            suggestions.append(ImprovementItem(
                section="Professional Summary",
                original_snippet=summary[:140] + ("..." if len(summary) > 140 else ""),
                recommended_rewrite=rec_summary,
                why="Sharpens career objective into a high-impact, keyword-dense summary tailored directly to the target role requirements.",
                cautionary_note="Only claim specialization areas you are confident discussing in an interview."
            ))

        return suggestions[:4]

    def _generate_missing_keyword_advice(self, missing_skills: List[SkillMatchItem]) -> List[MissingKeywordRecommendation]:
        recs = []
        for m in missing_skills[:6]:
            if m.importance == "critical":
                where = "Skills section + relevant Work Experience bullet"
                advice = f"If you have hands-on experience with {m.name}, explicitly add it under Technical Skills and describe the specific project where you deployed or maintained it."
            else:
                where = "Skills or Projects section"
                advice = f"If you have used {m.name} in side projects, coursework, or secondary tasks, consider mentioning it to capture secondary ATS keyword matching."

            recs.append(MissingKeywordRecommendation(
                keyword=m.name,
                importance=m.importance.title(),
                where_to_add=where,
                advice=advice,
                cautionary_note="Only add a keyword if you genuinely have experience with it."
            ))
        return recs


# ---------------------------------------------------------------------------
# Gemini LLM Provider (Optional Advanced Reasoning)
# ---------------------------------------------------------------------------

class GeminiProvider(BaseLLMProvider):
    """
    Calls Gemini API with structured prompt and strict schema fallback.
    """

    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash"):
        self.api_key = api_key
        self.model_name = model_name
        self.fallback = HybridHeuristicSemanticProvider()

    def analyze(
        self,
        resume_data: ResumeStructure,
        jd_data: JDStructure,
        raw_resume: str,
        raw_jd: str,
    ) -> Dict[str, Any]:
        try:
            from google import genai
            client = genai.Client(api_key=self.api_key)

            prompt = f"""
You are an expert ATS (Applicant Tracking System) and Technical Hiring Director.
Analyze the following Candidate Resume against the Job Description.

STRICT ANTI-HALLUCINATION RULES:
- Never invent candidate experience, metrics, certifications, or past employers.
- If a skill is not explicitly supported by the resume, mark it as missing or partial.
- Clearly distinguish exact matches from partial matches (e.g. RabbitMQ is NOT an exact match for Kafka; Spring is NOT an exact match for Spring Boot).
- For bullet rewrites, ALWAYS use bracketed placeholders like [X% improvement] or [X users] instead of inventing fake numbers.
- Provide objective, explainable evaluation.

RESUME TEXT:
{raw_resume[:4000]}

JOB DESCRIPTION:
{raw_jd[:3000]}

Respond ONLY with valid JSON matching this exact structure:
{{
  "strengths": ["string", "string"],
  "skills_analysis": {{
    "strong_matches": [
      {{"name": "Java", "category": "Programming Language", "status": "strong", "importance": "critical", "is_required": true, "reason": "...", "resume_evidence": "..."}}
    ],
    "partial_matches": [
      {{"name": "Kafka", "category": "Message Broker", "status": "partial", "importance": "critical", "is_required": true, "reason": "...", "resume_evidence": "..."}}
    ],
    "missing": [
      {{"name": "Kubernetes", "category": "DevOps", "status": "missing", "importance": "critical", "is_required": true, "reason": "...", "resume_evidence": null}}
    ]
  }},
  "recommendations": [
    {{
      "section": "Work Experience",
      "original_snippet": "...",
      "recommended_rewrite": "...",
      "why": "...",
      "cautionary_note": "Only add this claim if you genuinely performed this work."
    }}
  ]
}}
"""
            response = client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )
            text_out = response.text or ""
            clean_json = re.sub(r"```(?:json)?", "", text_out).strip()
            data = json.loads(clean_json)

            # Validate against heuristic baseline
            heuristic_res = self.fallback.analyze(resume_data, jd_data, raw_resume, raw_jd)
            if "skills_analysis" in data and "strong_matches" in data["skills_analysis"]:
                # Convert LLM items to typed SkillMatchItem
                strong = [SkillMatchItem(**item) for item in data["skills_analysis"].get("strong_matches", [])]
                partial = [SkillMatchItem(**item) for item in data["skills_analysis"].get("partial_matches", [])]
                missing = [SkillMatchItem(**item) for item in data["skills_analysis"].get("missing", [])]

                heuristic_res["skills"].strong_matches = strong or heuristic_res["skills"].strong_matches
                heuristic_res["skills"].partial_matches = partial or heuristic_res["skills"].partial_matches
                heuristic_res["skills"].missing = missing or heuristic_res["skills"].missing
                if data.get("strengths"):
                    heuristic_res["strengths"] = data["strengths"]

            return heuristic_res
        except Exception as e:
            logger.warning(f"Gemini LLM inference failed or unavailable, falling back to Hybrid Heuristic Engine: {e}")
            return self.fallback.analyze(resume_data, jd_data, raw_resume, raw_jd)


# ---------------------------------------------------------------------------
# Provider Factory
# ---------------------------------------------------------------------------

def get_llm_provider() -> BaseLLMProvider:
    provider_type = settings.llm_provider.lower()
    
    if (provider_type == "gemini" or provider_type == "auto") and settings.gemini_api_key:
        logger.info("Initializing Gemini LLM Provider")
        return GeminiProvider(api_key=settings.gemini_api_key, model_name=settings.llm_model)

    logger.info("Using built-in Hybrid Heuristic Semantic Engine (100% offline & robust)")
    return HybridHeuristicSemanticProvider()
