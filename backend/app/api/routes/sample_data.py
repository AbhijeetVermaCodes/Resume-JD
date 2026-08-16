from fastapi import APIRouter
from app.sample_data import SAMPLE_RESUME_TEXT, SAMPLE_JD_TEXT
from app.parsers.resume_parser import ResumeParser
from app.parsers.jd_parser import JDParser

router = APIRouter(prefix="/sample-data", tags=["Sample Data"])


@router.get("")
def get_sample_data():
    """
    Returns realistic sample Software Engineer resume and Job Description
    for 1-click interactive demo testing.
    """
    resume_struct = ResumeParser.parse_raw_text(SAMPLE_RESUME_TEXT)
    jd_struct = JDParser.parse_raw_text(SAMPLE_JD_TEXT)

    return {
        "sample_resume_text": SAMPLE_RESUME_TEXT,
        "sample_jd_text": SAMPLE_JD_TEXT,
        "sample_resume_structured": resume_struct,
        "sample_jd_structured": jd_struct,
        "meta": {
            "title": "Senior Backend Software Engineer vs Cloud Platforms JD",
            "scenario": "Demonstrates strong matches (Java, Spring Boot, REST APIs, AWS S3, Docker, Postgres), partial match (Kafka vs RabbitMQ), missing required skills (Kubernetes), and missing preferred skills (Terraform, AWS Lambda)."
        }
    }
