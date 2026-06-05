import json
from datetime import datetime, timezone
from typing import Any, Dict

from . import __version__
from .crypto import sha256_json

ALLOWED_DECISIONS = {"ADMIT", "REFUSE", "NARROW", "HALT", "ESCALATE"}
ALLOWED_EFFECTS = {"BOUND", "NO_BIND", "PREVENTED", "PENDING"}
REQUIRED_FIELDS = (
    "receipt_id",
    "movement_id",
    "boundary_system",
    "boundary_decision",
    "reason",
    "protected_effect",
    "replay_status",
    "timestamp",
)


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_receipt(receipt: Dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_FIELDS if field not in receipt]
    if missing:
        raise ValueError(f"Missing required receipt fields: {', '.join(missing)}")

    if receipt["boundary_decision"] not in ALLOWED_DECISIONS:
        raise ValueError(f"Unsupported boundary_decision: {receipt['boundary_decision']}")
    if receipt["protected_effect"] not in ALLOWED_EFFECTS:
        raise ValueError(f"Unsupported protected_effect: {receipt['protected_effect']}")


def compliance_posture(boundary_decision: str, protected_effect: str) -> str:
    pair = (boundary_decision, protected_effect)
    mapping = {
        ("REFUSE", "NO_BIND"): "effect_prevented_by_boundary",
        ("HALT", "PREVENTED"): "effect_prevented_by_boundary",
        ("NARROW", "PENDING"): "consequence_requires_narrowed_review",
        ("ESCALATE", "PENDING"): "consequence_requires_escalation",
        ("ADMIT", "BOUND"): "consequence_admitted_by_boundary",
    }
    return mapping.get(pair, "unknown_boundary_posture")


def build_packet(receipt: Dict[str, Any]) -> Dict[str, Any]:
    validate_receipt(receipt)
    boundary_decision = receipt["boundary_decision"]
    protected_effect = receipt["protected_effect"]

    packet = {
        "packet_type": "elyria_compliance_evidence_packet",
        "source_receipt_id": receipt["receipt_id"],
        "movement_id": receipt["movement_id"],
        "boundary_system": receipt["boundary_system"],
        "compliance_posture": compliance_posture(boundary_decision, protected_effect),
        "boundary_decision": boundary_decision,
        "protected_effect": protected_effect,
        "reason": receipt["reason"],
        "replay_status": receipt["replay_status"],
        "review_note": "Compliance packet records an already-decided boundary outcome. It does not grant permission.",
        "source_hash": sha256_json(receipt),
        "created_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "wrapper_version": __version__,
    }
    packet["packet_hash"] = sha256_json(packet)
    return packet
