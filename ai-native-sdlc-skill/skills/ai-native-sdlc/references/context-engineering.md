# Context Engineering

## Principle

Context is a scarce execution resource. Load the minimum evidence necessary for the current decision.

## Retrieval order

1. Current user request/change ID
2. Current lifecycle artifact
3. Files named by the artifact
4. Repository instructions
5. Relevant tests and CI commands
6. Relevant specialized skills
7. ADRs/history only when needed

## Avoid

- loading every skill;
- dumping the entire repository;
- keeping obsolete conversations as authoritative state;
- duplicating stable institutional knowledge in every prompt.
