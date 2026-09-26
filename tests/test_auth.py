"""Test Suite for Authentication, User Accounts, and Security Controls."""

import pytest
from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_user_registration_and_login_flow():
    username = "test_engineer_42"
    email = "test42@ai58.internal"
    password = "SecurePassword2026!"

    # 1. Register
    reg_res = client.post("/api/auth/register", json={
        "username": username,
        "email": email,
        "password": password,
        "full_name": "Test Engineer"
    })
    assert reg_res.status_code == 200
    token = reg_res.json()["access_token"]
    assert token is not None

    # 2. Login
    login_res = client.post("/api/auth/login", json={
        "username_or_email": username,
        "password": password
    })
    assert login_res.status_code == 200
    assert login_res.json()["access_token"] is not None

    # 3. Profile
    prof_res = client.get("/api/auth/profile", headers={"Authorization": f"Bearer {token}"})
    assert prof_res.status_code == 200
    assert prof_res.json()["username"] == username

    # 4. Preferences Update
    pref_res = client.put(
        "/api/auth/preferences",
        json={"theme": "cyberpunk", "favorite_tier": "ADVANCED"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert pref_res.status_code == 200
    assert pref_res.json()["preferences"]["theme"] == "cyberpunk"

    # 5. Account Deletion (Privacy controls)
    del_res = client.delete("/api/auth/account", headers={"Authorization": f"Bearer {token}"})
    assert del_res.status_code == 200

    # 6. Verify cannot login after deletion
    post_del_login = client.post("/api/auth/login", json={
        "username_or_email": username,
        "password": password
    })
    assert post_del_login.status_code == 401
