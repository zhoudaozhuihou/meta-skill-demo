"""
Minimal conceptual LangGraph-style state machine for WikiSkill.

Wire these node names to your own model/tool implementations.
"""

from typing import TypedDict, Any

class WikiSkillState(TypedDict, total=False):
    iteration: int
    best_score: float
    training_traces: list[dict[str, Any]]
    wiki_update: dict[str, Any]
    proposal: dict[str, Any]
    candidate_score: float
    accepted: bool

def route_gate(state: WikiSkillState) -> str:
    return "accept" if state["candidate_score"] > state["best_score"] else "rollback"

NODES = [
    "rollout",
    "sample",
    "wiki_maintainer",
    "skill_proposer",
    "apply_candidate",
    "validate",
    "accept",
    "rollback",
    "record_impact",
]
