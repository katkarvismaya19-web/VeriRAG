from rag.generation.models import Citation, GeneratedAnswer


def test_generated_answer_can_store_answer_and_citations():
    citation = Citation(
        citation_id=1,
        page_number=12,
        section="Leave Policy",
    )

    result = GeneratedAnswer(
        answer="Employees receive twenty days of annual paid leave.",
        citations=[citation],
        has_evidence=True,
    )

    assert result.answer == (
        "Employees receive twenty days of annual paid leave."
    )
    assert len(result.citations) == 1

    assert result.citations[0].citation_id == 1
    assert result.citations[0].page_number == 12
    assert result.citations[0].section == "Leave Policy"

    assert result.has_evidence is True


def test_generated_answer_defaults_to_no_citations_and_no_evidence():
    result = GeneratedAnswer(
        answer="I could not find sufficient evidence to answer this question."
    )

    assert result.answer == (
        "I could not find sufficient evidence to answer this question."
    )
    assert result.citations == []
    assert result.has_evidence is False

