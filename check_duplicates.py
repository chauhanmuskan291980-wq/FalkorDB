
from app.db.connection import get_graph

graph = get_graph()

queries = {
    "Device relationships": """
        MATCH (a:Account)-[r:USED_DEVICE]->(d:Device)
        RETURN a.account_id, d.device_id, count(r)
    """,
    "Transaction relationships": """
        MATCH (a:Account)-[r:MADE]->(t:Transaction)
        RETURN a.account_id, t.transaction_id, count(r)
    """,
}

for title, query in queries.items():
    print(f"\n--- {title} ---")
    result = graph.query(query)

    for row in result.result_set:
        print(row)
