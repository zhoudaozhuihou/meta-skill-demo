"""Illustrative LangGraph lifecycle skeleton.

Wire these nodes to your actual artifact store, model gateway, tools, and policy service.
"""
from __future__ import annotations

try:
    from langgraph.graph import END, StateGraph
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("Install langgraph to use this adapter") from exc

from state import SDLCState


def discover(state: SDLCState) -> SDLCState:
    return {**state, "stage": "DISCOVERY"}


def intent(state: SDLCState) -> SDLCState:
    return {**state, "stage": "INTENT"}


def design(state: SDLCState) -> SDLCState:
    return {**state, "stage": "DESIGN"}


def plan(state: SDLCState) -> SDLCState:
    return {**state, "stage": "PLAN"}


def build(state: SDLCState) -> SDLCState:
    return {**state, "stage": "BUILD"}


def verify(state: SDLCState) -> SDLCState:
    return {**state, "stage": "VERIFY"}


def review(state: SDLCState) -> SDLCState:
    return {**state, "stage": "REVIEW"}


def release(state: SDLCState) -> SDLCState:
    return {**state, "stage": "RELEASE"}


def verification_route(state: SDLCState) -> str:
    return "review" if state.get("verification_passed") else "build"


def build_graph():
    graph = StateGraph(SDLCState)
    for name, node in {
        "discover": discover,
        "intent": intent,
        "design": design,
        "plan": plan,
        "build": build,
        "verify": verify,
        "review": review,
        "release": release,
    }.items():
        graph.add_node(name, node)

    graph.set_entry_point("discover")
    graph.add_edge("discover", "intent")
    graph.add_edge("intent", "design")
    graph.add_edge("design", "plan")
    graph.add_edge("plan", "build")
    graph.add_edge("build", "verify")
    graph.add_conditional_edges("verify", verification_route, {"review": "review", "build": "build"})
    graph.add_edge("review", "release")
    graph.add_edge("release", END)
    return graph.compile()
