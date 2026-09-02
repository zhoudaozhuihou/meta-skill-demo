# Architecture

## Layered model

```text
Human / Product Owner
        │
        ▼
AI-Native SDLC Orchestrator
        │
        ├── Artifact State
        ├── Lifecycle State
        ├── Risk Classification
        └── Skill Routing
        │
        ├──────── Specialized Skills
        │         security / API / UI / data / compliance / testing
        │
        ├──────── Narrow Agents
        │         planner / implementer / verifier / reviewer
        │
        ├──────── Deterministic Controls
        │         hooks / CI / branch protection / approvals
        │
        └──────── Evals + Observability
```

## Why artifact-driven

Chat context is transient, hard to audit, and difficult to share across independent agents. Change-scoped files are inspectable, versionable, and suitable as contracts between lifecycle stages.

## Why the orchestrator is thin

The SDLC skill owns state transitions and artifact quality. It should not become a giant repository of Java, React, cloud, security, or compliance rules. Those belong in specialized skills so they can evolve independently and be retrieved only when relevant.

## Why deterministic controls are external

An instruction can reduce mistakes but cannot guarantee compliance. Protected paths, production gates, secrets, branch rules, required tests, and mandatory approvals need enforceable mechanisms outside the model.
