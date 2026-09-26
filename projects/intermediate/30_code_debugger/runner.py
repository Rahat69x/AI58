"""Runner for Project #30: Code Debugger (INTERMEDIATE)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 30
PROJECT_NAME = "Code Debugger"
PROJECT_SLUG = "30_code_debugger"
PROJECT_TIER = "INTERMEDIATE"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute Code Debugger logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
