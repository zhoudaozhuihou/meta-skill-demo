from pathlib import Path
IGNORE = {"node_modules",".git",".next","dist","build","coverage",".turbo",".cache"}
def files(root, suffixes):
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in suffixes and not any(x in IGNORE for x in p.parts):
            yield p
def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")
def rel(p, root):
    try: return str(p.relative_to(root))
    except: return str(p)
