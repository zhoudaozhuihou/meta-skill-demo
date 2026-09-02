#!/usr/bin/env python3
"""Example protected-path guard.

Usage: pre_edit_protected_paths.py <path>
Exit 0 = allowed, exit 2 = blocked.
"""
from pathlib import Path
import sys

PROTECTED = (
    ".git/",
    "vendor/",
    "dist/generated/",
    "src/generated/",
)

if len(sys.argv) != 2:
    print("usage: pre_edit_protected_paths.py <path>", file=sys.stderr)
    sys.exit(2)

path = Path(sys.argv[1]).as_posix().lstrip("./")
for prefix in PROTECTED:
    if path == prefix.rstrip("/") or path.startswith(prefix):
        print(f"BLOCKED: protected path: {path}", file=sys.stderr)
        sys.exit(2)

sys.exit(0)
