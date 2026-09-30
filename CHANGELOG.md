# Workflow changes

## 0.3.17 — candidate, 2026-09-30

- Skill additions/removals/renames: none. All four workflows remain.
- Upgrade and missing-command checks are discoverable in the installed skill
  entrypoints, including reconnecting host-owned MCPs and the running viewer.
- The optional routing snippet has a revision marker. Review only an existing
  ObsDog section in AGENTS.md/CLAUDE.md; no file is overwritten automatically.
- Canonical explanations are question-oriented and updated selectively when
  relevant sources change. The work-owning agent closes source-backed search
  repairs with read-back and intended-answer lookup, including delegated handoffs.
- References document optional authored-link discovery and local source-file
  probes only when the installed CLI advertises them. These next-CLI candidate
  commands are not available in published v0.2.19; Markdown navigation remains.
- No hooks, implicit upload, automatic restart, schema migration or recall
  policy change is introduced. Publication remains separate from this candidate.

## 0.3.16 — 2026-09-30

- Skill additions/removals/renames: none. The same four entrypoints remain.
- Find recalls throughout investigation, implementation and verification.
- Remember handles individual new notes and ordinary existing-note updates.
- Maintain organizes structure, duplicates, conflicts, sources and navigation.
- Documentify investigates code, docs, infrastructure, issues and work context.
- Operational instructions move into each skill's `references/cli.md`.
- The optional global snippet becomes three routing bullets. Capture consent
  and actual Space/storage restrictions remain explicit installation choices.
- Care criteria now permit grounded cross-source explanations and useful work
  context; they do not require pointer-only notes or a task diary.
- Existing restart/health, probe, append, revision, retirement and attribution
  contracts remain. No transport, automatic hook or sync change is introduced.

Update using your client's plugin manager, then start a new agent session.
Cache-only edits can be overwritten. Merge the optional global snippet into
only your ObsDog section; preserve unrelated instructions and explicit limits.
Installed package checks do not demonstrate actual skill invocation or quality.

## Earlier changes

These historical entries describe earlier guidance. Use the current skill
entrypoints and setup guide for today's routing and capabilities.

Plugin v0.3.15 makes running-dashboard and MCP identity checks discoverable in
the installed workflows and explains label hiding versus duplicate retirement.
Use the [update checklist](docs/SETUP.md#updating-cli-and-agent-guidance) after
an upgrade; installing a plugin does not restart a long-lived CLI process.

Plugin v0.3.14 distinguishes observed task search from the CLI v0.2.12+
diagnostic probe. After a no-hit repair, agents can check the original query
without adding a retrieval run. It also explains the direct split/merge guard
and read-only legacy layout diagnosis; these do not repair old structure.

Plugin v0.3.13 brings running-dashboard and MCP restart checks into the AI
client update guide. `documentify` now separates imported, relation-reviewed,
resolved, unresolved, and intentionally standalone documents at handoff;
authored references are verified without treating links as a quota or a
search-quality claim.

Plugin v0.3.12 makes the no-hit completion owner explicit: when source-backed
work reveals a reusable answer after a miss, the same agent closes the
remember/maintain/no-write decision before finishing. Delegated work reports
that disposition to its parent. A miss alone never requires a new note.
Plugin v0.3.10 guides exact-revision full-document update, title correction and
evidence-backed duplicate supersession on CLI v0.2.10+, while retaining
block-level correction and structural Care on older compatible installs.
Plugin v0.3.8 makes the create-only `document import` identity boundary
explicit: find and inspect an existing canonical note before import, update
its current blocks or use care when it exists, and reserve new import for a
genuinely new document. The guide also distinguishes managed plugin updates
from hand-made links into versioned caches.
Plugin v0.3.7 adds a selective infrastructure repository map to documentify
and the optional onboarding guide; code and runbooks remain in their source repos.
Plugin v0.3.6 connects bounded no-hit source discovery to selective capture and
removes the redundant report skill; use `obsdog dashboard serve` for local
visibility. [AI client integration decisions](docs/AI_CLIENT_INTEGRATION.md)
explain the instruction-file, MCP and hook boundaries. Plugin v0.3.5 added concrete task-entry recall and authorized completion-capture
gates. It does not search merely because a name appears or save every session.

Migration from plugin 0.3.5 or earlier: `obsdog:report` was removed, not renamed.
Use `obsdog dashboard serve` for the live local view, `obsdog insights show` or
`obsdog metrics summary` for CLI data, and explicit HTML export when needed.
Plugin-managed upgrades replace its skill set; if you made your own symlink to
a versioned plugin cache, remove that stale link and use the supported plugin
installer instead. Do not point a new link at another versioned cache folder.
Bounded maintenance uses exact plans, actual outcome receipts and conditional
recovery; connected care requires server v0.1.29+ and compatible active writers.
No hooks, blanket transcript collection or background worker are installed.

Plugin v0.3.4 uses frozen result pages with global ranks, exact relative-reference
readback after documentification, and concise observed-memory summaries. It keeps
authored references, observed query/co-use and unconfirmed comment proposals
distinct. First-page use needs real page evidence, not an assumed Top 10. These
workflows never manufacture links or ratings just to fill a graph or dashboard.
