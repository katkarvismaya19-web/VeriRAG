from pathlib import Path

from rag.ingestion.parsers.docx import parse_docx
from rag.ingestion.parsers.pdf import parse_pdf


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
}


def parse_document(file_path: str | Path) -> list[dict]:
    """
    Parse a supported document using the appropriate parser.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        return parse_pdf(path)

    if extension == ".docx":
        return parse_docx(path)

    raise ValueError(
        f"Unsupported document type: {extension}. "
        f"Supported types: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
    )