"""Runner for Project #13: Study Planner (BEGINNER)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 13
PROJECT_NAME = "Study Planner"
PROJECT_SLUG = "13_study_planner"
PROJECT_TIER = "BEGINNER"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute Study Planner logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
