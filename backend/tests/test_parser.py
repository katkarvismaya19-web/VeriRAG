from pathlib import Path

import pytest

from rag.ingestion.parser import parse_document


def test_parse_unsupported_file_type(tmp_path: Path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is not supported.")

    with pytest.raises(ValueError, match="Unsupported document type"):
        parse_document(test_file)