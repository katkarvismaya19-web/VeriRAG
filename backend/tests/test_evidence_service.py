from uuid import uuid4

from rag.generation.evidence import EvidenceContext
from rag.generation.evidence_service import EvidenceService
from rag.retrieval.models import RetrievalResult


class FakeRetrievalService:
    def retrieve(self, db, query, limit=5):
        return [
            RetrievalResult(
                chunk_id=uuid4(),
                document_id=uuid4(),
                text="Employees receive twenty days of annual paid leave.",
                score=0.88,
                page_number=12,
            ),
            RetrievalResult(
                chunk_id=uuid4(),
                document_id=uuid4(),
                text="Leave requests must be submitted through the HR portal.",
                score=0.81,
                page_number=13,
            ),
        ]


def test_evidence_service_returns_evidence_context():
    service = EvidenceService(
        retrieval_service=FakeRetrievalService()
    )

    context = service.get_evidence(
        db=None,
        query="How much annual leave do employees receive?",
        limit=5,
    )

    assert isinstance(context, EvidenceContext)
    assert context.has_evidence is True
    assert len(context.items) == 2

    assert context.items[0].citation_id == 1
    assert context.items[0].score == 0.88
    assert context.items[0].page_number == 12

    assert context.items[1].citation_id == 2
    assert context.items[1].score == 0.81
    assert context.items[1].page_number == 13


def test_evidence_service_returns_empty_context_when_no_evidence():
    class EmptyRetrievalService:
        def retrieve(self, db, query, limit=5):
            return []

    service = EvidenceService(
        retrieval_service=EmptyRetrievalService()
    )

    context = service.get_evidence(
        db=None,
        query="What is the company's policy on Mars colonization?",
        limit=5,
    )

    assert isinstance(context, EvidenceContext)
    assert context.has_evidence is False
    assert context.items == []

