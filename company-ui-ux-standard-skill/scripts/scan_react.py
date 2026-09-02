#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import re,json,argparse
from common import files,read,rel
CLASS=re.compile(r'className\s*=\s*(?:"([^"]+)"|\'([^\']+)\'|`([^`]+)`)')
COMP=re.compile(r'<([A-Z][A-Za-z0-9_.]*)\b')
def scan(root):
    cls=Counter(); comps=Counter(); count=0
    for p in files(root,{".tsx",".jsx"}):
        count+=1; text=read(p)
        for m in CLASS.finditer(text):
            v=next((g for g in m.groups() if g), "")
            for c in re.split(r"\s+",v.strip()):
                if c and "{" not in c and "$" not in c: cls[c]+=1
        for c in COMP.findall(text): comps[c]+=1
    return {"files_scanned":count,"top_tailwind_classes":cls.most_common(200),"component_usage":comps.most_common(200)}
if __name__=="__main__":
    a=argparse.ArgumentParser(); a.add_argument("root"); a.add_argument("--out")
    x=a.parse_args(); result=scan(Path(x.root).resolve()); text=json.dumps(result,indent=2)
    Path(x.out).write_text(text,encoding="utf-8") if x.out else print(text)
