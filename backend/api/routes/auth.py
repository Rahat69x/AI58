"""Authentication and User Account routes for AI58."""

from datetime import datetime, timezone
import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database.session import get_db
from backend.models.entities import User
from backend.schemas.user import UserRegister, UserLogin, UserOut, TokenResponse, UserPreferencesUpdate
from backend.core.security import hash_password, verify_password, create_access_token, get_current_user_required

router = APIRouter(prefix="/auth", tags=["Authentication & User Account"])

@router.post("/register", response_model=TokenResponse)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user account."""
    existing_user = db.query(User).filter(
        (User.username == user_data.username) | (User.email == user_data.email)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this username or email already exists."
        )

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        full_name=user_data.full_name or user_data.username,
        role="engineer",
        preferences_json=json.dumps({"theme": "dark", "favorite_tier": "ALL", "ai_provider": "builtin"}),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token({"sub": str(new_user.id), "username": new_user.username, "role": new_user.role})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": UserOut(
            id=new_user.id,
            username=new_user.username,
            email=new_user.email,
            full_name=new_user.full_name,
            role=new_user.role,
            preferences=new_user.preferences,
            created_at=new_user.created_at,
        ),
    }

@router.post("/login", response_model=TokenResponse)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    """Authenticate existing user credentials."""
    user = db.query(User).filter(
        (User.username == login_data.username_or_email) | (User.email == login_data.username_or_email)
    ).first()
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please verify your username and password."
        )

    token = create_access_token({"sub": str(user.id), "username": user.username, "role": user.role})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": UserOut(
            id=user.id,
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            role=user.role,
            preferences=user.preferences,
            created_at=user.created_at,
        ),
    }

@router.get("/profile", response_model=UserOut)
def get_profile(current_user: dict = Depends(get_current_user_required), db: Session = Depends(get_db)):
    """Retrieve currently authenticated user profile."""
    user = db.query(User).filter(User.id == int(current_user["sub"])).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut(
        id=user.id,
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        role=user.role,
        preferences=user.preferences,
        created_at=user.created_at,
    )

@router.put("/preferences")
def update_preferences(prefs: UserPreferencesUpdate, current_user: dict = Depends(get_current_user_required), db: Session = Depends(get_db)):
    """Update user preferences and AI provider configs."""
    user = db.query(User).filter(User.id == int(current_user["sub"])).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    current_prefs = user.preferences
    current_prefs.update(prefs.model_dump(exclude_unset=True))
    user.preferences = current_prefs
    db.commit()
    return {"status": "success", "preferences": user.preferences}

@router.delete("/account")
def delete_account(current_user: dict = Depends(get_current_user_required), db: Session = Depends(get_db)):
    """Permanently delete user account and associated history (Privacy controls)."""
    user = db.query(User).filter(User.id == int(current_user["sub"])).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"status": "success", "message": "Account and all associated project data permanently removed."}
