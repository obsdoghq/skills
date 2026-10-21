---
name: remember
description: Write findings, decisions, investigation results and work context to ObsDog as work progresses. Update matching notes during investigation, implementation and verification, including after successful searches. Save preliminary findings and open questions with their status, then revise them as evidence arrives.
---

# Remember with ObsDog

Make memory truly useful by writing the context that work produces and updating
it as understanding develops. Follow the
[mission](https://github.com/obsdoghq/obsdog/blob/main/docs/MISSION.md) through
ongoing capture and read-back.

## Write during the work

Use the selected Space and capture permission already established by the user.
Carry out writes as findings arise, including after a successful lookup, without
waiting for another save request or for the whole task to finish.

Capture these concrete outputs:

- Source and code locations, component roles, configuration and behavior learned.
- Decisions, the reasons for them and the alternatives considered.
- Approaches tried, their results, errors encountered and fixes applied.
- Tests and checks performed, their results and the conditions they covered.
- Current investigation context, provisional explanations, open questions and
  the next checks or actions.

Write observations as observations and hypotheses as hypotheses. Include the
available evidence, uncertainty and next check, then update the same note as the
answer becomes clearer. An unfinished investigation still produces context to
save; preserve its current state without presenting it as a confirmed conclusion.

## Find the existing home and update it

Search for the subject and read the matching document before writing. Add the new
context to the relevant section, or create a document when the subject has no
existing home. Keep the same document identity as findings accumulate.

Organize the explanation around the question and task. Incorporate the latest
finding alongside the background and rationale needed to understand it. Preserve
source/version distinctions and the history needed to explain a changed decision.
Connect related notes using their actual document or block identifiers.

Use `maintain` for reconciling multiple notes or structural changes, and
`documentify` for source investigation and connected explanations.

## Make the saved context readable and findable

Use a title and terms from the task, source names, identifiers and error messages.
Include the source location, checked version or date, applicability and result.
Keep maintained contracts linked to their source, and write the explanation,
investigation context and relationships in ObsDog.

Summarize logs and conversations into observations, attempts, decisions, results
and next steps. State what remains unconfirmed in the same readable content.

## Finish writes and read them back

At the transition from investigation to implementation, after verification, and
before completion, pause or handoff, save the accumulated findings and current
context. Use the [capture checkpoints](references/checkpoints.md).

Read back the accepted revision and check its Space, title, content and links.
For a new note or retrieval repair, check that the task's lookup reaches the
answer using the runtime's diagnostic policy. Reuse a check already completed
for the same revision. Return the saved location and actual verification result.
If a tool operation fails, retain its exact outcome and report what remains unsaved
or unverified while continuing the task's available work.

## Runtime

Use [remote MCP](../find/references/remote-mcp.md) for the selected hosted
connection, or [CLI usage](references/cli.md) for the selected local library.
Preserve current revision bases, request identity, attribution and the selected
Space. Follow the user's source/upload scope and explicit read-only/no-memory
instructions. Keep secrets out of saved content.
