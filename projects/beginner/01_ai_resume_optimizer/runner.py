"""Runner for Project #01: AI Resume Optimizer (BEGINNER)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 1
PROJECT_NAME = "AI Resume Optimizer"
PROJECT_SLUG = "01_ai_resume_optimizer"
PROJECT_TIER = "BEGINNER"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute AI Resume Optimizer logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
