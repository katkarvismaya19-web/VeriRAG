from pathlib import Path

from docx import Document


def parse_docx(file_path: str | Path) -> list[dict]:
    """
    Extract text from a DOCX document while preserving paragraph order.

    Returns one dictionary per paragraph containing:
    - paragraph number
    - extracted text
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"DOCX file not found: {path}")

    document = Document(path)

    paragraphs = []

    for paragraph_number, paragraph in enumerate(
        document.paragraphs,
        start=1,
    ):
        text = paragraph.text.strip()

        if text:
            paragraphs.append(
                {
                    "paragraph_number": paragraph_number,
                    "text": text,
                }
            )

    return paragraphs