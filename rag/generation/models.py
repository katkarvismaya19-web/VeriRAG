
from dataclasses import dataclass, field


@dataclass
class Citation:
    """A citation pointing to evidence used in an answer."""

    citation_id: int
    page_number: int | None = None
    section: str | None = None


@dataclass
class GeneratedAnswer:
    """Structured answer returned by the generation layer."""

    answer: str
    citations: list[Citation] = field(default_factory=list)
    has_evidence: bool = False

