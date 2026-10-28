---
name: find
description: Search and read ObsDog at task start and when new questions, components, errors or sources appear. Apply the context and write what the lookup and investigation reveal.
---

# Find with ObsDog

At task start, search for the question, project or component. Open matching notes,
read the surrounding explanation, and follow links to related notes and sources.
Apply that context to the work.

## Search as questions arise

Search again when a new question, component, error, term or source appears. Use
names and identifiers discovered in the notes and source material. When a query
misses, try related terms and investigate the available sources.

Use the actual question and exact error names. Check each answer's environment,
version and status against the task before applying it; an imported old source
is not a newer fact. Open the relevant detail directly when found, without forcing
every lookup through an overview. If finding the answer required alternate terms
or assembling scattered notes, improve the existing explanation even when the
lookup succeeded. Repair missing vocabulary and recheck the original question; see
[retrieval authoring](../maintain/references/retrieval-authoring.md).

## Turn reading into writing

After finding an answer or reading a source, write what you learned and how it
applies to this task. Update the matching explanation, including the sources and
conditions being checked. Record open questions and the next check as they arise.
When the subject has no note, create one from the investigation so far and keep
updating it. Include the original question and the vocabulary used in the lookup.

- A note explains retries; the source reveals a timeout interaction. Add that
  interaction and its applicability to the same explanation.
- A search finds no answer; a log reveals a symptom. Record the symptom, source,
  current hypothesis and next check, then continue investigating.

This is the ongoing `remember` and `maintain` workflow: capture the finding and
integrate it into the explanation as one continuous action. At phase changes and
before the final response, finish outstanding saves and read-back using the
[capture checkpoints](../remember/references/checkpoints.md).

## Tools and destination

Use [remote MCP](references/remote-mcp.md) when connected ObsDog tools are available,
keeping the selected account and Space. For an explicitly selected local library,
use [CLI usage](references/cli.md). When no connected ObsDog tools exist in the
session, use an already installed `obsdog` CLI for the same authorized Space;
verify `obsdog space status --space <space-id> --format json` and follow that
CLI reference. A hosted denial, lost permission or broken selection is not tool
absence and does not authorize a local/account fallback. Do not install, log in,
migrate or broaden access just to capture. Keep source/upload and read-only or
no-memory restrictions. Resolve an unclear Space once; use returned identifiers
and current exact revisions for writes.
