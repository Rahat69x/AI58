"""Direct endpoints for testing and interacting with the 11 Shared AI Engine services."""

from typing import Dict, Any, Optional, List
from fastapi import APIRouter, Body
from pydantic import BaseModel

from backend.services.ai_engine import (
    llm_service, prompt_manager, agent_manager,
    embedding_service, vector_db, document_processor,
    rag_engine, speech_to_text_service, text_to_speech_service,
    vision_service, code_analysis_service
)
from backend.services.data_engine import data_engine

router = APIRouter(prefix="/ai-engine", tags=["Shared AI Engine Services"])

class LLMRequest(BaseModel):
    prompt: str
    system_prompt: Optional[str] = None
    temperature: float = 0.7

class RAGQueryRequest(BaseModel):
    collection: str = "default_docs"
    query: str
    top_k: int = 3

class CodeReviewRequest(BaseModel):
    code: str
    language: str = "python"

class TTSRequest(BaseModel):
    text: str
    voice: str = "nova-voice"
    rate: float = 1.0

@router.get("/services")
def list_shared_services():
    """List the 11 centralized shared AI services available on AI58."""
    return {
        "services": [
            {"id": "llm_service", "name": "LLM Service", "status": "active", "description": "Unified frontier & local generation"},
            {"id": "prompt_manager", "name": "Prompt Manager", "status": "active", "description": "Persona management and prompt templating"},
            {"id": "agent_manager", "name": "Agent Manager", "status": "active", "description": "Multi-step reasoning and tool dispatching"},
            {"id": "rag_engine", "name": "RAG Engine", "status": "active", "description": "Semantic document retrieval and context synthesis"},
            {"id": "embedding_service", "name": "Embedding Service", "status": "active", "description": "Deterministic normalized text vectorization"},
            {"id": "vector_db", "name": "Vector Database Interface", "status": "active", "description": "In-memory & persisted vector storage"},
            {"id": "document_processor", "name": "Document Processor", "status": "active", "description": "PDF/text chunking and section detection"},
            {"id": "speech_to_text", "name": "Speech-to-Text Service", "status": "active", "description": "Audio transcription modeling"},
            {"id": "text_to_speech", "name": "Text-to-Speech Service", "status": "active", "description": "Voice audio parameter synthesis"},
            {"id": "vision_service", "name": "Vision Service", "status": "active", "description": "Image metadata analysis and OCR layout"},
            {"id": "code_analysis", "name": "Code Analysis Service", "status": "active", "description": "AST parsing, linting, and vulnerability audits"}
        ]
    }

@router.post("/llm/generate")
async def generate_text(req: LLMRequest):
    text = await llm_service.generate_text(prompt=req.prompt, system_prompt=req.system_prompt, temperature=req.temperature)
    tokens = llm_service.count_tokens_estimate(text)
    return {"generated_text": text, "tokens_estimated": tokens, "provider": llm_service.provider}

@router.post("/code/analyze")
def analyze_code(req: CodeReviewRequest):
    ast_info = code_analysis_service.analyze_python_ast(req.code) if req.language.lower() == "python" else {}
    security_issues = code_analysis_service.scan_security_issues(req.code, req.language)
    maintainability = code_analysis_service.calculate_maintainability_index(req.code)
    return {
        "ast_metrics": ast_info,
        "security_issues": security_issues,
        "maintainability": maintainability
    }

@router.post("/rag/index-sample")
def index_sample_documents(docs: List[Dict[str, str]] = Body(...), collection: str = "default_docs"):
    total_chunks = 0
    for d in docs:
        c = rag_engine.ingest_document(collection, d.get("id", "doc"), d.get("text", ""))
        total_chunks += c
    return {"status": "indexed", "total_chunks": total_chunks, "collection": collection}

@router.post("/rag/query")
def query_rag(req: RAGQueryRequest):
    return rag_engine.build_rag_context(req.collection, req.query, top_k=req.top_k)

@router.post("/tts/synthesize")
def synthesize_speech(req: TTSRequest):
    return text_to_speech_service.synthesize_spec(req.text, voice=req.voice, rate=req.rate)

@router.get("/tts/voices")
def get_voices():
    return {"voices": text_to_speech_service.get_voices()}

@router.post("/data/clean-csv")
def clean_csv(csv_content: str = Body(..., media_type="text/plain")):
    return data_engine.clean_csv_data(csv_content)
