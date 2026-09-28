---
name: report
description: Inspect and explain the current state, activity, graph and source evidence of a selected ObsDog Space using local read-only insights and the offline dashboard. Export HTML only when explicitly requested; do not treat counts as causal proof.
---

# Report with ObsDog

Use CLI v0.2.2+, confirm the selected Space and inspect `obsdog insights --help`.
The default is an evidence-backed status explanation, not an HTML file:

`obsdog insights show --space <space-id> --days 30 --actor all --format json`

For a requested browser dashboard, run `obsdog dashboard serve --space <space-id>`
and use its announced loopback URL (default 127.0.0.1:47777). `wiki serve` opens
the reading entrypoint of that same UI. No login, LAN scan, cloud upload, hosted
bridge or background service is required or authorized by viewing status.

Omit `--space` only for authorized Personal use. An explicit project/Org ID must
be passed through; cwd does not select a Space, and there is no `init` step.

Treat insights and the dashboard as private: they can include document titles,
links, source-check evidence and actor identities. They are not anonymous metrics.
Do not proxy the loopback service to a network or submit its JSON elsewhere.

## Interpret responsibly

- Prioritize visibility: current state, real trends, outcome quality, AI activity
  and data freshness. No edit/approve/apply/reject/undo UI or mandatory user work
  queue. The user requests changes through their authorized AI workflow; include
  scoped evidence/reference details only where the report actually provides them.
- Keep snapshot totals distinct from time-series evidence. Insights supplies
  actual 7/30/90-day UTC events, not historical inventory snapshots. Never derive growth/activity history
  from current update timestamps, interpolate absent samples or invent a quality
  score. Show period/timezone/coverage and compare only compatible windows when
  that data genuinely exists.
- Report metric numerators and denominators; “not enough data” is different from zero.
- On CLI v0.2.3+, `first_page_used / page_eligible` measures explicit same-actor
  use from page 1 among completed runs with recorded page metadata. Legacy runs
  remain excluded, not guessed from Top 10. Page size varies by run. This is not
  first-query task success. Top 1/3/10 among used runs has a different denominator;
  show observation coverage alongside it. Period deltas require both samples.
- Separate retrieval from selection, direct use, and explicit evaluation.
- Explain that high usage can reflect popularity or dependency, not correctness; low usage can reflect poor discovery or narrow scope, not low value.
- Treat maintenance counts as candidates for AI investigation, not chores for the user. A report-only request stays read-only; do not resolve comments, accept suggestions or rewrite content from aggregate data alone. In a separately authorized maintenance task, the AI should inspect and fix supported routine issues itself.
- Call out sample-size and collection gaps before recommending action.
- Separate source-check coverage, content freshness and task usefulness when
  actually available. A pointer is not an imported manual; an old decision can
  still be relevant. Unknown legacy provenance, failed source checks and unjudged
  notes are not passing quality. CLI v0.1.14+ supplies current source declarations
  and 30-day revision-bound authoring aggregates by evaluator/method. Preserve the
  exact window and denominators; older reports do not have these fields. Never
  infer checks from note dates or comment text.
- Keep unresolved links, proposals and quality-review notes distinct from task
  outcomes. Current graph strength counts citations, not correctness/usefulness;
  a prose `knowledge-care/v1` comment is not a typed care record. Do not
  imply that an adaptive ranker or automatic cleanup runs behind the report.
- Where actual receipts exist, distinguish AI-completed improvements, technical/
  evidence deferrals and genuine authority/intent decisions. Show reasons and
  recovery limitations, not an approval card for every suggestion. Do not invent
  these counts from today's open-comment totals or call AI review human review.
- Explain actor scope: activity/evaluation filters are selected; current inventory,
  graph and source coverage are not filtered to that actor. Disclose truncation,
  unavailable reads and stale refreshes instead of treating them as zeros.
- Summarize what the user can observe and any genuine decision needed. Return the
  local dashboard URL only when started or verified; do not pretend it is the
  hosted app's synced view. A report-only request does not authorize maintenance.

## Optional portable snapshot

Only for an explicitly requested HTML export, inspect `obsdog report --help`,
choose a new private path and run `obsdog report create --space <space-id>
--output <new-file>.html --format json`. Never overwrite an artifact. The older
HTML projection is not the live dashboard and does not have the same event-window
charts; do not claim feature parity. Return the actual file and its limits.
