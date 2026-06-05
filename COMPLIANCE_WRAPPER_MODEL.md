# Compliance Wrapper Model

## Placement

```text
Elyria / Veritas runtime boundary
  -> decision receipt
  -> replay result
  -> compliance evidence wrapper
  -> control mapping
  -> audit packet
```

The wrapper is downstream of the runtime boundary.

It does not create authority, admit consequence, or override a refusal.

## Inputs

A public-safe boundary receipt may include:

- receipt id
- corridor
- decision
- reason code
- protected effect
- authority basis
- evidence basis
- replay basis
- timestamp

## Outputs

A compliance packet includes:

- packet id
- wrapper version
- source receipt hash
- source decision
- consequence posture
- control mappings
- evidence summary
- review posture
- packet hash

## Boundary invariant

```text
No compliance packet can convert REFUSE, HALT, ESCALATE, REDIRECT, or QUARANTINE into EXECUTE.
```

Compliance evidence is descriptive. Runtime admission is governing.
