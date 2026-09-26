"""Roadmap routes providing Level 1, 2, and 3 visualization data and 8-point checklists."""

from typing import Optional, Dict, Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.models.entities import ProjectChecklist
from backend.projects.registry import PROJECT_REGISTRY
from backend.core.security import get_current_user_optional

router = APIRouter(prefix="/roadmap", tags=["Visual Roadmap & Checklists"])

@router.get("")
def get_roadmap_data(
    current_user: Optional[dict] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """Returns structured 3-level roadmap tree with 8-point checklist tracking for all 58 projects."""
    user_id = int(current_user["sub"]) if current_user else None

    # Load custom checklist overrides if user is logged in
    user_checklists = {}
    if user_id:
        records = db.query(ProjectChecklist).filter(ProjectChecklist.user_id == user_id).all()
        for r in records:
            user_checklists[r.project_id] = {
                "scaffold": r.scaffold, "ui": r.ui, "backend": r.backend,
                "ai_integration": r.ai_integration, "database": r.database,
                "testing": r.testing, "documentation": r.documentation, "deployment": r.deployment
            }

    levels = [
        {"level": 1, "tier": "BEGINNER", "title": "LEVEL 1 — BEGINNER (Projects 01–19)", "description": "Foundational AI utilities, personal productivity agents, and career tools.", "range": "01–19", "projects": []},
        {"level": 2, "tier": "INTERMEDIATE", "title": "LEVEL 2 — INTERMEDIATE (Projects 20–39)", "description": "Developer tooling, code intelligence, testing engines, DevOps, and data pipelines.", "range": "20–39", "projects": []},
        {"level": 3, "tier": "ADVANCED", "title": "LEVEL 3 — ADVANCED (Projects 40–58)", "description": "High-complexity reasoning agents, domain coaches, simulation engines, and public good systems.", "range": "40–58", "projects": []},
    ]

    total_checklist_items = 58 * 8
    completed_items = 0

    for p in PROJECT_REGISTRY:
        pid = p["id"]
        chk = user_checklists.get(pid, {
            "scaffold": True, "ui": True, "backend": True,
            "ai_integration": True, "database": True,
            "testing": True, "documentation": True, "deployment": True
        })
        completed_in_proj = sum(1 for v in chk.values() if v)
        completed_items += completed_in_proj

        proj_entry = {
            "id": pid,
            "slug": p["slug"],
            "name": p["name"],
            "tier": p["tier"],
            "category": p["category"],
            "checklist": chk,
            "checklist_completed": completed_in_proj,
            "checklist_total": 8,
            "status": "Ready"
        }

        if p["tier"] == "BEGINNER":
            levels[0]["projects"].append(proj_entry)
        elif p["tier"] == "INTERMEDIATE":
            levels[1]["projects"].append(proj_entry)
        elif p["tier"] == "ADVANCED":
            levels[2]["projects"].append(proj_entry)

    overall_completion_pct = round((completed_items / total_checklist_items) * 100, 1)

    return {
        "overall_completion_percentage": overall_completion_pct,
        "total_projects": 58,
        "completed_checklist_items": completed_items,
        "total_checklist_items": total_checklist_items,
        "levels": levels
    }
