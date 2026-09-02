---
name: company-ui-ux-standard
description: >
  Extract, compile, apply, and audit a company's UI/UX standards from existing
  React applications, TailwindCSS configuration, CSS variables, shared components,
  layouts, and interaction patterns. Use for reverse-engineering design systems,
  generating DESIGN.md, standardizing internal products, implementing React/Tailwind
  pages consistently, or reviewing UI for visual and UX drift.
version: 1.0.0
---

# Company UI/UX Standard

## Operating Modes

```text
EXTRACT
APPLY
AUDIT
EVOLVE
```

Determine the mode first.

## Core Rules

### Evidence Before Preference

Use this precedence:

1. approved design-system documentation/configuration;
2. design-token package;
3. Tailwind/theme configuration;
4. CSS custom properties;
5. shared UI component library;
6. repeated production patterns;
7. page-local patterns;
8. generic UI/UX recommendations.

Do not present level 8 as an existing company standard.

### Standard Classification

Every rule must be one of:

- `normative` — explicit, approved, or authoritative;
- `observed` — repeatedly present in production code;
- `recommended` — proposed improvement;
- `unresolved` — conflicting or insufficient evidence.

### Confidence

Default confidence model:

```text
1.00 explicit token/config
0.90 shared design-system component
0.80 repeated shared pattern
0.65 repeated page-local pattern
0.40 weak/inconsistent evidence
0.00 recommendation only
```

Default thresholds:

```text
normative >= 0.85
observed  >= 0.60
review    <  0.60
```

## EXTRACT Workflow

### 1. Repository Discovery

Inspect:

```text
package.json
tailwind.config.*
src/
app/
pages/
components/
styles/
theme/
tokens/
design-system/
ui/
packages/
```

Identify framework, Tailwind version, styling approach, UI libraries, icon libraries, form libraries, chart libraries, and shared UI packages.

### 2. Extract Design Tokens

From Tailwind and CSS variables extract where available:

- colors and semantic colors;
- font families, sizes, weights, line heights;
- spacing;
- radius;
- shadow/elevation;
- breakpoints;
- widths/max widths;
- z-index;
- animation and transition.

Never invent unresolved exact values.

Do not execute untrusted Tailwind configuration merely to inspect it.

### 3. Mine React Component Patterns

At minimum inspect:

```text
Button Input Select Checkbox Radio Switch Textarea
FormField Card Table Tabs Badge Alert Toast
Dialog Modal Drawer Tooltip Dropdown Pagination
Breadcrumb Sidebar Header PageShell
EmptyState LoadingState ErrorState
```

For each component record:

- canonical source;
- variants;
- sizes;
- states;
- token usage;
- accessibility behavior;
- usage count;
- confidence;
- exceptions.

Prefer shared components over local copies.

### 4. Mine Layout Patterns

Extract recurring:

- page shell;
- max width;
- gutters;
- sidebar width;
- header height;
- grid;
- card gap/padding;
- content density;
- responsive breakpoints;
- mobile behavior;
- sticky/fixed regions.

### 5. Mine UX Patterns

Inspect behavioral evidence for:

- form validation;
- submit/save states;
- loading;
- skeleton;
- empty states;
- errors;
- retry/recovery;
- toast/feedback;
- destructive confirmation;
- search/filter;
- pagination;
- bulk actions;
- focus/keyboard;
- responsive navigation.

Visual tokens alone are insufficient evidence for behavioral UX rules.

### 6. Compile Canonical Artifacts

Generate:

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

## DESIGN.md Contract

Use YAML frontmatter for machine-readable tokens and Markdown for rationale.

Recommended frontmatter:

```yaml
---
version: "1"
name: "<company/product>"
description: "<evidence-derived description>"
colors: {}
typography: {}
rounded: {}
spacing: {}
components: {}
---
```

Recommended section order:

```text
## Overview
## Colors
## Typography
## Layout
## Elevation & Depth
## Shapes
## Components
## Do's and Don'ts
```

Additional enterprise sections may follow.

Tokens are normative values. Prose explains how and why to use them.

## APPLY Workflow

Before implementing UI:

1. read `.company-ui/DESIGN.md`;
2. read relevant `.company-ui/COMPONENTS.md`;
3. read relevant `.company-ui/UX.md`;
4. search existing shared components;
5. reuse existing components/tokens;
6. implement using the repository's architecture;
7. run tests/lint/build;
8. audit the resulting UI.

Priority:

```text
existing company component
>
existing company pattern
>
company token
>
approved library primitive
>
new custom component
```

## AUDIT Workflow

Review implementation against company standards, not personal taste.

Check:

### Visual
- unsupported colors;
- raw values where semantic tokens exist;
- spacing drift;
- typography drift;
- radius/shadow drift.

### Components
- duplicate primitives;
- unsupported variants;
- inconsistent states;
- local reinvention of shared components.

### UX
- missing loading/empty/error states;
- inconsistent validation;
- inconsistent feedback;
- destructive actions that violate the standard;
- inconsistent filtering/pagination/navigation.

### Accessibility
Review focus, semantic controls, labels, keyboard access, contrast risk, reduced motion, and target sizes.

If company accessibility policy is absent, report improvements as recommendations rather than existing standards.

### Responsive
Use company breakpoints when available.

Fallback review widths, if no company standard exists:

```text
375 768 1024 1440
```

These are review defaults, not extracted company tokens.

## EVOLVE Workflow

Do not change the company standard because one page differs.

Require evidence such as:

- approved design decision;
- updated design-system package;
- repeated adoption;
- explicit product exception.

Preserve provenance.

## Anti-Patterns

Never:
- derive the whole design system from one screenshot;
- equate class frequency with an approved standard;
- make one-off page styling globally normative;
- present generic best practice as company policy;
- create a new primitive before searching the repository;
- load the entire repository into context when targeted retrieval is enough.

## Required Extraction Summary

```text
Framework:
Tailwind:
Design-system source:
Files scanned:

Artifacts:
✓ DESIGN.md
✓ UX.md
✓ COMPONENTS.md
✓ tokens.json
✓ evidence.json

High-confidence rules:
Observed conventions:
Needs review:
Major conflicts:
```

## Core Principle

```text
Code is evidence.
Repeated implementation is convention.
Approved tokens are standards.
Agent recommendations are proposals.
```
