---
name: wikiskill
description: >
  Compile agent execution experience into a persistent wiki and use that knowledge
  to discover, refine, validate, and rollback reusable agent skills. Use when an
  agent system needs experience-driven skill evolution, recurring failure analysis,
  reusable procedural knowledge, or validation-gated skill improvement.
version: 1.0.0
license: research-adaptation
---

# WikiSkill

## Purpose

Use this skill to evolve executable agent skills from accumulated execution experience.

WikiSkill is a **meta-skill**. It does not solve one domain task directly. It manages a continuous loop that converts task executions into durable knowledge and validated procedural skills.

## When to Apply

Apply WikiSkill when one or more of these conditions hold:

- an agent repeatedly performs similar tasks;
- successful and failed trajectories are available;
- recurring failure modes should become reusable guidance;
- manually maintained skills are becoming stale;
- you want skills to improve from execution evidence;
- proposed skill edits require objective validation before activation;
- rejected skill changes must not be forgotten and repeated;
- procedural knowledge should transfer independently of model weights.

## When NOT to Apply

Do not invoke a full WikiSkill evolution cycle when:

- there are too few comparable executions to infer a general pattern;
- no objective or reasonably deterministic validation signal exists;
- the task is one-off and has no expected reuse;
- raw traces contain secrets or sensitive reasoning that cannot be safely retained;
- skill mutation is forbidden by policy;
- the requested change is a manually approved deterministic edit and no evolution is needed.

## Core Architecture

Maintain three layers with different persistence semantics:

```text
raw/       = immutable execution evidence
wiki/      = persistent accumulated knowledge
skills/    = reversible active procedures
```

Never collapse these three layers into one file or one chat history.

## Required Workspace

```text
workspace/
├── raw/
│   └── traces/
│       └── <iteration>/
│           └── <task-id>.json
│
├── wiki/
│   ├── index.md
│   ├── log.md
│   ├── skill-impact.md
│   └── patterns/
│       └── <pattern-name>.md
│
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md
│       └── PURPOSE.md
│
└── state/
    └── evolution.json
```

Read `references/architecture.md` for the layer contract.

# Evolution Loop

Execute the following stages in order.

## Stage 0 — Baseline

Before proposing any skill change:

1. identify the training/task set;
2. identify an independent validation set;
3. define the scoring function;
4. evaluate the current active skill set;
5. save the best known validation score.

Do not optimize against the test set.

## Stage 1 — Inference Rollouts

Run the task-performing agent using the **currently active skills**.

Write every rollout as an immutable trace under `raw/traces/`.

The inference agent should normally **not read `wiki/` during training rollouts**.

The trace must capture enough observable evidence to reconstruct:
- task input or task reference;
- active skills/version;
- observations;
- actions/tool calls;
- tool results;
- final output;
- evaluator score/outcome;
- runtime metadata.

Do not store hidden chain-of-thought. Store externally observable actions, outputs, concise rationale when available, and evaluation evidence.

See:
- `schemas/trace.schema.json`
- `templates/trace.json`

## Stage 2 — Wiki Maintenance

Use the Wiki Maintainer to analyze a stratified sample of successful and failed traces.

The maintainer must:

1. compare success and failure behavior;
2. diagnose root causes rather than copy error messages;
3. extract generalizable action patterns;
4. update existing patterns instead of duplicating them;
5. keep pattern pages concise and evidence-backed;
6. update the complete `wiki/index.md`;
7. append a chronological entry to `wiki/log.md`.

Prefer incremental patch-based edits.

Read:
- `agents/wiki-maintainer.md`
- `references/pattern-authoring.md`

## Stage 3 — Skill Proposal

Use the Skill Proposer after Wiki maintenance.

The proposer must inspect:

1. `wiki/index.md`;
2. `wiki/skill-impact.md`;
3. relevant pattern pages;
4. relevant raw traces;
5. existing target skills.

Before proposing a change, inspect at least four relevant execution traces when four or more are available.

Allowed proposal actions:

```text
create
patch
no_action
```

A proposal must target only one skill per evolution iteration.

Prefer patching an existing partially-correct skill over creating a redundant skill.

Every active skill should contain:

```text
<skill>/
├── SKILL.md
└── PURPOSE.md
```

`PURPOSE.md` must link the procedural skill to motivating wiki patterns and evolution history.

Read:
- `agents/skill-proposer.md`
- `schemas/proposal.schema.json`
- `templates/PURPOSE.md`

