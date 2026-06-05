<p align="center">
  <img src="assets/elyria-compliance-evidence-wrapper-hero.svg" alt="Elyria Compliance Evidence Wrapper" width="100%">
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-public%20proof%20surface-gold?style=for-the-badge">
  <img alt="Boundary" src="https://img.shields.io/badge/boundary-compliance%20evidence-0ea5e9?style=for-the-badge">
  <img alt="Runtime" src="https://img.shields.io/badge/runtime-not%20included-111827?style=for-the-badge">
  <img alt="Use" src="https://img.shields.io/badge/use-restricted%20evaluation-b91c1c?style=for-the-badge">
</p>

# Elyria Compliance Evidence Wrapper

Elyria Compliance Evidence Wrapper is a public-safe evidence translation proof surface. It converts already-decided Elyria / VERITA consequence-boundary receipts into compliance-readable evidence packets.

It does not govern execution.

It does not decide admissibility.

It does not authorize consequence.

It does not convert refusal into permission.

```text
Boundary first.
Evidence wrapper second.
Compliance review third.
```

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

## Core flow

```text
boundary receipt
  -> evidence packet builder
  -> compliance evidence packet
  -> deterministic packet hash
  -> verifier
```

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e .

elyria-wrap build examples/boundary_receipt_refuse.json --out out/refuse_packet.json
elyria-wrap verify out/refuse_packet.json
pytest -q
```

Expected output:

```text
packet written: out/refuse_packet.json
verification passed
tests passed
```

## Decision rule

Compliance does not make an action admissible.

A compliance packet is valid only as evidence about a boundary decision that already occurred.

## Reviewer documents

| Document | Purpose |
|---|---|
| `PUBLIC_DISCLOSURE_BOUNDARY.md` | Public/private boundary and non-certification posture. |
| `COMPLIANCE_WRAPPER_MODEL.md` | Placement of the wrapper downstream of runtime admission. |
| `CONTROL_MAPPING.md` | Public synthetic control mapping examples. |
| `REGULATED_REVIEW_PATH.md` | Regulated review path. |
| `NON_PRODUCTION_NOTICE.md` | Production-use restriction and diligence requirements. |
| `LICENSE` | Proprietary evaluation license. |

## Status

Protected public proof surface. Proprietary / restricted use. Evaluation only unless separate written agreement exists.
