#!/usr/bin/env python3
from pathlib import Path
import re, json, argparse
from common import files, read, rel
VAR=re.compile(r"(--[\w-]+)\s*:\s*([^;}{]+);")
def extract(root):
    values={}; evidence={}
    for p in files(root,{".css",".scss"}):
        for k,v in VAR.findall(read(p)):
            values.setdefault(k,v.strip())
            evidence.setdefault(k,[]).append(rel(p,root))
    return {"css_variables":values,"evidence":evidence}
if __name__=="__main__":
    a=argparse.ArgumentParser(); a.add_argument("root"); a.add_argument("--out")
    x=a.parse_args(); result=extract(Path(x.root).resolve()); text=json.dumps(result,indent=2)
    Path(x.out).write_text(text,encoding="utf-8") if x.out else print(text)
