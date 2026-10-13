
from app.db.connection import get_graph

graph = get_graph()

result = graph.query("""
CREATE (p:Person {name: 'Muskan', role: 'Backend Developer'})
RETURN p.name, p.role
""")

print("Node created successfully!")
print(result.result_set)
