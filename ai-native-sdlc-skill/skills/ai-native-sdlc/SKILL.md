# AI-Native SDLC

## Purpose

Use this skill to orchestrate non-trivial software engineering work as an artifact-driven, verifiable, governed lifecycle instead of a direct `request → code` interaction.

This skill is intentionally model-agnostic. It may be used by Claude Code, Codex, GitHub Copilot, OpenCode, LangGraph agents, or custom engineering agents.

## Governing rules

1. **Artifact > Conversation.** Important engineering intent and decisions must be persisted into structured artifacts.
2. **Plan before code.** For non-trivial changes, implementation must not begin before intent, specification, and plan are sufficiently clear.
3. **Deterministic outside, probabilistic inside.** Use the model for reasoning; use hooks, CI, policies, permissions, and approval systems for enforcement.
4. **Verify before complete.** Code generation is not completion. Execute available build, lint, test, static-analysis, and runtime checks.
5. **Review against intent.** Review the implementation against `intent.md`, `spec.md`, and `plan.md`, not only the diff.
6. **Preserve human gates.** Never bypass required approval, release, compliance, database, or production controls.
7. **Incident → Regression.** Significant failures and repeated agent mistakes should become eval or regression cases.
8. **Minimize context.** Load only task-relevant artifacts, source files, instructions, and specialized skills.

## Lifecycle states

Determine the current state before acting:

- `DISCOVERY`
- `INTENT`
- `DESIGN`
- `PLAN`
- `BUILD`
- `VERIFY`
- `REVIEW`
- `RELEASE`
- `OPERATE`
- `INCIDENT`

Inspect the repository before creating new artifacts. Look for existing change packages, issue/PR context, ADRs, instructions, skills, hooks, tests, and CI workflows.

## Change-scoped artifact location

Prefer:

```text
docs/changes/<CHANGE-ID>/
├── intent.md
├── spec.md
├── plan.md
├── verification.md
├── review.md
└── release.md
```

For incidents:

```text
docs/incidents/<INCIDENT-ID>/incident.md
```

Avoid one global `intent.md`/`spec.md`/`plan.md` when multiple changes may run concurrently.

## Stage 1 — Intent

Goal: capture the problem, desired outcome, actors, boundaries, constraints, success criteria, unknowns, and risks without prematurely locking in implementation.

Create/update `intent.md` using `templates/intent.md`.

A valid intent explains:

```text
WHAT
WHY
WHO
CONSTRAINTS
SUCCESS
UNKNOWN
```

Do not turn product intent directly into code.

## Stage 2 — Specification

Goal: translate intent into an implementable technical contract.

Read `intent.md`, inspect the relevant repository architecture and code, and route to specialized skills only when they are relevant (security, API, frontend, backend, database, compliance, testing, observability, etc.).

Create/update `spec.md` using `templates/spec.md`.

The specification should cover current state, target state, functional requirements, non-functional requirements, architecture, interfaces, data changes, failure modes, compatibility, migration, acceptance criteria, and trade-offs.

## Stage 3 — Implementation Plan

Goal: create a plan detailed enough that another competent engineer or agent can execute it without relying on the previous conversation.

Create/update `plan.md` using `templates/plan.md`.

The plan must identify:

- files to add/modify/remove;
- implementation order;
- interface or contract changes;
- configuration/dependency/database changes;
- security and compatibility considerations;
- tests;
- exact verification commands or mechanisms when discoverable;
- risks;
- rollback;
- definition of done.

Quality test:

> Could a competent engineer who has never seen the conversation implement this change using only the repository and `plan.md`?

If not, improve the plan.

## Stage 4 — Build

Implement from the artifact chain:

```text
intent.md + spec.md + plan.md + repository instructions + relevant skills
```

Rules:

- inspect before modifying;
- prefer existing conventions and abstractions;
- do not invent files, APIs, database objects, dependencies, commands, or environment variables without checking;
- keep changes cohesive and scoped;
- avoid unrelated refactors;
- preserve backward compatibility where required;
- obey generated/protected-path rules and tool permissions.

## Stage 5 — Verify

Discover actual verification commands from repository evidence such as `CLAUDE.md`, `AGENTS.md`, `README`, `Makefile`, `package.json`, `pyproject.toml`, `pom.xml`, `build.gradle`, scripts, and CI workflows.

Run applicable checks, typically:

```text
format → lint → typecheck → build → unit → integration → security/static analysis → E2E/runtime
```

Do not invent commands.

Record verification evidence in `verification.md` using `templates/verification.md` when the change is non-trivial or auditable evidence is useful.

If verification fails, do not claim completion. Capture the error, diagnose, fix when in scope, and rerun.

## Stage 6 — Review

