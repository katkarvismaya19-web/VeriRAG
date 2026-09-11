from sqlalchemy.orm import Session

from rag.embeddings.embedding_service import EmbeddingService
from rag.retrieval.models import RetrievalResult
from rag.retrieval.vector_search import search_similar_chunks


class RetrievalService:
    """Retrieve relevant document chunks for a natural-language query."""

    def __init__(
        self,
        embedding_service: EmbeddingService | None = None,
        min_score: float = 0.75,
    ):
        if not 0.0 <= min_score <= 1.0:
            raise ValueError("min_score must be between 0.0 and 1.0.")

        self.embedding_service = embedding_service or EmbeddingService()
        self.min_score = min_score

    def retrieve(
        self,
        db: Session,
        query: str,
        limit: int = 5,
    ) -> list[RetrievalResult]:
        """Embed a query and return sufficiently relevant document chunks."""

        if not query or not query.strip():
            raise ValueError("Query must not be empty.")

        if limit <= 0:
            raise ValueError("Limit must be greater than zero.")

        query_embedding = self.embedding_service.embed_text(query)

        results = search_similar_chunks(
            db=db,
            query_embedding=query_embedding,
            limit=limit,
        )

        return [
            result
            for result in results
            if result.score >= self.min_score
        ]