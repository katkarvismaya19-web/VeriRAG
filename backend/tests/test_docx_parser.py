from pathlib import Path

from rag.ingestion.parsers.docx import parse_docx


def test_parse_docx():
    docx_path = Path("data/uploads")

    docx_files = list(docx_path.glob("*.docx"))

    if not docx_files:
        return

    paragraphs = parse_docx(docx_files[0])

    assert isinstance(paragraphs, list)

    if paragraphs:
        first_paragraph = paragraphs[0]

        assert "paragraph_number" in first_paragraph
        assert "text" in first_paragraph
        