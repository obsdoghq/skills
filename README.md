# ObsDog Skills

Internal implementation is tracked in Project draft tickets, not duplicate Issues.
Use [GitHub issues](https://github.com/obsdoghq/skills/issues) for product feedback and follow
[the feedback guide](https://github.com/obsdoghq/obsdog-releases/blob/main/FEEDBACK.md);
private execution plans do not belong here.

Official skills and plugins for [ObsDog](https://obsdog.ai), the
local-first knowledge tool for people and AI. The same four workflows support
Codex and Claude Code. This repository is public; installing a plugin does not
grant access to any private Space.

The single `obsdog` plugin intentionally groups four user workflows so
clients display a stable namespace:

- `obsdog:find` — retrieve and apply knowledge and context throughout work;
- `obsdog:remember` — capture findings and update existing notes;
- `obsdog:maintain` — organize, reconcile and improve the knowledge base;
- `obsdog:documentify` — investigate sources and build connected explanations.

The namespace is provided by the plugin. Portable skill folders keep the short
names so both clients load the same instructions. Claude Code exposes commands
such as `/obsdog:find`; Codex shows the four skills within the ObsDog plugin and
invokes their short skill names such as `$find`.

Benchmark and product-comparison workflows are intentionally not distributed in
this user plugin. They remain separate internal evaluation work.

## Requirements and data boundaries

Use [ObsDog CLI v0.2.4 or newer](https://github.com/obsdoghq/obsdog-releases)
for the current workflow set, including Living memory and source-aware care.
The skills inspect installed capabilities before using a command. Keep explicit
agent authorship on import/update as well as search/open/use. Evaluation identity is
separate. With no explicit boundary, commands share Personal across directories;
`init` and filesystem Space selectors have been removed. Use `--space personal`
or an exact local Space ID; cwd is never a selection boundary. A broken explicit
selection must not silently fall back to Personal. Check installed help
before use; never silently omit unsupported attribution flags. An already-scoped
MCP server can provide its own agent identity without CLI flags. Merely adding
this plugin does not install the CLI; the explicit Quick Start below can prepare
both.

## Install

### Quick Start: CLI + plugin together

On Apple silicon macOS, first install your chosen agent client. Homebrew is
needed if the ObsDog CLI is not already installed.
The first-party `https://obsdog.ai/install.sh` entry pins and checksum-verifies
the public helper. It performs both installs for one client and checks the CLI:

```sh
curl -fsSL https://obsdog.ai/install.sh | sh -s -- --client codex
obsdog version
obsdog document list
```

For Claude Code, change the final flag to `--client claude`. You can
[inspect the exact helper](https://github.com/obsdoghq/obsdog-releases/blob/d64550e384c3ed7c577c26d707f062e847c5985a/scripts/setup-agent.sh)
and download the first-party entry for inspection before running it, or append
`--dry-run`. An empty list is normal; no project
`init`, account, sync or sample upload is involved. Open a fresh agent session
and call ObsDog `find` to confirm skill discovery. The helper does not edit
AGENTS.md or CLAUDE.md. If Homebrew is unavailable, use the separate steps below.

The plugin supplies instructions; the CLI runs the local knowledge store. A
successful `plugin add` alone does not install the `obsdog` executable.

### Separate installation steps

### 1. Install or verify the CLI

Follow the [official CLI installation guide](https://github.com/obsdoghq/obsdog-releases#cli-free-beta--apple-silicon-macos),
then run:

```sh
obsdog version
obsdog document list
```

The current skills require CLI **v0.2.4+**. `command not found` means the CLI is
missing or not on your client process's `PATH`; see the guide before proceeding.
An empty document list is normal for a new Personal Space. No login or project
initialization is required. Do not install both Homebrew and standalone copies.

### 2. Add the plugin to your chosen client

```sh
codex plugin marketplace add obsdoghq/skills
codex plugin add obsdog@obsdog-skills
```

Claude Code uses the same repository as a marketplace:

```sh
claude plugin marketplace add obsdoghq/skills
claude plugin install obsdog@obsdog-skills
```

### 3. Verify in a fresh client session

Choose **find** inside the ObsDog plugin in Codex, or use `/obsdog:find` in Claude
Code, and ask it to find an existing note in the intended Space. Verify that the
client loads the skill and can run `obsdog version`. An empty result is okay for
a new Space; a missing skill or executable is not successful setup. CLI smoke
tests alone do not verify next-session skill invocation.

For ongoing AI-managed knowledge, add the short **optional**
[global instruction snippet and setup prompt](docs/SETUP.md#optional-proactive-use).
Manual skill invocation works without changing global instructions.
For an empty library, the [optional bootstrap guide](docs/SETUP.md#optional-first-library-bootstrap)
can propose a few source pointers or a task-oriented infrastructure repository
map before any import; installation itself does not scan repositories.

## Browse your documents

Plugin v0.3.17 keeps four short workflows and links runtime/update checks from
their installed entrypoints. Find recalls
throughout work; remember creates and updates individual findings; maintain
organizes/reconciles the knowledge base; documentify builds connected explanations
from authorized sources. CLI mechanics live in focused references. Capture is
independent of search success. There are no new hooks, uploads or automatic jobs,
and no measured invocation or retrieval-quality gain is claimed.

Use the [update checklist](docs/SETUP.md#updating-cli-and-agent-guidance) to restart
your dashboard and reconnect long-lived MCP sessions after a CLI upgrade. See
[workflow changes and migration notes](CHANGELOG.md) for earlier versions,
including the removal of `obsdog:report`.

```sh
obsdog document list
obsdog document list --space personal --format json
obsdog document read --id <document-id>
obsdog dashboard serve
```

List shows document IDs, titles and active block counts, newest update first.
The dashboard opens at `http://127.0.0.1:47777`; its Knowledge tab reads Markdown.
Listing and overview viewing do not imply that every document was opened or used.

## Update or remove

Update the package explicitly:

```sh
codex plugin marketplace upgrade obsdog-skills
codex plugin add obsdog@obsdog-skills

claude plugin marketplace update obsdog-skills
claude plugin update obsdog@obsdog-skills
```

Only when you want to uninstall:

```sh
codex plugin remove obsdog@obsdog-skills
claude plugin uninstall obsdog@obsdog-skills
```

The Codex-only MCP declaration inside `.codex-plugin/plugin.json` is disabled by
default. Claude Code receives CLI-driven skills with **no automatically loaded
MCP server**. Both clients can use all four skills through the installed CLI.
The existing stdio MCP covers scoped discovery/read and retrieval observations,
not remember, direct use, feedback or care writes; it is not a full CLI replacement.
Enable or configure an optional MCP connection only after confirming access to
the exact selected Space. The Codex declaration uses `mcp --space personal`;
for another authorized Space, explicitly use `obsdog mcp --space <space-id>`.
Do not copy Codex-specific enablement flags into Claude's auto-loaded `.mcp.json`.

No package, binary, or hosted credential is included. Installation does not
grant access to a Space and never broadens the authorization of the invoking
human or agent.

## Feedback

[Report a bug, installation experience or idea](https://github.com/obsdoghq/obsdog-releases/issues/new/choose).
Use a tiny synthetic example and include CLI/plugin/client versions and what
you actually tested. Public issues must not contain documents, query histories,
tokens, private repository URLs or raw Space/diagnostic exports. See the
[feedback safety guide](https://github.com/obsdoghq/obsdog-releases/blob/main/FEEDBACK.md).
Posting product feedback is optional and separate from knowledge usefulness
ratings stored locally by `obsdog feedback add`.

## Knowledge care and Living memory

The [retrieval authoring guide](plugins/obsdog/skills/maintain/references/retrieval-authoring.md)
adds optional source-grounded entity overviews, question-to-source navigation,
context-complete reading and fair validation. Categories and graph density are
not ranking votes; finding a hub does not mean acquiring its linked answer.

The shared [care guide](plugins/obsdog/skills/maintain/references/knowledge-care.md)
explains source ownership, context-preserving blocks, justified references,
revision-bound review and recoverable changes. Maintain code contracts and
runbooks with their authoritative source; retain useful pointers or reusable
lessons in ObsDog instead of copying a parallel manual. Routine corrections are
AI-managed within existing authority, with evidence and readback. Missing
authority still requires consent. Reports use read-only local insights and the
offline dashboard; HTML is an optional explicit export, not the default.
Never invent historical trends or present AI judgments as human verification.

`obsdog dashboard serve` provides Knowledge, Graph, Activity and Sources on this
device without login or sync. `obsdog insights show` supplies bounded JSON and
actual UTC event windows. Source checks can record private-clone evidence with
`care source`; the MCP remains read-only for care mutations. Substring search
ignores spaces while preserving original text and earlier traces.

Actual open/use/evaluation records can strengthen query associations and co-use
connections; old activation fades without deleting knowledge. CLI v0.1.16 and
server v0.1.27 support this bounded policy. `memory show` inspects the evidence;
`--ranking lexical` retains the comparison baseline. Low usage is not bad quality.
Browser views observe synced CLI evidence rather than inventing click/use ratings.
No background worker, automatic upload or source deletion is enabled by installing
the plugin. Keep the four skills and their shared reference together.

## Validate a source checkout

```sh
python3 scripts/validate.py
```

`python3 scripts/validate.py` also verifies client-specific discovery boundaries
(no root `.mcp.json` or Claude MCP declaration) and executes the Codex-declared
MCP command through a
temporary harmless stub. The integration check proves the process receives the
fixed `mcp --space personal` arguments independently of its working directory, inherits
only the declared `PATH` plus operating-system locale bootstrap variables, and
receives no sync credential.

Validation checks the entire public checkout, documentation and metadata for accidental internal
details. This is a limited publication check, not a comprehensive secret audit.
Deployment and runner administration are not part of the plugin package.
CI runs these same checks on GitHub-hosted Ubuntu, with read-only permissions
and no deployment credentials.

### Existing contributors

Repository history was sanitized on 2026-09-28. Preserve any uncommitted work
and clone a fresh checkout before contributing. Do not merge the old history
back into `main`; carefully reapply only reviewed changes. Existing outside
clones and plugin caches are not changed by this repository update.

## License

Proprietary; public availability is not an open-source license. See [LICENSE](LICENSE).
