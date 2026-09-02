# AI-Native SDLC Skill Pack

A model-agnostic engineering skill pack for turning software delivery from conversation-driven coding into an artifact-driven, verifiable, governed, closed-loop SDLC.

## What this package provides

- A top-level orchestration skill: `skills/ai-native-sdlc/SKILL.md`
- Lifecycle and artifact contracts
- Templates for intent, specification, plan, verification, review, release, incident, ADR, and eval cases
- Narrow sub-agent role definitions
- Deterministic hook examples
- Risk, review, permissions, and production-gate policies
- Example eval cases and grader guidance
- Runtime adapters for Claude Code, Codex, GitHub Copilot, OpenCode, and LangGraph
- Scripts for creating change workspaces and validating artifacts
- A complete example change package

## Core model

```text
Request
  ↓
Intent
  ↓
Specification
  ↓
Implementation Plan
  ↓
Build
  ↓
Verification
  ↓
Review
  ↓
Release Gate
  ↓
Production
  ↓
Observation / Incident
  └──────────────→ Intent
```

The package follows five governing ideas:

1. **Artifact > Conversation** — durable engineering state lives in files, not chat history.
2. **Plan before code** — non-trivial work is specified and planned before implementation.
3. **Deterministic outside, probabilistic inside** — agents reason; hooks, CI, policies, and permissions enforce.
4. **Agent must verify its own work** — completion requires evidence.
5. **Incident → Eval** — production failures should become regression protection.

## Recommended repository integration

Copy `skills/ai-native-sdlc/` into your repository skill directory, then adapt one runtime folder under `adapters/`.

For change-scoped artifacts, use:

```text
docs/changes/<CHANGE-ID>/
├── intent.md
├── spec.md
├── plan.md
├── verification.md
├── review.md
└── release.md
```

## Quick start

Create a change workspace:

```bash
python scripts/init_change.py FEATURE-123 --root .
```

Validate artifacts:

```bash
python scripts/validate_artifacts.py docs/changes/FEATURE-123
```

Then ask your coding agent to execute `ai-native-sdlc` against that change ID.

## Package layout

See `docs/architecture.md` for the full architecture and `docs/adoption-guide.md` for rollout guidance.
