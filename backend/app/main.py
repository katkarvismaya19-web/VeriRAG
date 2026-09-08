from fastapi import FastAPI

from backend.app.api.documents import router as documents_router


app = FastAPI(
    title="VeriRAG API",
    description="Evidence-Grounded Enterprise Knowledge & Decision Intelligence Platform",
    version="0.1.0",
)


app.include_router(documents_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "verirag-api",
        "version": "0.1.0",
    }