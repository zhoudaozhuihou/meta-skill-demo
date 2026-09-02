#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--state", required=True)
    p.add_argument("--candidate-score", type=float, required=True)
    p.add_argument("--iteration", type=int, required=True)
    p.add_argument("--candidate-revision", required=True)
    args = p.parse_args()

    state_path = Path(args.state)
    state = json.loads(state_path.read_text(encoding="utf-8"))
    best = float(state["best_score"])
    accepted = args.candidate_score > best

    record = {
        "iteration": args.iteration,
        "previous_best_score": best,
        "candidate_score": args.candidate_score,
        "candidate_revision": args.candidate_revision,
        "decision": "Accepted" if accepted else "Rejected",
    }
    state.setdefault("history", []).append(record)
    state["iteration"] = args.iteration

    if accepted:
        state["best_score"] = args.candidate_score
        state["accepted_skill_revision"] = args.candidate_revision

    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record))

if __name__ == "__main__":
    main()
