
from app.db.connection import get_graph


def seed_graph() -> None:
    """Create the synthetic TraceGuard fraud-investigation graph."""
    graph = get_graph()

    # Create customers only if they do not already exist.
    graph.query("""
        MERGE (:Customer {customer_id: 'CUS-001'})
    """)
    graph.query("""
        MERGE (:Customer {customer_id: 'CUS-002'})
    """)

    # Create accounts only if they do not already exist.
    graph.query("""
        MERGE (:Account {account_id: 'ACC-001'})
    """)
    graph.query("""
        MERGE (:Account {account_id: 'ACC-002'})
    """)

    # Create one device.
    graph.query("""
        MERGE (:Device {device_id: 'DEV-001'})
    """)

    # Connect customers to accounts.
    graph.query("""
        MATCH (c:Customer {customer_id: 'CUS-001'}),
              (a:Account {account_id: 'ACC-001'})
        MERGE (c)-[:OWNS]->(a)
    """)

    graph.query("""
        MATCH (c:Customer {customer_id: 'CUS-002'}),
              (a:Account {account_id: 'ACC-002'})
        MERGE (c)-[:OWNS]->(a)
    """)

    # Connect both accounts to the shared device.
    graph.query("""
        MATCH (a:Account {account_id: 'ACC-001'}),
              (d:Device {device_id: 'DEV-001'})
        MERGE (a)-[:USED_DEVICE]->(d)
    """)

    graph.query("""
        MATCH (a:Account {account_id: 'ACC-002'}),
              (d:Device {device_id: 'DEV-001'})
        MERGE (a)-[:USED_DEVICE]->(d)
    """)

    print("Synthetic graph seeded successfully.")


if __name__ == "__main__":
    seed_graph()
