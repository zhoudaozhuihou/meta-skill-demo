# Lifecycle Reference

## State transitions

```text
DISCOVERY → INTENT → DESIGN → PLAN → BUILD → VERIFY → REVIEW → RELEASE → OPERATE
                               ↑          │        │                    │
                               └──────────┴────────┴──── remediation ──┘
OPERATE → INCIDENT → INTENT
```

## Entry criteria

### DISCOVERY
Use when repository state, current artifacts, or scope are not yet understood.

### INTENT
Use when the problem/outcome is missing, contradictory, or only available in conversation.

### DESIGN
Use when intent is stable but technical behavior/contracts are not.

### PLAN
Use when specification is sufficient but executable steps are missing.

### BUILD
Use only when a workable plan exists for non-trivial changes.

### VERIFY
Use after implementation changes or when validating an existing change.

### REVIEW
Use when verification evidence is available or when explicitly auditing an implementation.

### RELEASE
Use when a change is technically ready and release readiness/gates must be prepared.

### OPERATE
Use for post-release observation and operational follow-up.

### INCIDENT
Use for production/service failures, security events, major regressions, or repeated severe defects.

## Shortened path

Trivial low-risk work may use:

```text
DISCOVERY → BUILD → VERIFY
```

but expected behavior, affected files, and validation must still be understood.
