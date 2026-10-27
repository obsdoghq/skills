# Find CLI Reference

Consult the relevant sections for command syntax and retrieval mechanics. Check installed help when version-dependent behavior matters.

## Select the boundary

Use the selected Space locally and offline when possible. An already scoped
local stdio MCP server can handle supported discovery/read calls, but it does not
provide the complete use, feedback and capture workflow. For those local operations
inspect `obsdog --help` and `obsdog space status --space <space-id> --format
json` and use the CLI. Avoid repeating a search through both transports solely
to switch interfaces. Never crawl for other private Spaces.

For an authorized hosted connection, use the [remote MCP reference](remote-mcp.md)
instead. Its actual tools can include creation and block updates. This local
reference is not permission to switch runtimes when a hosted operation is denied.

CLI v0.2.0 defaults to the same Personal library across directories without
`init`. Use `--space personal` only when no explicit project/Org boundary applies;
otherwise preserve the exact selected Space. A broken selection is an error,
not permission to search a different library or connect cloud sync.

## Retrieve intentionally

For an inventory request, use `obsdog document list --space <space-id> --format
json` on CLI v0.2.2+, or suggest `obsdog dashboard serve` for local browsing.
Do not issue broad searches or open every document to simulate a list. Listing
is not exposure or use. Verify `obsdog version` if the command is absent;
installing this plugin alone does not install or update the CLI.

CLI v0.2.2 uses whitespace-insensitive substring discovery across languages:
`사과` finds `사과나무`, `충돌` finds `충돌은`, and `동시수정` finds `동시 수정`.
Unquoted terms are OR candidates; quotes group contiguous normalized characters;
`-term` excludes partial matches. Exact full title/content matches rank first.
This is not stemming, synonym expansion or fuzzy spelling. Do not add particle
variants solely to work around the older tokenizer. Inspect `lexical_policy`;
raw scores from different versions are not a controlled comparison.
Quoted characters must be contiguous after whitespace removal, so quotes can
exclude a note that discusses two separated identifiers. On CLI v0.2.12+, a
quoted zero-hit can show a bounded count of unquoted candidates; treat it as a
query hint, not an answer or proof of missing coverage.

1. On CLI v0.2.0+, search with `obsdog search --space <space-id> --format json --query <need> --actor-type agent --actor <agent-id>`. Returned hits are retrieved, not read or judged.
2. Add a canonical label filter only when routing requires it. Discover definitions first and use expressions such as `label:memory:horizon=long_term AND NOT label:lifecycle:state=stale`.
3. Choose from rank, document, block, exact revision, snippet, and matched labels.
4. Open only a result actually placed in human view or agent context: `obsdog search open --space <space-id> --run <run-id> --rank <n> --actor-type agent --actor <agent-id>`. This records selection for that hit, not every returned result.
5. Record `obsdog search use --space <space-id> --run <run-id> --rank <n> --type answer_evidence|citation|quote|copy|link --actor-type agent --actor <agent-id>` only when that exact revision materially supports the output.
6. Use `obsdog trace show --space <space-id> --run <run-id>` when provenance or retrieval behavior needs inspection.

Keep the same nonempty, non-sensitive agent ID across the task. CLI transport
remains `cli`; an agent actor does not make it an MCP event. Check installed help
for these flags before recording events. If unavailable, request/perform an
authorized CLI update or use the already-scoped MCP server's agent attribution;
do not fall back to the CLI's default human actor. Do not add CLI-only flags to
MCP arguments. Opening results for an agent is not genuine human feedback.

Do not open every hit for telemetry. Unopened results remain unjudged. If the first result solves the task, only that result should become selected or used.

On CLI v0.2.3+, `--limit` fixes page size (default 10, up to 100). Continue the
same frozen window with `search page --run <id> --page <n>` and the original
Space/actor flags, or scoped MCP `obsdog_search_page`. Open/use/feedback take
the returned **global rank**, not `page_rank`. Page replay adds no observations.
At most 100 candidates are retained; this is not an exhaustive corpus count.
Start a new run if the query/filters change or the current device lacks the
original frozen chunks. Unreturned candidates are not read/used/judged.

