# Claude Code Adapter

1. Copy `skills/ai-native-sdlc/` to your repository's preferred skill location.
2. Use the sample `CLAUDE.md` as repository context, not as a replacement for the skill.
3. Adapt `.claude/settings.example.json` to connect hooks supported by your Claude Code environment.
4. Keep company-specific security/compliance knowledge in separate skills and route to them from the SDLC orchestrator.

Do not copy hook examples into production without adapting paths and approval integrations.
