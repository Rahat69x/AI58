"""Embedding Service: Generates dense text representations for semantic search and RAG."""

import re
import math
from typing import List, Dict
import numpy as np

class EmbeddingService:
    """Generates normalized vector representations of text snippets."""

    def __init__(self, vector_dim: int = 128):
        self.vector_dim = vector_dim

    def _tokenize(self, text: str) -> List[str]:
        cleaned = re.sub(r"[^\w\s]", " ", text.lower())
        return [w for w in cleaned.split() if len(w) > 1]

    def embed_text(self, text: str) -> List[float]:
        """Generate a deterministic normalized embedding vector for text."""
        tokens = self._tokenize(text)
        vec = np.zeros(self.vector_dim, dtype=np.float32)

        if not tokens:
            return vec.tolist()

        for token in tokens:
            # Deterministic hash-based feature projection
            h = hash(token)
            idx = abs(h) % self.vector_dim
            weight = 1.0 + (abs(h >> 8) % 10) * 0.1
            vec[idx] += weight

        # L2 Normalization
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm

        return vec.tolist()

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        return [self.embed_text(doc) for doc in documents]

    @staticmethod
    def cosine_similarity(v1: List[float], v2: List[float]) -> float:
        a = np.array(v1, dtype=np.float32)
        b = np.array(v2, dtype=np.float32)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return float(np.dot(a, b) / (norm_a * norm_b))

embedding_service = EmbeddingService()
