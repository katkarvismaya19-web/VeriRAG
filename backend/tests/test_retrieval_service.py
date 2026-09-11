from uuid import uuid4

from backend.app.database import SessionLocal
from backend.app.models.document import Document
from backend.app.models.document_chunk import DocumentChunk
from rag.embeddings.embedding_service import EmbeddingService
from rag.retrieval.retrieval_service import RetrievalService


def test_retrieval_service_returns_relevant_chunks():
    db = SessionLocal()
    document = None

    try:
        document = Document(
            id=uuid4(),
            title="Retrieval Service Test",
            filename="retrieval-service-test.pdf",
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
                text="Employees receive twenty days of annual paid leave.",
                page_number=1,
            ),
            DocumentChunk(
                document_id=document.id,
                chunk_index=1,
                text="The company provides technical support for enterprise customers.",
                page_number=2,
            ),
            DocumentChunk(
                document_id=document.id,
                chunk_index=2,
                text="The office cafeteria serves lunch between noon and two PM.",
                page_number=3,
            ),
        ]

        db.add_all(chunks)
        db.commit()

        embedding_service = EmbeddingService()

        embeddings = embedding_service.embed_texts(
            [chunk.text for chunk in chunks]
        )

        for chunk, embedding in zip(chunks, embeddings):
            chunk.embedding = embedding

        db.commit()

        retrieval_service = RetrievalService(
            embedding_service=embedding_service,
            min_score=0.75,
        )

        results = retrieval_service.retrieve(
            db=db,
            query="How many days of paid annual leave do employees receive?",
            limit=3,
        )

        assert len(results) == 1

        assert results[0].text == (
            "Employees receive twenty days of annual paid leave."
        )

        assert results[0].page_number == 1
        assert results[0].score >= 0.75
        assert results[0].score <= 1.0

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


def test_retrieval_service_returns_no_evidence_for_unrelated_query():
    db = SessionLocal()
    document = None

    try:
        document = Document(
            id=uuid4(),
            title="Retrieval Insufficient Evidence Test",
            filename="retrieval-insufficient-evidence-test.pdf",
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
                text="Employees receive twenty days of annual paid leave.",
                page_number=1,
            ),
            DocumentChunk(
                document_id=document.id,
                chunk_index=1,
                text="The company provides technical support for enterprise customers.",
                page_number=2,
            ),
            DocumentChunk(
                document_id=document.id,
                chunk_index=2,
                text="The office cafeteria serves lunch between noon and two PM.",
                page_number=3,
            ),
        ]

        db.add_all(chunks)
        db.commit()

        embedding_service = EmbeddingService()

        embeddings = embedding_service.embed_texts(
            [chunk.text for chunk in chunks]
        )

        for chunk, embedding in zip(chunks, embeddings):
            chunk.embedding = embedding

        db.commit()

        retrieval_service = RetrievalService(
            embedding_service=embedding_service,
            min_score=0.75,
        )

        results = retrieval_service.retrieve(
            db=db,
            query="What is the company's policy on Mars colonization?",
            limit=3,
        )

        assert results == []

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