## Stage 4 — Gating and Rollback

Apply the candidate change in an isolated candidate workspace.

Evaluate the candidate against the validation set.

Default paper-faithful acceptance policy:

```text
candidate_score > best_score  => ACCEPT
candidate_score <= best_score => REJECT + ROLLBACK SKILLS
```

On rejection:

- restore the previously accepted `skills/`;
- retain all `raw/` evidence;
- retain all `wiki/` knowledge;
- append the rejected proposal, diff, score, and outcome to `wiki/skill-impact.md`.

On acceptance:

- promote the candidate skills;
- update `best_score`;
- append the accepted proposal, diff, score, and outcome to `wiki/skill-impact.md`.

The Wiki is never rolled back merely because a candidate skill fails validation.

Read:
- `references/gating-and-rollback.md`
- `policies/default-gating.yaml`

# Knowledge Access Rules

## Inference Agent

May read:
- task context;
- tools;
- active `skills/`.

Should not normally read:
- `wiki/`;
- rejected proposal history;
- optimizer-only traces from unrelated tasks.

## Wiki Maintainer

May read:
- sampled raw traces;
- complete wiki;
- active skill metadata where needed.

May write:
- `wiki/index.md`;
- `wiki/log.md`;
- `wiki/patterns/*`.

Must not directly activate skill changes.

## Skill Proposer

May read:
- wiki;
- current active skills;
- latest execution outcomes;
- selected raw traces.

May produce:
- one atomic candidate proposal.

Must not decide final acceptance.

## Gating Harness

Must be deterministic wherever possible.

Responsible for:
- applying proposal to candidate workspace;
- running validation;
- computing score;
- comparing to best score;
- accepting or rolling back;
- writing `wiki/skill-impact.md`.

# Pattern Quality Rules

A wiki pattern should answer:

1. What repeatedly happens?
2. Why does it happen?
3. What evidence supports it?
4. What concrete action avoids or reproduces it?
5. When does the workaround apply?
6. What could be harmed by overgeneralizing it?

Do not create a pattern from a single accidental error unless its importance is exceptional.

Prefer:
- concrete actions;
- observable conditions;
- exact commands or tool sequences when relevant;
- success/failure contrast.

Avoid:
- vague advice;
- personality descriptions;
- unsupported causal claims;
- model-specific hacks presented as universal rules.

# Skill Quality Rules

A generated or patched `SKILL.md` must:

- include YAML frontmatter with a unique `name` and concise `description`;
- explicitly state when to apply the skill;
- explicitly state when not to apply it;
- provide concrete procedural instructions;
- remain as concise as the task permits;
- avoid embedding raw trace history;
- avoid reproducing the entire wiki;
- generalize from evidence without inventing unsupported rules.

Use `PURPOSE.md` for provenance rather than bloating `SKILL.md`.

# Progressive Disclosure

Do not load every WikiSkill reference into context.

Start with this `SKILL.md`.

Then load only what the active stage requires:

```text
Need architecture?       -> references/architecture.md
Maintaining wiki?        -> agents/wiki-maintainer.md
Proposing skill?         -> agents/skill-proposer.md
Validating proposal?     -> references/gating-and-rollback.md
Writing patterns?        -> references/pattern-authoring.md
Designing traces?        -> references/trace-contract.md
```

# Safety and Governance

Do not retain secrets, credentials, or unnecessarily sensitive data in raw traces.

Do not store private hidden reasoning or chain-of-thought. Store observable execution evidence and concise derived summaries instead.

Skill evolution does not override:
- human approval requirements;
- repository permissions;
- security hooks;
- compliance policies;
- production deployment gates.

A skill becoming “better” on a validation metric does not make an unsafe behavior acceptable.

# Stop Conditions

Stop the evolution loop when any of these apply:

- maximum iteration budget reached;
- validation performance reaches the configured maximum;
- no meaningful proposal is produced;
- repeated proposals fail to improve validation;
- evidence is insufficient;
- policy requires human review;
- validation signal is unreliable.

# Required Auditability

For every candidate skill change, preserve:

- iteration;
- target skill;
- action;
- proposal;
- patch/diff;
- prior best score;
- candidate score;
- acceptance decision;
- motivating patterns;
- validation configuration.

# Canonical Principle

```text
Experience is permanent evidence.
Knowledge is cumulative understanding.
Skills are executable hypotheses.
Validation decides which hypotheses become active.
```
