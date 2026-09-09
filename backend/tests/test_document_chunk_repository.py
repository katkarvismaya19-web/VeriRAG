from uuid import uuid4

from backend.app.database import SessionLocal
from backend.app.models.document import Document
from backend.app.models.document_chunk import DocumentChunk
from backend.app.repositories.document_chunk import (
    create_chunks,
    get_chunks_by_document,
)


def test_create_and_get_document_chunks():
    db = SessionLocal()

    try:
        document = Document(
            id=uuid4(),
            title="Repository Test Document",
            filename="repository-test.pdf",
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
                text="This is the first chunk.",
                page_number=1,
            ),
            DocumentChunk(
                document_id=document.id,
                chunk_index=1,
                text="This is the second chunk.",
                page_number=2,
            ),
        ]

        created_chunks = create_chunks(
            db,
            chunks,
        )

        assert len(created_chunks) == 2

        retrieved_chunks = get_chunks_by_document(
            db,
            document.id,
        )

        assert len(retrieved_chunks) == 2

        assert retrieved_chunks[0].chunk_index == 0
        assert retrieved_chunks[0].text == "This is the first chunk."
        assert retrieved_chunks[0].page_number == 1

        assert retrieved_chunks[1].chunk_index == 1
        assert retrieved_chunks[1].text == "This is the second chunk."
        assert retrieved_chunks[1].page_number == 2

    finally:
        db.query(DocumentChunk).filter(
            DocumentChunk.document_id == document.id
        ).delete()

        db.query(Document).filter(
            Document.id == document.id
        ).delete()

        db.commit()
        db.close()