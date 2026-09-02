# Iteration State Machine

```text
BASELINE
   ↓
ROLLOUT
   ↓
SAMPLE
   ↓
MAINTAIN_WIKI
   ↓
PROPOSE
   ├── no_action ──→ STOP/next iteration
   ↓
APPLY_CANDIDATE
   ↓
VALIDATE
   ↓
GATE
  / \
 /   \
ACCEPT ROLLBACK
 \   /
  \ /
RECORD_IMPACT
   ↓
NEXT_ITERATION
```

Failure during Wiki maintenance must not mutate accepted skills.

Failure during candidate application must discard the candidate workspace.

Failure during validation must be treated as rejection unless policy explicitly defines another outcome.
