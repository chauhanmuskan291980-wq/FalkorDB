
from app.db.connection import get_graph


def reset_graph() -> None:
    graph = get_graph()

    graph.query("MATCH (n) DETACH DELETE n")

    print("TraceGuard graph cleared successfully.")


if __name__ == "__main__":
    reset_graph()
