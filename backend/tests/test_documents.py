from io import BytesIO

from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_upload_pdf():
    pdf_content = b"%PDF-1.4 fake pdf content"

    response = client.post(
        "/api/v1/documents/",
        files={
            "file": (
                "test.pdf",
                BytesIO(pdf_content),
                "application/pdf",
            )
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["filename"] == "test.pdf"
    assert data["file_type"] == "pdf"
    assert data["status"] == "UPLOADED"
    assert "id" in data


def test_reject_unsupported_file_type():
    response = client.post(
        "/api/v1/documents/",
        files={
            "file": (
                "test.txt",
                BytesIO(b"not a supported document"),
                "text/plain",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Only PDF and DOCX files are supported."
    )