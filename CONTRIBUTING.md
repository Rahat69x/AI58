# Contributing to AI58 — Unified AI Project Platform

Thank you for your interest in contributing to the **AI58 Platform**. AI58 houses 58 interconnected AI projects spanning Beginner (19), Intermediate (20), and Advanced (19) tiers.

## Core Rules for Contributions
1. **Never drop, rename, or omit any project**: All 58 projects are permanent, individually identifiable modules.
2. **Use Shared Services**: All projects must leverage the Shared Core:
   - `services.ai_engine` (LLM, Prompt, Agent, RAG, Embedding, Vector DB, STT/TTS, Vision, Code Analysis)
   - `services.data_engine` (Dataset, Preprocessing, Normalization, Anomaly Detection)
3. **8-Point Checklist**:
   Every project maintains its deployment checklist:
   `[ ] Scaffold  [ ] UI  [ ] Backend  [ ] AI integration  [ ] Database  [ ] Testing  [ ] Documentation  [ ] Deployment`
4. **Verification**:
   Run the project count verification test before opening any pull request:
   ```bash
   python scripts/verify_project_count.py
   ```
   All 58 projects must pass count and health checks.

## Development Workflow
1. Fork and clone the repository.
2. Setup virtual environment and dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run backend:
   ```bash
   python -m uvicorn backend.api.main:app --reload --port 8000
   ```
4. Run frontend:
   ```bash
   cd frontend
   npm run dev
   ```
5. Run tests:
   ```bash
   pytest tests/
   ```
