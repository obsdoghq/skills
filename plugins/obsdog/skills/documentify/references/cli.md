# Documentify CLI Reference

## Save and update documents

Follow the [remember CLI reference](../../remember/references/cli.md) for Space selection, existing-note discovery, agent attribution, creation, conditional updates, and read-back verification.

Compare existing notes by subject, purpose, and canonical source location before each import batch. Use `document list` when an inventory is needed and `search` for targeted discovery.

`document import` creates a new document; it is not an upsert. Update existing document identities. Use the [care execution reference](../../maintain/references/care-execution.md) for structural changes.

## Resolve links

Use actual document and block IDs returned by the selected Space. Read both ends before asserting a relationship.

On CLI v0.2.3+, relative Markdown references resolve against exact imported paths within the selected Space. Missing or ambiguous paths remain unresolved. Check installed support before relying on relative paths; older graphs resolve stable IDs only.

For new overviews and detailed notes, save the notes, read back their IDs and current revisions, then add references through conditional updates with agent attribution and reasons. Read back the resulting links.

For a batch, complete the same-work reference pass after all target IDs exist.
Report imported/updated notes separately from relation-reviewed notes, resolved
links, unresolved targets and intentionally standalone notes. A successful
import does not prove that its references resolved; standalone notes need no
invented links or connectivity quota.

Inspect `insights show` and its graph output, or the local dashboard's Graph, when verifying document relationships. `memory show` describes retrieval and co-use observations, not the authored document map. Check installed help for command details.

If installed help exposes `document links`, inspect a changed note's bounded
outbound references directly using the [find reference](../../find/references/cli.md#follow-authority-not-just-a-familiar-answer).
This candidate command avoids computing the whole graph and reports unresolved
targets; it does not certify relationships or record target reads.

An unresolved target remains an explicit limitation. Use a current-revision `question` comment for an uncertain relationship. Shared tags or semantic similarity alone do not establish a citation.

## Verify retrieval

Use representative questions to check whether the explanations can be found. For diagnostic checks, use `search --no-observe` on CLI v0.2.12+; these checks create no run or use handle. Follow the [find CLI reference](../../find/references/cli.md) for query syntax and version-specific behavior.

Verify the actual content and resolved references, not only successful import or update responses. Keep checked source versions and uncertainty explicit; a stored explanation does not automatically track later source changes.
