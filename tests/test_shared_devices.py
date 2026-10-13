
from app.tools.shared_devices import find_shared_devices


def test_find_shared_devices():
    results = find_shared_devices("ACC-001")

    assert any(
        item["related_account_id"] == "ACC-002"
        and item["device_id"] == "DEV-001"
        for item in results
    )
