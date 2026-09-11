
from abc import ABC, abstractmethod

from rag.generation.evidence import EvidenceContext
from rag.generation.models import GeneratedAnswer


class BaseGenerator(ABC):
    """Interface for evidence-grounded answer generators."""

    @abstractmethod
    def generate(
        self,
        query: str,
        evidence: EvidenceContext,
    ) -> GeneratedAnswer:
        """Generate an answer using the supplied evidence."""
        raise NotImplementedError

