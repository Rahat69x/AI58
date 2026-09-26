# AI58 Platform Architecture — Technical Blueprint

## 1. Executive Architecture Overview

**AI58** is a single connected AI project platform housing **58 interconnected, individually identifiable AI systems** categorized into three tiers:
- **Beginner Tier (Projects 01–19)**: Foundational AI utilities, career tools, and personal productivity agents.
- **Intermediate Tier (Projects 20–39)**: Developer tooling, code intelligence, testing engines, DevOps, and data pipelines.
- **Advanced Tier (Projects 40–58)**: High-complexity reasoning agents, domain coaches, simulation engines, and public good systems.

```
                    AI PROJECT HUB (AI58)
                             |
             +---------------+---------------+
             |               |               |
         BEGINNER       INTERMEDIATE      ADVANCED
          01–19            20–39            40–58
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

## 2. Shared AI Engine Architecture

Rather than duplicating AI logic across 58 separate projects, AI58 provides 11 centralized, high-performance shared services:

1. **LLM Service (`backend.services.ai_engine.llm_service`)**:
   - Provider router supporting Google Gemini, OpenAI, Anthropic, and the Built-in Intelligence Engine.
   - Built-in engine delivers instant, offline-capable, high-precision results without external API keys.

2. **Prompt Manager (`backend.services.ai_engine.prompt_manager`)**:
   - Manages role personas (Senior Reviewer, Career Coach, Clinical Triage, Financial Educator, ML Architect).
   - Parameterized prompt template injection and formatting.

3. **Agent Manager (`backend.services.ai_engine.agent_manager`)**:
   - Executes multi-step reasoning cycles (Thought → Plan → Action → Observation → Conclusion) with full audit traces.

4. **RAG Engine (`backend.services.ai_engine.rag_engine`)**:
   - Document chunking, vector indexing, semantic retrieval, and citation compilation.

5. **Embedding Service (`backend.services.ai_engine.embedding_service`)**:
   - Generates normalized deterministic text vector representations and computes cosine similarity.

6. **Vector Database Interface (`backend.services.ai_engine.vector_db_interface`)**:
   - Manages collections and top-k nearest-neighbor queries.

7. **Document Processor (`backend.services.ai_engine.document_processor`)**:
   - PDF, plain text, and markdown parsing, section detection, and overlapping chunking.

8. **Speech-to-Text Service (`backend.services.ai_engine.speech_to_text_service`)**:
   - Audio transcription formatting and Web Speech bridge schemas.

9. **Text-to-Speech Service (`backend.services.ai_engine.text_to_speech_service`)**:
   - Voice configuration (Nova, Echo, Zen, Atlas) and speech synthesis specifications.

10. **Vision Service (`backend.services.ai_engine.vision_service`)**:
    - Image dimension inspection, OCR structure simulation, and WCAG accessibility descriptions.

11. **Code Analysis Service (`backend.services.ai_engine.code_analysis_service`)**:
    - Python AST parsing, cyclomatic complexity calculation, security smell detection, and maintainability scoring.

---

## 3. Shared Data Engine

The **Data Engine** (`backend.services.data_engine.pipeline`) powers tabular and time-series projects:
- **Tabular Cleansing**: Automatically detects and imputes missing values, removes duplicate records, identifies outliers via Interquartile Range (IQR), and standardizes data types.
- **Time-Series Anomaly Detection**: Computes rolling Z-score deviations on continuous data streams for Project #50 (Emergency Overload Predictor) and Project #53 (Traffic Flow Optimizer).

---

## 4. User Account & Data Sovereignty System

AI58 implements complete account management:
- **Registration & Authentication**: Salted PBKDF2-HMAC-SHA256 password hashing with signed JWT bearer tokens.
- **User Profiles & Preferences**: Configurable theme, preferred tier, and custom API keys.
- **Execution History & Saved Outputs**: Persistent run logging in SQLite/PostgreSQL with execution duration.
- **8-Point Deployment Checklists**: Real-time progress tracking for all 58 projects.
- **Privacy Controls**: Permanent single-click account deletion and data scrubbing.
