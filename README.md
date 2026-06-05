<p align="center">
  <img src="assets/elyria-compliance-evidence-wrapper-hero.svg" alt="Elyria Compliance Evidence Wrapper" width="100%">
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-public%20proof%20surface-C7A86B?style=for-the-badge&labelColor=17202A&color=C7A86B">
  <img alt="Boundary" src="https://img.shields.io/badge/boundary-compliance%20evidence-8FA3B8?style=for-the-badge&labelColor=17202A&color=8FA3B8">
  <img alt="Runtime" src="https://img.shields.io/badge/runtime-not%20included-4F5A68?style=for-the-badge&labelColor=17202A&color=4F5A68">
  <img alt="Use" src="https://img.shields.io/badge/use-restricted%20evaluation-B8B2A6?style=for-the-badge&labelColor=17202A&color=B8B2A6">
</p>

<p align="center">
  <img alt="Packet" src="https://img.shields.io/badge/packet-deterministic%20hash-26313E?style=flat-square&labelColor=10151C&color=26313E">
  <img alt="Review" src="https://img.shields.io/badge/review-regulated%20path-596575?style=flat-square&labelColor=10151C&color=596575">
  <img alt="Authority" src="https://img.shields.io/badge/authority-boundary%20first-C7A86B?style=flat-square&labelColor=10151C&color=C7A86B">
  <img alt="Certification" src="https://img.shields.io/badge/certification-not%20claimed-6E6250?style=flat-square&labelColor=10151C&color=6E6250">
</p>

<div align="center">

# Elyria Compliance Evidence Wrapper

### Public-safe evidence translation for consequence-boundary decisions

**Boundary first. Evidence wrapper second. Compliance review third.**

</div>

---

## Position

Elyria Compliance Evidence Wrapper is a public-safe evidence translation proof surface.

It converts already-decided Elyria / VERITA consequence-boundary receipts into compliance-readable evidence packets.

It does not govern execution.

It does not decide admissibility.

It does not authorize consequence.

It does not convert refusal into permission.

```text
runtime boundary decides whether consequence may bind
wrapper translates the decision into compliance-readable evidence
reviewer verifies the packet and determines diligence posture
```

---

## Proof surface

| Surface | Function |
|---|---|
| Boundary receipt | Source decision from the governed runtime boundary. |
| Evidence packet | Compliance-readable record derived from the receipt. |
| Packet hash | Deterministic integrity check for review. |
| Verification command | Confirms the packet has not been altered. |
| Regulated review path | Guides enterprise, compliance, and regulator-facing diligence. |

---

## What this is

- compliance evidence wrapper
- evidence packet generator
- control-mapping surface
- receipt-to-review translator
- public-safe proof corridor for enterprise diligence

## What this is not

- not the Elyria runtime boundary
- not a separate runtime authority
- not the protected runtime authority
- not financial, clinical, legal, or security advice
- not production compliance certification
- not a substitute for regulated customer review
- not a release of protected runtime logic

---

## Core flow

```text
boundary receipt
  -> evidence packet builder
  -> compliance evidence packet
  -> deterministic packet hash
  -> verifier
  -> regulated review path
```

---

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e .

elyria-wrap build examples/boundary_receipt_refuse.json --out out/refuse_packet.json
elyria-wrap verify out/refuse_packet.json
python -m pytest -q
```

Expected output:

```text
packet written: out/refuse_packet.json
verification passed
tests passed
```

---

## Decision rule

Compliance does not make an action admissible.

A compliance packet is valid only as evidence about a boundary decision that already occurred.

```text
REFUSE remains REFUSE
HALT remains HALT
NARROW remains NARROW
ESCALATE remains ESCALATE
ADMIT remains ADMIT
```

The wrapper reports. It does not promote, override, or soften the boundary outcome.

---

## Reviewer documents

| Document | Purpose |
|---|---|
| `PUBLIC_DISCLOSURE_BOUNDARY.md` | Public/private boundary and non-certification posture. |
| `COMPLIANCE_WRAPPER_MODEL.md` | Placement of the wrapper downstream of runtime admission. |
| `CONTROL_MAPPING.md` | Public synthetic control mapping examples. |
| `REGULATED_REVIEW_PATH.md` | Regulated review path. |
| `NON_PRODUCTION_NOTICE.md` | Production-use restriction and diligence requirements. |
| `LICENSE` | Proprietary evaluation license. |

---

## Status

```text
PUBLIC PROOF SURFACE
PROPRIETARY / RESTRICTED USE
PROTECTED RUNTIME NOT INCLUDED
PRODUCTION CERTIFICATION NOT CLAIMED
```

Evaluation only unless a separate written agreement exists.
