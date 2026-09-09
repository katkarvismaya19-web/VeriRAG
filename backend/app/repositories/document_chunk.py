from uuid import UUID

from sqlalchemy.orm import Session

from backend.app.models.document_chunk import DocumentChunk


def create_chunks(
    db: Session,
    chunks: list[DocumentChunk],
) -> list[DocumentChunk]:
    """
    Persist document chunks in the database.
    """

    if not chunks:
        return []

    db.add_all(chunks)
    db.commit()

    for chunk in chunks:
        db.refresh(chunk)

    return chunks


def get_chunks_by_document(
    db: Session,
    document_id: UUID,
) -> list[DocumentChunk]:
    """
    Retrieve all chunks belonging to a document.
    """

    return (
        db.query(DocumentChunk)
        .filter(DocumentChunk.document_id == document_id)
        .order_by(DocumentChunk.chunk_index)
        .all()
    )