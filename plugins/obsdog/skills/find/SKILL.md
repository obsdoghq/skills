---
name: find
description: Actively search and read ObsDog knowledge at task start and throughout investigation, implementation and verification. Open matching notes and related context, expand searches as questions arise, apply what you read and connect new findings to ongoing writes.
---

# Find with ObsDog

Make memory truly useful by reading and applying knowledge throughout work.
Follow the [mission](https://github.com/obsdoghq/obsdog/blob/main/docs/MISSION.md)
through actual lookup, reading, use and updates.

## Search throughout the task

Start with the task's subject, project, component, error or question. Search again
when investigation introduces another component, decision, procedure or source.
Use names, identifiers, file paths, configuration keys and terms found during
work to expand the lookup. Reuse already-read evidence for the same question,
and search the additional questions it raises.

When a query misses, reformulate it with source terminology and related names.
Continue into authorized sources, then write the answer and context back through
`remember`. Preserve the original lookup cue so the new explanation can be found.

## Read the answer and its context

Open matching results and read the surrounding document. Follow links to prior
decisions, prerequisites, procedures and sources that explain the current question.
Read the destination content, not only its title. Use overviews to reach detailed
answers and read adjacent sections when they supply missing context.

Compare the retrieved explanation with the code, documents, configuration or
runtime evidence used in the task. Record the checked version and applicability.
Keep differing source statements and open questions visible while investigating.

## Apply and update

Use what you read to answer the question, choose an implementation approach or
continue the investigation. As work adds findings, source locations, explanations
or changed context, use `remember` to update the matching note. This applies after
both successful retrieval and search misses.

Use `maintain` to incorporate corrections, reconcile related notes and improve
entry points. Use `documentify` to investigate and connect the sources needed for
a broader explanation. Before completion or handoff, finish the corresponding
writes and read-back using the [capture checkpoints](../remember/references/checkpoints.md).

## Record the lookup and its contribution

For hosted MCP, acknowledge received searches with the available completion tool,
open exact results, then record actual use and supported feedback after applying
the content. For local CLI, use its search/open/use and feedback commands with
agent attribution. Preserve the returned run, hit and revision identities.

Describe what the evidence helped answer and what remains to be investigated.
When later work uses an updated note, record that task's observed outcome.

## Runtime

For the selected hosted connection, read [remote MCP](references/remote-mcp.md).
It supplies search, exact reads and supported writes without requiring the CLI.
For the selected local library, read [CLI usage](references/cli.md).
Use the actual tools and preserve the selected Space, authorized sources and
explicit read-only/no-memory instructions.
