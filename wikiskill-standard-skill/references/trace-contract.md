# Trace Contract

A WikiSkill trace should preserve externally observable execution evidence.

Recommended fields:

```json
{
  "trace_id": "...",
  "iteration": 1,
  "split": "train",
  "task_id": "...",
  "task": {},
  "active_skills": [],
  "events": [],
  "final_output": {},
  "score": 0.0,
  "passed": false,
  "metadata": {}
}
```

An event may contain:

```json
{
  "step": 1,
  "observation": "...",
  "action": {
    "type": "tool_call",
    "name": "...",
    "arguments": {}
  },
  "result": "...",
  "rationale_summary": "optional concise non-sensitive summary"
}
```

## Do not persist

- hidden chain-of-thought;
- passwords;
- auth tokens;
- unnecessary PII;
- secrets from environment variables;
- full sensitive documents when a reference is sufficient.

Use redaction before writing traces.
