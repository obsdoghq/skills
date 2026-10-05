# Set up ObsDog for your AI client

The plugin teaches four workflows for a selected local CLI library or an
already-authorized remote MCP connection. Remote tools need no ObsDog CLI.
For the local path, install both using the [Quick Start](../README.md#quick-start-cli--plugin-together),
or use the documented separate steps. The user-invoked setup helper composes
the public Homebrew CLI and agent marketplace; there is no plugin post-install
download, automatic knowledge upload or automatic global-file edit.
MCP is optional; CLI-driven skills need no MCP setup. From plugin v0.3.3,
Codex keeps a disabled declaration inside its own manifest, while Claude
has no automatically discovered plugin MCP server. This avoids relying on one
client's enablement flags in another client. Updating the plugin does not enable
a connection or modify an independently configured MCP server.

## Remote readiness checklist

1. The client lists the plugin's four skills and its connected ObsDog app.
2. Inspect the actual remote capabilities and permitted Spaces. Preserve the
   selected exact Space and policy; read access is not write permission.
3. In a fresh task, select find and search/open a harmless existing note. This
   checks actual skill invocation and tool access separately from installation.
4. If writes are authorized, check a bounded write receipt and read the exact
   accepted revision back. An unavailable tool remains unavailable; do not
   install or use the CLI to bypass the connected app's policy.

Use the [private bundle guide](PRIVATE_PLUGIN.md) to combine skills with an
existing registered app. Package validation, installation, model invocation
and read/write acceptance are distinct checks.

## Local readiness checklist

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

Local Codex can load the short routing context from the packaged SessionStart
command hook after the client reviews and trusts that command. It reads only
its own static context file and emits `additionalContext`; it does not edit
AGENTS.md, collect transcripts or perform searches/writes. The POSIX launcher
requires `python3`. Review changed hook commands again when the client asks.

ChatGPT and dots use plugin skills when selected for a relevant task; this
personal command hook does not run in their cloud orchestration. To request
ongoing proactive use there, adopt a short approved preference or include the
rule in the task. Installing a plugin alone does not guarantee selection on
every task or authorize capture. See [client integration](AI_CLIENT_INTEGRATION.md).

If you prefer file-based instructions, put this **small routing
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

Before adopting the capture rule, check whether your Personal Space is local-only
or already connected: new notes in a connected Space can upload. Choose the
mode you want once; ordinary work in that approved mode needs no per-repository
approval. Merge once under an existing
ObsDog heading if present; do not replace the file or add repeated copies.

```md
## ObsDog

<!-- Routing snippet: obsdog-routing/2026-09-30; plugin 0.3.17+. -->

- Use ObsDog find throughout the work to retrieve and apply relevant knowledge,
  context, and background. Search again as new questions arise; reuse evidence
  already checked for the same question and scope. If memory misses or is
  unavailable, continue from authorized source material.
- Use remember to capture new knowledge and update existing notes with findings
  from the work, regardless of whether retrieval succeeded. Use maintain to
  organize and improve the knowledge base.
- Use documentify to investigate source material and build or expand connected
  knowledge that future work can find and use.
```

For **search-only** use, replace the remember/maintain and documentify bullets with:
“Search and read only. Ask before remembering or changing knowledge.”

Adopting the write workflows authorizes ongoing capture and supported
maintenance in your selected, already-reviewed storage mode. Follow explicit
Space/source/upload restrictions and read-only/no-memory requests. With no
explicit boundary, use Personal; a broken explicit selection does not fall back.
No per-note permission question is needed within that standing scope.

These rules guide behavior, not guaranteed automatic execution on every task.
They do not alter client approvals or grant access to an unauthorized Space.
When a source-backed answer repairs a search miss, the work-owning agent saves or
updates it within the approved scope, then returns the document and verification
in its completion/handoff. Check that the original lookup finds the intended
answer, not merely any result. Keep this procedure in skills, not a longer global
routing prompt.
On CLI v0.2.12+, verify a repair with `obsdog search --no-observe --query
"<original query>"` in the same Space. This leaves no retrieval run or use
handle; ordinary task searches should still be observed. Older CLIs record a
diagnostic retry, so keep its agent attribution and do not read that run as
unbiased product traffic.
Use `obsdog dashboard serve` for local visibility and `obsdog insights show`
for machine-readable measures. HTML export remains an explicit CLI option.

This is a workflow throughout active work. The start hook supplies instructions
only; it does not record tool calls, save sessions or run background maintenance.
See the
[synthetic evaluation cases and measurement limits](EVALUATION.md) for how missed
recall and unsafe capture should be checked independently of search ranking.

## Optional first-library bootstrap

Installation intentionally leaves the library empty. If GitHub, Slack or
repository tools are already connected to your AI client, ask for a **proposal**
before copying anything into ObsDog. Connected access is not permission to
ingest everything. The AI should check the selected Space and sync mode,
inspect only authorized sources, identify a few durable candidate notes or
source pointers, name each source owner/version and intended Space, then ask
which candidates to import. Maintained code contracts and runbooks stay in
their source repositories. Search for duplicates, import only selected items,
and read back the results. A blank start is also a valid choice.

For infrastructure repositories, one useful candidate is a compact navigation
map: common task or question → owning repository → maintained architecture or
runbook → relevant code/configuration entry point. Include cross-repository
handoffs only when the authorized sources establish them. This is a proposal,
not an automatic crawl or a snapshot of every file; verify moving paths against
the repository before acting on them.

```text
Help me bootstrap my ObsDog library, but do not import anything yet. Check the
selected Space and whether it syncs. Survey only the repositories or connected
tools I authorize for this task. Propose up to five reusable, source-grounded
notes or pointers with their canonical source, checked version/date, privacy
boundary and why future work would retrieve them. Ask me which to create;
do not copy raw conversations, secrets, transient logs or whole repositories.
If infrastructure repositories are in scope, consider a compact map from common
questions to the owning repo, maintained docs and code/configuration entry points
instead of a file-tree dump.
```

Use `documentify` for systematic source investigation and connected explanations,
including multiple repositories, docs, configurations, infrastructure or work
records within the agreed scope. For an individual finding, use `remember`.

## Updating CLI and agent guidance

CLI and plugin versions advance separately. For a Homebrew CLI, use
`brew update && brew upgrade obsdoghq/tap/obsdog`; a verified standalone CLI
uses `obsdog update --check` and `obsdog update`. Refresh the agent marketplace
separately:

```sh
codex plugin marketplace upgrade obsdog-skills
codex plugin add obsdog@obsdog-skills
# Or, for Claude Code:
claude plugin marketplace update obsdog-skills
claude plugin update obsdog@obsdog-skills
```

After updating, restart any running `obsdog dashboard serve` or
`obsdog wiki serve` process with its previous Space/port flags; a browser
refresh alone keeps the old server. Reconnect existing agent sessions so
host-owned `obsdog mcp` processes and skill metadata load the new versions.
Check `obsdog version`
in a new shell and, when MCP is enabled, from the reconnected client. See the
[local dashboard lifecycle](https://github.com/obsdoghq/obsdog-releases/blob/main/guides/local-dashboard.md).
The installer does not terminate user-managed processes.

For a machine-readable check on CLI v0.2.19+, run
`obsdog dashboard status --port 47777 --format json` (use your actual port).
This reads only the existing listener and never initializes a library. The
running dashboard's existing endpoint is
`http://127.0.0.1:47777/_obsdog/health`: it reports `version`, `channel`,
`space_id` and `restart_required`; newer viewers also report `started_at`.
It is not `/api/version` or `/healthz`. A 404 or unverifiable response is not
evidence that the installed CLI is serving that port. For MCP, invoke
`obsdog_version` **in the existing connection** and compare with the new shell.
That process may still be old even when the dashboard is current. Check after
restarting/reconnecting; do not terminate unrelated listeners or agent sessions.

The plugin never overwrites AGENTS.md or CLAUDE.md: compare any newer optional routing
snippet with your existing rule and merge only the desired change. Do not
remove organization policy or silently grant capture/sync authority.

The snippet revision marks guidance, not the CLI schema or a migration gate.
An older custom rule is not automatically wrong. Review new workflow changes
and merge only the changes you want under the existing ObsDog heading; keep
command syntax in the installed skills. Do not append another copy at each
upgrade. The installed skill entrypoints link back to this checklist.

Use the client's plugin manager for updates. Hand-made links from a global
skills directory into a version-numbered plugin cache are **not** managed by
this installer and can keep loading an old skill after the marketplace updates.
If you use such links, verify every resolved `SKILL.md` after an update or
remove the duplicate manual links and use the plugin-provided skills. Do not
infer an effective skill version from `claude plugin update` when working in
Codex (or vice versa); check the client you are actually using.

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
