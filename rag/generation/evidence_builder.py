from rag.generation.evidence import EvidenceContext, EvidenceItem
from rag.retrieval.models import RetrievalResult


def build_evidence_context(
    results: list[RetrievalResult],
) -> EvidenceContext:
    """Convert retrieval results into citation-ready evidence."""

    items = [
        EvidenceItem(
            citation_id=index,
            chunk_id=result.chunk_id,
            document_id=result.document_id,
            text=result.text,
            score=result.score,
            page_number=result.page_number,
            section=result.section,
        )
        for index, result in enumerate(results, start=1)
    ]

    return EvidenceContext(items=items)
