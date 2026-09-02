#!/usr/bin/env bash
set -euo pipefail

# Example only. In production, query your actual change-management/approval system.
if [[ "${TARGET_ENVIRONMENT:-}" != "production" ]]; then
  exit 0
fi

if [[ "${PRODUCTION_APPROVED:-false}" != "true" ]]; then
  echo "BLOCKED: production deployment requires external approval" >&2
  exit 2
fi
