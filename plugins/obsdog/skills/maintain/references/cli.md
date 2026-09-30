# Maintain CLI Reference

Use the relevant sections for maintenance commands and verification. Check installed help for version-dependent behavior.

## Inspect before mutation

For upgrade diagnosis, identify the running process before interpreting results.
On CLI v0.2.19+, use `obsdog dashboard status --port <port> --format json`;
compatible older viewers expose the loopback `/_obsdog/health` receipt.
`version` identifies the listener; `restart_required` means its executable was
replaced, not that a newer public release exists. Check `obsdog_version` in the
existing MCP connection separately. Restart the owned viewer with its previous
Space/port flags and reconnect host-owned MCP sessions after upgrading; a new
shell or browser refresh does not replace them. Never kill an unknown port owner.
See the [update checklist](https://github.com/obsdoghq/skills/blob/main/docs/SETUP.md#updating-cli-and-agent-guidance).

For retrieval complaints, consult
[the discovery rubric](retrieval-authoring.md). Separate missing
knowledge/context from candidate/ranking failure, and test the intended repair
without counting maintenance replay as useful task feedback.

- Use CLI v0.2.0+ and confirm `obsdog space status --space <space-id> --format json`.
  Pass that same selector on each command below; only use Personal by default
  when no explicit project/Org boundary applies. `init` and path selectors are removed.
- Read a document as Markdown first. Use `document read --structure`, `block show`, or `history` only when stable block identity or an exact revision matters.
- Use the installed `--help` surface because commands and schema compatibility may evolve.
- On CLI v0.1.14+, inspect `care show --format json` and follow the shared typed
  source/review workflow. Keep request IDs, current revisions and causal stream
  heads; do not reuse an old check after changing text.

## Revisions

When the installed CLI exposes bounded care execution, read
[execution receipts](care-execution.md) for conditional plans,
connected capability checks, actual outcomes and recovery. Prefer that
inspect/check/apply/readback loop for supported structural care. It requires
CLI v0.2.4+; connected care also needs server v0.1.29+ and compatible active
writers. Do not assume plugin installation upgrades either component.

`block update` creates an immutable block revision, a corresponding document revision, and a new index snapshot. On CLI v0.1.11+, supply `--actor-type agent --actor <agent-id>`, the read-back `--base-revision`, and a concrete reason. Never fall back to human authorship if flags are unsupported. Read the exact target back after updating and inspect `obsdog history --type block --id <id>` when continuity matters.

On CLI v0.2.10+, use `document update --id <id> --base-revision <document-revision> --file <edited-markdown> --reason <reason>` for a full Markdown correction that preserves block count, order, kind, depth and parent context. Use `document rename` with the same exact-base pattern for a title-only correction; the stored title need not equal H1. Both use one attributed Care receipt, not a create-only import. A structural change needs a reviewed structural plan. For a proven duplicate, `document supersede --id <duplicate> --base-revision <source-revision> --by <canonical> --by-revision <target-revision> --reason <reason> --evidence-ref <source> --evidence-revision <version> --evidence-finding <finding>` retires only the duplicate; it copies no blocks and leaves the canonical revision untouched. Read both documents and provide actual duplicate evidence first. Confirm protocol-2 preparation for a connected Space, inspect the receipt and read back both IDs. A deferred/conflicted action is not success; re-read and reconcile rather than retrying with a stale head.

No `init` is required for Personal maintenance. Use the confirmed default only
when no explicit project/Org boundary applies; do not repair a broken selection
by switching libraries or enabling synchronization.

On CLI v0.2.14+, `document append --id <id> --base-revision <document-revision>
--file <markdown> --reason <reason>` adds headings and other Markdown blocks at
the end while preserving existing identities. Pass the same Space/actor flags.
`document update` cannot add or remove blocks, and leaf split is not mixed-kind
insertion. Inspect append's conditional Care receipt and read back the document;
connected append needs compatible writers and server v0.1.34+.

Use structure operations only when the installed CLI help exposes them:

- `block split --id <id> --part <text> --part <text> --reason <reason>` replaces one active leaf with 2–20 explicit successors. It retires the predecessor; it does not delete history.
- `block merge --ids <id>,<id> --content <text> --reason <reason>` accepts only contiguous active sibling leaves of the same type and depth. Supply reconciled content explicitly rather than hiding a concatenation decision.
- `block move --id <id> --before <anchor>` or `--after <anchor>` preserves block and content-revision identity while moving the complete heading subtree. It does not reparent.
- `block lineage --id <id>` reads direct exact-revision split/merge edges and moves for an active or retired identity.

Do not copy labels, comments, evaluations, or verification state from retired predecessors to successors unless a separate attributable policy explicitly requires it. Verify successor IDs and current Markdown after split/merge, verify the complete subtree after move, and use `block lineage` for provenance. Do not edit the SQLite database directly.
On CLI v0.2.12+, direct split/merge reject successors whose Markdown kind or
whole-document layout would disagree with stored structure. They do not add a
new heading or another block kind. `obsdog doctor` can report older layout
mismatches, but does not repair them. Do not force a mixed-kind split or rewrite
SQLite to bypass the guard; preserve the exact revision and seek a reviewed
structural repair path when needed.

## Labels and comments

Choose hiding or retirement deliberately:

| Operation | Default search | `--include-deprecated` | Exact-ID evidence |
| --- | --- | --- | --- |
| Active `lifecycle:state=deprecated` label | Hides active candidates | Can return those active candidates | Original document and history |
| `document supersede` | Retires duplicate blocks from the index | Cannot return retired blocks | Redirect, old revisions and Care recovery receipt |

Neither erases history. Frozen traces retain their original evidence. A document
label participates in search candidate filtering on CLI v0.2.8+ without creating
separate block assignments. `label list` can distinguish its recorded revision
from the current revision; editing does not silently revoke lifecycle hiding.

- Discover definitions with `obsdog label definitions`; do not hard-code a Space registry beyond definitions the CLI returns.
- Apply labels to the whole authored idea at block level. Comments are separate metadata and never rewrite the document.
- Agents should use `--state suggested` unless policy clearly permits active low-risk routing labels.
- `epistemic:state=verified` is protected: an agent must suggest it for review unless a disclosed verifier policy authorizes application.
- If a human chooses to review, the current human-only route is `obsdog label review --assignment <id> --decision accept|reject`. Do not invoke it as a fake human or make it a prerequisite for every supported text correction. Leave protected suggestions deferred when no real agent-verifier capability exists. Never retry a completed review or activate a stale suggestion.
- Use comments for questions, explanations, corrections, and evidence. Use structured feedback—not a comment alone—to evaluate retrieval or task performance.
- Change discussion state with `obsdog comment status --id <id> --status resolved|wont_fix|open --reason <reason>`. Use `open` only to reopen a terminal thread, and inspect `comment history` when resolution provenance matters.
- Preserve actor identity, rationale, confidence, target revision, and prior assignment history.

## Reference maintenance

On CLI v0.2.3+, start with `memory show --summary` for compact counts/coverage.
Use `memory show` (v0.1.16+) to investigate observed query/co-use paths,
fading and evidence. These derived links need no manual materialization or
cleanup. They are separate from the authored reference maintenance below;
never turn a co-use observation into a factual support edge automatically.

When the task involves disconnected knowledge, inspect actual body links and
current block comments, not only graph density. The document map is
`insights show` → `graph`, not `memory show`. On CLI v0.2.3+, relative Markdown paths resolve
only against exact imported paths inside the selected Space; a missing import
or ambiguous title/path must not be repaired by guessing.

Read both ends before adding a relationship. Preserve canonical prose unless a
revision is warranted. A current `explanation`/`evidence` comment can record a
concrete citation; an uncertain relationship belongs in a `question` comment
with a stable target ID and a specific reason. Inspect existing comments and
links first, keep changes bounded, and retain agent attribution. Never impose a
minimum link count or claim semantic similarity is verified evidence.

Only open comments bound to the current revision contribute graph links. The
hosted graph accepts block comments; CLI v0.2.3+ also exposes document-scoped
current comments locally. Local `graph.proposals` is separate from `graph.edges`
and does not increase citation strength. After editing a block, re-evaluate relevant old comments rather than
silently copying their judgments. Close rejected proposals with `wont_fix` and
a reason. Closing a question does not automatically turn it into a reference;
an accepted citation needs its own attributable body revision or evidence/
explanation comment. Use the installed CLI help and read back the result.

## Portability and recovery

- `space export` creates an inspectable directory of canonical Markdown, block maps, and a manifest. It is for portability, not a full telemetry restore.
- `space backup` creates a consistent private archive containing the manifest and operational SQLite database.
- `space restore --backup <file>` validates and restores the unchanged archive ID
  into the profile catalog, refusing an existing destination. It changes no default
  and transmits nothing. Use an isolated `OBSDOG_HOME` for recovery inspection;
  never overwrite a live Space or treat a backup as cloud enrollment.
- Prepare a private backup when it is proportionate to an already authorized change; backup is a prerequisite, not a reason to request approval for every edit. Do not create one during an unrelated read-only task or treat a backup as authorization for an otherwise unsupported operation.

After mutations, use JSON read-back to verify the exact Space, target, revision,
actor and state. Preserve concurrent edits: re-read/replan on conflict; never
force-write or restore an old whole-Space backup over newer work. Correct a failed
change only through a supported conditional operation. Stop bounded retries and
defer unresolved issues; don't reapply an explicitly reverted change without new
evidence. Keep private content and metadata inside the Space boundary.
