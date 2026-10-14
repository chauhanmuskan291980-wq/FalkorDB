from app.tools.flagged_transactions import find_flagged_transactions


def test_find_flagged_transactions():
    results = find_flagged_transactions("ACC-001")

    assert len(results) == 1
    assert results[0]["transaction_id"] == "TXN-002"
    assert results[0]["amount"] == 9500
    assert results[0]["status"] == "flagged"


def test_account_without_flagged_transactions():
    results = find_flagged_transactions("ACC-UNKNOWN")

    assert results == []