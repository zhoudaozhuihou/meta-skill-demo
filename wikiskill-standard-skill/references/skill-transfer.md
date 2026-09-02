# Skill Transfer Considerations

Evolved procedural knowledge can transfer across models, but transfer is not guaranteed.

Prefer transferable skills that encode:
- domain procedures;
- invariant tool workflows;
- error-prevention checks;
- general action sequences.

Be cautious with:
- model-specific command shortcuts;
- workarounds for weak tool-use behavior;
- highly fragmented micro-instructions;
- procedures tied to one model's interaction budget.

For cross-model deployment, run a target-model validation gate instead of assuming a source-model skill transfers.
