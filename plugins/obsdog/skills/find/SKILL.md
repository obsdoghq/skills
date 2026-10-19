---
name: find
description: Find and apply knowledge, context, and background relevant to the work using ObsDog. Search for code locations and repository structure, architecture and infrastructure, decisions and implementation rationale, incidents and fixes, configuration and conventions, workflows and work history, domain knowledge, and prior investigations. Use throughout the work without waiting for an explicit user request, and search again as new questions arise.
---

# Find with ObsDog

## Use the selected runtime

When the selected, authorized ObsDog connection exposes remote MCP tools, use
[remote MCP](references/remote-mcp.md). Search and read through those tools
without checking for or installing the ObsDog CLI. For a selected local library,
use the existing CLI reference instead. Preserve the selected Space and storage
mode; unavailable remote operations do not authorize a switch to local storage.

## Find knowledge for the work

Use ObsDog throughout the work to find knowledge and context. Do not wait for an explicit user request or certainty that a relevant note exists.

Search beyond the start of a task. Search during investigation, implementation, and verification as new questions arise or background needs to be understood.

Reuse evidence already checked for the same question and scope. Check again when the subject, environment, version, or assumptions change.

## Search specifically and read the necessary context

Express what you need to learn in concrete search terms. Use project names, component names, file paths, configuration keys, error codes, issue IDs, and domain terms.

Open promising results and read the surrounding context and related knowledge needed to understand the answer. Reading a title or link does not mean its linked content has been read.

If the first search misses, adjust terms, identifiers, quotes, or filters. If no useful results appear or search is unavailable, continue the work by investigating authorized source material.

## Apply retrieved knowledge to the current work

Use retrieved knowledge as evidence for answers, direction for investigations, pointers to code and documents, and background for decisions.

Check claims about the current state against source code, documentation, configuration, or other relevant sources. Use historical records to understand decisions and their rationale at the time. If a source cannot be checked, distinguish established facts from remaining uncertainty.

## Connect knowledge gained during the work

Regardless of whether search succeeded, use `remember` to capture new knowledge and update existing notes with findings established during the work. Use `maintain` to organize the knowledge base, reconcile duplication or conflicts across notes, and improve its structure or discoverability.

Use `documentify` when investigating source material to systematically connect knowledge and build or expand a knowledge base.

Follow the corresponding skill for capture, updates, and verification.

When source-backed work answers a search miss, the agent doing that work completes the corresponding save or repair and checks the original lookup before finishing. For delegated work, return the original query/run, the saved or maintained document, and read-back/retrieval verification; explain a remaining limitation when the loop cannot be closed.

Use the [capture checkpoints](../remember/references/checkpoints.md) before delegation, pause or handoff. Search success, source progress and capture completion are separate; the parent verifies an actual write/read-back receipt rather than treating a worker's promise as stored knowledge.

## Record actual use and observed evaluations

Distinguish results returned by search, results actually read, and results applied to the work.

For a selected local CLI library, use `open` to read selected results and `use`
to record results that supported an answer or decision. Preserve the retrieval
run, result rank and exact revision, with agent attribution.

When feedback writes are authorized and actual work supplies evidence, evaluate
the inspected result yourself with agent attribution and a reason. Do not wait
for the user to rate each hit. Read the selected runtime's feedback reference
before writing: use relevance for an opened result rejected for this query;
usefulness requires real recorded use. Correctness and freshness require their
own evidence and are not mandatory ratings after each search.

At a meaningful search conclusion, state whether no results were returned,
none of the inspected results helped, evidence supported the task, or evidence
was insufficient to judge. Name the inspected scope; do not claim that the
library has no answer. Continue the task when nothing helps. This statement is
not a persisted run evaluation. Noise on one hit can coexist with useful hits.
Leave unopened hits unjudged. Record positive and negative observed outcomes
honestly; do not target a rating distribution or invent use to permit feedback.

For remote MCP, acknowledge a received native search when its metadata and
actual tools support `obsdog_search_complete`. Search/open receipts alone state
`server_response_prepared`; completion is a client-declared receipt, not use.
Read the exact content and apply it to the work before declaring direct use.
Submit genuine use or feedback only through an available authorized tool with
its required exact target. If unavailable, report the limitation without switching
runtimes or inventing a record. See the [remote workflow and observation
reference](references/remote-mcp.md) for completion, use and dashboard coverage.

Do not manufacture searches, opens, uses, or feedback to increase ranking or usage counts.

## Respect search scope and access boundaries

Work within the selected Space and authorized sources. Honor explicit read-only and no-memory requests, along with storage and upload restrictions. Keep secrets out of queries and records.

Read [CLI usage](references/cli.md) for a selected local runtime, or the remote
MCP reference above for hosted calls. Use only attribution and observation
operations exposed by that runtime; do not require a CLI to manufacture missing
remote use or feedback records.

Keep installed-runtime checks in the [update checklist](https://github.com/obsdoghq/skills/blob/main/docs/SETUP.md#updating-cli-and-agent-guidance). Consult it after an upgrade or a missing command, not before every search.
