"""Automated 58-Project Count and Verification Script for AI58 Platform.
Enforces strict completion criteria:
- Total: 58 projects
- Beginner: 19 projects
- Intermediate: 20 projects
- Advanced: 19 projects
- Folder structure verification on disk
- Async runner execution check for every project
"""

import sys
import asyncio
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from backend.projects.registry import PROJECT_REGISTRY
from backend.projects.runner_dispatcher import dispatch_project_run, RUNNER_REGISTRY

EXPECTED_TOTAL = 58
EXPECTED_BEGINNER = 19
EXPECTED_INTERMEDIATE = 20
EXPECTED_ADVANCED = 19

async def verify_platform():
    print("=" * 70)
    print("AI58 PLATFORM — AUTOMATED COUNT & HEALTH VERIFICATION")
    print("=" * 70)

    # 1. Registry Count Check
    total = len(PROJECT_REGISTRY)
    beginner = [p for p in PROJECT_REGISTRY if p["tier"] == "BEGINNER"]
    intermediate = [p for p in PROJECT_REGISTRY if p["tier"] == "INTERMEDIATE"]
    advanced = [p for p in PROJECT_REGISTRY if p["tier"] == "ADVANCED"]

    b_count = len(beginner)
    i_count = len(intermediate)
    a_count = len(advanced)

    print(f"Registry Total Projects : {total} (Expected: {EXPECTED_TOTAL})")
    print(f"Beginner Tier (01-19)   : {b_count} (Expected: {EXPECTED_BEGINNER})")
    print(f"Intermediate (20-39)    : {i_count} (Expected: {EXPECTED_INTERMEDIATE})")
    print(f"Advanced Tier (40-58)   : {a_count} (Expected: {EXPECTED_ADVANCED})")

    assert total == EXPECTED_TOTAL, f"Count Mismatch! Expected {EXPECTED_TOTAL}, got {total}"
    assert b_count == EXPECTED_BEGINNER, f"Beginner count mismatch! Expected {EXPECTED_BEGINNER}, got {b_count}"
    assert i_count == EXPECTED_INTERMEDIATE, f"Intermediate count mismatch! Expected {EXPECTED_INTERMEDIATE}, got {i_count}"
    assert a_count == EXPECTED_ADVANCED, f"Advanced count mismatch! Expected {EXPECTED_ADVANCED}, got {a_count}"
    print("\n[PASSED] Registry counts match expected specifications perfectly.\n")

    # 2. Filesystem Structure Check
    print("Verifying filesystem folders and module files...")
    projects_dir = BASE_DIR / "projects"
    missing_files = []

    for p in PROJECT_REGISTRY:
        tier_dir = p["tier"].lower()
        slug = p["slug"]
        proj_path = projects_dir / tier_dir / slug

        if not proj_path.exists():
            missing_files.append(f"Directory missing: {proj_path}")
            continue

        for req_file in ["__init__.py", "runner.py", "docs.md"]:
            f_path = proj_path / req_file
            if not f_path.exists():
                missing_files.append(f"Missing file: {f_path}")

    if missing_files:
        print("[FAILED] Missing filesystem files:")
        for m in missing_files:
            print(f"  - {m}")
        sys.exit(1)
    else:
        print("[PASSED] All 58 project directories, runners, docs, and inits verified on disk.\n")

    # 3. Execution Verification Check
    print("Testing async runner dispatch across all 58 projects...")
    run_failures = []
    for p in PROJECT_REGISTRY:
        pid = p["id"]
        default_in = p["default_input"]
        try:
            res = await dispatch_project_run(pid, default_in)
            if res.get("status") != "success":
                run_failures.append((pid, p["name"], "Status not success"))
        except Exception as e:
            run_failures.append((pid, p["name"], str(e)))

    if run_failures:
        print(f"[FAILED] {len(run_failures)} runners failed during execution:")
        for pid, name, err in run_failures:
            print(f"  Project #{pid:02d} ({name}): {err}")
        sys.exit(1)
    else:
        print(f"[PASSED] All 58 project runners executed successfully with 0 failures!\n")

    print("=" * 70)
    print("ALL VERIFICATION CHECKS PASSED: 58/58 PROJECTS READY")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(verify_platform())
