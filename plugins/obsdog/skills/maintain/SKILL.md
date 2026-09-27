---
name: maintain
description: Evolve and organize knowledge in an ObsDog Space through attributable revisions, review queues, labels, comments, and recoverable maintenance. Use for updates, cleanup, follow-ups, stale knowledge, or structural changes; do not mutate a Space for read-only requests.
---

# Maintain ObsDog

Canonical Markdown stays primary. Structured block operations exist for exact edits and metadata.

Start from evidence: open comments, suggested labels, stale or review-due labels, orphaned annotations, negative evaluations, and revision history are work candidates—not automatic permission to rewrite knowledge. Present meaningful or risky changes for review.

## Inspect before mutation

- Confirm the intended Space with `obsdog space status --format json`.
- Read a document as Markdown first. Use `document read --structure`, `block show`, or `history` only when stable block identity or an exact revision matters.
- Use the installed `--help` surface because commands and schema compatibility may evolve.

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
- A human reviews one exact suggestion with `obsdog label review --assignment <id> --decision accept|reject`. A corrected acceptance may add `--value`; always preserve the reason. Never retry a completed review or activate a suggestion that the CLI reports as stale.
- Use comments for questions, explanations, corrections, and evidence. Use structured feedback—not a comment alone—to evaluate retrieval or task performance.
- Change discussion state with `obsdog comment status --id <id> --status resolved|wont_fix|open --reason <reason>`. Use `open` only to reopen a terminal thread, and inspect `comment history` when resolution provenance matters.
- Preserve actor identity, rationale, confidence, target revision, and prior assignment history.

## Portability and recovery

- `space export` creates an inspectable directory of canonical Markdown, block maps, and a manifest. It is for portability, not a full telemetry restore.
- `space backup` creates a consistent private archive containing the manifest and operational SQLite database.
- `space restore` accepts only a new, uninitialized destination. Never overwrite a live Space.
- Before a bulk or risky maintenance operation, offer a backup when it is proportionate; do not create one during an unrelated read-only task.

After mutations, use JSON read-back to verify the exact Space, target, revision, actor, and state. Keep private content and metadata inside the Space boundary.
