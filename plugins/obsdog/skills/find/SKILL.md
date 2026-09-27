---
name: find
description: Find and read knowledge from a selected ObsDog Space while preserving retrieval, exposure, selection, direct-use, and feedback semantics. Use for questions, citations, source discovery, or retrieval traces in ObsDog; do not use for generic filesystem search.
---

# Find with ObsDog

Use the selected Space locally and offline when possible. Prefer an already scoped ObsDog MCP server; otherwise inspect `obsdog --help` and `obsdog space status --path <space> --format json`. Never crawl for other private Spaces.

CLI v0.1.11 defaults to the same Personal library across directories without
`init`. Use `--space personal` only when no explicit project/Org boundary applies;
otherwise preserve the exact selected Space. A broken selection is an error,
not permission to search a different library or connect cloud sync.

## Retrieve intentionally

1. On CLI v0.1.8+, search with `obsdog search --path <space> --format json --query <need> --actor-type agent --actor <agent-id>`. Returned hits are retrieved, not read or judged.
2. Add a canonical label filter only when routing requires it. Discover definitions first and use expressions such as `label:memory:horizon=long_term AND NOT label:lifecycle:state=stale`.
3. Choose from rank, document, block, exact revision, snippet, and matched labels.
4. Open only a result actually placed in human view or agent context: `obsdog search open --path <space> --run <run-id> --rank <n> --actor-type agent --actor <agent-id>`. This records selection for that hit, not every returned result.
5. Record `obsdog search use --path <space> --run <run-id> --rank <n> --type answer_evidence|citation|quote|copy|link --actor-type agent --actor <agent-id>` only when that exact revision materially supports the output.
6. Use `obsdog trace show --path <space> --run <run-id>` when provenance or retrieval behavior needs inspection.

Keep the same nonempty, non-sensitive agent ID across the task. CLI transport
remains `cli`; an agent actor does not make it an MCP event. Check installed help
for these flags before recording events. If unavailable, request/perform an
authorized CLI update or use the already-scoped MCP server's agent attribution;
do not fall back to the CLI's default human actor. Do not add CLI-only flags to
MCP arguments. Opening results for an agent is not genuine human feedback.

Do not open every hit for telemetry. Unopened results remain unjudged. If the first result solves the task, only that result should become selected or used.

## Feedback

When requested or useful to an explicit evaluation task, keep judgments distinct: relevance links query to hit; usefulness links a used revision to the task; correctness evaluates supported claims; freshness follows a review policy. Identify agent judgments as `--evaluator-type agent --evaluator <agent-id>`, include a concise reason, and never represent them as human feedback. Evaluator flags do not replace retrieval actor flags; preserve the exact target revision and selected Space.

Keep JSON stdout machine-clean. Do not send raw queries, content, paths, Space identifiers, comments, or reasons to external diagnostics.
