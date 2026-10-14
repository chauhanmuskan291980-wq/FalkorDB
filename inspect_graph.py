
from app.db.connection import get_graph

graph = get_graph()

print("Accounts:")
print(graph.query("""
    MATCH (a:Account)
    RETURN a.account_id, count(a)
""").result_set)

print("\nDevice relationships:")
print(graph.query("""
    MATCH (a:Account)-[r:USED_DEVICE]->(d:Device)
    RETURN a.account_id, d.device_id, id(r)
""").result_set)

print("\nTransaction relationships:")
print(graph.query("""
    MATCH (a:Account)-[r:MADE]->(t:Transaction)
    RETURN a.account_id, t.transaction_id, id(r)
""").result_set)
