
from rag.generation.evidence import EvidenceContext
from rag.generation.models import Citation, GeneratedAnswer


class GenerationService:
    """Generate evidence-grounded answers from retrieved evidence."""

    INSUFFICIENT_EVIDENCE_MESSAGE = (
        "I could not find sufficient evidence in the provided documents "
        "to answer this question."
    )

    def generate(
        self,
        query: str,
        evidence: EvidenceContext,
    ) -> GeneratedAnswer:
        """Generate an answer using only the supplied evidence."""

        if not query or not query.strip():
            raise ValueError("Query must not be empty.")

        if not evidence.has_evidence:
            return GeneratedAnswer(
                answer=self.INSUFFICIENT_EVIDENCE_MESSAGE,
                citations=[],
                has_evidence=False,
            )

        answer = evidence.items[0].text

        citations = [
            Citation(
                citation_id=item.citation_id,
                page_number=item.page_number,
                section=item.section,
            )
            for item in evidence.items
        ]

        return GeneratedAnswer(
            answer=answer,
            citations=citations,
            has_evidence=True,
        )

