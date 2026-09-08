from fastapi import FastAPI

app = FastAPI(
    title="VeriRAG API",
    description="Evidence-Grounded Enterprise Knowledge & Decision Intelligence Platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "verirag-api",
        "version": "0.1.0",
    }