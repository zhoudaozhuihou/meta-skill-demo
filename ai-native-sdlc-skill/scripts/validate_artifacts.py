#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = {
    "intent.md": ["## Problem", "## Desired Outcome", "## Success Criteria"],
    "spec.md": ["## Current State", "## Target State", "## Acceptance Criteria"],
    "plan.md": ["## Implementation Sequence", "## Tests", "## Verification", "## Rollback Strategy"],
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate minimum AI-Native SDLC artifacts")
    parser.add_argument("artifact_dir")
    args = parser.parse_args()

    root = Path(args.artifact_dir)
    errors: list[str] = []

    for filename, headings in REQUIRED.items():
        path = root / filename
        if not path.exists():
            errors.append(f"missing {filename}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"{filename}: missing heading {heading}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(2)

    print("Artifact validation passed")


if __name__ == "__main__":
    main()
