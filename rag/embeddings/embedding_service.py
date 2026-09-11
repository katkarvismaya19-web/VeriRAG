from sentence_transformers import SentenceTransformer


MODEL_NAME = "BAAI/bge-small-en-v1.5"


class EmbeddingService:
    """Generate vector embeddings for text using a local Sentence Transformer."""

    def __init__(self, model_name: str = MODEL_NAME):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str) -> list[float]:
        """Generate a normalized embedding for a single text string."""
        if not text or not text.strip():
            raise ValueError("Text must not be empty.")

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """Generate normalized embeddings for multiple text strings."""
        if not texts:
            return []

        if any(not text or not text.strip() for text in texts):
            raise ValueError("Texts must not contain empty strings.")

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()