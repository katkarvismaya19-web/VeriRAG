from rag.ingestion.chunking.text_chunker import chunk_text


def test_chunk_text():
    text = "A" * 2500

    chunks = chunk_text(
        text,
        chunk_size=1000,
        chunk_overlap=200,
    )

    assert len(chunks) == 3
    assert len(chunks[0]) == 1000
    assert len(chunks[1]) == 1000
    assert len(chunks[2]) == 900


def test_empty_text():
    assert chunk_text("") == []


def test_invalid_overlap():
    try:
        chunk_text(
            "some text",
            chunk_size=100,
            chunk_overlap=100,
        )
        assert False
    except ValueError:
        assert True


def test_chunk_overlap():
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = chunk_text(
        text,
        chunk_size=10,
        chunk_overlap=3,
    )

    assert chunks[0] == "ABCDEFGHIJ"
    assert chunks[1] == "HIJKLMNOPQ"


def test_invalid_chunk_size():
    try:
        chunk_text(
            "some text",
            chunk_size=0,
            chunk_overlap=0,
        )
        assert False
    except ValueError:
        assert True