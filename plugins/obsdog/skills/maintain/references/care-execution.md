# Bounded execution receipts

This workflow is for a care-capable CLI/server pair, not a promise that every
installed version supports it. It requires CLI v0.2.4+ and, for connected care,
server v0.1.29+ with compatible active writers. First inspect `obsdog care --help`; if `check`, `apply`,
`runs`, `defer` and `revert` are absent, use supported revision/comment
operations or retain the capability gap. Do not install an experimental binary
on the user's knowledge to make a proposed action possible.

## Own the small loop

Choose one evidence-backed change needed by the active task. Read the source and
current Markdown, then obtain exact document/block heads with structured reading.
Write an `obsdog.care-plan/v1` JSON file inside the authorized private boundary:

- exact `space_id`, one caller `request_id`, `actor_type: agent`, agent ID;
- `action`, `documents: [{id, revision_id}]` and any selected
  `blocks: [{id, revision_id}]`;
- concrete `reason`, `evidence: [{reference, checked_revision, finding}]`;
- the action's complete replacement, parts or title, never just a vague goal.

A complete fictional extraction plan follows. Replace every example identity
with the current selected Space and exact heads before checking it. The schema
uses `id`/`revision_id`, not document/block field aliases:

```json
{
  "schema": "obsdog.care-plan/v1",
  "space_id": "spc_example",
  "request_id": "request_example",
  "actor_type": "agent",
  "actor_id": "agent_example",
  "action": "extract-document",
  "documents": [{"id": "doc_example", "revision_id": "rev_document_example"}],
  "blocks": [{"id": "blk_example", "revision_id": "rev_block_example"}],
  "title": "Prior context",
  "reason": "Separate the selected complete section",
  "evidence": [{"reference": "fixture:source", "checked_revision": "rev_document_example", "finding": "Inspected the exact selected section and its boundaries"}]
}
```

Use IDs returned by the CLI, not titles, ranks or identifiers from this guide.
Evidence describes what you checked; it is not a human verification certificate.
Do not include credentials or copy a private source outside its permitted home.

| Action | Payload and boundary |
| --- | --- |
| `update-block` | One document/block, complete `content`; same authored kind/depth. |
| `update-document` | One document, complete replacement Markdown with unchanged block structure and/or a stored `title`; exact document head. |
| `append-document` | One exact document head, a heading-led Markdown suffix of at most 20 new blocks; preserve every existing block identity/revision. Requires the append capability on a connected Space. |
| `insert-document` | Capability-gated action: one exact document head, heading-led `content` and exact `before_block_id`; its receipt must prove that anchor and preserve all existing identities/parents. |
| `supersede-document` | Two exact document heads, duplicate source first and active canonical target second; no block copy or target revision change. Require concrete duplicate evidence. |
| `split-block` | One leaf, 2–20 explicit `parts`; each stays context-complete. |
| `merge-blocks` | 2–20 contiguous sibling leaves; reconciled `content`. |
| `extract-document` | One document, a complete contiguous subtree/range and new `title`. |
| `extract-titled-document` | When installed help advertises it: the same extraction plus one newly authored H1 root. Requires exact endpoint title-extraction capability when connected. |
| `merge-documents` | Two documents, source first and destination second; no block list. |

Stay within the runtime's bounds: two affected documents, at most 200 active
blocks per document, 256 KiB plan and 256 KiB each before/after frame. Resolve
relative/reference-style links to exact stable targets first when supported;
do not strip a link to force an extraction. No cross-Space move or hard deletion.

On CLI v0.2.10+, prefer `obsdog document update`, `document rename` or
`document supersede` when those exact operations fit; v0.2.14+ also offers
`document append` for a bounded new section. These high-level commands
construct the Care plan and return its receipt; `document import` never edits an
existing identity. A replacement that changes block boundaries is deferred
rather than guessed. An exact-ID read of a superseded document retains its
redirect and history; ordinary search omits its retired blocks.
All four document operations require protocol-2 preparation on a connected
Space, including a title-only rename or same-layout update. Append additionally
requires that exact server's `document_append_v1` capability (v0.1.34+).
Server/client versions alone do not satisfy preparation. Local-only operations
need no server; ordinary content-only `block update` is a separate revision path.

```sh
obsdog care check --space SPACE_ID --file plan.json --format json
obsdog care apply --space SPACE_ID --file plan.json --format json
obsdog care runs --space SPACE_ID --run RUN_ID --format json
```

`check` is a read-only preview, not a lock. Apply rechecks every base. A lost
response calls for exact request lookup before retry:

```sh
obsdog care runs --space SPACE_ID --request-id REQUEST_ID --actor-type agent --actor AGENT_ID --format json
```

