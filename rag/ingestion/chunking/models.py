from dataclasses import dataclass
from uuid import UUID


@dataclass
class DocumentChunk:
    """
    A retrievable chunk of a document with source metadata.
    """

    document_id: UUID
    chunk_index: int
    text: str

    page_number: int | None = None
    section: str | None = None