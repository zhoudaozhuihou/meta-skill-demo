# WikiSkill Harness Responsibilities

The meta-skill defines reasoning and artifact contracts.

The harness should implement deterministic mechanics:

- trace capture;
- redaction;
- immutable raw storage;
- workspace snapshots;
- proposal application;
- validation execution;
- metric calculation;
- candidate promotion;
- rollback;
- impact log append;
- iteration budgets;
- permissions.

This boundary keeps the probabilistic agent focused on analysis and proposal generation while the environment owns state integrity.
