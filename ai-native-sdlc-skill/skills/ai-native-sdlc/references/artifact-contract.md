# Artifact Contract

Artifacts are durable hand-off contracts between humans and agents.

## Required properties

Each change artifact should be:

- change-scoped;
- human-readable;
- reviewable in version control;
- sufficient for the next stage;
- explicit about assumptions and unresolved questions;
- updated when reality diverges from the plan.

## Source-of-truth hierarchy

When conflicts exist, prefer:

1. explicit current user/product-owner decision;
2. approved current change artifact;
3. repository policy/instruction;
4. current code and tests;
5. historical documentation;
6. conversation memory.

Do not silently resolve material conflicts. Record the decision in the relevant artifact.

## Drift handling

Implementation may reveal that the specification or plan is wrong. Do not force the code to follow a stale artifact. Update the artifact and record the reason.
