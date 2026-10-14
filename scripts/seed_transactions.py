
from app.db.connection import get_graph


def seed_transactions() -> None:
    """Seed synthetic transactions without duplicate relationships."""
    graph = get_graph()

    transactions = [
        {
            "transaction_id": "TXN-001",
            "account_id": "ACC-001",
            "amount": 1200,
            "status": "completed",
        },
        {
            "transaction_id": "TXN-002",
            "account_id": "ACC-001",
            "amount": 9500,
            "status": "flagged",
        },
        {
            "transaction_id": "TXN-003",
            "account_id": "ACC-002",
            "amount": 8700,
            "status": "flagged",
        },
    ]

    for transaction in transactions:
        graph.query(
            """
            MERGE (a:Account {account_id: $account_id})
            MERGE (t:Transaction {
                transaction_id: $transaction_id
            })
            SET t.amount = $amount,
                t.status = $status
            MERGE (a)-[:MADE]->(t)
            """,
            transaction,
        )

    print("Synthetic transactions seeded successfully.")


if __name__ == "__main__":
    seed_transactions()
