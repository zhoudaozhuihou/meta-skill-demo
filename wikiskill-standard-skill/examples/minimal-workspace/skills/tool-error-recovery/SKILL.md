---
name: tool-error-recovery
description: Recover from deterministic tool validation errors without blindly repeating the same invalid call.
---

# Tool Error Recovery

## When to Apply

Apply when a tool returns a deterministic schema, argument, or validation error.

## When NOT to Apply

Do not apply this procedure to transient network or service availability failures unless the response indicates an invalid request.

## Procedure

1. Read the structured error.
2. Identify the exact invalid field or value.
3. Compare it with the submitted arguments.
4. Correct the invalid argument.
5. Retry once with the corrected call.
6. If the same deterministic error persists, stop repeating the identical call and inspect the tool contract.
