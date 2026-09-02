---
name: design-system-extractor
description: Extract visual tokens, layout rules, and provenance from React/Tailwind source.
---

# Design System Extractor

Output structured evidence for `DESIGN.md` and `tokens.json`.

Rules:
- prefer explicit tokens;
- preserve exact values and source paths;
- never invent missing values;
- assign confidence;
- flag conflicts;
- separate semantic values from raw implementation values.
