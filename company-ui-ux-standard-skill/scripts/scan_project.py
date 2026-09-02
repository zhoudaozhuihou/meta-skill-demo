#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys,datetime
sys.path.insert(0,str(Path(__file__).parent))
from extract_tailwind import extract as tailwind
from extract_css_tokens import extract as css
from scan_react import scan as react
from find_components import scan as components
def package(root):
    p=root/"package.json"
    if not p.exists():return {}
    d=json.loads(p.read_text(encoding="utf-8"))
    deps={**d.get("dependencies",{}),**d.get("devDependencies",{})}
    return {"name":d.get("name"),"scripts":d.get("scripts",{}),"dependencies":deps}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("root"); ap.add_argument("--out",required=True)
    a=ap.parse_args(); root=Path(a.root).resolve(); out=Path(a.out).resolve(); out.mkdir(parents=True,exist_ok=True)
    report={"project":package(root),"tailwind":tailwind(root),"css":css(root),"react":react(root),"components":components(root)}
    (out/"scan-report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    evidence={"repository":str(root),"generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"rules":[],"conflicts":[],"recommendations":[]}
    (out/"evidence.json").write_text(json.dumps(evidence,indent=2),encoding="utf-8")
    for n in ["DESIGN.md","UX.md","COMPONENTS.md"]:
        p=out/n
        if not p.exists():p.write_text(f"# {n[:-3]}\n\n> Pending agent synthesis from scan-report.json.\n",encoding="utf-8")
    print(json.dumps({"out":str(out),"react_files":report["react"]["files_scanned"],"component_candidates":len(report["components"])},indent=2))
if __name__=="__main__":main()
