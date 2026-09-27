---
name: report
description: Generate and explain a private standalone HTML knowledge-health report for a selected ObsDog Space. Use for current-state summaries, retrieval health, usage, maintenance queues, or sync status; do not treat aggregate counts as causal proof.
---

# Report with ObsDog

Confirm the selected Space, inspect `obsdog report --help`, and choose a new output path. Generate with:

`obsdog report create --path <space> --output <new-file>.html --format json`

The command must not overwrite an existing artifact. Treat the output as private even though it excludes exact queries, document bodies, comments, evaluation reasons, and annotation text.

## Interpret responsibly

- Report metric numerators and denominators; “not enough data” is different from zero.
- Separate retrieval from selection, direct use, and explicit evaluation.
- Explain that high usage can reflect popularity or dependency, not correctness; low usage can reflect poor discovery or narrow scope, not low value.
- Treat maintenance counts as queues for review. Do not auto-resolve comments, accept suggestions, or rewrite content from aggregate data alone.
- Call out sample-size and collection gaps before recommending action.
- Keep unresolved links, proposals and quality-review notes distinct from task
  outcomes. Current graph strength counts citations, not correctness/usefulness;
  a `knowledge-care/v1` comment is not yet a structured aggregate metric. Do not
  imply that an adaptive ranker or automatic cleanup runs behind the report.
- Link or return the generated local HTML path. Summarize only the decisions the user needs; preserve the report as the detailed artifact.
