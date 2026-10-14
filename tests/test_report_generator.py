
from app.core.report_generator import generate_investigation_report


def test_report_contains_flagged_transaction_and_shared_device():
    investigation = {
        "account_id": "ACC-001",
        "evidence": {
            "flagged_transactions": [
                {
                    "account_id": "ACC-001",
                    "transaction_id": "TXN-002",
                    "amount": 9500,
                    "status": "flagged",
                }
            ],
            "shared_devices": [
                {
                    "account_id": "ACC-001",
                    "device_id": "DEV-001",
                    "related_account_id": "ACC-002",
                }
            ],
        },
        "summary": {
            "flagged_transaction_count": 1,
            "shared_device_connection_count": 1,
        },
    }

    report = generate_investigation_report(investigation)

    assert report["account_id"] == "ACC-001"
    assert len(report["findings"]) == 2
    assert report["findings"][0]["type"] == "flagged_transaction"
    assert report["findings"][1]["type"] == "shared_device"
    assert "TXN-002" in report["findings"][0]["description"]
    assert "DEV-001" in report["findings"][1]["description"]
    assert "do not establish fraud" in report["conclusion"]


def test_report_handles_no_findings():
    investigation = {
        "account_id": "ACC-003",
        "evidence": {
            "flagged_transactions": [],
            "shared_devices": [],
        },
        "summary": {
            "flagged_transaction_count": 0,
            "shared_device_connection_count": 0,
        },
    }

    report = generate_investigation_report(investigation)

    assert report["account_id"] == "ACC-003"
    assert report["findings"] == []
    assert "does not prove" in report["conclusion"]
