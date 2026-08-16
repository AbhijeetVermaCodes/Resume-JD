import pytest
from app.parsers.resume_parser import ResumeParser
from app.parsers.jd_parser import JDParser
from app.services.llm_service import HybridHeuristicSemanticProvider
from app.sample_data import SAMPLE_RESUME_TEXT, SAMPLE_JD_TEXT


def test_semantic_skill_matching_exact_synonym_partial_missing():
    resume_struct = ResumeParser.parse_raw_text(SAMPLE_RESUME_TEXT)
    jd_struct = JDParser.parse_raw_text(SAMPLE_JD_TEXT)
    
    provider = HybridHeuristicSemanticProvider()
    result = provider.analyze(
        resume_data=resume_struct,
        jd_data=jd_struct,
        raw_resume=SAMPLE_RESUME_TEXT,
        raw_jd=SAMPLE_JD_TEXT,
    )
    
    skills = result["skills"]
    strong_names = [s.name.lower() for s in skills.strong_matches]
    partial_names = [s.name.lower() for s in skills.partial_matches]
    missing_names = [s.name.lower() for s in skills.missing]

    # 1. Exact & Synonym matches
    assert any("java" in name for name in strong_names)
    assert any("spring boot" in name for name in strong_names)
    assert any("rest" in name for name in strong_names)
    assert any("postgres" in name for name in strong_names)
    assert any("docker" in name for name in strong_names)
    assert any("s3" in name or "aws" in name for name in strong_names)

    # 2. Sibling partial match: Kafka required in JD, RabbitMQ in resume
    kafka_match = next((s for s in skills.partial_matches if "kafka" in s.name.lower()), None)
    assert kafka_match is not None, "Kafka should be detected as a partial match due to RabbitMQ in resume."
    assert "rabbitmq" in kafka_match.reason.lower()
    # Anti-hallucination check: ensure RabbitMQ was not classified as a full/strong exact Kafka match
    assert not any("kafka" in name for name in strong_names)

    # 3. Missing or Partial gap skills: Kubernetes (Critical), Terraform (Preferred), AWS Lambda (Preferred)
    assert any("kubernetes" in name or "k8s" in name for name in missing_names)
    assert any("terraform" in name for name in missing_names)
    assert any("lambda" in name for name in missing_names + partial_names)


def test_evidence_extraction_and_side_by_side():
    resume_struct = ResumeParser.parse_raw_text(SAMPLE_RESUME_TEXT)
    jd_struct = JDParser.parse_raw_text(SAMPLE_JD_TEXT)
    
    provider = HybridHeuristicSemanticProvider()
    result = provider.analyze(
        resume_data=resume_struct,
        jd_data=jd_struct,
        raw_resume=SAMPLE_RESUME_TEXT,
        raw_jd=SAMPLE_JD_TEXT,
    )

    side_by_side = result["side_by_side"]
    assert len(side_by_side) > 5

    # Check that Java side-by-side has direct evidence
    java_sbs = next((item for item in side_by_side if "java" in item.jd_requirement.lower()), None)
    assert java_sbs is not None
    assert java_sbs.match_status == "strong"
    assert "java" in java_sbs.resume_evidence.lower()
