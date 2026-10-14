
from fastapi import FastAPI
from app.api.investigations import router as investigations_router

app = FastAPI(
    title="TraceGuard AI",
    description="Evidence-backed fraud investigation using FalkorDB.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Confirm that the API process is running."""
    return {"status": "healthy", "service": "traceguard-api"}

app.include_router(investigations_router)