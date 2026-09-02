#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import re,json,argparse
from common import files,read,rel
HEX=re.compile(r'#[0-9a-fA-F]{3,8}\b')
def audit(root):
    colors=Counter(); findings=[]
    for p in files(root,{".tsx",".jsx",".css",".scss"}):
        t=read(p)
        for c in HEX.findall(t): colors[c.lower()]+=1
        if p.suffix in {".tsx",".jsx"} and "style={{" in t:
            findings.append({"severity":"low","file":rel(p,root),"rule":"inline-style","message":"Review whether a company token/pattern should replace inline styling."})
    return {"raw_color_literals":colors.most_common(100),"findings":findings}
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("root");a.add_argument("--out")
    x=a.parse_args();r=audit(Path(x.root).resolve());t=json.dumps(r,indent=2)
    Path(x.out).write_text(t,encoding="utf-8") if x.out else print(t)
