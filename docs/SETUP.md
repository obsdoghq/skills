# Set up ObsDog for your AI client

The CLI stores and operates on knowledge. The plugin teaches four workflows.
Install both using the [Quick Start](../README.md#quick-start-cli--plugin-together),
or use the documented separate steps. The user-invoked setup helper composes
the public Homebrew CLI and agent marketplace; there is no plugin post-install
download, automatic knowledge upload or automatic global-file edit.
MCP is optional; CLI-driven skills need no MCP setup. From plugin v0.3.3,
Codex keeps a disabled declaration inside its own manifest, while Claude
has no automatically discovered plugin MCP server. This avoids relying on one
client's enablement flags in another client. Updating the plugin does not enable
a connection or modify an independently configured MCP server.

## Readiness checklist

1. `obsdog version` prints v0.2.4 or newer **inside the agent's environment**.
   If a desktop client inherited an older PATH, restart the client after fixing
   PATH using the CLI installation guide. Do not add a second CLI copy as a fix.
2. The intended client lists the ObsDog plugin and its four skills.
3. Start a fresh session and explicitly select the plugin's `find` skill.
   Claude Code also supports `/obsdog:find`; in Codex select find under ObsDog
   before using `$find` if other plugins use the same short name.
4. Ask it to inspect `obsdog space status`, list documents, then find a known
   harmless note. Search and open only what you intend to examine. Do not
   manufacture use/ratings just to complete setup; no documents is a valid state.

This is three different checks: package installed, executable available, and
skill actually invoked. The CLI and plugin have independent versions/updates.
No account, sync, repository `init`, background worker or hosted permission is
required. Installation does not ingest a repository or upload a Space.

## Optional proactive use

If you want the AI to use ObsDog during ordinary work, put this **small routing
rule** in your user-level instructions. Leave procedures and command syntax in
the versioned skills, not in every project prompt. This is not required for
explicit skill invocation and is not a security boundary enforced by the CLI.

- Codex: `~/.codex/AGENTS.md`, or `AGENTS.md` inside your configured `CODEX_HOME`.
  If a global `AGENTS.override.md` is active, inspect precedence first; do not
  delete it or silently write a rule into a file that will not load.
- Claude Code: `~/.claude/CLAUDE.md` for all your projects. Keep organization and
  project policies intact. Do not import the complete plugin README into it.
- For one project only, use that project's existing instruction file. Specify
  the intended exact Space ID when its knowledge must stay separate. Current
  directory alone does not select a Space. Do not commit personal Space IDs or
  private paths into a public repository.

Copy after reviewing the capture permission below. Merge once under an existing
ObsDog heading if present; do not replace the file or add repeated copies.

```md
## ObsDog knowledge

- Use ObsDog find early for prior decisions/fixes/incidents, existing internal
  behavior/configuration/conventions, and nontrivial debugging/design/migrations
  where project history could change the approach, even without an ObsDog request.
  Search a few specific terms, open promising hits and verify current source
  evidence. No useful hit or unavailable memory must not block the actual task.
- After a bounded no-hit retry, distinguish a search miss from a real coverage
  gap. If authorized source work verifies reusable missing knowledge, hand it
  to remember before finishing; a no-hit alone is not a reason to save.
- Skip incidental recall for general concepts, supplied-text transformations and
  name mentions alone. Reuse already-read task evidence instead of searching
  every follow-up. Honor explicit source restrictions and no-memory requests.
- Honor an explicitly selected Space on every command. Otherwise use Personal
  only for knowledge permitted there; a broken explicit boundary must not fall
  back. Never copy organization/project-private material to Personal implicitly.
- I authorize relevant local capture and supported maintenance during active
  tasks. At meaningful completion, use remember for verified reusable findings
  or durable decisions: check the canonical home and duplicates, retain source,
  checked date/version and scope, then read back. No useful new learning means
  no write. Do not save chatter, raw logs, secrets or unverified claims as facts.
  Read-only/no-memory requests override this rule.
- Attribute agent actions; distinguish returned, opened, used and useful.
  Record use only when knowledge actually supports the work, with honest reasons.
- Do not enable login, sync, sharing, publishing, telemetry or background jobs
  from this instruction. A Space already connected to sync can upload new notes;
  inspect its status and existing owner permissions before capture.
```

For **search-only** use, replace the capture/maintenance permission bullet with:
“Search and read only. Ask before remembering or changing knowledge.”

These rules guide behavior, not guaranteed automatic execution on every task.
They do not alter client approvals or grant access to an unauthorized Space.
Use `obsdog dashboard serve` for local visibility and `obsdog insights show`
for machine-readable measures. HTML export remains an explicit CLI option.

This is an entry/exit decision during active work, not a hook that records every
tool call or saves every session. The plugin does not install automatic recall,
transcript collection or background maintenance. See the
[synthetic evaluation cases and measurement limits](EVALUATION.md) for how missed
recall and unsafe capture should be checked independently of search ranking.

## Copyable setup request

Paste into your AI client after installing the CLI and plugin:

```text
Check my ObsDog setup without changing knowledge or enabling cloud sync.
Verify the CLI version in your process, the installed plugin, the intended Space
and the available skills. Tell me which checks you actually performed.
Inspect my active user-level instruction file and any override before proposing
the optional ObsDog routing snippet from the official setup guide. Preserve
unrelated rules and show the scoped diff; apply it only after I agree to the
capture permission. Do not install/reinstall anything or launch background jobs.
Then guide me through a fresh-session find invocation using a harmless existing
note; if the library is empty, say so instead of creating a test note or rating.
```

We deliberately do not copy RTK's command-rewriting hooks: ObsDog needs
task-sensitive selection, authorized capture and evidence-based evaluation, not
rewriting every shell command. A separate setup skill is unnecessary for these
few one-time checks; the guide is the single installation entrypoint. See
[AI client integration](AI_CLIENT_INTEGRATION.md) for the `@`-import, MCP and
hook tradeoffs.

## References

Checked 2026-09-28:

- [Codex global/project instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Claude Code user instructions and skills guidance](https://code.claude.com/docs/en/memory)
- [RTK supported-agent setup](https://github.com/rtk-ai/rtk/blob/develop/docs/guide/getting-started/supported-agents.md)

For installation problems use the [public feedback forms](https://github.com/obsdoghq/obsdog-releases/issues/new/choose)
with sanitized versions and reproduction steps, never your actual knowledge.
