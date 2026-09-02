# Parallelism and Subagents

Parallelism is useful when work is decomposable and independently verifiable.

## Recommended roles

- researcher: inspect architecture/dependencies;
- planner: produce executable implementation plan;
- implementer: modify code;
- verifier: execute tests and inspect evidence;
- security reviewer: narrow security audit;
- spec reviewer: compare implementation to intent/spec;
- simplifier: remove unnecessary complexity after correctness is established.

## Isolation

Use separate branches or worktrees for concurrent code-writing agents when possible.

## Constraint

The bottleneck is review/coordination capacity. Do not maximize agent count for its own sake.
