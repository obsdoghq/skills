---
name: find
description: Find and read knowledge from a selected ObsDog Space while preserving retrieval, exposure, selection, direct-use, and feedback semantics. Use for questions, citations, source discovery, or retrieval traces in ObsDog; do not use for generic filesystem search.
---

# Find with ObsDog

Use the selected Space locally and offline when possible. Prefer an already scoped ObsDog MCP server; otherwise inspect `obsdog --help` and `obsdog space status --path <space> --format json`. Never crawl for other private Spaces.

## Retrieve intentionally

1. Search with `obsdog search --path <space> --format json --query <need>`. Returned hits are retrieved, not read or judged.
2. Add a canonical label filter only when routing requires it. Discover definitions first and use expressions such as `label:memory:horizon=long_term AND NOT label:lifecycle:state=stale`.
3. Choose from rank, document, block, exact revision, snippet, and matched labels.
4. Open only a result actually placed in human view or agent context: `obsdog search open --run <run-id> --rank <n>`. This records selection for that hit, not every returned result.
5. Record `obsdog search use --run <run-id> --rank <n> --type answer_evidence|citation|quote|copy|link` only when that exact revision materially supports the output.
6. Use `obsdog trace show --run <run-id>` when provenance or retrieval behavior needs inspection.

Do not open every hit for telemetry. Unopened results remain unjudged. If the first result solves the task, only that result should become selected or used.

## Feedback

When requested or useful to an explicit evaluation task, keep judgments distinct: relevance links query to hit; usefulness links a used revision to the task; correctness evaluates supported claims; freshness follows a review policy. Identify agent judgments as `--evaluator-type agent`, include a concise reason, and never represent them as human feedback.

Keep JSON stdout machine-clean. Do not send raw queries, content, paths, Space identifiers, comments, or reasons to external diagnostics.
