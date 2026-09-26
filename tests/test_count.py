"""Automated Project Count and Completeness Tests for AI58 Platform."""

import pytest
from pathlib import Path
from backend.projects.registry import PROJECT_REGISTRY, PROJECTS_BY_ID

BASE_DIR = Path(__file__).resolve().parent.parent

def test_exact_project_counts():
    """Verify strictly enforced completion criteria: 58 total, 19 beginner, 20 intermediate, 19 advanced."""
    total = len(PROJECT_REGISTRY)
    beginner = [p for p in PROJECT_REGISTRY if p["tier"] == "BEGINNER"]
    intermediate = [p for p in PROJECT_REGISTRY if p["tier"] == "INTERMEDIATE"]
    advanced = [p for p in PROJECT_REGISTRY if p["tier"] == "ADVANCED"]

    assert total == 58, f"Expected 58 projects, found {total}"
    assert len(beginner) == 19, f"Expected 19 beginner projects, found {len(beginner)}"
    assert len(intermediate) == 20, f"Expected 20 intermediate projects, found {len(intermediate)}"
    assert len(advanced) == 19, f"Expected 19 advanced projects, found {len(advanced)}"

def test_sequential_ids_and_unique_slugs():
    """Verify IDs are continuous 1..58 and slugs are strictly unique."""
    ids = [p["id"] for p in PROJECT_REGISTRY]
    assert ids == list(range(1, 59)), "Project IDs must be 1 to 58 consecutively"

    slugs = [p["slug"] for p in PROJECT_REGISTRY]
    assert len(slugs) == len(set(slugs)), "Project slugs must be unique"

def test_all_project_filesystem_artifacts_exist():
    """Verify each project has its own folder, __init__.py, runner.py, and docs.md."""
    projects_dir = BASE_DIR / "projects"

    for p in PROJECT_REGISTRY:
        tier_dir = p["tier"].lower()
        slug = p["slug"]
        proj_dir = projects_dir / tier_dir / slug

        assert proj_dir.exists(), f"Directory missing for {slug}: {proj_dir}"
        assert (proj_dir / "__init__.py").exists(), f"__init__.py missing for {slug}"
        assert (proj_dir / "runner.py").exists(), f"runner.py missing for {slug}"
        assert (proj_dir / "docs.md").exists(), f"docs.md missing for {slug}"
