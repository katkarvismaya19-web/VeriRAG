from rag.embeddings.embedding_service import EmbeddingService


def test_embed_text_returns_384_dimensions():
    service = EmbeddingService()

    embedding = service.embed_text(
        "VeriRAG provides evidence-grounded answers."
    )

    assert isinstance(embedding, list)
    assert len(embedding) == 384
    assert all(isinstance(value, float) for value in embedding)


def test_embed_texts_returns_one_embedding_per_text():
    service = EmbeddingService()

    texts = [
        "Human resources policy.",
        "Technical documentation.",
        "Financial report.",
    ]

    embeddings = service.embed_texts(texts)

    assert len(embeddings) == len(texts)
    assert all(len(embedding) == 384 for embedding in embeddings)


def test_empty_text_is_rejected():
    service = EmbeddingService()

    try:
        service.embed_text("")
        assert False, "Expected ValueError"
    except ValueError as error:
        assert str(error) == "Text must not be empty."


def test_empty_text_list_returns_empty_list():
    service = EmbeddingService()

    assert service.embed_texts([]) == []