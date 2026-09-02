# React Scanning

High-value signals:

```text
className=
cn(...)
clsx(...)
cva(...)
tailwind-merge
variant / variants
aria-*
role=
data-state=
```

High-value locations:

```text
components/ui/
components/common/
src/components/
src/design-system/
packages/ui/
```

Detect external libraries from `package.json`; do not assume a library based only on file names.
