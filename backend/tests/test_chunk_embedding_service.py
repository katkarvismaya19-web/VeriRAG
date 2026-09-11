from uuid import uuid4

from backend.app.database import SessionLocal
from backend.app.models.document import Document
from backend.app.models.document_chunk import DocumentChunk
from rag.embeddings.chunk_embedding_service import ChunkEmbeddingService


def test_embed_chunks_persists_embeddings():
    db = SessionLocal()
    document = None

    try:
        document = Document(
            id=uuid4(),
            title="Embedding Integration Test",
            filename="embedding-test.pdf",
            file_type="pdf",
            status="PROCESSED",
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        chunks = [
            DocumentChunk(
                document_id=document.id,
                chunk_index=0,
                text="VeriRAG retrieves evidence from enterprise documents.",
                page_number=1,
            ),
            DocumentChunk(
                document_id=document.id,
                chunk_index=1,
                text="The system generates semantic embeddings for retrieval.",
                page_number=2,
            ),
        ]

        db.add_all(chunks)
        db.commit()

        service = ChunkEmbeddingService()

        embedded_chunks = service.embed_chunks(
            db,
            chunks,
        )

        assert len(embedded_chunks) == 2

        for chunk in embedded_chunks:
            assert chunk.embedding is not None
            assert len(chunk.embedding) == 384
            assert all(isinstance(value, float) for value in chunk.embedding)

    finally:
        if document is not None:
            db.query(DocumentChunk).filter(
                DocumentChunk.document_id == document.id
            ).delete()

            db.query(Document).filter(
                Document.id == document.id
            ).delete()

            db.commit()

        db.close()