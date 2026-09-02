# Codex Adapter

Use `AGENTS.md` for stable repository instructions and expose `skills/ai-native-sdlc/SKILL.md` through the execution harness used by your Codex environment.

Recommended mapping:

- `AGENTS.md` → repository context and commands;
- `SKILL.md` → lifecycle orchestration;
- `docs/changes/<ID>` → durable task state;
- CI/hooks → deterministic enforcement;
- eval cases → behavior regression suite.
