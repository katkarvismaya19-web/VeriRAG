from uuid import uuid4

from backend.app.database import SessionLocal
from backend.app.models.document import Document
from backend.app.models.document_chunk import DocumentChunk
from rag.embeddings.embedding_service import EmbeddingService
from rag.retrieval.vector_search import search_similar_chunks


def test_search_similar_chunks_returns_relevant_chunk():
    db = SessionLocal()
    document = None

    try:
        document = Document(
            id=uuid4(),
            title="Vector Search Integration Test",
            filename="vector-search-test.pdf",
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

        chunk_embeddings = embedding_service.embed_texts(
            [chunk.text for chunk in chunks]
        )

        for chunk, embedding in zip(chunks, chunk_embeddings):
            chunk.embedding = embedding

        db.commit()

        query = "How many days of paid annual leave do employees receive?"

        query_embedding = embedding_service.embed_text(query)

        results = search_similar_chunks(
            db=db,
            query_embedding=query_embedding,
            limit=3,
            document_id=document.id,
        )

        assert len(results) == 3

        top_result = results[0]

        assert top_result.text == (
            "Employees receive twenty days of annual paid leave."
        )

        assert top_result.document_id == document.id
        assert top_result.page_number == 1
        assert top_result.score > 0.0
        assert top_result.score <= 1.0
        assert results[0].score >= results[1].score
        assert results[1].score >= results[2].score
  
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

