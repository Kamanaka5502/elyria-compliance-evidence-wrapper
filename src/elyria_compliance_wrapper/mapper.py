import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from jsonschema import validate

from . import __version__
from .crypto import sha256_json

ALLOWED_DECISIONS = {"ADMIT", "REFUSE", "NARROW", "HALT", "ESCALATE"}
ALLOWED_EFFECTS = {"BOUND", "NO_BIND", "PREVENTED", "PENDING"}
NON_ADMIT_FORBIDDEN_WORDS = ("execute", "allow", "admit")


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def schema_path(name: str) -> Path:
    return Path(__file__).resolve().parents[2] / "schemas" / name


def validate_receipt(receipt: Dict[str, Any]) -> None:
    path = schema_path("boundary_receipt.schema.json")
    if path.exists():
        validate(receipt, load_json(str(path)))

    decision = receipt.get("boundary_decision")
    effect = receipt.get("protected_effect")

    if decision not in ALLOWED_DECISIONS:
        raise ValueError(f"Unsupported boundary_decision: {decision}")
    if effect not in ALLOWED_EFFECTS:
        raise ValueError(f"Unsupported protected_effect: {effect}")


def compliance_posture(boundary_decision: str, protected_effect: str) -> str:
    if boundary_decision == "REFUSE" and protected_effect == "NO_BIND":
        return "effect_prevented_by_boundary"
    if boundary_decision == "HALT" and protected_effect == "PREVENTED":
        return "effect_prevented_by_boundary"
    if boundary_decision == "NARROW" and protected_effect == "PENDING":
        return "consequence_requires_narrowed_review"
    if boundary_decision == "ESCALATE" and protected_effect == "PENDING":
        return "consequence_requires_escalation"
    if boundary_decision == "ADMIT" and protected_effect == "BOUND":
        return "consequence_admitted_by_boundary"
    return "unknown_boundary_posture"


def no_refusal_conversion(packet: Dict[str, Any]) -> None:
    decision = packet.get("boundary_decision")
    if decision == "ADMIT":
        return

    text = json.dumps(packet, sort_keys=True).lower()
    for word in NON_ADMIT_FORBIDDEN_WORDS:
        if word in text:
            raise ValueError(f"Non-ADMIT packet contains forbidden wording: {word}")


def build_packet(receipt: Dict[str, Any]) -> Dict[str, Any]:
    validate_receipt(receipt)

    boundary_decision = receipt["boundary_decision"]
    protected_effect = receipt["protected_effect"]
    source_hash = sha256_json(receipt)

    packet = {
        "packet_type": "elyria_compliance_evidence_packet",
        "wrapper_version": __version__,
        "source_receipt_id": receipt["receipt_id"],
        "movement_id": receipt["movement_id"],
        "boundary_system": receipt["boundary_system"],
        "compliance_posture": compliance_posture(boundary_decision, protected_effect),
        "boundary_decision": boundary_decision,
        "protected_effect": protected_effect,
        "reason": receipt.get("reason", ""),
        "replay_status": receipt.get("replay_status", "UNKNOWN"),
        "review_note": "Compliance packet records an already-decided boundary outcome. It does not authorize execution.",
        "source_hash": source_hash,
        "created_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }

    no_refusal_conversion(packet)
    packet["packet_hash"] = sha256_json(packet)
    return packet
