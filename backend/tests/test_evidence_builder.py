from uuid import uuid4

from rag.generation.evidence import EvidenceContext
from rag.generation.evidence_builder import build_evidence_context
from rag.retrieval.models import RetrievalResult


def test_build_evidence_context_creates_citation_ids():
    document_id = uuid4()

    results = [
        RetrievalResult(
            chunk_id=uuid4(),
            document_id=document_id,
            text="Employees receive twenty days of annual paid leave.",
            score=0.88,
            page_number=12,
        ),
        RetrievalResult(
            chunk_id=uuid4(),
            document_id=document_id,
            text="Employees must submit leave requests through the HR portal.",
            score=0.81,
            page_number=13,
        ),
    ]

    context = build_evidence_context(results)

    assert isinstance(context, EvidenceContext)
    assert context.has_evidence is True
    assert len(context.items) == 2

    assert context.items[0].citation_id == 1
    assert context.items[1].citation_id == 2

    assert context.items[0].text == (
        "Employees receive twenty days of annual paid leave."
    )
    assert context.items[0].score == 0.88
    assert context.items[0].page_number == 12

    assert context.items[1].text == (
        "Employees must submit leave requests through the HR portal."
    )
    assert context.items[1].score == 0.81
    assert context.items[1].page_number == 13


def test_build_evidence_context_handles_no_results():
    context = build_evidence_context([])

    assert isinstance(context, EvidenceContext)
    assert context.items == []
    assert context.has_evidence is False