Review the implementation against the artifact chain, not only the diff.

Use the repository's `REVIEW.md` or equivalent when present. Otherwise inspect relevant dimensions:

- correctness;
- security;
- maintainability;
- performance;
- reliability;
- compatibility;
- test coverage;
- architecture;
- data integrity;
- observability;
- accessibility;
- compliance.

Use severity: `BLOCKER`, `HIGH`, `MEDIUM`, `LOW`, `NIT`.

Every material finding should contain location, problem, impact, evidence, and recommended fix.

Complex changes may delegate to narrow independent reviewers. Do not create unnecessary reviewer fan-out for small changes.

## Stage 7 — Release

Before release, verify that required checks, review, migration readiness, configuration, rollback, observability, and approvals are in place.

Create `release.md` when appropriate using `templates/release.md`.

Production is a privileged transition:

```text
Agent → Build → Verify → Review → Staging/Release Ready → POLICY/HUMAN GATE → Production
```

Never bypass mandatory production approval.

## Stage 8 — Operate

Operational inputs may include metrics, logs, traces, alerts, user reports, support cases, security events, SLO violations, or regressions.

Prefer deterministic detection (rules, thresholds, statistical detectors, monitoring systems) to decide when agent reasoning should be invoked.

Do not use an LLM as the sole anomaly detector.

## Stage 9 — Incident

For incidents:

1. collect evidence;
2. establish timeline and impact;
3. identify affected systems;
4. reproduce when possible;
5. determine root cause and contributing factors;
6. propose remediation;
7. verify remediation;
8. create regression/eval protection;
9. create follow-up intent when meaningful engineering work is required.

Use `templates/incident.md`.

## Risk classification

Classify meaningful changes using `policies/risk-classification.yaml`.

- `LOW`: docs, isolated copy, well-tested internal refactors.
- `MEDIUM`: APIs, business logic, dependencies, ordinary schema changes.
- `HIGH`: authn/authz, secrets, payments, encryption, destructive DB actions, production infrastructure, regulated/customer data.

Higher risk requires proportionally stronger planning, verification, review, rollback, and approval.

## Skill routing

This skill is an orchestrator. It should route to specialized skills rather than duplicate them.

Examples:

- authentication/authorization → security/secure-coding skill;
- API contract change → API design skill;
- React/UI → frontend skill;
- schema/data migration → database migration skill;
- regulated data → compliance skill;
- release → deployment/release skill.

Load only relevant skills.

## Skill vs deterministic control

Use skills for advisory institutional knowledge.
Use hooks/CI/policies/permissions for deterministic enforcement.

Critical security or release controls must not rely only on prompt compliance.

## Parallelism

Use parallel agents only when work can be isolated. Prefer worktrees/branches for concurrent repository modification.

Useful narrow subagents:

- intent clarifier;
- architecture researcher;
- implementation planner;
- verifier;
- security reviewer;
- test reviewer;
- simplifier;
- spec-consistency reviewer.

The parent agent remains responsible for synthesis and completion.

## Context strategy

Context priority:

```text
1. current task
2. current artifact
3. relevant source files
4. repository instructions
5. applicable specialized skills
6. relevant historical decisions
```

Prefer targeted retrieval to dumping the full repository into context.

## Definition of done

For a non-trivial change, complete only when applicable conditions hold:

```text
[ ] Intent is explicit
[ ] Specification matches intent
[ ] Plan is executable
[ ] Implementation matches plan or deviations are recorded
[ ] Tests exist where appropriate
[ ] Verification passed or unresolved failures are explicit
[ ] Security concerns addressed
[ ] Review findings resolved or accepted by policy
[ ] Documentation updated
[ ] Rollback considered
[ ] Required human/policy gates preserved
[ ] Regression eval added when appropriate
```

## Output behavior

Communicate current lifecycle status concisely:

```text
Current stage: PLAN
Existing: intent, spec
Missing: implementation plan
Next action: create plan and identify verification mechanisms
```

Expose decisions, evidence, assumptions, risks, and artifacts. Do not expose unnecessary internal reasoning.

## Anti-patterns

Do not:

- execute `request → code` for meaningful changes without durable artifacts;
- build a monolithic prompt containing every company rule;
- treat skills as enforcement for critical controls;
- let one high-risk agent implement, approve, and deploy without independent gates;
- claim success without running available verification;
- load all repository files and skills by default;
- launch uncoordinated agents into the same working tree;
- use an LLM as the sole production anomaly detector.

## References

Read only as needed:

- `references/lifecycle.md`
- `references/artifact-contract.md`
- `references/routing.md`
- `references/risk-model.md`
- `references/governance.md`
- `references/context-engineering.md`
- `references/parallelism.md`
