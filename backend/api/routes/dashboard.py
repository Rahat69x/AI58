"""Dashboard stats and metrics route for AI58."""

from collections import Counter
from typing import Optional, Dict, Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.database.session import get_db
from backend.models.entities import ProjectRun, UserFavorite, SavedOutput
from backend.projects.registry import PROJECT_REGISTRY, PROJECTS_BY_ID
from backend.core.security import get_current_user_optional

router = APIRouter(prefix="/dashboard", tags=["Dashboard Platform Metrics"])

@router.get("/stats")
def get_dashboard_stats(
    current_user: Optional[dict] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """Aggregated stats and platform breakdown satisfying all dashboard requirements."""
    total_projects = len(PROJECT_REGISTRY)
    beginner_count = sum(1 for p in PROJECT_REGISTRY if p["tier"] == "BEGINNER")
    intermediate_count = sum(1 for p in PROJECT_REGISTRY if p["tier"] == "INTERMEDIATE")
    advanced_count = sum(1 for p in PROJECT_REGISTRY if p["tier"] == "ADVANCED")

    # Category counts
    cat_counter = Counter(p["category"] for p in PROJECT_REGISTRY)
    categories = [{"name": cat, "count": count} for cat, count in cat_counter.most_common()]

    # Query recent runs
    user_id = int(current_user["sub"]) if current_user else None
    run_query = db.query(ProjectRun)
    if user_id:
        run_query = run_query.filter(ProjectRun.user_id == user_id)

    total_runs_count = run_query.count()
    recent_run_entities = run_query.order_by(ProjectRun.created_at.desc()).limit(8).all()

    recent_runs = []
    for r in recent_run_entities:
        proj = PROJECTS_BY_ID.get(r.project_id)
        recent_runs.append({
            "run_id": r.id,
            "project_id": r.project_id,
            "project_name": proj["name"] if proj else f"Project #{r.project_id}",
            "tier": proj["tier"] if proj else "UNKNOWN",
            "status": r.status,
            "execution_time_ms": r.execution_time_ms,
            "created_at": r.created_at.isoformat()
        })

    # Query favorites
    fav_ids = []
    saved_count = 0
    if user_id:
        favs = db.query(UserFavorite.project_id).filter(UserFavorite.user_id == user_id).all()
        fav_ids = [f[0] for f in favs]
        saved_count = db.query(SavedOutput).filter(SavedOutput.user_id == user_id).count()

    # Active projects (recently run distinct project IDs)
    recent_distinct_pids = [
        r[0] for r in db.query(ProjectRun.project_id)
        .distinct()
        .order_by(ProjectRun.created_at.desc())
        .limit(6)
        .all()
    ]
    active_projects = [
        {
            "id": pid,
            "name": PROJECTS_BY_ID[pid]["name"],
            "tier": PROJECTS_BY_ID[pid]["tier"],
            "slug": PROJECTS_BY_ID[pid]["slug"]
        }
        for pid in recent_distinct_pids if pid in PROJECTS_BY_ID
    ]

    return {
        "total_projects": total_projects,
        "beginner_count": beginner_count,
        "intermediate_count": intermediate_count,
        "advanced_count": advanced_count,
        "total_runs_executed": total_runs_count,
        "saved_outputs_count": saved_count,
        "platform_readiness_percentage": 100.0,
        "categories": categories,
        "recent_runs": recent_runs,
        "favorite_project_ids": fav_ids,
        "active_projects": active_projects
    }
