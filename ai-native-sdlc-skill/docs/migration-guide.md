# Migration from Conversation-Driven Coding

## Before

```text
Ticket → Chat → Code → PR → Human discovers missing context
```

## After

```text
Ticket → Intent → Spec → Plan → Code → Verification → Review → Release
```

## Migration rule

Do not force every historical document into the new format. Start at the next meaningful change boundary. Existing ADRs, tickets, PR descriptions, and architecture documents may remain authoritative and be referenced from the change package.

## Existing large prompts

Split them into:

- repository instructions: stable local facts and commands;
- specialized skills: reusable domain knowledge;
- task artifacts: current change state;
- policies/hooks: enforceable controls.
