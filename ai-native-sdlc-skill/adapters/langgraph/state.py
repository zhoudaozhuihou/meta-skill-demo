from __future__ import annotations

from typing import Literal, TypedDict

Stage = Literal[
    "DISCOVERY", "INTENT", "DESIGN", "PLAN", "BUILD",
    "VERIFY", "REVIEW", "RELEASE", "OPERATE", "INCIDENT"
]
Risk = Literal["LOW", "MEDIUM", "HIGH"]


class SDLCState(TypedDict, total=False):
    change_id: str
    stage: Stage
    risk: Risk
    artifact_dir: str
    intent_path: str
    spec_path: str
    plan_path: str
    verification_path: str
    review_path: str
    release_path: str
    verification_passed: bool
    review_status: str
    errors: list[str]
