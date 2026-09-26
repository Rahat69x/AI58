"""RAG Engine: Document indexing, context retrieval, and augmented generation."""

from typing import List, Dict, Any, Optional
from backend.services.ai_engine.document_processor import document_processor
from backend.services.ai_engine.vector_db_interface import vector_db

class RAGEngine:
    """Manages ingestion of corpora, semantic retrieval, and augmented context compilation."""

    def ingest_document(self, collection_name: str, doc_id: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> int:
        chunks = document_processor.chunk_text(content, chunk_size=200, overlap=40)
        items = []
        for i, chunk in enumerate(chunks):
            chunk_meta = (metadata or {}).copy()
            chunk_meta.update({"source_doc": doc_id, "chunk_index": i})
            items.append({
                "id": f"{doc_id}_chunk_{i}",
                "text": chunk,
                "metadata": chunk_meta,
            })
        vector_db.add_documents(collection_name, items)
        return len(chunks)

    def retrieve(self, collection_name: str, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        return vector_db.query(collection_name, query, top_k=top_k)

    def build_rag_context(self, collection_name: str, query: str, top_k: int = 3) -> Dict[str, Any]:
        results = self.retrieve(collection_name, query, top_k=top_k)
        context_blocks = []
        citations = []
        for res in results:
            context_blocks.append(f"Source [{res['id']}] (relevance: {res['score']}):\n{res['text']}")
            citations.append({
                "source": res["id"],
                "score": res["score"],
                "snippet": res["text"][:120] + "..." if len(res["text"]) > 120 else res["text"],
            })

        compiled_context = "\n\n".join(context_blocks)
        return {
            "query": query,
            "context": compiled_context,
            "citations": citations,
            "num_chunks_retrieved": len(results),
        }

rag_engine = RAGEngine()
