#!/usr/bin/env python3
from pathlib import Path
import re, sys

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

def parse_frontmatter(text):
    m = FRONTMATTER.match(text)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_skill.py <skill-dir>")
    d = Path(sys.argv[1])
    skill = d/"SKILL.md"
    purpose = d/"PURPOSE.md"
    errors = []

    if not skill.exists():
        errors.append("missing SKILL.md")
    else:
        fm = parse_frontmatter(skill.read_text(encoding="utf-8"))
        if not fm:
            errors.append("missing YAML frontmatter")
        else:
            if not fm.get("name"):
                errors.append("frontmatter missing name")
            if not fm.get("description"):
                errors.append("frontmatter missing description")

    if not purpose.exists():
        errors.append("missing PURPOSE.md")

    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("OK")

if __name__ == "__main__":
    main()
