# Company UI/UX Standard Skill

Enterprise meta-skill for reverse-engineering UI/UX standards from existing React + TailwindCSS projects, compiling them into durable design-system artifacts, and using those artifacts to guide new UI implementation and review.

Inspired by Google Labs `DESIGN.md` and `ui-ux-pro-max-skill`.

## Outputs

```text
.company-ui/
├── DESIGN.md
├── UX.md
├── COMPONENTS.md
├── tokens.json
├── component-patterns.json
├── evidence.json
└── audit-policy.yaml
```

## Modes

- EXTRACT — derive standards from source.
- APPLY — build React/Tailwind UI using company standards.
- AUDIT — find UI/UX drift.
- EVOLVE — update approved standards.

## Quick start

```bash
python scripts/scan_project.py /path/to/react-project --out /path/to/react-project/.company-ui
```

Then let an agent synthesize `scan-report.json` into the canonical artifacts using `SKILL.md`.
