"""Runner for Project #06: Email Summarizer (BEGINNER)."""

from typing import Dict, Any, Optional
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

PROJECT_ID = 6
PROJECT_NAME = "Email Summarizer"
PROJECT_SLUG = "06_email_summarizer"
PROJECT_TIER = "BEGINNER"

async def run(inputs: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute Email Summarizer logic."""
    return await dispatch_project_run(PROJECT_ID, inputs, options)
