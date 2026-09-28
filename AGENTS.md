# AGENTS.md

- `plugins/obsdog/skills/` contains the authored workflows.
- The plugin name is `obsdog`; clients expose its skills with the `obsdog:` prefix.
- Keep local MCP disabled by default until access to the exact configured Space is authorized; cwd is not a Space selector.
- Never broaden a selected Space or document authorization through a skill or plugin.
- Keep credentials, private content, raw queries, labels, and comments out of this repository.
- Validate every skill and plugin before committing.
- Treat the entire repository, its history and Actions output as public.
  Keep named runners, host topology, private runbook paths and real account or
  Space identifiers in private operator documentation, never in that payload.
- Run publication-boundary tests with the packaging validator. Use GitHub-hosted
  validation only, with read-only permissions and no deployment credentials.
- Do not reintroduce pre-cleanup history; preserve local work and start from a
  fresh clone when contributing after the 2026-09-28 history cleanup.
- Commit messages use `{type}: {imperative message}`.
- This repository is public and proprietary. Do not imply an open-source license.
