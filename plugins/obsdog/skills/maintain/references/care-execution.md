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

Use IDs returned by the CLI, not titles, ranks or identifiers from this guide.
Evidence describes what you checked; it is not a human verification certificate.
Do not include credentials or copy a private source outside its permitted home.

| Action | Payload and boundary |
| --- | --- |
| `update-block` | One document/block, complete `content`; same authored kind/depth. |
| `update-document` | One document, complete replacement Markdown with unchanged block structure and/or a stored `title`; exact document head. |
| `append-document` | One exact document head, a heading-led Markdown suffix of at most 20 new blocks; preserve every existing block identity/revision. Requires the append capability on a connected Space. |
| `insert-document` | Capability-gated unreleased action: one exact document head, heading-led `content` and exact `before_block_id`; its receipt must prove that anchor and preserve all existing identities/parents. |
| `supersede-document` | Two exact document heads, duplicate source first and active canonical target second; no block copy or target revision change. Require concrete duplicate evidence. |
| `split-block` | One leaf, 2–20 explicit `parts`; each stays context-complete. |
| `merge-blocks` | 2–20 contiguous sibling leaves; reconciled `content`. |
| `extract-document` | One document, a complete contiguous subtree/range and new `title`. |
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

## Match structural guidance to installed capabilities

Read `obsdog document --help` and `obsdog block --help` before choosing syntax.
Check the installed help and exact server capability before using these
commands. Some installed versions predate the structural shorthands or connected
batches. A plugin update does not upgrade the CLI/server.

- `document split --id DOC_ID --base-revision REV_ID --blocks BLOCK_ID,BLOCK_ID --title TITLE --reason TEXT --actor-type agent --actor AGENT_ID` performs one bounded `extract-document` Care transaction. A selected heading includes its descendants. Read both resulting documents and repair known navigation with returned successor IDs. This is not a move into an existing document.
- If direct split is absent, the existing `extract-document` plan above is the supported atomic operation. Capture exact document/block heads, run `care check`, then `care apply`; preserve its reference and subtree refusals. A missing shorthand alone does not require leaving every extraction unexecuted.
- `block list --document DOC_ID --format json` or `document read --id DOC_ID --with-block-ids --format json` obtains document-scoped IDs. Older CLIs already return them through `document read --id DOC_ID --structure --format json`; no whole-Space export is needed.
- `document append --id DOC_ID --base-revision REV_ID --file answer.md --before BLOCK_ID --reason TEXT --actor-type agent --actor AGENT_ID` inserts a heading-led section in one transaction. Choose an anchor that preserves existing parent context, usually the first older peer section after the title. This uses a distinct `insert-document` receipt and requires authenticated `document_insertion_v1` preparation when connected. Without it, execution records no unsupported receipt or outbox. Never replace it with append-then-N-moves while claiming atomicity.
- `block move --ids BLOCK_ID,BLOCK_ID --before ANCHOR_ID --base-document-revision REV_ID --reason TEXT --actor-type agent --actor AGENT_ID` moves source-ordered disjoint complete subtrees atomically. In the v0.2.32 source candidate, connected changing batches require fresh authenticated `document_reorder_v1` preparation for the exact endpoint and Space. First adoption excludes older consumers/writers; update all active sessions before applying. Missing capability refuses the mutation without a new receipt/outbox. Existing Care bounds require 2–200 roots and at most 200 blocks in the complete document frame. Keep root order, choose an external anchor and preserve Markdown parents. Read the Care receipt and document back. Already-in-position succeeds with `no_op: true` and no new history after exact-base checks.
- `document status --id DOC_ID --since-revision REV_ID --format json` compares heads without reading bodies. It is a change signal, not a reservation. `document read --format markdown` emits raw Markdown.

For several corrections with the same block layout, read the current full JSON
Markdown once, assert the intended old strings, and use one existing
`document update --id DOC_ID --base-revision REV_ID --file edited.md --reason TEXT`.
This avoids rebuilding the complete search snapshot for every individual patch.
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
