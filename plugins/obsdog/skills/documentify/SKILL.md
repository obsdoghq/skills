---
name: documentify
description: Investigate code, documents, configuration and work records while building connected ObsDog explanations. Write each understood part and update the explanation as sources and checks reveal more.
---

# Documentify with ObsDog

Investigate sources and build the explanation together. Write each understood
part as it emerges, then keep reading and updating as the task develops.

## Start from the question

Search ObsDog for the subject, existing explanations and prior decisions. Read
matching notes and follow their source links. Investigate the code, documents,
configuration, tests or work records needed to answer the current question.
Search again with the questions, names and terms those sources introduce.

For a new explanation or substantial revision, read the shared
[authoring guide](references/authoring-guide.md) and the relevant
[worked examples](references/authoring-examples.md). Choose the shape that answers
the reader's question; do not delay recording an unfinished understanding.

## Build the explanation during investigation

After reading a source or completing a check, update the subject's existing note
with what it reveals and how that applies to the task. Create a note when the
subject has no home. Explain component roles, relationships, behavior, procedures
and reasons, with source locations and the applicable version or environment.

Record observations, hypotheses and open questions with their status and next
check. Update them when a later source or test supports or changes the explanation.
Distinguish specification, implementation and observed runtime behavior in the text.

For example, a configuration file establishes the retry limit while the worker
code explains when it resets. Write those two parts and link their sources now.
Record the untested timeout interaction as a hypothesis with a runtime check,
then update it with that check's result.

## Connect and finish each phase

Organize around readers' questions. Link overviews, procedures and detailed notes
with what each destination explains. Use the ongoing `remember` and `maintain`
flow to save findings and integrate them into current explanations.

When additions introduce an independent question or bury the current answer in
history, use [note structure](references/note-structure.md) to choose sections,
extraction or consolidation. Keep prerequisites, exceptions and evidence with
the explanation they qualify; length alone is not a split rule.

At phase changes and before the final response or handoff, save the accumulated
explanation, work state and next checks. Read back saved content and check its
links. For a new note or search repair, check that the task's lookup finds the
answer. Return saved locations and any unfinished write or check.

## Tools and destination

Use [remote MCP](../find/references/remote-mcp.md) for the connected account and
Space selected for this task. Resolve available Spaces from current tools when
needed. For an explicitly selected local library, use [CLI usage](references/cli.md).
Follow source/upload scope and explicit read-only or no-memory requests.
Keep secrets out of saved content.
