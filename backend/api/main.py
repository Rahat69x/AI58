"""FastAPI Main Application Entry Point for AI58 Platform."""

from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.core.config import settings
from backend.database.session import init_db
from backend.api.routes import auth, projects, dashboard, roadmap, ai_services

# Ensure database tables exist
init_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print(f"[{settings.PLATFORM_NAME}] Database initialized successfully at {settings.DATABASE_URL}")
    yield

app = FastAPI(
    title=f"{settings.PLATFORM_NAME} — Unified AI Project Platform",
    description="A unified AI platform hosting 58 interconnected AI projects spanning Beginner, Intermediate, and Advanced tiers.",
    version=settings.PLATFORM_VERSION,
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(auth.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")
app.include_router(roadmap.router, prefix="/api")
app.include_router(ai_services.router, prefix="/api")

@app.get("/api/health")
def health_check():
    """Platform health check."""
    return {
        "status": "healthy",
        "platform": settings.PLATFORM_NAME,
        "version": settings.PLATFORM_VERSION,
        "total_projects": settings.EXPECTED_TOTAL_PROJECTS,
        "environment": settings.ENVIRONMENT
    }

from fastapi.responses import FileResponse
from fastapi import HTTPException

# Mount static frontend build if present
frontend_dist = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"
if frontend_dist.exists():
    assets_dir = frontend_dist / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="static_assets")

    @app.get("/")
    async def serve_index():
        return FileResponse(frontend_dist / "index.html")

    @app.get("/{full_path:path}")
    async def serve_spa_catch_all(full_path: str):
        if full_path.startswith("api") or full_path.startswith("docs") or full_path.startswith("openapi.json"):
            raise HTTPException(status_code=404, detail="API route not found")
        file_path = frontend_dist / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        return FileResponse(frontend_dist / "index.html")

