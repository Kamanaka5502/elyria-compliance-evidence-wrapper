from elyria_compliance_wrapper.mapper import build_packet, compliance_posture
from elyria_compliance_wrapper.verify import check_packet


def make_receipt(decision="REFUSE", effect="NO_BIND"):
    return {
        "receipt_id": "br-test",
        "movement_id": "mv-test",
        "boundary_system": "Elyria / VERITA",
        "boundary_decision": decision,
        "reason": "test_reason",
        "protected_effect": effect,
        "replay_status": "PASSED",
        "timestamp": "2026-06-05T00:00:00Z",
    }


def test_refuse_packet_builds_and_checks():
    packet = build_packet(make_receipt())
    assert packet["compliance_posture"] == "effect_prevented_by_boundary"
    assert check_packet(packet)


def test_changed_packet_fails_check():
    packet = build_packet(make_receipt())
    packet["protected_effect"] = "PENDING"
    assert not check_packet(packet)


def test_posture_mapping_core_cases():
    assert compliance_posture("REFUSE", "NO_BIND") == "effect_prevented_by_boundary"
    assert compliance_posture("NARROW", "PENDING") == "consequence_requires_narrowed_review"
    assert compliance_posture("ESCALATE", "PENDING") == "consequence_requires_escalation"
