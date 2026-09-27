# ObsDog Skills

## Connected knowledge care (0.2.2)

Capture workflows search before adding, retain justified citations and separate
uncertain relationships as question-comment proposals. Maintenance reads the
[knowledge-care rubric](plugins/obsdog/skills/maintain/references/knowledge-care.md)
for meaningful block boundaries, merge/split/link decisions, review evidence,
recoverable retirement and before/after verification. Low usage is not bad
quality, and reference strength is not usefulness. Structural synchronization
needs separate acceptance; no new schema or background cleanup is enabled.

The same authored workflows ship for Codex and Claude. This source update does
not install/reinstall either plugin or enroll any Space in synchronization.

Official private-preview skills and plugins for [ObsDog](https://obsdog.ai), the
knowledge observability platform.

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

Use CLI v0.1.11 or newer for no-init Personal selection and explicit agent
authorship on import/update as well as search/open/use. Evaluation identity is
separate. With no explicit boundary, commands share Personal across directories;
`init` is optional project guidance, not a prerequisite. A broken explicit
selection must not silently fall back to Personal. Check installed help
before use; never silently omit unsupported attribution flags. An already-scoped
MCP server can provide its own agent identity without CLI flags. This repository
does not install or update the CLI/plugin on the user's behalf.

## Private development install

```sh
codex plugin marketplace add obsdoghq/skills
codex plugin add obsdog@obsdog-skills
```

Claude Code uses the same repository as a marketplace:

```sh
claude plugin marketplace add obsdoghq/skills
claude plugin install obsdog@obsdog-skills
```

Update or remove the private-preview package explicitly:

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

`python3 scripts/validate.py` also executes the declared MCP command through a
temporary harmless stub. The integration check proves the process receives the
fixed `mcp --path .` arguments, starts in only the selected directory, inherits
only the declared `PATH` plus operating-system locale bootstrap variables, and
receives no sync credential.

## License

Proprietary and confidential. See [LICENSE](LICENSE).
