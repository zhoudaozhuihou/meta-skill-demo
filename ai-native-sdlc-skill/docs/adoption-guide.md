# Adoption Guide

## Phase 1 — Artifact discipline

Introduce change-scoped `intent.md`, `spec.md`, and `plan.md` for medium/high-risk work. Do not change all tooling at once.

## Phase 2 — Self-verification

Make repository verification commands discoverable and require agents to run them before completion.

## Phase 3 — Specialized skills

Move institutional knowledge out of monolithic prompts into focused skills such as secure coding, API standards, frontend conventions, data governance, and testing.

## Phase 4 — Deterministic enforcement

Add hooks/CI for protected paths, secret scanning, required tests, policy checks, and production approvals.

## Phase 5 — Independent AI review

Add narrow reviewers for security, correctness, and spec consistency on medium/high-risk changes.

## Phase 6 — Agent evals

Build a 20–50 case suite from real tasks and incidents. Run it when model, prompts, skills, hooks, or orchestration behavior changes.

## Phase 7 — Closed-loop operations

Connect deterministic monitoring to incident diagnosis and turn significant incidents into follow-up intent plus regression evals.
