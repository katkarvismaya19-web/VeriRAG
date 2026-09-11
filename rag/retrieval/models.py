from dataclasses import dataclass
from uuid import UUID


@dataclass
class RetrievalResult:
    """A retrieved document chunk with its similarity score and source metadata."""

    chunk_id: UUID
    document_id: UUID
    text: str
    score: float
    page_number: int | None = None
    section: str | None = None
