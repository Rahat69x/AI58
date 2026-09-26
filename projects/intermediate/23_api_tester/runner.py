"""Runner for Project #23: API Tester (INTERMEDIATE)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 23
PROJECT_NAME = "API Tester"
PROJECT_SLUG = "23_api_tester"
PROJECT_TIER = "INTERMEDIATE"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute API Tester logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
