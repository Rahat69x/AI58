"""Runner for Project #20: Code Reviewer (INTERMEDIATE)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 20
PROJECT_NAME = "Code Reviewer"
PROJECT_SLUG = "20_code_reviewer"
PROJECT_TIER = "INTERMEDIATE"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute Code Reviewer logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