Use `search --no-observe` only for deliberate diagnostics such as checking a
repair, not for normal task retrieval. Its returned rows have no stable run/hit
receipt and cannot be opened, marked used or evaluated through search actions.
The optional scoped MCP equivalent is `obsdog_search_probe` when the connected
CLI supports it. A version mismatch in a long-running MCP session requires a
reconnect; do not assume an upgraded binary changed the existing process.
Compare `obsdog_version` in that existing connection with a fresh shell's
`obsdog version`; use the [running-process checklist](../../maintain/references/cli.md#inspect-before-mutation).

## Follow authority, not just a familiar answer

When the installed `obsdog document --help` advertises `links`, use
`obsdog document links --space <space-id> --id <document-id> --limit 5 --format json`
to inspect a selected note's direct authored navigation. The scoped MCP equivalent
is `obsdog_document_links` when present in its actual tool list. This is a next-CLI
candidate capability, not part of published v0.2.19; older runtimes can read the
links in the Markdown. Read needed destinations explicitly. The command records
no exposure/use, does not follow redirects or modify ranking, and reports
missing/ambiguous/truncated results. A link or title is not its target's evidence.

For heading-only hits, missing entity context or a noisy hub, follow
[retrieval-oriented authoring](../../maintain/references/retrieval-authoring.md).
Read the needed source/parent context; a landing-page hit is not acquisition of
its linked answer. Diagnose coverage vs ranking vs reading before changing notes.
CLI v0.2.3+ offers `--exclude-headings` (MCP `exclude_headings`) when answer-body
retrieval is the job. It filters before ranking, not after the page is cut.
Heading open still reads only that exact revision; no section-body exposure is
implied. Do not remove useful navigation headings from source merely to raise scores.

Identify whether a hit is native guidance, a discovery pointer, a derived note or
an old snapshot. Check material source/version/applicability; import time and a
working URL do not prove currency. Follow the original within existing access
when current facts matter. A pointer can genuinely help discovery without its
unread destination becoming verified evidence. Offline or denied checks remain
explicit limitations, not proof that the cached claim is incorrect.

Read necessary parent scope, warnings and surrounding procedure when the returned
leaf is insufficient. Prefer current applicable guidance for a current task;
history can answer "why" or an older-version question. On CLI v0.1.14+,
`--source-role` and `--temporal` are available; inspect help and care records
first. Do not hide unknown legacy notes by default. Authoring/source repairs use the bundled
[care criteria](../../maintain/references/knowledge-care.md), not a whole-Space rewrite.

## Feedback

CLI v0.1.16+ defaults to bounded, query-conditioned usefulness reranking. Inspect
`ranking_policy` and `learning_status` when explaining order; use `--ranking
lexical` for that installed version's baseline. `memory show --query <need>` reads the
actual activation/connection evidence. Read the bundled care guide's usage
section when investigating fading or reinforcement. Do not create repeated
searches or artificial feedback to manipulate weight; unjudged is not bad and
graph associations are not factual citations.

When feedback writes are authorized and actual work supplies an observed outcome,
evaluate it yourself instead of requiring the user to rate each result. Keep
judgments distinct: relevance links query to hit; usefulness links a genuinely
used revision to the task; correctness evaluates supported claims; freshness
follows a review policy. Identify agent judgments as `--evaluator-type agent
--evaluator <agent-id>`, include a reason, and never represent them as human
feedback. Evaluator flags do not replace retrieval actor flags; preserve the
exact target revision and Space. Read-only requests and missing evidence mean
no feedback write; an AI assessment does not prove that a human found it useful.

All four local kinds require `search open` for that exact run and global rank.
The allowed values and caller responsibilities are:

| Kind | Allowed values | Recorded state and caller responsibility |
| --- | --- | --- |
| relevance | relevant, partially_relevant, irrelevant, noise | Judge the query-hit relationship; downstream use is not required. |
| usefulness | useful, partially_useful, not_useful | Record genuine `search use` first, then judge the observed task outcome. |
| correctness | correct, partially_correct, incorrect, unverifiable | Assess the opened claims against evidence; downstream use is not required. |
| freshness | current, review_due, stale, time_independent | Apply the relevant time/review policy; downstream use is not required. |

For a used result, the order is `search` → `search open --run RUN --rank N` →
`search use --run RUN --rank N` →
`feedback add --run RUN --rank N --kind usefulness --value useful`.
Choose `partially_useful` or `not_useful` instead when that is the observed
outcome. Preserve Space and actor flags throughout; evaluator attribution
is supplied separately. An opened but rejected result can instead receive
`feedback add --run RUN --rank N --kind relevance --value irrelevant`, or the
same exact target with `--value noise`, without `use`.
Never record fictitious use to unlock `not_useful`.

The CLI enforces the recorded open/use preconditions. Claim evidence,
time/review policy and task-outcome judgments are caller responsibilities;
the command does not independently verify them or require its optional reason
field for every evaluator. The agent workflow still supplies an honest reason.

Evaluate only kinds for which work supplies evidence. An unrelated result is
not automatically incorrect or stale. At search conclusion, report zero results,
no useful result within the inspected scope, useful evidence, or insufficient
evidence to judge. This report is not a run-level `feedback add` record; that
command targets an actual hit. Positive-only samples may reflect selection
bias, but do not manufacture negative ratings to change a percentage.

CLI v0.2.3 defaults the evaluator ID to `local-<evaluator-type>`, matching the
default search caller. Keep an explicit task-specific ID on both sides when
one was used; a distinct evaluator is retained but does not impersonate the
original actor's activation sample. Older releases need the explicit ID to
avoid the mismatched agent default. Do not rewrite historical events to repair it.

Use `remember` to capture new conclusions and update notes with corrected context,
links, or current facts. Use `maintain` for duplication, conflicts across notes,
and knowledge-base organization. After source-backed work fills a coverage gap
or fixes an existing note's discoverability, read it back and rerun the original
query with `--no-observe`. If quotes or filters caused the miss, also check the
corrected query. Verify the intended current answer/revision, not merely a
nonzero count; a zero-result hint is not answer evidence. The work-owning agent
closes this loop before its handoff, rather than leaving capture to an unspecified
later agent.

Keep JSON stdout machine-clean. Do not send raw queries, content, paths, Space identifiers, comments, or reasons to external diagnostics.


On CLI v0.2.34+, options must precede positional search text. Use
`obsdog search --space SPACE_ID --no-observe --query "example query" --format json`
for a diagnostic query. Use `--query` or a `--` terminator for literal text that
looks like an option. A misplaced option is a refusal, never permission to use
Personal or observe the diagnostic query. A normal search's explicit
`not_recorded_writer_busy` fallback is unobserved and has no run/hit receipt.
Status/doctor and diagnostic search do not repair caches or require a writer.

Read-only status/probe/direct document reads acquire no writer and record no
observation, but can still fail on file access, WAL recovery or other SQLite
conditions. Do not promise `--no-observe` always succeeds. On CLI v0.2.35+ use
`space write-readiness` separately for an instantaneous rollback-only writer
probe. Preserve the other writer. Search/open/direct read/append timings describe
separate operations; an open records selection/exposure and can need a writer.
API unavailable is a remote transport/server outcome, not proof of a Space lock.


On CLI v0.2.36+, a known observation admission refusal can return complete open
content with `observation.persistence=not_recorded`, no exposure/selection event
and an exact `next_read` target. Diagnostic search also supplies block/revision
navigation. Use `block show --id BLOCK --revision REV` or advertised local MCP
`obsdog_block_read`; this is a read, not a fabricated observed run or use. An
`unknown` commit outcome is not a safe automatic retry. Inspect the original
trace/request. Successful reads and writer availability remain separate facts.
Default document list omits retired documents; use `--include-retired` only when
an audit/recovery task needs them. Exact read/history remains available.
