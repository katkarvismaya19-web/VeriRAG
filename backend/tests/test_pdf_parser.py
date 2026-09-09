from pathlib import Path

from pypdf import PdfWriter

from rag.ingestion.parsers.pdf import parse_pdf


def test_parse_pdf(tmp_path: Path):
    pdf_path = tmp_path / "test.pdf"

    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)

    with pdf_path.open("wb") as file:
        writer.write(file)

    pages = parse_pdf(pdf_path)

    assert isinstance(pages, list)
    assert len(pages) == 1

    assert pages[0]["page_number"] == 1
    assert "text" in pages[0]