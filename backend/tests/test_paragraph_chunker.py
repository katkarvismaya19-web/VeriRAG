from rag.ingestion.chunking.paragraph_chunker import chunk_paragraphs


def test_chunk_paragraphs():
    paragraphs = [
        "This is the first paragraph.",
        "This is the second paragraph.",
        "This is the third paragraph.",
    ]

    chunks = chunk_paragraphs(
        paragraphs,
        chunk_size=70,
    )

    assert len(chunks) == 2
    assert chunks[0].chunk_index == 0
    assert chunks[1].chunk_index == 1

    assert "first paragraph" in chunks[0].text
    assert "second paragraph" in chunks[0].text
    assert "third paragraph" in chunks[1].text


def test_empty_paragraphs():
    assert chunk_paragraphs([]) == []


def test_invalid_chunk_size():
    try:
        chunk_paragraphs(
            ["Some paragraph"],
            chunk_size=0,
        )
        assert False
    except ValueError:
        assert True


def test_large_paragraph_is_split():
    paragraph = "A" * 2500

    chunks = chunk_paragraphs(
        [paragraph],
        chunk_size=1000,
    )

    assert len(chunks) == 3

    assert len(chunks[0].text) == 1000
    assert len(chunks[1].text) == 1000
    assert len(chunks[2].text) == 500