# Bounded execution receipts

This workflow is for a care-capable CLI/server pair, not a promise that every
installed version supports it. Published CLI v0.2.3 does **not** contain these
execution commands. First inspect `obsdog care --help`; if `check`, `apply`,
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
| `split-block` | One leaf, 2–20 explicit `parts`; each stays context-complete. |
| `merge-blocks` | 2–20 contiguous sibling leaves; reconciled `content`. |
| `extract-document` | One document, a complete contiguous subtree/range and new `title`. |
| `merge-documents` | Two documents, source first and destination second; no block list. |

Stay within the runtime's bounds: two affected documents, at most 200 active
blocks per document, 256 KiB plan and 256 KiB each before/after frame. Resolve
relative/reference-style links to exact stable targets first when supported;
do not strip a link to force an extraction. No cross-Space move or hard deletion.

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
