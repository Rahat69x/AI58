"""AI58 Platform Configuration Settings."""

import os
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseModel):
    PLATFORM_NAME: str = os.getenv("PLATFORM_NAME", "AI58")
    PLATFORM_VERSION: str = os.getenv("PLATFORM_VERSION", "1.0.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() in ("true", "1", "yes")

    # Security & Auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "ai58-platform-master-secret-key-2026-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))

    # Server & CORS
    BACKEND_HOST: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    BACKEND_PORT: int = int(os.getenv("BACKEND_PORT", "8000"))
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "*",
    ]

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/ai58.db")

    # AI Engine Settings
    AI_PROVIDER: str = os.getenv("AI_PROVIDER", "builtin")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

    # Directory Paths
    BASE_DIR: Path = BASE_DIR
    PROJECTS_DIR: Path = BASE_DIR / "projects"
    UPLOAD_DIR: Path = BASE_DIR / "uploads"

    # Strict Platform Project Counts
    EXPECTED_TOTAL_PROJECTS: int = 58
    EXPECTED_BEGINNER_PROJECTS: int = 19
    EXPECTED_INTERMEDIATE_PROJECTS: int = 20
    EXPECTED_ADVANCED_PROJECTS: int = 19

settings = Settings()
