
from app.db.connection import get_graph


def find_shared_devices(account_id: str) -> list[dict]:
    """Find other accounts connected through a shared device."""
    graph = get_graph()

    query = """
        MATCH (account:Account {account_id: $account_id})
              -[:USED_DEVICE]->(device:Device)
              <-[:USED_DEVICE]-(other:Account)
        WHERE other.account_id <> $account_id
        RETURN
            account.account_id AS account_id,
            device.device_id AS device_id,
            other.account_id AS related_account_id
    """

    result = graph.query(query, {"account_id": account_id})

    return [
        {
            "account_id": row[0],
            "device_id": row[1],
            "related_account_id": row[2],
        }
        for row in result.result_set
    ]
