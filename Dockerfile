# Multi-stage Dockerfile for AI58 Platform

# Stage 1: Build Frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci || npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Python Backend & Unified Server
FROM python:3.13-slim AS runner
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend, projects, docs, scripts
COPY backend/ ./backend/
COPY projects/ ./projects/
COPY docs/ ./docs/
COPY scripts/ ./scripts/

# Copy built frontend assets
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

ENV ENVIRONMENT=production \
    BACKEND_HOST=0.0.0.0 \
    BACKEND_PORT=8000 \
    DATABASE_URL=sqlite:///./ai58.db

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "backend.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
