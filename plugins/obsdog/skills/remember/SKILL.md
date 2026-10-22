---
name: remember
description: Write user requirements, preferences, findings, decisions, attempts and results to ObsDog as they arise. Record hypotheses and open questions immediately, then update the same notes as work progresses.
---

# Remember with ObsDog

Write while the work happens, within the user's established task scope and
selected Space. Continue saving without waiting for completion or another request.

## Write at the event

| What happens | What to write |
| --- | --- |
| The user gives a requirement, preference or correction | The current requirement or preference, its scope and stated reason. Update the previous explanation when corrected. |
| A lookup or source answers a question | What was learned, where it came from and how it applies to this task. |
| A decision is made | The choice, reason and alternatives considered. |
| An approach or check runs | What was tried, its conditions, result and next action, including failures. |
| Understanding is incomplete | Observations, hypotheses and open questions with their status and next check. |
| Work changes phase or reaches the final response | Accumulated findings, current work state and next actions. |

Save observations and hypotheses immediately with their status. When a check
supports, changes or rejects a hypothesis, update that same explanation with the
result and the next step. Continue writing after successful searches.

## Keep the subject's existing home current

Search for the subject and read its matching note. Update the relevant section;
create a note when the subject has no home. Keep its identity as work develops.
Integrate the new understanding into the explanation, including source locations,
versions or dates and the question being answered. Link related notes and sources.

Recording a finding and incorporating it into the explanation are one continuous
writing flow. Use the `maintain` workflow for reconciling several notes or changing
their structure as needed.

For example, record a failed timeout adjustment with the observed error and next
check. When a later test identifies the cause, update that investigation with the
cause and result. If the user changes the rollout requirement, update its existing
section and the next actions that depend on it.

## Save and read back

Read back accepted saves and confirm the content and links. For a new note or a
search repair, check that the task's lookup finds the explanation. At phase changes
and before the final response or handoff, finish remaining saves using the
[capture checkpoints](references/checkpoints.md).

Return saved locations and actual unfinished writes or checks.

## Tools and destination

Use [remote MCP](../find/references/remote-mcp.md) for the connected account and
Space selected for the task. Use the sole available Space when no selection
exists; resolve an unclear choice among several once. Use current revisions and
returned identifiers for updates. Use [CLI usage](references/cli.md) only for an
explicitly selected local library. Follow source/upload scope and explicit
read-only or no-memory requests. Keep secrets out of saved content.
