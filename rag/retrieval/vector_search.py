from uuid import UUID

from sqlalchemy.orm import Session

from backend.app.models.document_chunk import DocumentChunk
from rag.retrieval.models import RetrievalResult


def search_similar_chunks(
    db: Session,
    query_embedding: list[float],
    limit: int = 5,
    document_id: UUID | None = None,
) -> list[RetrievalResult]:
    """Return ranked document chunks with similarity scores."""

    if not query_embedding:
        raise ValueError("Query embedding must not be empty.")

    if len(query_embedding) != 384:
        raise ValueError("Query embedding must contain 384 dimensions.")

    if limit <= 0:
        raise ValueError("Limit must be greater than zero.")

    distance = DocumentChunk.embedding.cosine_distance(query_embedding)

    query = (
        db.query(DocumentChunk, distance)
        .filter(DocumentChunk.embedding.is_not(None))
    )

    if document_id is not None:
        query = query.filter(
            DocumentChunk.document_id == document_id
        )

    rows = (
        query
        .order_by(distance)
        .limit(limit)
        .all()
    )

    return [
        RetrievalResult(
            chunk_id=chunk.id,
            document_id=chunk.document_id,
            text=chunk.text,
            score=1.0 - float(distance_value),
            page_number=chunk.page_number,
            section=chunk.section,
        )
        for chunk, distance_value in rows
    ]
