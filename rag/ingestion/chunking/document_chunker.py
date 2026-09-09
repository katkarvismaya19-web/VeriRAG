from uuid import UUID

from rag.ingestion.chunking.models import DocumentChunk
from rag.ingestion.chunking.paragraph_chunker import chunk_paragraphs
from rag.ingestion.chunking.text_chunker import chunk_text


def chunk_parsed_document(
    document_id: UUID,
    parsed_content: list[dict],
    file_type: str,
    chunk_size: int = 1000,
) -> list[DocumentChunk]:
    """
    Convert parsed document content into retrievable document chunks.

    PDF:
        Each parsed page is chunked independently while preserving
        the page number.

    DOCX:
        Parsed paragraphs are grouped into chunks while preserving
        paragraph boundaries.
    """

    chunks: list[DocumentChunk] = []

    if file_type == "pdf":
        for page in parsed_content:
            page_number = page["page_number"]
            text = page["text"]

            page_chunks = chunk_text(
                text,
                chunk_size=chunk_size,
                chunk_overlap=200,
            )

            for text_chunk in page_chunks:
                chunks.append(
                    DocumentChunk(
                        document_id=document_id,
                        chunk_index=len(chunks),
                        text=text_chunk,
                        page_number=page_number,
                    )
                )

    elif file_type == "docx":
        paragraphs = [
            item["text"]
            for item in parsed_content
            if item.get("text")
        ]

        paragraph_chunks = chunk_paragraphs(
            paragraphs,
            chunk_size=chunk_size,
        )

        for paragraph_chunk in paragraph_chunks:
            chunks.append(
                DocumentChunk(
                    document_id=document_id,
                    chunk_index=len(chunks),
                    text=paragraph_chunk.text,
                )
            )

    else:
        raise ValueError(
            f"Unsupported file type: {file_type}"
        )

    return chunks