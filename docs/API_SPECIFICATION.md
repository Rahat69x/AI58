# AI58 Platform — API Specification

The AI58 API exposes RESTful endpoints with automatic OpenAPI documentation available at `/docs` and `/redoc`.

## Base URLs
- Local Development: `http://localhost:8000/api`
- Interactive Swagger: `http://localhost:8000/docs`

---

## 1. Authentication & User System (`/api/auth`)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/auth/register` | Register new user account with hashed password | No |
| `POST` | `/api/auth/login` | Authenticate credentials and receive signed JWT | No |
| `GET` | `/api/auth/profile` | Retrieve active user profile and roles | Yes (Bearer) |
| `PUT` | `/api/auth/preferences` | Update theme, AI provider, and API keys | Yes (Bearer) |
| `DELETE` | `/api/auth/account` | Permanently delete account and execution history | Yes (Bearer) |

---

## 2. Project Registry & Workbench (`/api/projects`)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/projects` | List all 58 projects with tier/category/search filters | Optional |
| `GET` | `/api/projects/{id}` | Retrieve single project metadata and docs | Optional |
| `POST` | `/api/projects/{id}/run` | Execute project runner with custom/default inputs | Optional |
| `GET` | `/api/projects/{id}/history`| Fetch past execution runs for this project | Optional |
| `POST` | `/api/projects/{id}/favorite`| Toggle star/favorite status | Yes (Bearer) |
| `PUT` | `/api/projects/{id}/checklist`| Update 8-point deployment checklist state | Yes (Bearer) |
| `POST` | `/api/projects/{id}/save-output`| Save execution output to portfolio | Yes (Bearer) |

---

## 3. Dashboard Metrics (`/api/dashboard`)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/dashboard/stats` | Aggregated counts (58 total, 19 B, 20 I, 19 A), active/recent runs | Optional |

---

## 4. Visual Roadmap (`/api/roadmap`)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/roadmap` | 3-tier level hierarchy (01-19, 20-39, 40-58) with checklists | Optional |

---

## 5. Shared AI Engine (`/api/ai-engine`)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/ai-engine/services` | List status of all 11 centralized AI services | No |
| `POST` | `/api/ai-engine/llm/generate` | Generate text via provider router | No |
| `POST` | `/api/ai-engine/code/analyze` | Run AST parsing, metrics, and security scan | No |
| `POST` | `/api/ai-engine/data/clean-csv`| Clean CSV data, impute missing, detect outliers | No |
| `POST` | `/api/ai-engine/rag/query` | Retrieve semantic context and citations | No |
| `POST` | `/api/ai-engine/tts/synthesize`| Generate voice synthesis audio specs | No |
