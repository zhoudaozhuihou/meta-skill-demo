#!/usr/bin/env python3
from pathlib import Path
import re, json, argparse
from common import read, rel
CANDIDATES=["tailwind.config.js","tailwind.config.cjs","tailwind.config.mjs","tailwind.config.ts"]
SECTIONS=["colors","fontFamily","fontSize","fontWeight","spacing","borderRadius","boxShadow","screens","zIndex","animation"]
def obj(text,start):
    b=text.find("{",start)
    if b<0:return None
    depth=0; quote=None; esc=False
    for i in range(b,len(text)):
        c=text[i]
        if quote:
            if esc: esc=False
            elif c=="\\": esc=True
            elif c==quote: quote=None
            continue
        if c in "'\"`": quote=c; continue
        if c=="{": depth+=1
        elif c=="}":
            depth-=1
            if depth==0:return text[b:i+1]
def extract(root):
    found=[root/n for n in CANDIDATES if (root/n).exists()]
    out={"files":[rel(p,root) for p in found],"sections":{}}
    for p in found:
        text=read(p)
        for s in SECTIONS:
            m=re.search(rf"\b{re.escape(s)}\s*:",text)
            if m:
                raw=obj(text,m.end())
                if raw: out["sections"].setdefault(s,[]).append({"file":rel(p,root),"raw":raw[:12000]})
    if found: out["warning"]="Static extraction only; dynamic executable config may be unresolved."
    return out
if __name__=="__main__":
    a=argparse.ArgumentParser(); a.add_argument("root"); a.add_argument("--out")
    x=a.parse_args(); result=extract(Path(x.root).resolve()); text=json.dumps(result,indent=2)
    Path(x.out).write_text(text,encoding="utf-8") if x.out else print(text)
