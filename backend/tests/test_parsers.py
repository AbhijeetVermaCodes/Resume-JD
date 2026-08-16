import pytest
from app.parsers.resume_parser import ResumeParser
from app.parsers.jd_parser import JDParser
from app.sample_data import SAMPLE_RESUME_TEXT, SAMPLE_JD_TEXT


def test_resume_parser_txt_and_sections():
    struct = ResumeParser.parse_raw_text(SAMPLE_RESUME_TEXT)
    
    assert struct.candidate_name == "Alex Morgan"
    assert struct.contact_info.email == "alex.morgan@techmail.io"
    assert struct.contact_info.phone is not None
    assert "San Francisco, CA" in (struct.contact_info.location or "")
    assert struct.professional_summary is not None
    assert len(struct.skills) > 5
    assert len(struct.work_experience) >= 2
    assert len(struct.projects) >= 1
    assert len(struct.education) >= 1
    assert len(struct.certifications) >= 1


def test_resume_parser_empty_text():
    with pytest.raises(ValueError):
        ResumeParser.parse_file(b"", "empty.txt", "txt")


def test_jd_parser_structured_extraction():
    struct = JDParser.parse_raw_text(SAMPLE_JD_TEXT)
    
    assert "Senior" in (struct.job_title or "")
    assert struct.required_years_experience == 5.0
    assert "Java" in struct.programming_languages
    assert any("Spring Boot" in s for s in struct.frameworks + struct.required_skills)
    assert any("Postgres" in d for d in struct.databases + struct.required_skills)
    assert any("Kafka" in s for s in struct.tools_and_devops + struct.required_skills)
    assert any("Kubernetes" in s for s in struct.tools_and_devops + struct.required_skills)
    assert any("Terraform" in s for s in struct.preferred_skills + struct.tools_and_devops)
