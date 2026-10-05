# AI client integration decisions

Remote packaging and hooks checked 2026-10-05 against official client docs;
local CLI behavior retains the earlier checked contract. This page distinguishes
instruction routing from actual tool access; neither a prompt nor a plugin
installation grants access to an unauthorized Space.

## Recommended shape

1. Install the four ObsDog skills with the selected runtime. A private connected
   app package uses authorized remote MCP tools without the ObsDog CLI. A local
   library uses the CLI. The skills describe *when* and *how* to find, remember,
   maintain and documentify while preserving actual capabilities and scope.
2. For proactive use in local Codex, review and trust the optional SessionStart
   command hook. It supplies short routing guidance without editing AGENTS.md.
   File-based clients can instead adopt the reviewed
   [routing rule](SETUP.md#optional-proactive-use). Neither path authorizes capture.
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
for details, or use the reviewed start hook without editing that file. Never
blindly append to a symlinked or overridden instruction
file. Do not copy the entire skill into every project.

RTK's hook rewrites eligible shell commands before execution; its awareness
file is a different problem. ObsDog's decision to search or capture depends on
task meaning, source authority, permission and Space scope. A generic
`PreToolUse` rewrite cannot make that decision. Automatic session capture or
shallow recall could be a separate, opt-in product with its own privacy and
quality evaluation; it is not installed by this plugin.

## Local and hosted MCP expose different capabilities

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
carries typed tools and enforces scope. This limitation describes local stdio,
not every hosted ObsDog connection.

The hosted MCP catalog can include search, frozen result paging/open, exact
document/block reads, revision paging, document creation, block updates and
request-receipt lookup. Read the actual catalog and capabilities. Creation and
updates require the selected Space's write policy, current paired base revisions
where applicable, stable request identity and exact read-back. Append, direct
use, feedback and structural care are not implied by write scope. The packaged
[remote reference](../plugins/obsdog/skills/find/references/remote-mcp.md)
describes these boundaries; unavailable operations do not trigger CLI fallback.

## One private plugin, four skills, client-specific routing

The private package combines one existing registered app mapping, all four
skills and an optional Codex hook. The registered app supplies remote tools and
authentication. The package does not create a second MCP connection. Follow the
[bundle guide](PRIVATE_PLUGIN.md) and keep private app IDs outside this public
checkout. A private upload is separate from a public marketplace submission.

| Client | Skills and remote tools | Proactive guidance |
| --- | --- | --- |
| Local Codex | Installed plugin and authorized connection | Reviewed SessionStart command hook, or existing instructions |
| ChatGPT | Installed supported plugin and connected app | Select the plugin for the task; optionally adopt a user-approved preference |
| dots | Supported installed/enabled account plugin and its connection | Give the task or dot a clear approved instruction; selection is task-dependent |

The hook reads only its packaged context and prints SessionStart
`additionalContext`. It does not read the event's transcript or working
directory, run ObsDog, search, capture or modify instruction files. The packaged
POSIX command requires `python3`. Non-managed command hooks require the client's
trust review; installing the plugin is not that review. Changed commands can
require review again.

Personal command hooks do not run in cloud-orchestrated ChatGPT/dots tasks,
even when a local computer provides executor tools. Plugin skills are considered
from their descriptions and loaded when selected. Do not claim they run on every
task merely because installed. dots can use supported connected account plugins;
local skill files need an available connected computer. This private remote app
package avoids that local ObsDog CLI dependency.

## Capture at delegated and interrupted boundaries

Include this compact checkpoint in the host's existing task handoff when the
user has authorized capture; it is not a new automatic hook or permission:

> Before delegating or yielding for input, return the capture disposition:
> what was established, the actual saved target/revision and read-back/retrieval
> checks, or the exact missing prerequisite. Capture new learning even after a
> successful search. Do not promise that a parent will save it without returning
> a real receipt or an explicitly unsaved private draft. No-memory prohibits
> saving or persisting a draft. The parent verifies evidence before accepting
> capture as complete; do not duplicate the write to perform that read-back.

Use the packaged [capture checkpoints](../plugins/obsdog/skills/remember/references/checkpoints.md)
for six concrete paths, including repaired misses, pauses and unavailable atomic
preparation. The original task may continue with a blocked capture disposition.
An unrelated unsupported atomic operation does not block ordinary supported
capture. Installed instruction loading, actual host invocation and actual saved
knowledge require separate checks; passing static packaging tests proves none
of those operating outcomes. Do not automatically edit a user's host files.

## Primary references

- [Codex AGENTS.md discovery and precedence](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Claude Code CLAUDE.md imports and loading](https://code.claude.com/docs/en/memory)
- [Claude Code plugin-provided MCP startup](https://code.claude.com/docs/en/mcp#plugin-provided-mcp-servers)
- [OpenAI plugin architecture: skills, MCP and hooks](https://developers.openai.com/plugins/concepts/plugins)
- [OpenAI skills versus MCP tools](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI plugin packaging and registered app mapping](https://developers.openai.com/plugins/build/plugins)
- [ChatGPT/Codex hook execution and trust](https://learn.chatgpt.com/docs/hooks)
- [Plugin skill loading](https://learn.chatgpt.com/docs/skills-and-plugins)
- [dots computers and connected apps](https://learn.chatgpt.com/docs/dots/computers-and-apps)
- [RTK supported-agent integration](https://github.com/rtk-ai/rtk/blob/develop/docs/guide/getting-started/supported-agents.md)
