# Wiki Pattern Authoring Guide

## Goal

Compile execution evidence into small pieces of reusable knowledge.

## Pattern Template

```markdown
# Pattern: <name>

## Summary
Specific problem or success strategy.

## Trigger / Context
Observable conditions under which it appears.

## Root Cause
Why the behavior occurs.

## Failure Evidence
- Iteration / task / action sequence / result

## Success Evidence
- Iteration / task / action sequence / result

## Recommended Strategy
Concrete, executable workaround or procedure.

## Boundaries
When the strategy should NOT be applied.

## Related Skills
- ...
```

## Create vs Update

Create a new pattern only if it represents a meaningfully distinct behavior.

Otherwise append evidence or refine an existing page.

## Index Entry

Use:

```markdown
- [pattern-name](patterns/pattern-name.md): PROBLEM + ROOT CAUSE + FIX.
```

The index is a routing layer, not a full explanation.
