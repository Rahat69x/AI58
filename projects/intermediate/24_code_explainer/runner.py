"""Runner for Project #24: Code Explainer (INTERMEDIATE)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 24
PROJECT_NAME = "Code Explainer"
PROJECT_SLUG = "24_code_explainer"
PROJECT_TIER = "INTERMEDIATE"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute Code Explainer logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
