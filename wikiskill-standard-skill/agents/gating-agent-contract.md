# Gating Harness Contract

Prefer deterministic code, not an LLM, for acceptance decisions.

Responsibilities:

1. snapshot accepted skill state;
2. apply one candidate proposal in isolation;
3. execute independent validation tasks;
4. compute the configured metric;
5. compare against best accepted score;
6. apply safety/regression policy;
7. accept or rollback;
8. append immutable impact record.

Never let the Skill Proposer self-approve its proposal.
