from app.db.connection import get_graph


def find_flagged_transactions(account_id: str) -> list[dict]:
    """Return flagged transactions associated with an account."""
    graph = get_graph()

    result = graph.query(
        """
        MATCH (a:Account {account_id: $account_id})-[:MADE]->(t:Transaction)
        WHERE t.status = 'flagged'
        RETURN
            a.account_id AS account_id,
            t.transaction_id AS transaction_id,
            t.amount AS amount,
            t.status AS status
        ORDER BY t.amount DESC
        """,
        {"account_id": account_id},
    )

    return [
        {
            "account_id": row[0],
            "transaction_id": row[1],
            "amount": row[2],
            "status": row[3],
        }
        for row in result.result_set
    ]