---
name: find
description: Find and apply knowledge, context, and background relevant to the work using ObsDog. Search for code locations and repository structure, architecture and infrastructure, decisions and implementation rationale, incidents and fixes, configuration and conventions, workflows and work history, domain knowledge, and prior investigations. Use throughout the work without waiting for an explicit user request, and search again as new questions arise.
---

# Find with ObsDog

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

## Record actual use

Distinguish results returned by search, results actually read, and results applied to the work.

Use `open` to read and record selected results, and `use` to record results that supported an answer or decision. Preserve the retrieval run, result rank, and exact revision, and attribute activity to an agent.

Do not manufacture searches, opens, uses, or feedback to increase ranking or usage counts.

## Respect search scope and access boundaries

Work within the selected Space and authorized sources. Honor explicit read-only and no-memory requests, along with storage and upload restrictions. Keep secrets out of queries and records.

Read [CLI usage](references/cli.md) when using CLI commands, selecting a Space, adjusting search syntax, paging through results, or recording activity.

Keep installed-runtime checks in the [update checklist](https://github.com/obsdoghq/skills/blob/main/docs/SETUP.md#updating-cli-and-agent-guidance). Consult it after an upgrade or a missing command, not before every search.
