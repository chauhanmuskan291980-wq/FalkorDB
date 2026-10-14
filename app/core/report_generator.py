
def generate_investigation_report(investigation: dict) -> dict:
    """Generate a readable report from graph-derived investigation evidence."""

    account_id = investigation["account_id"]
    evidence = investigation["evidence"]
    summary = investigation["summary"]

    flagged_transactions = evidence["flagged_transactions"]
    shared_devices = evidence["shared_devices"]

    findings = []

    for transaction in flagged_transactions:
        findings.append(
            {
                "type": "flagged_transaction",
                "description": (
                    f"Transaction {transaction['transaction_id']} "
                    f"has been flagged for account {account_id}. "
                    f"Amount: {transaction['amount']}."
                ),
                "evidence": transaction,
            }
        )

    for connection in shared_devices:
        findings.append(
            {
                "type": "shared_device",
                "description": (
                    f"Account {account_id} and account "
                    f"{connection['related_account_id']} share device "
                    f"{connection['device_id']}."
                ),
                "evidence": connection,
            }
        )

    if findings:
        conclusion = (
            "Review recommended: graph evidence contains one or more "
            "indicators that may warrant further investigation. "
            "These indicators alone do not establish fraud."
        )
    else:
        conclusion = (
            "No matching flagged transactions or shared-device connections "
            "were found by the current investigation tools. "
            "This does not prove that the account is free of fraud."
        )

    return {
        "account_id": account_id,
        "findings": findings,
        "summary": summary,
        "conclusion": conclusion,
    }
