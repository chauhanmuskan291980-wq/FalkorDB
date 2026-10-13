
from app.db.connection import get_graph


def check_database() -> dict:
    """Check whether FalkorDB can execute a query."""
    try:
        graph = get_graph()
        result = graph.query("RETURN 1 AS health")

        if result.result_set and result.result_set[0][0] == 1:
            return {
                "status": "healthy",
                "database": "falkordb",
            }

        return {
            "status": "unhealthy",
            "database": "falkordb",
        }

    except Exception:
        # Avoid exposing internal connection details to API clients.
        return {
            "status": "unhealthy",
            "database": "falkordb",
        }
