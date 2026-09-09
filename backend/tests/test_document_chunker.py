from uuid import uuid4

from rag.ingestion.chunking.document_chunker import (
    chunk_parsed_document,
)


def test_chunk_parsed_pdf():
    document_id = uuid4()

    parsed_content = [
        {
            "page_number": 1,
            "text": "This is page one content.",
        },
        {
            "page_number": 2,
            "text": "This is page two content.",
        },
    ]

    chunks = chunk_parsed_document(
        document_id=document_id,
        parsed_content=parsed_content,
        file_type="pdf",
        chunk_size=1000,
    )

    assert len(chunks) == 2

    assert chunks[0].document_id == document_id
    assert chunks[0].page_number == 1
    assert chunks[0].text == "This is page one content."

    assert chunks[1].document_id == document_id
    assert chunks[1].page_number == 2
    assert chunks[1].text == "This is page two content."


def test_chunk_parsed_docx():
    document_id = uuid4()

    parsed_content = [
        {
            "paragraph_number": 1,
            "text": "First paragraph.",
        },
        {
            "paragraph_number": 2,
            "text": "Second paragraph.",
        },
    ]

    chunks = chunk_parsed_document(
        document_id=document_id,
        parsed_content=parsed_content,
        file_type="docx",
        chunk_size=1000,
    )

    assert len(chunks) == 1

    assert chunks[0].document_id == document_id
    assert "First paragraph." in chunks[0].text
    assert "Second paragraph." in chunks[0].text


def test_reject_unsupported_file_type():
    document_id = uuid4()

    try:
        chunk_parsed_document(
            document_id=document_id,
            parsed_content=[],
            file_type="txt",
        )
        assert False
    except ValueError:
        assert True