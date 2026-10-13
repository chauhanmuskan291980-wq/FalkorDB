
from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="TraceGuard AI",
    description="Evidence-based AI fraud investigation platform.",
    version="0.1.0",
)

app.include_router(health_router)


@app.get("/", tags=["Root"])
def root() -> dict:
    """Return basic application information."""
    return {
        "name": "TraceGuard AI",
        "message": "Fraud investigation API is running.",
    }
