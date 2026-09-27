---
name: report
description: Generate and explain a private read-only HTML knowledge-health report for a selected ObsDog Space. Use for current state, supported trends, retrieval health, AI activity or sync status; do not treat aggregate counts as causal proof.
---

# Report with ObsDog

Confirm the selected Space, inspect `obsdog report --help`, and choose a new output path. Generate with:

`obsdog report create --path <space> --output <new-file>.html --format json`

The command must not overwrite an existing artifact. Treat the output as private even though it excludes exact queries, document bodies, comments, evaluation reasons, and annotation text.

## Interpret responsibly

- Prioritize visibility: current state, real trends, outcome quality, AI activity
  and data freshness. No edit/approve/apply/reject/undo UI or mandatory user work
  queue. The user requests changes through their authorized AI workflow; include
  scoped evidence/reference details only where the report actually provides them.
- Keep snapshot totals distinct from time-series evidence. The current all-time
  report does not supply historical trends. Never derive growth/activity history
  from current update timestamps, interpolate absent samples or invent a quality
  score. Show period/timezone/coverage and compare only compatible windows when
  that data genuinely exists.
- Report metric numerators and denominators; “not enough data” is different from zero.
- Separate retrieval from selection, direct use, and explicit evaluation.
- Explain that high usage can reflect popularity or dependency, not correctness; low usage can reflect poor discovery or narrow scope, not low value.
- Treat maintenance counts as candidates for AI investigation, not chores for the user. A report-only request stays read-only; do not resolve comments, accept suggestions or rewrite content from aggregate data alone. In a separately authorized maintenance task, the AI should inspect and fix supported routine issues itself.
- Call out sample-size and collection gaps before recommending action.
- Keep unresolved links, proposals and quality-review notes distinct from task
  outcomes. Current graph strength counts citations, not correctness/usefulness;
  a `knowledge-care/v1` comment is not yet a structured aggregate metric. Do not
  imply that an adaptive ranker or automatic cleanup runs behind the report.
- Where actual receipts exist, distinguish AI-completed improvements, technical/
  evidence deferrals and genuine authority/intent decisions. Show reasons and
  recovery limitations, not an approval card for every suggestion. Do not invent
  these counts from today's open-comment totals or call AI review human review.
- Link or return the generated local HTML path. Summarize only the decisions the user needs; preserve the report as the detailed artifact.
