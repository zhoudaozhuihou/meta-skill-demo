# Purpose

WikiSkill is a meta-skill for compiling agent execution experience into persistent, structured knowledge and using that knowledge to discover or refine executable agent skills.

## Origin

Adapted from the 2026 paper **WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution**.

## Primary capability

Separate:

1. raw execution experience,
2. accumulated knowledge,
3. executable procedural skills,

and evolve them under different persistence semantics.

## Design invariant

- `raw/`: immutable evidence.
- `wiki/`: persistent knowledge that compounds across iterations.
- `skills/`: active procedural instructions that may be accepted or rolled back.

## Why this package exists

The paper describes a research framework. This package turns its methodology into a portable standard skill with:
- explicit trigger conditions,
- reusable agent definitions,
- artifact contracts,
- JSON schemas,
- deterministic scripts,
- validation gates,
- adapters for common agent runtimes.