Reuse the same request ID only with identical input. Read the current Markdown
and receipt after success. Verify intended context, successors, links and actor;
do not fabricate search use or a useful rating for a maintenance replay.

## Explicit boundary changes

For retirement, a new heading that intentionally changes parents, another parent,
or transfer into an existing document, read [structural Care](structural-care.md).
When installed help advertises `care structure --dry-run`, use it; ordinary update/move/insertion
retain their original protections. A contiguous `document split` is only one
expressible extraction, not a general cross-document movement capability.
`care schema --format json` returns the current field schema. Known defer causes
include `offending_block_ids`; check those exact blocks and preserve links.

## Match structural guidance to installed capabilities

Read `obsdog document --help` and `obsdog block --help` before choosing syntax.
Check the installed help and exact server capability before using these
commands. Some installed versions predate the structural shorthands or connected
batches. A plugin update does not upgrade the CLI/server.

- `document split --id DOC_ID --base-revision REV_ID --blocks BLOCK_ID,BLOCK_ID --title TITLE --reason TEXT --actor-type agent --actor AGENT_ID` performs one bounded `extract-document` Care transaction. A selected heading includes its descendants. Read both resulting documents and repair known navigation with returned successor IDs. This is not a move into an existing document.
- When installed help advertises it, add `--dry-run` to check the exact same split syntax without creating a document, receipt or writer floor. A ready check is not a reservation. Add `--with-title-heading` when a new H1 root is required; this uses the separate `extract-titled-document` receipt. Prepare `document_title_extraction_v1` for the exact connected endpoint/Space and update every active consumer first. A selected existing H1 already provides a root title.
- If direct split is absent, the existing `extract-document` plan above is the supported atomic operation. Capture exact document/block heads, run `care check`, then `care apply`; preserve its reference and subtree refusals. A missing shorthand alone does not require leaving every extraction unexecuted.
- `block list --document DOC_ID --format json` or `document read --id DOC_ID --with-block-ids --format json` obtains document-scoped IDs. Older CLIs already return them through `document read --id DOC_ID --structure --format json`; no whole-Space export is needed.
- `document append --id DOC_ID --base-revision REV_ID --file answer.md --before BLOCK_ID --reason TEXT --actor-type agent --actor AGENT_ID` inserts a heading-led section in one transaction. Choose an anchor that preserves existing parent context, usually the first older peer section after the title. This uses a distinct `insert-document` receipt and requires authenticated `document_insertion_v1` preparation when connected. Without it, execution records no unsupported receipt or outbox. Never replace it with append-then-N-moves while claiming atomicity.
- `block move --ids BLOCK_ID,BLOCK_ID --before ANCHOR_ID --base-document-revision REV_ID --reason TEXT --actor-type agent --actor AGENT_ID` moves source-ordered disjoint complete subtrees atomically. Connected changing batches require fresh authenticated `document_reorder_v1` preparation for the exact endpoint and Space. Persisting this new receipt grammar excludes older consumers/writers, including supported deferred/failed outcomes; update all active sessions before applying. A read-only check, no-op or unsupported refusal persists no receipt and raises no floor. Missing capability refuses the mutation without a new receipt/outbox. Existing Care bounds require 2–200 roots and at most 200 blocks in the complete document frame. Human and agent batches both require the explicit document base. List each heading root once; its descendants travel with it and must not also appear in `--ids`. Keep root order, choose an external anchor and preserve Markdown parents. Read the Care receipt and document back. Already-in-position succeeds with `no_op: true` and no new history after exact-base checks.
- `document status --id DOC_ID --since-revision REV_ID --format json` compares heads without reading bodies. It is a change signal, not a reservation. `document read --format markdown` emits raw Markdown.

For several corrections with the same block layout, read the current full JSON
Markdown once, assert the intended old strings, and use one existing
`document update --id DOC_ID --base-revision REV_ID --file edited.md --reason TEXT`.
Choose it for one exact-base transaction and one publication, not an unconditional speed guarantee. Compare equal changed content, layout, cache and writer conditions before making a performance claim.
Block count, order, kind/depth and parent relationships must remain unchanged;
a conflict requires a new read and intent. Never turn a boundary refusal into a
copy/delete workaround.

Append/insertion accepts at most 20 **parsed blocks**, beginning with a heading.
Each bullet is a block. The current parser treats continuation paragraphs in a
multi-line list item as additional blocks; write a bullet on one line when it
must be a single block. Do not silently drop continuation text to fit the limit.
Oversized section diagnostics report the parsed count; split into coherent
bounded sections. Use `block split` to change one block into several, preserving
its verbatim semantics and explicit successor lineage.

