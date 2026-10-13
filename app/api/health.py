
from fastapi import APIRouter

from app.db.health import check_database

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check() -> dict:
    """Return the application and database health status."""
    database_status = check_database()

    if database_status["status"] != "healthy":
        return {
            "status": "degraded",
            "database": database_status["status"],
        }

    return {
        "status": "healthy",
        "database": database_status["status"],
    }

