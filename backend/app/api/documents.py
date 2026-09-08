from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from backend.app.api.dependencies import get_db
from backend.app.models.document import Document
from backend.app.schemas.document import DocumentResponse


router = APIRouter(
    prefix="/api/v1/documents",
    tags=["documents"],
)


UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post(
    "/",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    extension = Path(file.filename or "").suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF and DOCX files are supported.",
        )

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File size must not exceed 10 MB.",
        )

    document_id = UUID(bytes=__import__("uuid").uuid4().bytes)

    safe_filename = f"{document_id}{extension}"
    file_path = UPLOAD_DIR / safe_filename

    file_path.write_bytes(contents)

    document = Document(
        id=document_id,
        title=Path(file.filename or "Untitled").stem,
        filename=file.filename or "unknown",
        file_type=extension.lstrip("."),
        status="UPLOADED",
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "id": str(document.id),
        "filename": document.filename,
        "file_type": document.file_type,
        "status": document.status,
    }