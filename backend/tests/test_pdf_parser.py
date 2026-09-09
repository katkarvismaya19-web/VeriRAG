from pathlib import Path

from rag.ingestion.parsers.pdf import parse_pdf


def test_parse_pdf():
    pdf_path = Path("data/uploads")

    pdf_files = list(pdf_path.glob("*.pdf"))

    assert pdf_files, "No PDF file found in data/uploads"

    pages = parse_pdf(pdf_files[0])

    assert isinstance(pages, list)
    assert len(pages) > 0

    first_page = pages[0]

    assert "page_number" in first_page
    assert "text" in first_page
    assert first_page["page_number"] == 1