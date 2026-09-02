# WikiSkill Standard Skill

A production-oriented, model-agnostic implementation of the WikiSkill methodology described in:

**WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution**  
Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu (2026).

This package converts the research framework into a reusable **standard agent skill / meta-skill** that can be integrated with Claude Code, Codex, GitHub Copilot, OpenCode, LangGraph, DeepAgents, or a custom agent harness.

> This is an engineering adaptation of the paper, not an official Google Research implementation.

## What WikiSkill does

WikiSkill continuously converts agent execution experience into reusable procedural knowledge:

```text
Agent Execution
     │
     ▼
raw/                     immutable traces
     │
     ▼
Wiki Maintainer
     │
     ▼
wiki/                    persistent, compounding knowledge
     │
     ▼
Skill Proposer
     │
     ▼
candidate skill change
     │
     ▼
validation gate
   ┌─┴─┐
 pass fail
  │    │
accept rollback
  │    │
  └─┬──┘
    ▼
wiki/skill-impact.md     permanent audit trail
```

## Three-layer architecture

```text
raw/       Permanent, write once
wiki/      Persistent, compounding, never reset
skills/    Reversible, validation-gated
```

## Core package

```text
wikiskill-standard-skill/
├── SKILL.md
├── PURPOSE.md
├── README.md
├── references/
├── agents/
├── templates/
├── schemas/
├── scripts/
├── policies/
├── evals/
├── examples/
└── adapters/
```

## Install

Copy this directory into a skill-compatible directory and expose `SKILL.md` to the agent runtime.

Typical examples:

```text
.claude/skills/wikiskill/
.github/skills/wikiskill/
skills/wikiskill/
```

## Initialize a WikiSkill workspace

```bash
python scripts/init_workspace.py /path/to/target-workspace
```

Result:

```text
target-workspace/
├── raw/
│   └── traces/
├── wiki/
│   ├── index.md
│   ├── log.md
│   ├── skill-impact.md
│   └── patterns/
├── skills/
└── state/
```

## Important separation

The task-performing inference agent should normally receive the **active skills**, but not the persistent Wiki. The Wiki is primarily for the Wiki Maintainer and Skill Proposer.

## Acceptance rule

The paper uses strict improvement:

```text
accept candidate if candidate_validation_score > best_validation_score
otherwise rollback the skill change
```

The wiki is retained in either case.
