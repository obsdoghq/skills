# Capture checkpoints and delegation

These are workflow examples, not new tool endpoints, automatic hooks or evidence
that a host has invoked a skill. Use the selected Space and the user's existing
capture authorization. A completed search and a completed capture are different
outcomes. Keep this checkpoint in the existing task handoff, not a second ledger.

## Before delegation

The parent states the question, authorized source/Space scope, whether ongoing
capture is allowed, and the exact existing target when already known. The worker
checks capability for that operation without widening access. Assign one capture
owner; other workers return findings instead of racing to write the same note.

> Investigate the scoped question. Capture source-checked new knowledge during
> the work when authorized, even after a successful search. Before handing back,
> return the capture disposition, actual target/revision receipt, read-back and
> retrieval verification, or the missing prerequisite. Preserve the original
> lookup cue for a miss. Do not invent a successful write or a replacement target.

## Worker handoff

Use this compact information in the existing handoff; values come from actual
operations, not from this example. Do not export private receipt details to a
public issue, repository or log.

- **Disposition:** saved-and-verified, saved-readback-pending, draft-only,
  blocked, no-new-knowledge, or prohibited. A proposal is never saved-and-verified.
- **Evidence:** established finding and source applicability; exact selected
  Space/document/block/revision from the real receipt when a write occurred.
- **Checks:** what was actually read back and retrieved, with unknown/not-run
  checks explicit. Existing `open`/`use` observations are not authoring receipts.
- **Resume:** exact missing permission, capability, base revision or source fact;
  no unconditional retry or fabricated deadline.

The parent checks the actual receipt and saved content before declaring capture
complete. A worker's prose statement, future intention or tool listing is not
verification. Do not repeat a write merely because the parent needs to read it.

## Six handoff cases

### Successful hit with new learning

Reuse the checked evidence, then capture genuinely new source-backed findings
through the ordinary authorized path. Read back the exact target and check its
retrievability. Search success does not suppress capture; no new finding means
no-new-knowledge, not an invented update for a metric.

### Repaired search miss

Preserve the original lookup cue/run when available. Investigate authorized
sources, save or repair the matching canonical note, then test that original
cue without recording a diagnostic retry as independent successful use. Use the
supported no-observe diagnostic path when available; otherwise mark this check
not run rather than manufacture observations. A different convenient query is
not proof that the original miss was repaired.

### Pause or input required

Before yielding, capture already-established reusable knowledge within existing
authorization; distinguish it from unresolved decisions. Return a partial or
blocked disposition and the exact missing input. Do not turn a source-checked
partial result into a claim that the whole task succeeded.

### Delegated result

The worker returns the checkpoint above, not just "parent will save". The parent
owns acceptance of the real receipt/read-back/retrieval evidence. A private draft
may be handed back when the worker lacks the authorized write capability; it is
not an assertion that knowledge is already stored or discoverable.

### No-memory or read-only request

Do not save or persist a capture draft. Honor the restriction even if useful
knowledge was found. Return prohibited for capture, continue the permitted task,
and do not run diagnostic searches merely to raise activity counts.

### Unavailable atomic preparation

First distinguish an ordinary supported update from an operation that actually
requires exact atomic prepare/commit. Ordinary authorized capture must not wait
for an unrelated atomic endpoint. For a genuinely unsupported atomic operation,
keep only a minimal private draft when storage is authorized: intended change,
exact target/base revision from inspected evidence, and the missing capability.
Revalidate that base before a later supported write. Do not substitute re-import,
packing many changes into one block, guessed identifiers, login, migration or
broader upload. Never describe that draft as a committed receipt.

## Boundaries

Use the existing [remember workflow](../SKILL.md) and [CLI reference](cli.md).
Do not add automatic network collection, host instruction edits, hooks, new
schemas or permissions as part of capture. Static contract tests can detect a
missing example or link, but actual host invocation and successful knowledge
retrieval require separate observed evidence.
