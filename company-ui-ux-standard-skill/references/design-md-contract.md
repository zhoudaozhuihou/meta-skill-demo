# DESIGN.md Contract

Use:
- YAML frontmatter for exact token values.
- Markdown body for rationale and application.

Recommended token groups:

```yaml
version:
name:
description:
omitted:
colors:
typography:
rounded:
spacing:
components:
```

Component tokens may reference global tokens:

```yaml
components:
  button-primary:
    backgroundColor: "{colors.action-primary}"
    textColor: "{colors.on-action-primary}"
    rounded: "{rounded.md}"
```

Preserve established company token names when evidence exists.
