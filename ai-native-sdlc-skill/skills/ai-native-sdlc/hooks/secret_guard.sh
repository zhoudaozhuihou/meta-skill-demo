#!/usr/bin/env bash
set -euo pipefail

# Example only. Prefer your organization's approved secret scanner in CI.
DIFF="$(git diff --cached --unified=0 2>/dev/null || true)"

if printf '%s' "$DIFF" | grep -Eiq '(BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|api[_-]?key\s*[:=]\s*["'"'']?[A-Za-z0-9_\-]{20,}|password\s*[:=]\s*["'"''][^"'"'']{8,})'; then
  echo "BLOCKED: possible credential or private key in staged diff" >&2
  exit 2
fi