## Connected Spaces and honest outcomes

Local success does not establish cloud delivery. Only an already authorized
connection may be used. Drain its existing outbox, pull current knowledge and
inspect `sync prepare-care --help`. If supported, `sync prepare-care` on that
exact Space/server authenticates capability discovery; it does not enable sync
or select another Space. It rejects unresolved old writes. An offline first
verification or incompatible server means defer, not a copy/delete workaround.
Preparing this protocol makes older clients incompatible with subsequent care;
do not downgrade or silently substitute clients. A verified connection can
queue bounded changes offline, but a local receipt is not a server acceptance.
The first connected full-document update or supersession additionally requires
CLI v0.2.10+ for any client that later syncs that Space; older protocol-2 clients
receive an upgrade-required response rather than an undecodable delta.

- `applied`: the named local transaction committed; check sync separately.
- `deferred`: no knowledge change; preserve the reason and investigate only
  within the current task's budget.
- `failed`: mutation rolled back; a persisted receipt exists only if recording
  it succeeded. An unavailable/uncertain receipt is not proof of failure.
- `reverted`: a compensating transaction committed; original history remains.

For an intentional deferral, use `care defer --file plan.json --reason-class`
with the installed vocabulary: evidence_missing, source_unavailable,
out_of_scope, capability_unavailable or no_material_change. A deferred/failed
request needs a new request ID after new evidence; bounded retries must not
become an unattended worker or a per-item human approval inbox.

## Conditional recovery, not a database restore

If reversal is authorized, write a new plan with `action: revert`,
`reverts_run_id`, actor, reason and evidence; omit documents/blocks/content/title.
Use `care revert --file revert-plan.json`. Every affected current head must
still match the original after-state. A later writer is preserved; reread and
reconcile or defer rather than force-writing.

The original applied receipt keeps its status and gains a derived
`reverted_by_run_id` on read. Replaying it never reapplies the change. A fresh
request alone is not permission to recreate a reverted layout: deliberate
reconsideration names `reconsiders_run_id` and genuinely new evidence.
Successor identities never inherit predecessor judgments. Redirected/retired
documents and exact old revisions remain historical evidence.

Summarize material outcomes, reason and recovery ID. Counts in
`insights show`/`dashboard serve` describe activity, not proven improvement.
There is no need for a person to edit, approve or undo each routine item in UI.

## Failed capture and long-task drift

When installed help exposes `document drafts` and `document recover`, `document import` stages a private local draft before its write.
If it fails or the response is uncertain, preserve the returned `capture_…` ID.
Inspect `document drafts --draft ID --space SPACE_ID --format json`, then use
`document recover --draft ID --space SPACE_ID --actor-type agent --actor ORIGINAL_AGENT`
with the original intent/actor. Do not issue a new import or `--fork` to bypass an
uncertain outcome. Recovery first resolves an already committed local receipt and
rechecks the same request under writer admission; a replay gives original identity
and revision evidence, not current body content. Read that document by ID. Existing
subject updates still require its exact current base; recovery does not authorize
copying into another Space or changing the original actor. Draft inventory returns
at most200 entries and an explicit `--after` cursor. Remote hosted tools use their
own request receipts; a local draft command is not a policy fallback for them.

At long-task phase changes, check the selected executable/capabilities again.
When these installed doctor flags are advertised, declare the guidance actually loaded using
`obsdog doctor --space SPACE_ID --guidance-version 0.3.36 --minimum-cli v0.2.39
--require-capability document_split_dry_run_v1 --format json`.
Loaded guidance is caller-declared or unknown. MCP/viewer versions come from their
existing connections/listeners, not the installed CLI. `--check-updates` is an
explicit bounded release check and performs no installation/restart. A failed
lookup is unavailable; a cached tag is unverified. An old CLI may not support
these doctor flags; inspect its actual help and retain the capability gap.

Current advertised search/open support separates available exact content from observation
persistence. Inspect `observation.persistence`, `retryable` and `retry_safe`.
`not_recorded` has no fabricated events or run/hit handles: follow `next_read`
through `block show --id BLOCK --revision REV` or the local MCP
`obsdog_block_read` when advertised. Do not declare observed selection/use or
feedback. Reopen an original recorded run after writer release before its use
workflow. `unknown` after an attempted commit is not automatically retryable;
inspect the original trace/request instead. Do not resend use just to repair
missing telemetry. Hosted MCP uses its own actual contract, not these local fields.

