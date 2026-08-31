# AGENTS.md

- `plugins/obsdog/skills/` contains the authored workflows.
- The plugin name is `obsdog`; clients expose its skills with the `obsdog:` prefix.
- Keep local MCP disabled by default because the install directory is not necessarily the intended Personal Space.
- Never broaden a selected Space or document authorization through a skill or plugin.
- Keep credentials, private content, raw queries, labels, and comments out of this repository.
- Validate every skill and plugin before committing.
- Commit messages use `{type}: {imperative message}`.
- This repository is proprietary and private until the release gate in `obsdoghq/obsdog` is satisfied.
