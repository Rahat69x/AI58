"""Runner for Project #31: Repo Summarizer (INTERMEDIATE)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 31
PROJECT_NAME = "Repo Summarizer"
PROJECT_SLUG = "31_repo_summarizer"
PROJECT_TIER = "INTERMEDIATE"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute Repo Summarizer logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
