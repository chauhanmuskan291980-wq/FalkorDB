
from app.db.connection import get_graph

graph = get_graph()


def remove_duplicate_relationships(
    relationship_type: str,
    source_label: str,
    target_label: str,
    source_id: str,
    target_id: str,
) -> None:
    # Keep one relationship for each source-target pair.
    query = f"""
        MATCH (source:{source_label})-[r:{relationship_type}]->(target:{target_label})
        WITH source, target, collect(r) AS relationships
        WHERE size(relationships) > 1
        UNWIND relationships[1..] AS duplicate
        DELETE duplicate
    """
    graph.query(query)
    print(f"Checked {relationship_type} relationships.")


remove_duplicate_relationships(
    "USED_DEVICE", "Account", "Device", "account_id", "device_id"
)

remove_duplicate_relationships(
    "MADE", "Account", "Transaction", "account_id", "transaction_id"
)

print("Cleanup completed.")
