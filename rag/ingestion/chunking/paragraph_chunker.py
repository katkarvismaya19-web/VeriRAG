from dataclasses import dataclass

from rag.ingestion.chunking.text_chunker import chunk_text


@dataclass
class ParagraphChunk:
    text: str
    chunk_index: int


def chunk_paragraphs(
    paragraphs: list[str],
    chunk_size: int = 1000,
) -> list[ParagraphChunk]:
    """
    Create chunks while preserving paragraph boundaries when possible.

    If an individual paragraph is larger than chunk_size,
    fall back to the standard text chunker for that paragraph.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    chunks = []
    chunk_index = 0

    current_paragraphs = []
    current_length = 0

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        paragraph_length = len(paragraph)

        # Handle paragraphs that are too large on their own.
        if paragraph_length > chunk_size:
            if current_paragraphs:
                chunks.append(
                    ParagraphChunk(
                        text="\n\n".join(current_paragraphs),
                        chunk_index=chunk_index,
                    )
                )

                chunk_index += 1
                current_paragraphs = []
                current_length = 0

            large_chunks = chunk_text(
                paragraph,
                chunk_size=chunk_size,
                chunk_overlap=0,
            )

            for text in large_chunks:
                chunks.append(
                    ParagraphChunk(
                        text=text,
                        chunk_index=chunk_index,
                    )
                )

                chunk_index += 1

            continue

        # Start a new chunk if adding this paragraph would exceed
        # the maximum chunk size.
        if (
            current_paragraphs
            and current_length + paragraph_length + 2 > chunk_size
        ):
            chunks.append(
                ParagraphChunk(
                    text="\n\n".join(current_paragraphs),
                    chunk_index=chunk_index,
                )
            )

            chunk_index += 1
            current_paragraphs = []
            current_length = 0

        current_paragraphs.append(paragraph)
        current_length += paragraph_length + 2

    # Store the final chunk.
    if current_paragraphs:
        chunks.append(
            ParagraphChunk(
                text="\n\n".join(current_paragraphs),
                chunk_index=chunk_index,
            )
        )

    return chunks