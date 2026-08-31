# ObsDog Skills

Official private-preview skills and plugins for [ObsDog](https://obsdog.ai), the
knowledge observability platform.

The single `obsdog` plugin intentionally groups three coherent workflows so
clients display a stable namespace:

- `obsdog:search` — search, open, use, and trace exact knowledge revisions;
- `obsdog:maintain` — revise, label, comment, export, back up, and restore;
- `obsdog:evaluate` — run reproducible retrieval evaluations and baselines.

The namespace is provided by the plugin. Portable skill folders keep the short
names `search`, `maintain`, and `evaluate` so manifests remain valid.

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

## License

Proprietary and confidential. See [LICENSE](LICENSE).
