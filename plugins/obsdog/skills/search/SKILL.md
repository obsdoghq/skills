---
name: search
description: Search and read an ObsDog Personal Space through the local CLI or MCP while preserving retrieval, exposure, selection, and direct-use measurement semantics. Use for finding, opening, citing, or tracing knowledge in ObsDog; do not use for generic filesystem search outside a selected Space.
---

# Search ObsDog

Use the selected local Personal Space without requiring login or network access.

## Establish the boundary

- Prefer an available ObsDog MCP tool when it is already scoped to the intended Space.
- Otherwise discover the installed surface with `obsdog version --format json` and `obsdog --help` before composing commands.
- Treat the current directory as the candidate Space only when the request or repository context makes that scope clear. Never crawl other directories looking for private Spaces.
- Read `obsdog space status --path <space> --format json`. Do not initialize, import, or connect a Space unless the user requested that mutation.

## Search and read

1. Run `obsdog search --path <space> --format json --query <need>`. A returned hit is only `retrieved`.
2. Inspect rank, document, block, exact revision, snippet, and explanation before choosing.
3. Run `obsdog search open --path <space> --run <run-id> --rank <n> --format json` only for a result actually placed in human view or agent context. This records exposure and selection for that one hit.
4. Run `obsdog search use --path <space> --run <run-id> --rank <n> --type answer_evidence|citation|quote|copy|link --format json` only when the task output actually uses that exact source.
5. Use `obsdog trace show` when the user asks what was returned, opened, used, or judged.

Do not open every returned result merely to produce telemetry. Do not turn uninspected hits into negative judgments. When rank one answers the need, the other returned hits remain retrieved and unjudged.

## Feedback

Record an agent judgment only when requested or when the task explicitly includes evaluation. Keep relationship types distinct:

- relevance: query to hit;
- usefulness: exact used revision to the task, and only after direct use;
- correctness: exact revision under an evidence-backed rubric;
- freshness: exact revision under a time or review policy.

Use `--evaluator-type agent`, identify the evaluator, and provide a concise reason. Never present model judgment as human feedback.

Keep JSON stdout machine-clean. Do not place raw queries, content, paths, Space IDs, or comments in external logs or diagnostics.
