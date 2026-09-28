---
name: maintain
description: Review, improve and verify knowledge in a selected ObsDog Space through attributable revisions, labels, comments and recoverable maintenance. Use for updates, cleanup, follow-ups, stale knowledge or structural changes; do not mutate a Space for read-only requests.
---

# Maintain ObsDog

Canonical Markdown stays primary. Structured block operations exist for exact edits and metadata.

Before choosing the source of truth, selective history, graph grouping,
split/merge, document or link quality, or retirement, read
[knowledge-care criteria](references/knowledge-care.md). Follow its bounded
find/use/evaluate/maintain/verify loop. A quality review is not a task-use event,
and structural sync compatibility is a separate gate from local command support.

Inspect a note's role before editing: native answer, pointer, derived synthesis
or retained snapshot. Recheck the authoritative claim/version, not just whether
its URL loads. Repair the original only when that write is in scope; preserve a
cached/old observation as such. Do not erase significant historical reasons,
create a new Space per topic, or prune revision history to simplify discovery.

Start from evidence: open comments, suggested labels, stale or review-due labels,
orphaned annotations, negative evaluations and history are investigation candidates,
not proof of a problem. Within the task's existing write authority, do the review,
supported correction and readback yourself; do not ask the user to approve each
routine change or edit the Markdown. Keep a concise outcome/reason/recovery record.

If evidence is weak, investigate within budget or defer with the original intact.
If an operation is unsupported, retain its capability gap instead of handing the
user a manual repair task. Ask only for missing authority or an owner-intent choice
that materially changes the result. Respect read-only/propose policies and user
suppression; this workflow cannot grant itself access, schedule a worker or enroll
a new model provider. Confidence alone is not permission or factual verification.

## Inspect before mutation

For retrieval complaints, consult
[the discovery rubric](references/retrieval-authoring.md). Separate missing
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

`block update` creates an immutable block revision, a corresponding document revision, and a new index snapshot. On CLI v0.1.11+, supply `--actor-type agent --actor <agent-id>`, the read-back `--base-revision`, and a concrete reason. Never fall back to human authorship if flags are unsupported. Read the exact target back after updating and inspect `obsdog history --type block --id <id>` when continuity matters.

No `init` is required for Personal maintenance. Use the confirmed default only
when no explicit project/Org boundary applies; do not repair a broken selection
by switching libraries or enabling synchronization.

Use structure operations only when the installed CLI help exposes them:

- `block split --id <id> --part <text> --part <text> --reason <reason>` replaces one active leaf with 2–20 explicit successors. It retires the predecessor; it does not delete history.
- `block merge --ids <id>,<id> --content <text> --reason <reason>` accepts only contiguous active sibling leaves of the same type and depth. Supply reconciled content explicitly rather than hiding a concatenation decision.
- `block move --id <id> --before <anchor>` or `--after <anchor>` preserves block and content-revision identity while moving the complete heading subtree. It does not reparent.
- `block lineage --id <id>` reads direct exact-revision split/merge edges and moves for an active or retired identity.

Do not copy labels, comments, evaluations, or verification state from retired predecessors to successors unless a separate attributable policy explicitly requires it. Verify successor IDs and current Markdown after split/merge, verify the complete subtree after move, and use `block lineage` for provenance. Do not edit the SQLite database directly.

## Labels and comments

- Discover definitions with `obsdog label definitions`; do not hard-code a Space registry beyond definitions the CLI returns.
- Apply labels to the whole authored idea at block level. Comments are separate metadata and never rewrite the document.
- Agents should use `--state suggested` unless policy clearly permits active low-risk routing labels.
- `epistemic:verified` is protected: an agent must suggest it for review unless a disclosed verifier policy authorizes application.
- If a human chooses to review, the current human-only route is `obsdog label review --assignment <id> --decision accept|reject`. Do not invoke it as a fake human or make it a prerequisite for every supported text correction. Leave protected suggestions deferred when no real agent-verifier capability exists. Never retry a completed review or activate a stale suggestion.
- Use comments for questions, explanations, corrections, and evidence. Use structured feedback—not a comment alone—to evaluate retrieval or task performance.
- Change discussion state with `obsdog comment status --id <id> --status resolved|wont_fix|open --reason <reason>`. Use `open` only to reopen a terminal thread, and inspect `comment history` when resolution provenance matters.
- Preserve actor identity, rationale, confidence, target revision, and prior assignment history.

## Reference maintenance

On CLI v0.1.16+, use `memory show` to investigate observed query/co-use paths,
fading and evidence. These derived links need no manual materialization or
cleanup. They are separate from the authored reference maintenance below;
never turn a co-use observation into a factual support edge automatically.

When the task involves disconnected knowledge, inspect actual body links and
current block comments, not only graph density. Relative Markdown paths resolve
only against exact imported paths inside the selected Space; a missing import
or ambiguous title/path must not be repaired by guessing.

Read both ends before adding a relationship. Preserve canonical prose unless a
revision is warranted. A current `explanation`/`evidence` comment can record a
concrete citation; an uncertain relationship belongs in a `question` comment
with a stable target ID and a specific reason. Inspect existing comments and
links first, keep changes bounded, and retain agent attribution. Never impose a
minimum link count or claim semantic similarity is verified evidence.

Only open comments bound to the current block revision contribute hosted graph
links. After editing a block, re-evaluate relevant old comments rather than
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