Response timings distinguish phase, admission attempts/backoff and total command
elapsed. CLI progress stays on stderr; MCP keeps protocol stdout clean. Actual
WAL lock diagnostics may name a competing PID with an OS basis. Missing ownership
has an explicit reason and transaction age can stay null. Same-PID sample span is
not continuous lock age or proof of self-contention. Preserve drafts; never kill
another writer, edit SQLite, delete events or change sync to force progress.
Capture inventory includes effective title/source_path. A failed import preserves
the original draft and structured recovery state; retry with that same draft and
actor. Ordinary append failure does not promise a draft: inspect its reported
base state, document status/read and original Care receipt before a new intent.

General `space status` is a read-only snapshot. `space write-readiness` on CLI
with installed support is a separate short, rollback-only writer reservation; `ready` describes
that instant, not a later write guarantee. Stdio MCP exposes the same distinction
through `obsdog_space_status` and `obsdog_write_readiness`. Tool metadata carries
operation/elapsed time and reservation failures expose attempt diagnostics.
Healthy WAL read snapshots remain usable under an ordinary writer; read-only
access is not a guarantee against every file, recovery or lock failure. An API
transport/unavailability error and local `space_writer_busy` are distinct; inspect
the actual endpoint/path and error rather than treating one as the other.


A successful read is not a committed open observation. For example, a response
with `ok: true`, returned Markdown, `observation.persistence: not_recorded`,
`reason: writer_admission_refused`, `use_available: false` and `event_ids: []`
means the content was read but the open/use prerequisite was not accepted. If
observation is needed, retry only `search open` with the original run/rank after
writer release. Proceed to use/feedback only after a committed open and the
actual applicable use. Do not repeat an already accepted document/block update.
A missing answer outside the requested rank/page bound requires a wider diagnostic
window before it can be called a missing save or missing search result.

## Correction failure and accepted work

When installed help advertises `document corrections`, block/document corrections
preserve private local intent before a write. Inspect `mutation_state.persistence`,
its evidence and fresh-head status. `committed` with a later read failure means
read the target without repeating the edit. `unknown` means inspect the original
request/history first. `not_committed` permits reconciling and retrying only that
failed target, preserving exact bases and any original receipt key. Do not rerun
already accepted sibling writes. A fresh head is observed, not reserved.

List `document corrections list --space SPACE_ID --format json`; inspect one with
`--draft ID`. Recover only that original draft with `document corrections recover
--draft ID --actor-type agent --actor ORIGINAL_AGENT --space SPACE_ID --format json`.
Recovery keeps original bases and does not silently rebase. When a newer writer
exists, reconcile the current content, author a new intent if needed, then use
`document corrections resolve --draft ID --revision CURRENT_DOCUMENT_REV --reason
TEXT` with the original actor to record an explicit local disposition. This does
not edit content or assert independent verification. Pending notices cover this
local installation; do not claim another device received them. Preserve these
private files separately before moving a profile; database-only Space backups do
not contain correction drafts. Existing capture drafts use their separate commands.
When installed help advertises --include-drafts, an idle-profile backup can include
both private draft trees. Check its coverage and byte counts; it is not an atomic
cross-file snapshot or a credential/profile clone.

Single-shot CLI commands share a default 60s deadline. Where advertised, prefix
`obsdog --timeout 90s ...` explicitly changes it; a failed mutation may use a
separate maximum 500ms read-only head reconciliation. Local MCP/viewer requests
have independent request bounds. A timeout alone does not prove rollback.
Default document inventory excludes settled redirect/retired documents; the audit
`--include-retired` view states lifecycle explicitly. A stale release cache is
not the latest installed version. Ordinary commands can warn on stderr about an
older same-Space default-port viewer. `dashboard restart --space SPACE_ID --port
PORT` authenticates private owned control; older viewers without that control
need one manual foreground stop before serving the new CLI. Do not kill a guessed
PID, change another Space or restart a separately owned MCP host.

On CLI v0.2.39+, write-readiness human reports the same ready/status/writer values
as JSON. Default exit0 means the probe executed; explicit --require-ready returns3
for an inspected non-ready state. OS lock inventory supplies owner/range, not
acquisition time: transaction_age_unavailable_reason explains a null age. Sample
span and process uptime cannot establish continuous transaction age.
For a disposable older listener on an ephemeral port, dashboard status
--space SYNTHETIC_SPACE_ID --port PRINTED_PORT --check-notice exercises the same
warning predicate without taking the live default port. Ordinary automatic probes
remain default-port-only. Follow the public [bounded reproduction guide](https://github.com/obsdoghq/obsdog-releases/blob/main/guides/accepted-work.md)
for a noninteractive sentinel holder; verify the acquired signal, live test child
and actual busy result before interpreting a sample.
