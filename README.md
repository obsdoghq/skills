# ObsDog Skills

Official skills and plugins for [ObsDog](https://obsdog.ai), the
local-first knowledge tool for people and AI. The same five workflows support
Codex and Claude Code. This repository is public; installing a plugin does not
grant access to any private Space.

The single `obsdog` plugin intentionally groups five user workflows so
clients display a stable namespace:

- `obsdog:find` — find, open, use, and trace exact knowledge revisions;
- `obsdog:remember` — capture intentional durable Markdown knowledge;
- `obsdog:maintain` — evolve, organize, review, and recover knowledge;
- `obsdog:report` — generate a private standalone HTML health report;
- `obsdog:documentify` — turn an authorized repository into auditable knowledge.

The namespace is provided by the plugin. Portable skill folders keep the short
names so both clients load the same instructions. Claude Code exposes commands
such as `/obsdog:find`; Codex shows the five skills within the ObsDog plugin and
invokes their short skill names such as `$find`.

Benchmark and product-comparison workflows are intentionally not distributed in
this user plugin. They remain separate internal evaluation work.

## Requirements and data boundaries

Use [ObsDog CLI v0.1.16 or newer](https://github.com/obsdoghq/obsdog-releases)
for the current workflow set, including Living memory and source-aware care.
The skills inspect installed capabilities before using a command. Keep explicit
agent authorship on import/update as well as search/open/use. Evaluation identity is
separate. With no explicit boundary, commands share Personal across directories;
`init` is optional project guidance, not a prerequisite. A broken explicit
selection must not silently fall back to Personal. Check installed help
before use; never silently omit unsupported attribution flags. An already-scoped
MCP server can provide its own agent identity without CLI flags. This repository
does not install or update the CLI/plugin on the user's behalf.

## Install

```sh
codex plugin marketplace add obsdoghq/skills
codex plugin add obsdog@obsdog-skills
```

Claude Code uses the same repository as a marketplace:

```sh
claude plugin marketplace add obsdoghq/skills
claude plugin install obsdog@obsdog-skills
```

Update or remove the package explicitly:

```sh
codex plugin marketplace upgrade obsdog-skills
codex plugin remove obsdog@obsdog-skills

claude plugin marketplace update obsdog-skills
claude plugin update obsdog@obsdog-skills
claude plugin uninstall obsdog@obsdog-skills
```

The bundled local MCP declaration is disabled by default. Enable it only after
selecting the intended Personal Space; otherwise use `obsdog mcp --path PATH`
explicitly. The skills also work through the installed ObsDog CLI.

No package, binary, or hosted credential is included. Installation does not
grant access to a Space and never broadens the authorization of the invoking
human or agent.

## Knowledge care and Living memory

The shared [care guide](plugins/obsdog/skills/maintain/references/knowledge-care.md)
explains source ownership, context-preserving blocks, justified references,
revision-bound review and recoverable changes. Maintain code contracts and
runbooks with their authoritative source; retain useful pointers or reusable
lessons in ObsDog instead of copying a parallel manual. Routine corrections are
AI-managed within existing authority, with evidence and readback. Missing
authority still requires consent. Reports are private, read-only HTML and never
invent historical trends or present AI judgments as human verification.

Actual open/use/evaluation records can strengthen query associations and co-use
connections; old activation fades without deleting knowledge. CLI v0.1.16 and
server v0.1.27 support this bounded policy. `memory show` inspects the evidence;
`--ranking lexical` retains the comparison baseline. Low usage is not bad quality.
Browser views observe synced CLI evidence rather than inventing click/use ratings.
No background worker, automatic upload or source deletion is enabled by installing
the plugin. Keep the five skills and their shared reference together.

## Validate a source checkout

```sh
python3 scripts/validate.py
```

`python3 scripts/validate.py` also executes the declared MCP command through a
temporary harmless stub. The integration check proves the process receives the
fixed `mcp --path .` arguments, starts in only the selected directory, inherits
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
