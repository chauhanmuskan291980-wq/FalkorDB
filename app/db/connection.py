
import os

from dotenv import load_dotenv
from falkordb import FalkorDB

load_dotenv()

FALKORDB_HOST = os.getenv("FALKORDB_HOST", "localhost")
FALKORDB_PORT = int(os.getenv("FALKORDB_PORT", "6379"))
GRAPH_NAME = os.getenv("FALKORDB_GRAPH", "learning_graph")


def get_graph():
    """Connect to FalkorDB and return the selected graph."""
    db = FalkorDB(
        host=FALKORDB_HOST,
        port=FALKORDB_PORT,
    )
    return db.select_graph(GRAPH_NAME)
