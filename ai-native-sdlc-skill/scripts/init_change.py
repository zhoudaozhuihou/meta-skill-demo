#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import shutil


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an AI-Native SDLC change workspace")
    parser.add_argument("change_id")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    package_root = Path(__file__).resolve().parents[1]
    templates = package_root / "skills" / "ai-native-sdlc" / "templates"
    target = root / "docs" / "changes" / args.change_id
    target.mkdir(parents=True, exist_ok=False)

    for name in ["intent.md", "spec.md", "plan.md", "verification.md", "review.md", "release.md"]:
        text = (templates / name).read_text(encoding="utf-8").replace("<CHANGE-ID>", args.change_id)
        (target / name).write_text(text, encoding="utf-8")

    print(target)


if __name__ == "__main__":
    main()
