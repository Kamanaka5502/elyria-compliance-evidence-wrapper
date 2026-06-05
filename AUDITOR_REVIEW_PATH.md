# Auditor Review Path

1. Confirm the source receipt is synthetic or authorized for review.
2. Confirm the runtime boundary decision is preserved.
3. Confirm the wrapper did not alter the decision.
4. Confirm the source receipt hash matches the packet.
5. Review mapped controls.
6. Review consequence posture.
7. Verify packet hash.
8. Determine whether private diligence is required.

## Private diligence trigger

Escalate to controlled review if the reviewer needs:

- production receipt internals
- private replay harness
- customer-specific control mapping
- deployment architecture
- protected runtime implementation
