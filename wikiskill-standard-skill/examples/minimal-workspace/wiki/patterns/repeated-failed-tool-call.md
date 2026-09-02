# Pattern: repeated-failed-tool-call

## Summary

The agent repeats an identical tool call after the environment has already returned a deterministic validation error.

## Trigger / Context

A tool returns a schema or argument validation error.

## Root Cause

The agent reacts to failure by retrying rather than extracting the invalid field from structured error feedback.

## Failure Evidence

- Iteration 1 / task-04: same call repeated 3 times.

## Success Evidence

- Iteration 1 / task-09: agent reads invalid field name, corrects argument, succeeds on second call.

## Recommended Strategy

After a deterministic tool error, compare the returned schema/argument error to the submitted call and change the invalid argument before retrying.

## Boundaries

Do not alter arguments after transient transport failures unless there is evidence the arguments were invalid.

## Related Skills

- `tool-error-recovery`
