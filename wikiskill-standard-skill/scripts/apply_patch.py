#!/usr/bin/env python3
from pathlib import Path
import json
import sys

def apply_edits(text, edits):
    for edit in edits:
        op = edit["op"]
        content = edit["content"]
        target = edit.get("target")
        if op == "append":
            text += content
        elif op == "replace":
            if target not in text:
                raise ValueError(f"replace target not found: {target!r}")
            text = text.replace(target, content, 1)
        elif op == "insert_after":
            if target not in text:
                raise ValueError(f"insert_after target not found: {target!r}")
            idx = text.index(target) + len(target)
            text = text[:idx] + content + text[idx:]
        else:
            raise ValueError(f"unsupported op: {op}")
    return text

def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: apply_patch.py <file> <edits.json>")
    path = Path(sys.argv[1])
    edits = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    original = path.read_text(encoding="utf-8")
    path.write_text(apply_edits(original, edits), encoding="utf-8")

if __name__ == "__main__":
    main()
