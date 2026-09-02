# Claude Code Adapter

Recommended install:

```text
.claude/skills/wikiskill/
```

Place the package there or symlink it from a shared skill catalog.

Keep the downstream evolved skills in the target repository's own skill directory.

Use hooks/CI for deterministic mutation and gating when possible rather than asking the model to self-enforce the acceptance rule.
