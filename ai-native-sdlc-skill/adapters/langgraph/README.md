# LangGraph Adapter

This adapter shows how to represent the lifecycle as an explicit state machine while keeping artifacts in the repository or artifact store.

Recommended graph:

```text
discover → intent → design → plan → build → verify
                                      ↑       │
                                      └─ fail ┘
verify(pass) → review → release_ready → END
operate/incident may create a new intent and start a new change graph.
```

`state.py` defines a minimal typed state. `graph.py` is intentionally a skeleton: inject your own model/tool/runtime implementations rather than coupling this package to one LLM vendor.
