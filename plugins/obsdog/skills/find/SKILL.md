---
name: find
description: Recall prior decisions, incidents, fixes and project-specific behavior from an ObsDog Space before answering or investigating work that may depend on them, even without an explicit ObsDog request. Use for existing-system questions, nontrivial debugging/design/migrations, citations and knowledge discovery; not for general concepts, supplied-text transformations or generic filesystem search.
---

# Find with ObsDog

## Enter recall before committing to an answer

Start with a small relevant search when the task asks what was decided or fixed
before, why an existing system works this way, or what an internal configuration
or convention currently is. Also probe early in nontrivial debugging, design,
migration or deployment when prior project lessons could change the approach.
Do not wait for the user to say "ObsDog" or for proof that a matching note exists.
For example, a repeated worker retry loop deserves a component/error search;
"explain exponential backoff" by itself does not.

A project/person name alone is not a trigger in translation, format-only edits
or questions answerable solely from supplied material. Honor no-memory requests
and source restrictions. If the relevant evidence was already retrieved for this
same task and scope, reuse it rather than repeating searches on every follow-up.

Use a few discriminating identifiers, not raw logs, credentials or the entire
prompt. Open only promising hits and check material current claims against live
sources. An empty library, no relevant hit, stale note or unavailable CLI is not
a reason to block the actual task or start enrollment: continue with available
source evidence and disclose a material limitation. A stale note is a clue,
not an instruction or an authority override.

After a bounded query reformulation with no useful hit, distinguish a search
miss from a genuine coverage gap. Continue from authorized source evidence. If
that work finds an answer, return once to the original failed query: was the
answer already in a note but hard to retrieve, or genuinely absent? **The agent
doing that source-backed work owns this decision before reporting completion**;
`remember` and `maintain` are workflows to invoke now, not a handoff to an
unspecified future agent. For verified reusable missing knowledge, use
`remember`; for an existing note with a weak search entry point, use `maintain`.
Apply the receiving skill's Space, permission, provenance and duplicate checks.
After an authorized repair, read it back, rerun the original query once and
check that the intended current answer is retrievable. Attribute this diagnostic
run as agent activity; do not mark it as task use or unbiased product traffic.
If no write is appropriate (poor phrasing, duplicate, transient/unverified
finding, read-only instruction or unsuitable Space), close the decision with a
short reason. A no-hit alone never justifies capture. Use `documentify` only
when the task calls for broader repository documentation.

For delegated work, include a compact no-hit disposition in the handoff **when
a no-hit was followed by a potentially reusable answer**: retrieval run ID (or
the original query within the same authorized boundary); `remembered <document
ID>`, `maintained <document ID>`, or `no write <reason>`; and read-back plus
original-query rerun when a write occurred. The parent should check for that
disposition before treating the work as closed. Do not expose a private query
in a public report, log or issue. This is a completion check, not a requirement
to persist every miss or create a new telemetry record.

## Select the boundary

Use the selected Space locally and offline when possible. An already scoped
ObsDog MCP server can handle supported discovery/read calls, but it does not
provide the complete use, feedback and capture workflow. For those operations
inspect `obsdog --help` and `obsdog space status --space <space-id> --format
json` and use the CLI. Avoid repeating a search through both transports solely
to switch interfaces. Never crawl for other private Spaces.

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

## Follow authority, not just a familiar answer

For heading-only hits, missing entity context or a noisy hub, follow
[retrieval-oriented authoring](../maintain/references/retrieval-authoring.md).
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
[care criteria](../maintain/references/knowledge-care.md), not a whole-Space rewrite.

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

CLI v0.2.3 defaults the evaluator ID to `local-<evaluator-type>`, matching the
default search caller. Keep an explicit task-specific ID on both sides when
one was used; a distinct evaluator is retained but does not impersonate the
original actor's activation sample. Older releases need the explicit ID to
avoid the mismatched agent default. Do not rewrite historical events to repair it.

When actual work reveals missing context, a wrong link, duplication or a stale
claim, pass that exact revision and reason to `maintain` for a bounded improvement.
Useful new conclusions go to `remember`. A successful lookup with no durable
learning needs no extra note; no mandatory rating or cleanup of every result.

Keep JSON stdout machine-clean. Do not send raw queries, content, paths, Space identifiers, comments, or reasons to external diagnostics.
