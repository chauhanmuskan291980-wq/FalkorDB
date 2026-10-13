
from app.db.connection import get_graph

graph = get_graph()

result = graph.query("RETURN 1 AS result")

print("FalkorDB connection successful!")
print(result.result_set)
