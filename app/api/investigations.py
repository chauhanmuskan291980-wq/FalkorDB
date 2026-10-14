
from fastapi import APIRouter

from app.tools.flagged_transactions import find_flagged_transactions
from app.tools.shared_devices import find_shared_devices

router = APIRouter(
    prefix="/investigations",
    tags=["Investigations"],
)


@router.get("/{account_id}")
def investigate_account(account_id: str) -> dict:
    """Collect graph evidence for a specific account."""

    flagged_transactions = find_flagged_transactions(account_id)
    shared_devices = find_shared_devices(account_id)

    return {
        "account_id": account_id,
        "evidence": {
            "flagged_transactions": flagged_transactions,
            "shared_devices": shared_devices,
        },
        "summary": {
            "flagged_transaction_count": len(flagged_transactions),
            "shared_device_connection_count": len(shared_devices),
        },
    }
