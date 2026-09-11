
from uuid import uuid4

from rag.generation.evidence import EvidenceContext, EvidenceItem
from rag.generation.generation_service import GenerationService


def test_generation_service_generates_answer_from_evidence():
    document_id = uuid4()

    evidence = EvidenceContext(
        items=[
            EvidenceItem(
                citation_id=1,
                chunk_id=uuid4(),
                document_id=document_id,
                text="Employees receive twenty days of annual paid leave.",
                score=0.88,
                page_number=12,
                section="Leave Policy",
            ),
            EvidenceItem(
                citation_id=2,
                chunk_id=uuid4(),
                document_id=document_id,
                text="Leave requests must be submitted through the HR portal.",
                score=0.81,
                page_number=13,
                section="Leave Policy",
            ),
        ]
    )

    service = GenerationService()

    result = service.generate(
        query="How much annual leave do employees receive?",
        evidence=evidence,
    )

    assert result.answer == (
        "Employees receive twenty days of annual paid leave."
    )

    assert result.has_evidence is True
    assert len(result.citations) == 2

    assert result.citations[0].citation_id == 1
    assert result.citations[0].page_number == 12
    assert result.citations[0].section == "Leave Policy"

    assert result.citations[1].citation_id == 2
    assert result.citations[1].page_number == 13
    assert result.citations[1].section == "Leave Policy"


def test_generation_service_refuses_to_answer_without_evidence():
    evidence = EvidenceContext(items=[])

    service = GenerationService()

    result = service.generate(
        query="What is the company's policy on Mars colonization?",
        evidence=evidence,
    )

    assert result.answer == (
        "I could not find sufficient evidence in the provided documents "
        "to answer this question."
    )

    assert result.citations == []
    assert result.has_evidence is False


def test_generation_service_rejects_empty_query():
    evidence = EvidenceContext(items=[])

    service = GenerationService()

    try:
        service.generate(
            query="",
            evidence=evidence,
        )
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == "Query must not be empty."

