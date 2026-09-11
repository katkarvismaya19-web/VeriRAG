from dataclasses import dataclass
from uuid import UUID


@dataclass
class EvidenceItem:
    """A piece of retrieved evidence that can be cited in an answer."""

    citation_id: int
    chunk_id: UUID
    document_id: UUID
    text: str
    score: float
    page_number: int | None = None
    section: str | None = None


@dataclass
class EvidenceContext:
    """Structured evidence supplied to the answer-generation layer."""

    items: list[EvidenceItem]

    @property
    def has_evidence(self) -> bool:
        """Return whether usable evidence is available."""
        return bool(self.items)