#!/usr/bin/env python3
from pathlib import Path
import json
import sys

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: init_workspace.py <workspace>")
    root = Path(sys.argv[1]).resolve()

    for p in [
        root / "raw/traces",
        root / "wiki/patterns",
        root / "skills",
        root / "state",
        root / "proposals",
        root / "validation",
    ]:
        p.mkdir(parents=True, exist_ok=True)

    defaults = {
        root/"wiki/index.md": "# Wiki Pattern Index\n\n",
        root/"wiki/log.md": "# Wiki Evolution Log\n\n",
        root/"wiki/skill-impact.md": "# Skill Impact Tracker\n\n",
        root/"state/evolution.json": json.dumps({
            "iteration": 0,
            "best_score": 0.0,
            "metric": "accuracy",
            "accepted_skill_revision": "baseline",
            "history": []
        }, indent=2) + "\n",
    }

    for p, content in defaults.items():
        if not p.exists():
            p.write_text(content, encoding="utf-8")

    print(root)

if __name__ == "__main__":
    main()
