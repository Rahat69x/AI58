# AI58 — Unified AI Project Platform
> **58 Connected AI Projects** | Beginner (19) → Intermediate (20) → Advanced (19)

[![CI/CD Pipeline](https://github.com/ai58-platform/ai58/actions/workflows/ci.yml/badge.svg)](https://github.com/ai58-platform/ai58)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![React: 18.3](https://img.shields.io/badge/React-18.3-61dafb.svg)](https://react.dev)

---

## 1. Executive Platform Summary

**AI58** is a production-grade, unified AI platform that houses **58 interconnected, individually identifiable and runnable AI systems** in a single connected codebase.

None of the 58 projects are combined, skipped, renamed, or left as placeholders. Each project features:
- Dedicated module folder under `projects/<tier>/<slug>/`
- Independent execution runner (`runner.py`) powered by the centralized Shared AI Engine
- Architectural documentation (`docs.md`)
- Interactive workbench interface with sample presets, live JSON execution, output visualizations, and history tracking
- 8-point deployment checklist: `[x] Scaffold  [x] UI  [x] Backend  [x] AI integration  [x] Database  [x] Testing  [x] Documentation  [x] Deployment`

---

## 2. High-Level Architecture

```
                    AI PROJECT HUB (AI58)
                             |
             +---------------+---------------+
             |               |               |
         BEGINNER       INTERMEDIATE      ADVANCED
       01–19 (19)       20–39 (20)       40–58 (19)
             |               |               |
             +---------------+---------------+
                             |
                       SHARED CORE
                             |
          +------------------+------------------+
          |                  |                  |
      AI ENGINE          DATA ENGINE       USER SYSTEM
          |                  |                  |
      Model Layer       Dataset Layer      Auth (JWT)
      Prompt Layer      Processing         Profiles
      RAG Layer         Storage            Settings
      Agent Layer       Pipelines          History & Checklists
                             |
                       API / DATABASE
                             |
                         DASHBOARD
```

---

## 3. Centralized Shared AI Engine

The 11 centralized AI services located in `backend/services/ai_engine/`:

1. **LLM Service**: Multi-provider routing (Gemini, OpenAI, Anthropic) with an offline, high-precision built-in intelligence engine.
2. **Prompt Manager**: Role persona library and template interpolation.
3. **Agent Manager**: Multi-step reasoning loops with structured audit traces.
4. **RAG Engine**: Document chunking, vector indexing, semantic retrieval, and citation compilation.
5. **Embedding Service**: Deterministic normalized vector representations and cosine similarity calculations.
6. **Vector DB Interface**: In-memory and persisted collection store with top-k cosine similarity queries.
7. **Document Processor**: PDF text extraction, markdown parsing, and section segmentation.
8. **Speech-to-Text Service**: Audio transcription bridge and Web Speech API schemas.
9. **Text-to-Speech Service**: Multi-voice audio synthesis parameters and cue generation.
10. **Vision Service**: Image metadata analysis, OCR structure perception, and WCAG accessibility descriptions.
11. **Code Analysis Service**: Python AST parsing, static analysis, cyclomatic complexity estimation, and OWASP security vulnerability linting.

---

## 4. Master 58-Project Index

| # | Project Name | Tier | Category | Status |
| :-: | :--- | :--- | :--- | :-: |
| **01** | AI Resume Optimizer | BEGINNER | Career & Professional | `Ready` |
| **02** | Portfolio Builder | BEGINNER | Career & Professional | `Ready` |
| **03** | Interview Coach | BEGINNER | Career & Professional | `Ready` |
| **04** | Salary Negotiator | BEGINNER | Career & Professional | `Ready` |
| **05** | Daily Productivity Manager | BEGINNER | Productivity & Lifestyle | `Ready` |
| **06** | Email Summarizer | BEGINNER | Productivity & Lifestyle | `Ready` |
| **07** | Meeting Memory | BEGINNER | Productivity & Lifestyle | `Ready` |
| **08** | Career Path Recommender | BEGINNER | Career & Professional | `Ready` |
| **09** | Learning Mentor | BEGINNER | Education & Learning | `Ready` |
| **10** | Networking Assistant | BEGINNER | Career & Professional | `Ready` |
| **11** | Personal Task Manager | BEGINNER | Productivity & Lifestyle | `Ready` |
| **12** | Smart Calendar | BEGINNER | Productivity & Lifestyle | `Ready` |
| **13** | Study Planner | BEGINNER | Education & Learning | `Ready` |
| **14** | Job Application Tracker | BEGINNER | Career & Professional | `Ready` |
| **15** | Freelancing Proposal Writer | BEGINNER | Career & Professional | `Ready` |
| **16** | Work-Life Balance Manager | BEGINNER | Productivity & Lifestyle | `Ready` |
| **17** | Research Assistant | BEGINNER | Education & Learning | `Ready` |
| **18** | Remote Work Buddy | BEGINNER | Productivity & Lifestyle | `Ready` |
| **19** | Personal Branding Assistant | BEGINNER | Career & Professional | `Ready` |
| **20** | Code Reviewer | INTERMEDIATE | Developer Tools | `Ready` |
| **21** | Bug Hunter | INTERMEDIATE | Developer Tools | `Ready` |
| **22** | PR Reviewer | INTERMEDIATE | Developer Tools | `Ready` |
| **23** | API Tester | INTERMEDIATE | Developer Tools | `Ready` |
| **24** | Code Explainer | INTERMEDIATE | Developer Tools | `Ready` |
| **25** | Code Refactorer | INTERMEDIATE | Developer Tools | `Ready` |
| **26** | System Design Partner | INTERMEDIATE | System Architecture & Security | `Ready` |
| **27** | Documentation Writer | INTERMEDIATE | Developer Tools | `Ready` |
| **28** | DSA Practice Buddy | INTERMEDIATE | Education & Learning | `Ready` |
| **29** | Learning Tracker | INTERMEDIATE | Education & Learning | `Ready` |
| **30** | Code Debugger | INTERMEDIATE | Developer Tools | `Ready` |
| **31** | Repo Summarizer | INTERMEDIATE | Developer Tools | `Ready` |
| **32** | DevOps Automator | INTERMEDIATE | Developer Tools | `Ready` |
| **33** | Testing Assistant | INTERMEDIATE | Developer Tools | `Ready` |
| **34** | Cloud Cost Optimizer | INTERMEDIATE | Developer Tools | `Ready` |
| **35** | Data Cleaner | INTERMEDIATE | Data & ML | `Ready` |
| **36** | SQL Query Helper | INTERMEDIATE | Developer Tools | `Ready` |
| **37** | AI Project Builder | INTERMEDIATE | Developer Tools | `Ready` |
| **38** | Model Evaluator | INTERMEDIATE | Data & ML | `Ready` |
| **39** | Security Vulnerability Finder | INTERMEDIATE | System Architecture & Security | `Ready` |
| **40** | Fitness Coach | ADVANCED | Health & Well-being | `Ready` |
| **41** | Nutrition Planner | ADVANCED | Health & Well-being | `Ready` |
| **42** | Habit Tracker | ADVANCED | Productivity & Lifestyle | `Ready` |
| **43** | Mood Journal | ADVANCED | Health & Well-being | `Ready` |
| **44** | Book Summarizer | ADVANCED | Education & Learning | `Ready` |
| **45** | Meditation Guide | ADVANCED | Health & Well-being | `Ready` |
| **46** | Skill Coach | ADVANCED | Education & Learning | `Ready` |
| **47** | Time Audit Tool | ADVANCED | Productivity & Lifestyle | `Ready` |
| **48** | Language Learning Buddy | ADVANCED | Education & Learning | `Ready` |
| **49** | Sleep Coach | ADVANCED | Health & Well-being | `Ready` |
| **50** | Emergency Overload Predictor | ADVANCED | Public Good & Civic | `Ready` |
| **51** | Disaster Relief Coordinator | ADVANCED | Public Good & Civic | `Ready` |
| **52** | Eco-Friendly Living Guide | ADVANCED | Public Good & Civic | `Ready` |
| **53** | Traffic Flow Optimizer | ADVANCED | Public Good & Civic | `Ready` |
| **54** | Job Matcher | ADVANCED | Career & Professional | `Ready` |
| **55** | Education Tutor | ADVANCED | Education & Learning | `Ready` |
| **56** | Healthcare Symptom Checker | ADVANCED | Health & Well-being | `Ready` |
| **57** | Accessibility Assistant | ADVANCED | Public Good & Civic | `Ready` |
| **58** | Financial Literacy Guide | ADVANCED | Public Good & Civic | `Ready` |

---

## 5. Quickstart Guide

### Prerequisites
- Python 3.11+
- Node.js 20+

### Option A: Unified Server (Single Command)
The built frontend bundle is automatically served by FastAPI:
```bash
# 1. Install dependencies
pip install -r requirements.txt
cd frontend && npm install && npm run build && cd ..

# 2. Start unified server
python -m uvicorn backend.api.main:app --host 0.0.0.0 --port 8000
```
Open **http://localhost:8000** in your browser.

### Option B: Separate Development Servers
```bash
# Terminal 1: Backend API
python -m uvicorn backend.api.main:app --reload --port 8000

# Terminal 2: Frontend Vite Dev Server
cd frontend
npm run dev
```
Open **http://localhost:3000** with hot module replacement (HMR).

### Option C: Docker Compose
```bash
docker compose up --build
```

---

## 6. Verification & Automated Count Check

Run the automated count check script before any pull request or deployment:
```bash
python scripts/verify_project_count.py
```
This script validates:
- Exactly 58 total registered projects
- Exactly 19 Beginner tier projects
- Exactly 20 Intermediate tier projects
- Exactly 19 Advanced tier projects
- All 58 directories, runners, docs, and inits exist on disk
- All 58 project runners execute successfully asynchronously

### Run Pytest Suite
```bash
pytest tests/ -v
```

---

## 7. Repository Layout

```
AI58/
├── backend/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── projects.py
│   │   │   ├── dashboard.py
│   │   │   ├── roadmap.py
│   │   │   └── ai_services.py
│   │   └── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── database/
│   │   └── session.py
│   ├── models/
│   │   └── entities.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── project.py
│   ├── services/
│   │   ├── ai_engine/ (11 shared services)
│   │   └── data_engine/
│   └── projects/
│       ├── registry.py
│       └── runner_dispatcher.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── DashboardView.jsx
│   │   │   ├── ProjectWorkbench.jsx
│   │   │   ├── RoadmapView.jsx
│   │   │   ├── AiEngineLab.jsx
│   │   │   └── AuthModal.jsx
│   │   ├── lib/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── projects/
│   ├── beginner/ (01_ai_resume_optimizer ... 19_personal_branding_assistant)
│   ├── intermediate/ (20_code_reviewer ... 39_security_vulnerability_finder)
│   └── advanced/ (40_fitness_coach ... 58_financial_literacy_guide)
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_SPECIFICATION.md
│   └── 58_PROJECTS_CATALOG.md
├── scripts/
│   ├── scaffold_projects.py
│   └── verify_project_count.py
├── tests/
│   ├── test_count.py
│   ├── test_auth.py
│   ├── test_projects.py
│   └── test_ai_engine.py
├── deployment/
│   ├── nginx.conf
│   └── ai58.service
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── LICENSE
├── SECURITY.md
└── CONTRIBUTING.md
```
