import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.sample_data import SAMPLE_RESUME_TEXT, SAMPLE_JD_TEXT

client = TestClient(app)


def test_health_check_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_sample_data_endpoint():
    response = client.get("/api/sample-data")
    assert response.status_code == 200
    data = response.json()
    assert "sample_resume_text" in data
    assert "sample_jd_text" in data
    assert "sample_resume_structured" in data


def test_resume_upload_and_delete_flow():
    # 1. Upload Resume Text
    upload_res = client.post("/api/resume/upload", data={"text": SAMPLE_RESUME_TEXT})
    assert upload_res.status_code == 200
    res_data = upload_res.json()
    resume_id = res_data["id"]
    assert resume_id is not None
    assert res_data["structured_data"]["candidate_name"] == "Alex Morgan"

    # 2. Upload JD Text
    jd_res = client.post("/api/job-description/upload", data={"text": SAMPLE_JD_TEXT})
    assert jd_res.status_code == 200
    jd_data = jd_res.json()
    jd_id = jd_data["id"]

    # 3. Perform Analysis by IDs
    analysis_res = client.post("/api/analyze", json={
        "resume_id": resume_id,
        "job_description_id": jd_id
    })
    assert analysis_res.status_code == 200
    analysis_data = analysis_res.json()
    analysis_id = analysis_data["id"]
    assert analysis_data["overall_score"] > 0
    assert analysis_data["estimated_screening_probability"] > 0
    assert len(analysis_data["skills"]["strong_matches"]) > 0
    assert len(analysis_data["experience_gap"]) > 0
    assert len(analysis_data["side_by_side"]) > 0
    assert len(analysis_data["recommendations"]) > 0

    # 4. Fetch Analysis by ID
    get_res = client.get(f"/api/analyze/{analysis_id}")
    assert get_res.status_code == 200
    assert get_res.json()["id"] == analysis_id

    # 5. Delete Resume (Privacy test)
    del_res = client.delete(f"/api/resume/{resume_id}")
    assert del_res.status_code == 200


def test_direct_analyze_with_raw_text():
    response = client.post("/api/analyze", json={
        "resume_text": SAMPLE_RESUME_TEXT,
        "job_description_text": SAMPLE_JD_TEXT,
        "custom_weights": {
            "weight_skills": 0.4,
            "weight_experience": 0.2,
            "weight_responsibilities": 0.15,
            "weight_education": 0.1,
            "weight_projects": 0.05,
            "weight_soft_skills": 0.05,
            "weight_ats_quality": 0.05
        }
    })
    assert response.status_code == 200
    data = response.json()
    assert 50.0 <= data["overall_score"] <= 95.0
    assert "probability_disclaimer" in data["final_assessment"]


def test_config_weights_endpoint():
    get_res = client.get("/api/config/weights")
    assert get_res.status_code == 200
    assert "weight_skills" in get_res.json()["raw_weights"]
