"""Runner for Project #08: Career Path Recommender (BEGINNER)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 8
PROJECT_NAME = "Career Path Recommender"
PROJECT_SLUG = "08_career_path_recommender"
PROJECT_TIER = "BEGINNER"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute Career Path Recommender logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
