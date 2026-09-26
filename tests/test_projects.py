"""Test Suite for Project Discovery, Execution, History, and Checklists."""

import pytest
from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_list_all_58_projects():
    res = client.get("/api/projects")
    assert res.status_code == 200
    data = res.json()
    assert data["total_count"] == 58
    assert len(data["projects"]) == 58

def test_filter_by_tier():
    beg = client.get("/api/projects?tier=BEGINNER").json()
    assert beg["total_count"] == 19

    inter = client.get("/api/projects?tier=INTERMEDIATE").json()
    assert inter["total_count"] == 20

    adv = client.get("/api/projects?tier=ADVANCED").json()
    assert adv["total_count"] == 19

def test_run_projects_across_tiers():
    # Test Beginner (#1 AI Resume Optimizer)
    r1 = client.post("/api/projects/1/run", json={"inputs": {
        "resume_text": "Software engineer with python skills",
        "target_job": "Senior Python Backend Engineer"
    }})
    assert r1.status_code == 200
    assert r1.json()["status"] == "success"
    assert "ats_match_score" in r1.json()["output"]

    # Test Intermediate (#20 Code Reviewer)
    r20 = client.post("/api/projects/20/run", json={"inputs": {
        "language": "python",
        "source_code": "def query(): eval('1+1')"
    }})
    assert r20.status_code == 200
    assert "security_issues" in r20.json()["output"]

    # Test Advanced (#58 Financial Literacy Guide)
    r58 = client.post("/api/projects/58/run", json={"inputs": {
        "monthly_income_net": 5000
    }})
    assert r58.status_code == 200
    assert "50_30_20_budget" in r58.json()["output"]

def test_project_history():
    res = client.get("/api/projects/1/history")
    assert res.status_code == 200
    assert "history" in res.json()

def test_dashboard_stats():
    res = client.get("/api/dashboard/stats")
    assert res.status_code == 200
    stats = res.json()
    assert stats["total_projects"] == 58
    assert stats["beginner_count"] == 19
    assert stats["intermediate_count"] == 20
    assert stats["advanced_count"] == 19

def test_roadmap_endpoint():
    res = client.get("/api/roadmap")
    assert res.status_code == 200
    roadmap = res.json()
    assert len(roadmap["levels"]) == 3
    assert roadmap["total_projects"] == 58
