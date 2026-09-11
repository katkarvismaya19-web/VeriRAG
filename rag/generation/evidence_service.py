from sqlalchemy.orm import Session

from rag.generation.evidence import EvidenceContext
from rag.generation.evidence_builder import build_evidence_context
from rag.retrieval.retrieval_service import RetrievalService


class EvidenceService:
    """Retrieve relevant chunks and convert them into citation-ready evidence."""

    def __init__(
        self,
        retrieval_service: RetrievalService | None = None,
    ):
        self.retrieval_service = retrieval_service or RetrievalService()

    def get_evidence(
        self,
        db: Session,
        query: str,
        limit: int = 5,
    ) -> EvidenceContext:
        """Retrieve relevant chunks and build an evidence context."""

        results = self.retrieval_service.retrieve(
            db=db,
            query=query,
            limit=limit,
        )

        return build_evidence_context(results)
    