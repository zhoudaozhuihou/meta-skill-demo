# Hook Examples

These are reference controls, not universal drop-in scripts. Adapt paths, commands, identity/approval mechanisms, and CI integration to your environment.

Principle:

- skill = advisory knowledge;
- hook/CI/policy = deterministic enforcement.

Examples:

- `pre_edit_protected_paths.py`: deny edits to protected/generated paths.
- `secret_guard.sh`: scan staged changes for common secret patterns.
- `verify_before_complete.sh`: run repository-owned verification command.
- `production_gate.sh`: block production transition unless an external approval condition is satisfied.
