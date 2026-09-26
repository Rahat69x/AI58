"""Vector Database Interface: In-memory & persisted vector storage with top-k similarity search."""

from typing import List, Dict, Any, Optional
from backend.services.ai_engine.embedding_service import embedding_service

class VectorDocument:
    def __init__(self, doc_id: str, text: str, metadata: Optional[Dict[str, Any]] = None, vector: Optional[List[float]] = None):
        self.doc_id = doc_id
        self.text = text
        self.metadata = metadata or {}
        self.vector = vector or embedding_service.embed_text(text)

class VectorDatabaseInterface:
    """Manages collections of vector embeddings and top-k cosine similarity queries."""

    def __init__(self):
        self.collections: Dict[str, Dict[str, VectorDocument]] = {}

    def get_or_create_collection(self, collection_name: str) -> Dict[str, VectorDocument]:
        if collection_name not in self.collections:
            self.collections[collection_name] = {}
        return self.collections[collection_name]

    def add_document(self, collection_name: str, doc_id: str, text: str, metadata: Optional[Dict[str, Any]] = None) -> VectorDocument:
        col = self.get_or_create_collection(collection_name)
        doc = VectorDocument(doc_id=doc_id, text=text, metadata=metadata)
        col[doc_id] = doc
        return doc

    def add_documents(self, collection_name: str, items: List[Dict[str, Any]]):
        for item in items:
            self.add_document(
                collection_name=collection_name,
                doc_id=item.get("id", str(hash(item.get("text", "")))),
                text=item.get("text", ""),
                metadata=item.get("metadata", {}),
            )

    def query(self, collection_name: str, query_text: str, top_k: int = 3) -> List[Dict[str, Any]]:
        col = self.get_or_create_collection(collection_name)
        if not col:
            return []

        query_vec = embedding_service.embed_text(query_text)
        scored = []
        for doc in col.values():
            sim = embedding_service.cosine_similarity(query_vec, doc.vector)
            scored.append({
                "id": doc.doc_id,
                "text": doc.text,
                "metadata": doc.metadata,
                "score": round(sim, 4),
            })

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]

    def clear_collection(self, collection_name: str):
        if collection_name in self.collections:
            del self.collections[collection_name]

vector_db = VectorDatabaseInterface()
