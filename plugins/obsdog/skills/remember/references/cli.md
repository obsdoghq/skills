# Remember CLI Reference

Check installed command help for version-dependent flags and behavior. Keep the same selected Space and agent identity throughout a save.

## Select the Space

Use the explicitly selected Space. Otherwise use Personal. Check `obsdog space status --space <space-id> --format json` for its current scope and sync mode. Follow any source, storage, or upload restrictions. A broken selection does not authorize switching Spaces or enabling sync.

## Find an existing note

Search for the subject or source and read likely candidates:

```sh
obsdog search --space <space-id> --query "<subject or source name>" --actor-type agent --actor <agent-id> --format json
obsdog document read --space <space-id> --id <candidate-document-id> --format json
```

Use `search open` and `search use` as described in the [find CLI reference](../../find/references/cli.md) for search results actually read and used. Use `document list` for an inventory when needed.

## Create or update

`document import` creates a new document; it is not an upsert by title, file path, or heading. Use it only for a new note:

```sh
obsdog document import --space <space-id> --file <markdown-file> --actor-type agent --actor <agent-id> --format json
```

If duplicate protection returns an existing ID, inspect and update that note. Do not bypass the result with `--fork` unless a distinct document is intended.

For a small correction that fits an existing Markdown block, use `block update`
with its exact current base revision, a concrete reason, and agent attribution.
Preserve that block's kind/depth; this ordinary revision path does not prepare
atomic Care. Check installed help for the supported flags.

On CLI v0.2.10+, a full Markdown update can preserve document identity when
block structure is unchanged. Unlike ordinary `block update`, this is atomic
Care even without a layout change: connected Spaces require verified
protocol-2 preparation and compatible active writers before local commit.
`document rename` has the same requirement.

```sh
obsdog document update --id <document-id> --base-revision <document-revision-id> --file <edited-markdown> --reason "<reason>" --actor-type agent --actor <agent-id> --space <space-id> --format json
```

This operation preserves block count, order, kind, depth, and parent context.
Use `document rename` with the current base revision for a stored-title
correction. The stored title and H1 are distinct.

On CLI v0.2.14+, use `document append --id <document-id> --base-revision
<document-revision-id> --file <new-markdown> --reason "<reason>"` with the same
Space/actor flags for new sections at the end. Existing blocks stay intact;
connected append requires verified protocol-2 preparation, compatible active
writers and the exact server's `document_append_v1` capability (v0.1.34+).
Version numbers or standing capture permission alone do not prepare a Space.
Local-only Spaces need no server preparation. Once a supported connection is
deliberately prepared and capture is authorized, no per-edit approval is needed.
If new blocks cannot be added, preserve a scoped private draft with the exact
target/base revision and continue the task. Do not silently prepare the library,
re-import the same note or force a multi-block section into one block update.
Read the [care execution reference](../../maintain/references/care-execution.md)
for that compatibility transition, not as a step before every ordinary capture.

For source records after ordinary protocol-1 edits, a compatible receiver must
retain the edit's document revision. A failed sync is queued delivery, not an
excuse to discard care or re-import the document.

For structural changes, read the [care execution reference](../../maintain/references/care-execution.md) and use a supported conditional plan. Routine updates remain part of `remember`; use `maintain` for broader organization, reconciliation, merging, or splitting. Do not re-import to bypass a structural limitation.

On a revision conflict, read the current content and reconcile the change before retrying. Preserve concurrent edits.

## Links and metadata

Use returned stable document or block IDs in Markdown links, such as `[Related decision](<document-id>)`. Read both ends and explain the actual relationship.

Use comments for questions, explanations, or evidence that should not change canonical prose. Inspect existing comments before adding one. For an uncertain connection, use a `question` comment on the exact current revision and state the uncertainty.

Discover label definitions before assigning labels. Use suggested state unless the Space policy permits the intended active assignment. Preserve agent attribution and protected verification rules.

## Read back and check retrieval

Read the created or updated document and verify its Space, identity, title, body, and links. Inspect history when revision continuity matters.

For a diagnostic search after a write, CLI v0.2.12+ supports `search --no-observe`. It creates no run or use handle. Reproduce the original query once when repairing a retrieval miss; if its quotes or filters prevent a match, also check a corrected query that expresses the same intent. Treat diagnostic results as verification, not task-use feedback.

Confirm that the result actually contains the intended answer and current
document/block revision. A count above zero can still be the wrong answer.
Return this verification with the saved document in delegated-work handoffs.

Keep JSON stdout machine-clean and keep secrets out of notes, queries, comments, and diagnostics.
