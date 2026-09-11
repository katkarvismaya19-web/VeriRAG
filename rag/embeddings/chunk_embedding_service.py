from sqlalchemy.orm import Session

from backend.app.models.document_chunk import DocumentChunk
from rag.embeddings.embedding_service import EmbeddingService


class ChunkEmbeddingService:
    """Generate and persist embeddings for document chunks."""

    def __init__(self, embedding_service: EmbeddingService | None = None):
        self.embedding_service = embedding_service or EmbeddingService()

    def embed_chunks(
        self,
        db: Session,
        chunks: list[DocumentChunk],
    ) -> list[DocumentChunk]:
        """Generate embeddings for chunks and persist them."""

        if not chunks:
            return []

        texts = [chunk.text for chunk in chunks]

        embeddings = self.embedding_service.embed_texts(texts)

        for chunk, embedding in zip(chunks, embeddings):
            chunk.embedding = embedding

        db.commit()

        for chunk in chunks:
            db.refresh(chunk)

        return chunks