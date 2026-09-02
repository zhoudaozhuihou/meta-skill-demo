#!/usr/bin/env bash
set -euo pipefail

# Configure VERIFY_COMMAND in the environment or replace with your repository command.
: "${VERIFY_COMMAND:?VERIFY_COMMAND must be set, e.g. 'make verify'}"

echo "Running verification: ${VERIFY_COMMAND}"
bash -lc "$VERIFY_COMMAND"
