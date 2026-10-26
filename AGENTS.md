# AGENTS.md

## Mission and workflow guidance

- Follow the [canonical mission](https://github.com/obsdoghq/obsdog/blob/main/docs/MISSION.md):
  **Knowledge, made observable.** and **Make memory truly useful.**
- Prioritize active lookup and ongoing writing. Give concrete actions for search,
  contextual reading, capture, updates and read-back throughout the task.
- Record preliminary observations, hypotheses and open questions with their
  status and next check. Update them as evidence arrives; avoid subjective
  “valuable enough” or “fully confirmed” gates before writing.
- Keep runtime mechanics in references and preserve existing task/Space scope.

## Contribution tracking

- Follow the [central tracking workflow](https://github.com/obsdoghq/obsdog/blob/main/docs/TASK_TRACKING.md)
  for current work and verification. Jira replaced the closed GitHub Project;
  retained draft tickets are historical evidence, not the current ledger.
  Issues remain public feedback intake. Do not create a second implementation
  tracker or copy private ticket bodies or access details into this repository.
- Keep public acceptance evidence in the PR and relevant public docs. Do not
  mark package validation as actual client-session invocation or delivery.

## Packaging and publication

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
