
from app.db.connection import get_graph


def seed_graph() -> None:
    """Create a small synthetic fraud-investigation graph."""
    graph = get_graph()

    # Create two fictional customers.
    graph.query("""
        CREATE
            (:Customer {customer_id: 'CUS-001', name: 'Asha'}),
            (:Customer {customer_id: 'CUS-002', name: 'Riya'})
    """)

    # Create their accounts.
    graph.query("""
        CREATE
            (:Account {account_id: 'ACC-001'}),
            (:Account {account_id: 'ACC-002'})
    """)

    # Link each customer to an account.
    graph.query("""
        MATCH (c:Customer {customer_id: 'CUS-001'}),
              (a:Account {account_id: 'ACC-001'})
        CREATE (c)-[:OWNS]->(a)
    """)

    graph.query("""
        MATCH (c:Customer {customer_id: 'CUS-002'}),
              (a:Account {account_id: 'ACC-002'})
        CREATE (c)-[:OWNS]->(a)
    """)

    # Create a shared device associated with both accounts.
    graph.query("""
        CREATE (:Device {device_id: 'DEV-001'})
    """)

    graph.query("""
        MATCH (a:Account {account_id: 'ACC-001'}),
              (d:Device {device_id: 'DEV-001'})
        CREATE (a)-[:USED_DEVICE]->(d)
    """)

    graph.query("""
        MATCH (a:Account {account_id: 'ACC-002'}),
              (d:Device {device_id: 'DEV-001'})
        CREATE (a)-[:USED_DEVICE]->(d)
    """)

    print("Synthetic graph created successfully.")


if __name__ == "__main__":
    seed_graph()
