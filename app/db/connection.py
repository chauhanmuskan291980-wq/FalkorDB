
import os
from functools import lru_cache

from dotenv import load_dotenv
from falkordb import FalkorDB

load_dotenv()

FALKORDB_HOST = os.getenv("FALKORDB_HOST", "localhost")
FALKORDB_PORT = int(os.getenv("FALKORDB_PORT", "6379"))
GRAPH_NAME = os.getenv("FALKORDB_GRAPH", "traceguard_graph")


@lru_cache(maxsize=1)
def get_db() -> FalkorDB:
    """Create and reuse the FalkorDB client."""
    return FalkorDB(
        host=FALKORDB_HOST,
        port=FALKORDB_PORT,
    )


def get_graph():
    """Return the configured FalkorDB graph."""
    return get_db().select_graph(GRAPH_NAME)
