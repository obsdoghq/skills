# AI client integration decisions

Checked 2026-09-29 against the current plugin and CLI. This page distinguishes
instruction routing from actual tool access; neither a prompt nor a plugin
installation grants access to an unauthorized Space.

## Recommended shape

1. Install the CLI and the ObsDog plugin. The four skills describe *when* and
   *how* to find, remember, maintain and documentify. The CLI is the complete
   local interface and keeps the selected Space, actor and evaluation records.
2. For proactive use, add the short, reviewed [routing rule](SETUP.md#optional-proactive-use)
   to the user's instruction file. It is deliberately optional and does not
   alter permissions, start hooks, or upload data.
3. Use `obsdog dashboard serve` for local state and trends. `obsdog insights
   show` is the machine-readable view. The older `obsdog report create` remains
   an explicit portable HTML export, not a separate everyday skill.

## Why not a bare `@ObsDog.md` line everywhere?

Claude Code explicitly expands `@path/to/file` imports in `CLAUDE.md` at
startup. An imported external file in a project can require user approval;
splitting a long file into imports does not reduce its loaded context. A small
shared user-level rule may be appropriate there, but it still needs the user's
capture and Space choices. Codex documents discovery of `AGENTS.md` and
`AGENTS.override.md`, with precedence by directory; it does **not** document
RTK-style `@file` expansion as a Codex import contract. A bare pointer could be
read as plain text and leave the routing rule inactive. For Codex, keep the short
actual routing rule in the loaded `AGENTS.md`, with a normal link to this guide
for details. Never blindly append to a symlinked or overridden instruction
file. Do not copy the entire skill into every project.

RTK's hook rewrites eligible shell commands before execution; its awareness
file is a different problem. ObsDog's decision to search or capture depends on
task meaning, source authority, permission and Space scope. A generic
`PreToolUse` rewrite cannot make that decision. Automatic session capture or
shallow recall could be a separate, opt-in product with its own privacy and
quality evaluation; it is not installed by this plugin.

## MCP is supported, but not a replacement for the full workflow

`obsdog mcp --space personal` serves local stdio MCP. The current server has
version/Space status, search, result paging/open, document read, trace,
lineage and care inspection tools. Search and open can record retrieval
observations. It does **not** yet expose remember/import/update, direct use,
feedback or care mutations. Calling it wholly read-only would obscure its
search/open telemetry, while calling it a full write interface would be false.

The Codex plugin contains a disabled Personal-scoped MCP declaration. Claude
Code loads plugin-bundled MCP servers automatically when a plugin is enabled,
so this package intentionally has no Claude MCP declaration. Explicitly
configure a client connection only after checking the exact Space and the
tools it would expose. Do not assume current working directory selects a
Space. Keep CLI as the documented complete path; use an already-authorized MCP
for its supported read/discovery tasks, not as a reason to add broad remote
access or duplicate a search through both transports. The skills remain useful
with either transport because they carry workflow and evidence rules; MCP
carries typed tools and enforces scope.

## Primary references

- [Codex AGENTS.md discovery and precedence](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Claude Code CLAUDE.md imports and loading](https://code.claude.com/docs/en/memory)
- [Claude Code plugin-provided MCP startup](https://code.claude.com/docs/en/mcp#plugin-provided-mcp-servers)
- [OpenAI plugin architecture: skills, MCP and hooks](https://developers.openai.com/plugins/concepts/plugins)
- [OpenAI skills versus MCP tools](https://developers.openai.com/plugins/concepts/skills)
- [RTK supported-agent integration](https://github.com/rtk-ai/rtk/blob/develop/docs/guide/getting-started/supported-agents.md)
