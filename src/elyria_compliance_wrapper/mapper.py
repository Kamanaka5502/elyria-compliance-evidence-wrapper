import json
import uuid
from pathlib import Path
from typing import Any, Dict, List

import yaml
from jsonschema import validate

from . import __version__
from .crypto import sha256_json

VALID_DECISIONS = {"EXECUTE", "REFUSE", "HALT", "ESCALATE", "REDIRECT", "QUARANTINE"}


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_controls(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_receipt(receipt: Dict[str, Any]) -> None:
    schema_path = Path(__file__).resolve().parents[2] / "schemas" / "boundary_receipt.schema.json"
    if schema_path.exists():
        validate(receipt, load_json(str(schema_path)))
    decision = receipt.get("decision")
    if decision not in VALID_DECISIONS:
        raise ValueError(f"Unsupported decision: {decision}")


def consequence_posture(decision: str) -> str:
    if decision == "EXECUTE":
        return "effect_admitted_by_boundary"
    if decision == "REFUSE":
        return "effect_prevented_by_boundary"
    if decision == "HALT":
        return "continuation_stopped_by_boundary"
    if decision == "ESCALATE":
        return "authorized_review_required_before_effect"
    if decision == "REDIRECT":
        return "alternate_corridor_required_before_effect"
    if decision == "QUARANTINE":
        return "isolated_pending_review"
    return "unknown"


def map_controls(receipt: Dict[str, Any], controls_cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    corridor = receipt.get("corridor", "")
    mapped = []
    for control in controls_cfg.get("controls", []):
        corridors = control.get("corridors")
        if corridors and corridor not in corridors:
            continue
        fields = control.get("evidence_fields", [])
        mapped.append({
            "control_id": control.get("id"),
            "framework": control.get("framework"),
            "area": control.get("area"),
            "evidence_available": {field: field in receipt for field in fields},
        })
    return mapped


def build_packet(receipt: Dict[str, Any], controls_cfg: Dict[str, Any]) -> Dict[str, Any]:
    validate_receipt(receipt)
    decision = receipt["decision"]
    review_map = controls_cfg.get("default_review_posture", {})
    packet = {
        "packet_id": f"cep-{uuid.uuid4()}",
        "wrapper_name": controls_cfg.get("wrapper", {}).get("name", "Elyria Compliance Evidence Wrapper"),
        "wrapper_version": controls_cfg.get("wrapper", {}).get("version", __version__),
        "source_receipt_hash": sha256_json(receipt),
        "source_receipt_id": receipt.get("receipt_id"),
        "source_decision": decision,
        "corridor": receipt.get("corridor"),
        "consequence_posture": consequence_posture(decision),
        "review_posture": review_map.get(decision, "review_required"),
        "control_mappings": map_controls(receipt, controls_cfg),
        "evidence_summary": {
            "reason_code": receipt.get("reason_code"),
            "protected_effect": receipt.get("protected_effect"),
            "authority_basis": receipt.get("authority_basis", ""),
            "evidence_basis": receipt.get("evidence_basis", ""),
            "replay_basis": receipt.get("replay_basis", ""),
            "ai_origin": receipt.get("ai_origin", False),
        },
        "boundary_notice": "Compliance evidence does not create admissibility. It reports a prior boundary decision.",
    }
    packet["packet_hash"] = sha256_json(packet)
    return packet


def verify_packet(packet: Dict[str, Any]) -> bool:
    expected = packet.get("packet_hash")
    candidate = dict(packet)
    candidate.pop("packet_hash", None)
    return sha256_json(candidate) == expected
