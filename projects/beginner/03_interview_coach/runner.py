"""Runner for Project #03: Interview Coach (BEGINNER)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 3
PROJECT_NAME = "Interview Coach"
PROJECT_SLUG = "03_interview_coach"
PROJECT_TIER = "BEGINNER"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute Interview Coach logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
