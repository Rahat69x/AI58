"""Pydantic Schemas for AI58 Projects, Runs, Checklists, and Outputs."""

from datetime import datetime
from typing import Optional, Any, Dict, List
from pydantic import BaseModel, Field, ConfigDict

class ChecklistSchema(BaseModel):
    scaffold: bool = True
    ui: bool = True
    backend: bool = True
    ai_integration: bool = True
    database: bool = True
    testing: bool = True
    documentation: bool = True
    deployment: bool = True

class ProjectMeta(BaseModel):
    id: int
    slug: str
    name: str
    difficulty: str  # BEGINNER, INTERMEDIATE, ADVANCED
    category: str
    description: str
    capabilities: List[str]
    inputs: Dict[str, Any]
    default_input: Dict[str, Any]
    technologies: List[str]
    status: str = "Ready"
    progress: int = 100
    checklist: ChecklistSchema
    is_favorite: bool = False

class ProjectRunRequest(BaseModel):
    inputs: Dict[str, Any] = Field(default_factory=dict)
    options: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ProjectRunResponse(BaseModel):
    project_id: int
    slug: str
    status: str
    execution_time_ms: float
    output: Dict[str, Any]
    run_id: Optional[int] = None
    created_at: str

class SavedOutputCreate(BaseModel):
    project_id: int
    title: str
    notes: Optional[str] = ""
    payload: Dict[str, Any]

class SavedOutputOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    project_id: int
    title: str
    notes: str
    payload: Dict[str, Any]
    created_at: datetime

class DashboardStats(BaseModel):
    total_projects: int = 58
    beginner_count: int = 19
    intermediate_count: int = 20
    advanced_count: int = 19
    active_runs_count: int = 0
    saved_outputs_count: int = 0
    completion_rate: float = 100.0
    categories: List[Dict[str, Any]]
    recent_runs: List[Dict[str, Any]]
    favorite_project_ids: List[int]
