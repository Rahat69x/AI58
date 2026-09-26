"""Test Suite for the 11 Shared AI Engine Services and Data Engine."""

import pytest
from backend.services.ai_engine import (
    embedding_service, vector_db, document_processor,
    rag_engine, code_analysis_service, text_to_speech_service
)
from backend.services.data_engine import data_engine

def test_embedding_and_similarity():
    v1 = embedding_service.embed_text("FastAPI backend microservices architecture")
    v2 = embedding_service.embed_text("FastAPI microservices and REST APIs")
    v3 = embedding_service.embed_text("Cooking recipes with olive oil and pasta")

    sim_related = embedding_service.cosine_similarity(v1, v2)
    sim_unrelated = embedding_service.cosine_similarity(v1, v3)

    assert sim_related > sim_unrelated
    assert 0.0 <= sim_related <= 1.0

def test_rag_pipeline():
    rag_engine.ingest_document("test_corpus", "doc_1", "Vector embeddings represent text in continuous vector space.")
    rag_engine.ingest_document("test_corpus", "doc_2", "FastAPI is a modern web framework for Python.")

    res = rag_engine.build_rag_context("test_corpus", "What are vector embeddings?", top_k=1)
    assert res["num_chunks_retrieved"] == 1
    assert "Vector embeddings" in res["context"]

def test_code_analysis():
    code = """
import os
def test_calc(x):
    eval('x + 1')
    return x * 2
"""
    ast_info = code_analysis_service.analyze_python_ast(code)
    assert ast_info["valid_syntax"] is True
    assert ast_info["num_functions"] == 1

    issues = code_analysis_service.scan_security_issues(code)
    assert any("eval" in i["rule"].lower() for i in issues)

def test_data_cleaner():
    raw_csv = "id,name,score\n1,Alex,90\n2,Bob,\n3,Alex,90\n4,Charlie,150"
    cleaned = data_engine.clean_csv_data(raw_csv)
    assert cleaned["success"] is True
    assert cleaned["duplicates_removed"] == 1
    assert cleaned["missing_values_imputed"] == 1

def test_tts_voices():
    voices = text_to_speech_service.get_voices()
    assert len(voices) >= 4
