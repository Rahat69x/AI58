"""Document Processor: Text extraction, PDF parsing, chunking, and structural analysis."""

import re
from typing import List, Dict, Any
from io import BytesIO

class DocumentProcessor:
    """Extracts, cleans, chunks, and segments structured documents."""

    def extract_text_from_bytes(self, content_bytes: bytes, filename: str) -> str:
        """Extract plain text from text, markdown, or PDF bytes."""
        lower_name = filename.lower()
        if lower_name.endswith(".pdf"):
            try:
                import pypdf
                reader = pypdf.PdfReader(BytesIO(content_bytes))
                pages = [page.extract_text() or "" for page in reader.pages]
                return "\n".join(pages)
            except Exception as e:
                return f"[PDF parsing fallback] Error: {str(e)}"
        else:
            try:
                return content_bytes.decode("utf-8", errors="replace")
            except Exception:
                return str(content_bytes)

    def chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
        """Split text into overlapping chunks."""
        words = text.split()
        if not words:
            return []

        chunks = []
        start = 0
        while start < len(words):
            end = min(start + chunk_size, len(words))
            chunk = " ".join(words[start:end])
            chunks.append(chunk)
            if end == len(words):
                break
            start += max(1, chunk_size - overlap)
        return chunks

    def detect_sections(self, text: str) -> Dict[str, str]:
        """Identify standard resume or document sections."""
        section_patterns = {
            "summary": r"(?:summary|objective|professional summary|about me)",
            "experience": r"(?:experience|employment history|work experience|career history)",
            "education": r"(?:education|academic background|qualifications)",
            "skills": r"(?:skills|technical skills|core competencies|technologies)",
            "projects": r"(?:projects|portfolio|personal projects)",
            "certifications": r"(?:certifications|licenses|courses)",
        }

        lines = text.split("\n")
        sections: Dict[str, List[str]] = {k: [] for k in section_patterns}
        current_section = "summary"

        for line in lines:
            line_strip = line.strip()
            if not line_strip:
                continue

            matched_sec = None
            for sec, pat in section_patterns.items():
                if re.match(rf"^#*\s*{pat}\s*:?$", line_strip, re.IGNORECASE):
                    matched_sec = sec
                    break

            if matched_sec:
                current_section = matched_sec
            else:
                sections[current_section].append(line_strip)

        return {k: "\n".join(v).strip() for k, v in sections.items() if v}

document_processor = DocumentProcessor()
