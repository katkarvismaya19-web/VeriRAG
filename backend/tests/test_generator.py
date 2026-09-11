
import pytest

from rag.generation.evidence import EvidenceContext
from rag.generation.generator import BaseGenerator
from rag.generation.models import GeneratedAnswer


class FakeGenerator(BaseGenerator):
    def generate(
        self,
        query: str,
        evidence: EvidenceContext,
    ) -> GeneratedAnswer:
        return GeneratedAnswer(
            answer="Test answer.",
            has_evidence=evidence.has_evidence,
        )


def test_base_generator_can_be_implemented():
    generator = FakeGenerator()

    evidence = EvidenceContext(items=[])

    result = generator.generate(
        query="Test question?",
        evidence=evidence,
    )

    assert isinstance(result, GeneratedAnswer)
    assert result.answer == "Test answer."
    assert result.has_evidence is False


def test_base_generator_is_abstract():
    with pytest.raises(TypeError):
        BaseGenerator()

