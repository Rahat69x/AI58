"""Project discovery, execution workbench, history, and checklist routes for AI58."""

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.models.entities import User, ProjectRun, UserFavorite, SavedOutput, ProjectChecklist
from backend.projects.registry import PROJECT_REGISTRY, PROJECTS_BY_ID, get_projects
from backend.projects.runner_dispatcher import dispatch_project_run
from backend.schemas.project import (
    ProjectRunRequest, ProjectRunResponse, ChecklistSchema,
    SavedOutputCreate, SavedOutputOut
)
from backend.core.security import get_current_user_optional, get_current_user_required

router = APIRouter(prefix="/projects", tags=["AI58 Projects Platform"])

@router.get("")
def list_all_projects(
    tier: Optional[str] = Query(None, description="BEGINNER, INTERMEDIATE, or ADVANCED"),
    category: Optional[str] = Query(None, description="Category filter"),
    search: Optional[str] = Query(None, description="Search term across title and capabilities"),
    favorites_only: bool = Query(False, description="Filter only favorited projects"),
    current_user: Optional[dict] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """Retrieve catalog of all 58 projects with optional filtering."""
    projects = get_projects(tier=tier, category=category, search=search)

    # Get favorite project IDs if user is logged in
    user_id = int(current_user["sub"]) if current_user else None
    favorite_ids = set()
    if user_id:
        favs = db.query(UserFavorite.project_id).filter(UserFavorite.user_id == user_id).all()
        favorite_ids = {f[0] for f in favs}

    # Fetch checklist progress if available
    checklist_map = {}
    if user_id:
        checklists = db.query(ProjectChecklist).filter(ProjectChecklist.user_id == user_id).all()
        for c in checklists:
            checklist_map[c.project_id] = {
                "scaffold": c.scaffold, "ui": c.ui, "backend": c.backend,
                "ai_integration": c.ai_integration, "database": c.database,
                "testing": c.testing, "documentation": c.documentation, "deployment": c.deployment
            }

    enhanced_projects = []
    for p in projects:
        pid = p["id"]
        is_fav = pid in favorite_ids
        if favorites_only and not is_fav:
            continue

        chk = checklist_map.get(pid, {
            "scaffold": True, "ui": True, "backend": True,
            "ai_integration": True, "database": True,
            "testing": True, "documentation": True, "deployment": True
        })

        enhanced_projects.append({
            "id": pid,
            "slug": p["slug"],
            "name": p["name"],
            "tier": p["tier"],
            "category": p["category"],
            "description": p["description"],
            "capabilities": p["capabilities"],
            "technologies": p["technologies"],
            "status": "Ready",
            "progress": 100,
            "is_favorite": is_fav,
            "checklist": chk,
            "default_input": p["default_input"]
        })

    return {
        "total_count": len(enhanced_projects),
        "projects": enhanced_projects
    }

@router.get("/{project_id}")
def get_project_detail(
    project_id: int,
    current_user: Optional[dict] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """Retrieve full detail, capabilities, sample inputs, and documentation for a project."""
    project = PROJECTS_BY_ID.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail=f"Project #{project_id} not found in AI58 registry.")

    user_id = int(current_user["sub"]) if current_user else None
    is_fav = False
    if user_id:
        is_fav = db.query(UserFavorite).filter(
            UserFavorite.user_id == user_id,
            UserFavorite.project_id == project_id
        ).first() is not None

    # Load documentation
    tier_dir = project["tier"].lower()
    slug = project["slug"]
    docs_path = Path(__file__).resolve().parent.parent.parent / "projects" / tier_dir / slug / "docs.md"
    docs_content = docs_path.read_text(encoding="utf-8") if docs_path.exists() else f"# {project['name']}\nDocumentation ready."

    # Load or default checklist
    chk_record = None
    if user_id:
        chk_record = db.query(ProjectChecklist).filter(
            ProjectChecklist.user_id == user_id,
            ProjectChecklist.project_id == project_id
        ).first()

    checklist_data = {
        "scaffold": chk_record.scaffold if chk_record else True,
        "ui": chk_record.ui if chk_record else True,
        "backend": chk_record.backend if chk_record else True,
        "ai_integration": chk_record.ai_integration if chk_record else True,
        "database": chk_record.database if chk_record else True,
        "testing": chk_record.testing if chk_record else True,
        "documentation": chk_record.documentation if chk_record else True,
        "deployment": chk_record.deployment if chk_record else True,
    }

    return {
        "id": project["id"],
        "slug": project["slug"],
        "name": project["name"],
        "tier": project["tier"],
        "category": project["category"],
        "description": project["description"],
        "capabilities": project["capabilities"],
        "technologies": project["technologies"],
        "status": "Ready",
        "progress": 100,
        "is_favorite": is_fav,
        "checklist": checklist_data,
        "default_input": project["default_input"],
        "documentation_markdown": docs_content
    }

@router.post("/{project_id}/run", response_model=ProjectRunResponse)
async def run_project_instance(
    project_id: int,
    payload: ProjectRunRequest,
    current_user: Optional[dict] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """Execute project runner with custom or default inputs and persist run history."""
    project = PROJECTS_BY_ID.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail=f"Project #{project_id} not found.")

    inputs = payload.inputs or project["default_input"]
    user_id = int(current_user["sub"]) if current_user else None

    try:
        run_result = await dispatch_project_run(project_id, inputs, payload.options)
    except Exception as e:
        # Record failed run
        err_run = ProjectRun(
            project_id=project_id,
            user_id=user_id,
            input_payload_json=json.dumps(inputs),
            output_payload_json=json.dumps({"error": str(e)}),
            execution_time_ms=0.0,
            status="error",
            error_message=str(e)
        )
        db.add(err_run)
        db.commit()
        raise HTTPException(status_code=500, detail=f"Project execution error: {str(e)}")

    # Record successful run
    run_record = ProjectRun(
        project_id=project_id,
        user_id=user_id,
        input_payload_json=json.dumps(inputs),
        output_payload_json=json.dumps(run_result["output"]),
        execution_time_ms=run_result["execution_time_ms"],
        status="success"
    )
    db.add(run_record)
    db.commit()
    db.refresh(run_record)

    return ProjectRunResponse(
        project_id=project_id,
        slug=project["slug"],
        status="success",
        execution_time_ms=run_result["execution_time_ms"],
        output=run_result["output"],
        run_id=run_record.id,
        created_at=run_record.created_at.isoformat()
    )

@router.get("/{project_id}/history")
def get_project_history(
    project_id: int,
    limit: int = 15,
    current_user: Optional[dict] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """Fetch past execution runs for this specific project."""
    query = db.query(ProjectRun).filter(ProjectRun.project_id == project_id)
    if current_user:
        query = query.filter(ProjectRun.user_id == int(current_user["sub"]))

    runs = query.order_by(ProjectRun.created_at.desc()).limit(limit).all()

    return {
        "project_id": project_id,
        "runs_count": len(runs),
        "history": [
            {
                "id": r.id,
                "created_at": r.created_at.isoformat(),
                "execution_time_ms": r.execution_time_ms,
                "status": r.status,
                "input": r.input_payload,
                "output": r.output_payload,
            }
            for r in runs
        ]
    }

@router.post("/{project_id}/favorite")
def toggle_project_favorite(
    project_id: int,
    current_user: dict = Depends(get_current_user_required),
    db: Session = Depends(get_db)
):
    """Toggle favorite star for the current user."""
    user_id = int(current_user["sub"])
    fav = db.query(UserFavorite).filter(
        UserFavorite.user_id == user_id,
        UserFavorite.project_id == project_id
    ).first()

    if fav:
        db.delete(fav)
        db.commit()
        return {"project_id": project_id, "is_favorite": False}
    else:
        new_fav = UserFavorite(user_id=user_id, project_id=project_id)
        db.add(new_fav)
        db.commit()
        return {"project_id": project_id, "is_favorite": True}

@router.put("/{project_id}/checklist")
def update_project_checklist(
    project_id: int,
    checklist: ChecklistSchema,
    current_user: dict = Depends(get_current_user_required),
    db: Session = Depends(get_db)
):
    """Update 8-point checklist deployment state."""
    user_id = int(current_user["sub"])
    rec = db.query(ProjectChecklist).filter(
        ProjectChecklist.user_id == user_id,
        ProjectChecklist.project_id == project_id
    ).first()

    if not rec:
        rec = ProjectChecklist(user_id=user_id, project_id=project_id)
        db.add(rec)

    rec.scaffold = checklist.scaffold
    rec.ui = checklist.ui
    rec.backend = checklist.backend
    rec.ai_integration = checklist.ai_integration
    rec.database = checklist.database
    rec.testing = checklist.testing
    rec.documentation = checklist.documentation
    rec.deployment = checklist.deployment

    db.commit()
    return {"status": "success", "checklist": checklist.model_dump()}

@router.post("/{project_id}/save-output", response_model=SavedOutputOut)
def save_project_output(
    project_id: int,
    data: SavedOutputCreate,
    current_user: dict = Depends(get_current_user_required),
    db: Session = Depends(get_db)
):
    """Save a project execution output to the user's permanent output portfolio."""
    user_id = int(current_user["sub"])
    saved = SavedOutput(
        user_id=user_id,
        project_id=project_id,
        title=data.title,
        notes=data.notes or "",
        payload_json=json.dumps(data.payload)
    )
    db.add(saved)
    db.commit()
    db.refresh(saved)
    return SavedOutputOut(
        id=saved.id,
        project_id=saved.project_id,
        title=saved.title,
        notes=saved.notes,
        payload=saved.payload,
        created_at=saved.created_at
    )
