from pathlib import Path

from pypdf import PdfReader


def parse_pdf(file_path: str | Path) -> list[dict]:
    """
    Extract text from a PDF while preserving page boundaries.

    Returns one dictionary per page containing:
    - page number
    - extracted text
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    reader = PdfReader(path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        pages.append(
            {
                "page_number": page_number,
                "text": text.strip(),
            }
        )

    return pages