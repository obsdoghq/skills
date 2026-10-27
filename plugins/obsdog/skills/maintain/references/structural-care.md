# Explicit structural Care

Use CLI v0.2.35+ only after installed help and authenticated exact-Space
`document_structural_v1` capability confirm this surface. Local-only Spaces need
no server. A connected Space requires compatible active consumers and normal
explicit preparation; a plugin update does not update the CLI/server or reload
instructions in an existing session. At phase boundaries check the running
executable, the existing MCP/viewer connection and actually loaded guidance.
Doctor compares a caller-declared loaded version with its bundled guidance
baseline. `older_than_cli_baseline` means read newer instructions when the session
can load them; it is not a measurement of the installed plugin or proof that a
cache refreshed. Unknown loaded/runtime versions remain unknown.

First read current Markdown and exact document/block IDs. These commands use
one source document and an explicit `--base-revision`, `--reason`, `--actor-type
agent`, `--actor AGENT_ID`, and `--space SPACE_ID`. Add `--dry-run` first. It uses
a coherent read snapshot without documents, receipts, events, outbox or floors;
a ready check does not reserve the next revision.

| `care structure --action` | Additional options and meaning |
| --- | --- |
| `retire-blocks` | `--ids ROOT_ID,ROOT_ID`: remove complete selected subtrees from current view. Keep exact history; no tombstone prose. An empty document becomes retired. |
| `insert-heading` | `--heading '# Title' --before BLOCK_ID`: insert one heading and recalculate parents. Works before an existing leading paragraph or inside a section. |
| `reparent-blocks` | `--ids ROOT_ID --after ANCHOR_ID` or `--before ANCHOR_ID`: move complete roots inside one document, deliberately recalculating parents. Heading level and content remain unchanged. |
| `transfer-blocks` | Source roots plus `--target-document DOC_ID --target-base-revision REV_ID` and an external target anchor: atomically retire source predecessors and create exact successor lineage in the existing destination. Disjoint roots can collect alternating topic paragraphs. |

List each root once, in source order. Its descendants follow; do not also list
them. An anchor must be outside the moved roots. `--after` means after that
anchor's complete subtree. Both documents must be in the same selected Space.
Transfer preserves raw bodies/type/depth and recalculates both resulting trees;
parent changes never authorize merging Markdown blocks or rewriting content.
For a new destination, first create the deliberately empty heading-only note,
then transfer into its exact head. This is actual lineage-preserving movement,
not a copy/delete workaround. A failed transfer can leave that empty destination;
read its receipt before planning another intent.

An identical high-level intent resolves its original request before reading
possibly retired current roots. Keep the same explicit bases/options for a lost
response retry. A later intent needs fresh reads/bases. Read both resulting
Markdown documents, predecessor/successor lineage and current references. Do not
transfer old usefulness judgments to successors. `care revert` remains a bounded
compensation requiring unchanged after heads; it appends history and keeps the
new reader/writer floor.

Relative/reference-style links whose scope cannot stay stable defer with known
`offending_block_ids`. Code spans and fenced/indented code are excluded from link
scans. Inspect the named blocks and their definitions; resolve to established
stable targets when authorized. Never remove links or rewrite code notation to
force a split. Unknown culprits remain unknown; do not binary-probe by creating
real documents. Existing `document split --dry-run` checks contiguous extraction.

For a manual plan, inspect `care schema --format json`, use exact `id` and
`revision_id` target keys, and follow the complete example in
[Care execution](care-execution.md). `move_anchor` is also `{id, revision_id}`;
`move_direction` is `before`/`after`. Optional fields must be omitted when unused,
not null. Decode errors identify JSON field locations without printing bodies.
The schema describes field shape; `care check` additionally validates action
applicability, exact heads, layout and evidence. A persisted defer using new
diagnostic fields also adopts the structural history grammar. Unsupported
endpoints do not receive an unsupported receipt/outbox; update consumers before
adopting the new format.


On CLI v0.2.36+, retire a whole temporary document without a sink using
`document retire --id DOC --base-revision REV --reason TEXT --actor-type agent
--actor AGENT_ID --space SPACE_ID --dry-run --format json`. Remove dry-run only
within the authorized cleanup scope. It uses the existing complete-root Care
contract and exact retry, preserves history and hides the document from current
inventory/search. `document list --include-retired` supports audit/recovery.
Retirement does not physically erase live retained history. For physical storage
maintenance read [storage maintenance](storage-maintenance.md); do not change a
retention policy or compact a user's DB merely because a diagnostic mentions size.
