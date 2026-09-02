# Three-Layer Knowledge Architecture

## Raw Layer — `raw/`

Purpose: permanent execution evidence.

Properties:
- append-only / write-once;
- never edited to make an analysis look cleaner;
- contains observable task execution traces;
- source material for Wiki Maintainer and Skill Proposer.

Recommended:

```text
raw/
└── traces/
    ├── iteration-000/
    ├── iteration-001/
    └── ...
```

## Wiki Layer — `wiki/`

Purpose: persistent, structured, compounding knowledge.

```text
wiki/
├── index.md
├── log.md
├── skill-impact.md
└── patterns/
```

### `index.md`

A concise routing catalog. Each line should tell an agent whether the detailed pattern is relevant.

### `log.md`

Chronological record of patterns identified/refined during evolution.

### `skill-impact.md`

Ground-truth audit trail written after validation gating. It records proposals, diffs, validation scores, and accept/reject outcomes.

### `patterns/`

One Markdown page per distinct, generalizable success/failure pattern.

## Skill Layer — `skills/`

Purpose: active procedural knowledge read by the inference agent.

Each skill:

```text
skills/<skill-name>/
├── SKILL.md
└── PURPOSE.md
```

Skill changes are reversible and conditional on validation. Wiki changes are retained even when a skill proposal is rejected.
