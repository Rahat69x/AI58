"""Runner for Project #22: PR Reviewer (INTERMEDIATE)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 22
PROJECT_NAME = "PR Reviewer"
PROJECT_SLUG = "22_pr_reviewer"
PROJECT_TIER = "INTERMEDIATE"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute PR Reviewer logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
