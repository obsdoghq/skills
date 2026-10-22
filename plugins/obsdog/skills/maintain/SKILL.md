---
name: maintain
description: Incorporate findings, user corrections and check results into existing ObsDog explanations as work progresses. Reconcile related notes and update their links and lookup vocabulary.
---

# Maintain ObsDog

Update explanations as reading and work change the current understanding.
Continue directly from recording a finding to integrating it into the relevant
section of the existing note.

## Update when understanding changes

Read the note, surrounding context and linked sources. Incorporate findings,
requirements, decisions, procedure changes and their reasons as they arise.
When the user corrects a requirement or a check changes a hypothesis, update its
existing explanation and any affected next steps.

When sources differ, record each observation with its version or environment,
the unresolved question and next check. Revise those statements as checks progress.

- A test rejects a recorded cause: mark that hypothesis rejected, retain the
  evidence and explain what will be checked next.
- A user corrects a deployment requirement: update the requirement and procedure
  that depended on it, linking the relevant decision.
- A search misses an existing answer: add the task's question or error term to
  the matching explanation and check the original lookup after saving.

## Connect and organize

Read both ends of a relationship and link the notes with the question the link
answers. Connect overviews to procedures, source locations and detailed explanations.
Combine overlapping explanations around their subject. Split subjects that need
independent explanations. Keep decision history and connect superseded guidance
to its current replacement. Use the runtime's supported structural operations.

## Apply and verify

Read the current revision, apply the update, then read back the accepted revision.
Check the explanation, structure and links. After a search repair, check the
original lookup. Return saved locations and any unfinished verification.

## Tools and destination

Use [remote MCP](../find/references/remote-mcp.md) for the connected account and
Space selected for the task. Resolve that destination from current tools when
needed. For an explicitly selected local library, use [CLI usage](references/cli.md).
Follow source/upload scope and explicit read-only or no-memory requests.

For merge, split, move and supersede operations, read
[care execution](references/care-execution.md). For source ownership and history,
read [knowledge care](references/knowledge-care.md). For lookup vocabulary and
navigation, read [retrieval authoring](references/retrieval-authoring.md).
