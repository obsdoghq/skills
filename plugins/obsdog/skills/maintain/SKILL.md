---
name: maintain
description: Maintain knowledge inside an ObsDog Space using attributable revisions, revision-bound labels, metadata comments, portable export, and recoverable backups. Use when creating, updating, classifying, commenting on, exporting, or backing up ObsDog knowledge; do not mutate a Space for read-only requests.
---

# Maintain ObsDog

Canonical Markdown stays primary. Structured block operations exist for exact edits and metadata.

## Inspect before mutation

- Confirm the intended Space with `obsdog space status --format json`.
- Read a document as Markdown first. Use `document read --structure`, `block show`, or `history` only when stable block identity or an exact revision matters.
- Use the installed `--help` surface because commands and schema compatibility may evolve.

## Revisions

`block update` creates an immutable block revision, a corresponding document revision, and a new index snapshot. Supply an attributable actor and a concrete reason. Read the exact target back after updating and inspect `obsdog history --type block --id <id>` when continuity matters.

Do not claim split, merge, or move lineage unless the installed CLI explicitly supports and records it. Do not edit the SQLite database directly.

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
