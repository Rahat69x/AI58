"""Pydantic Schemas for AI58 User and Authentication."""

from datetime import datetime
from typing import Optional, Any, Dict
from pydantic import BaseModel, Field, ConfigDict

class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=64)
    email: str = Field(..., min_length=5, max_length=128)
    password: str = Field(..., min_length=6)
    full_name: Optional[str] = ""

class UserLogin(BaseModel):
    username_or_email: str
    password: str

class UserPreferencesUpdate(BaseModel):
    theme: Optional[str] = "dark"
    favorite_tier: Optional[str] = "ALL"
    ai_provider: Optional[str] = "builtin"
    gemini_key: Optional[str] = None
    openai_key: Optional[str] = None
    anthropic_key: Optional[str] = None
    auto_save_runs: Optional[bool] = True

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    full_name: str
    role: str
    preferences: Dict[str, Any]
    created_at: datetime

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut
