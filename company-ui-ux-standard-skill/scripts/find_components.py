#!/usr/bin/env python3
from pathlib import Path
import json,argparse,re
from common import files,read,rel
NAMES=["button","input","select","checkbox","radio","switch","textarea","card","table","tabs","badge","alert","toast","dialog","modal","drawer","tooltip","dropdown","pagination","breadcrumb","sidebar","header","skeleton","empty"]
def scan(root):
    out=[]
    for p in files(root,{".tsx",".jsx",".ts",".js"}):
        hits=[n for n in NAMES if n in p.stem.lower()]
        if not hits: continue
        t=read(p)
        out.append({"file":rel(p,root),"candidates":hits,"has_variants":bool(re.search(r"\b(cva|variant|variants)\b",t)),"has_aria":"aria-" in t or "role=" in t})
    return out
if __name__=="__main__":
    a=argparse.ArgumentParser(); a.add_argument("root"); a.add_argument("--out")
    x=a.parse_args(); result=scan(Path(x.root).resolve()); text=json.dumps(result,indent=2)
    Path(x.out).write_text(text,encoding="utf-8") if x.out else print(text)
