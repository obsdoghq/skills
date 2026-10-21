---
name: remember
description: Save reusable findings, decisions, tested fixes and changed procedures in ObsDog when established during work or before completion. Use for explicit memory requests and proactive capture under existing permission, even after a successful search. Update matching notes and verify saved content.
---

# Remember with ObsDog

## Decide and finish capture

Apply the user's explicit instructions over this workflow. Establish the selected
Space, storage/upload scope and permission from the request or existing standing
instructions. Reuse that permission; tool availability or an approval setting
alone does not authorize collecting unrelated work. If permission is missing,
continue the task and raise a concrete save proposal only when useful.

Capture when work establishes something future work needs: a decision and its
reason, a tested fix, changed applicability, a source location or a reusable
explanation. A successful search does not suppress new learning. Search misses
are another trigger, not a prerequisite. Skip unchanged duplicates, trivial
edits and transient progress; preserve explicitly requested uncertainty as such.

Before task completion, pause or handoff, close the capture loop: save and read
back eligible findings, or retain an accurate no-new-knowledge, prohibited or
blocked disposition. A promised save or private draft is not a completed write.
Keep this check in the task workflow, not a separate ledger or a mandatory
user-facing report for every turn.

## Use the selected runtime

For a selected, authorized remote ObsDog connection, use
[remote MCP](../find/references/remote-mcp.md) to create documents or update
existing blocks. CLI installation is not required. Use the local CLI reference
only for a selected local library. A missing hosted write capability is not
permission to create a different local copy or change sync settings.

## Capture knowledge established during the work

Record facts, decisions, explanations, and context established during the work so they can be found and used later. Use both user-provided information and findings checked against source material.

When standing instructions authorize ongoing capture, do not wait for a separate save request each time. Record findings as they become clear and continue the work.

Distinguish facts, decisions, hypotheses, and unresolved questions. Preserve the user's wording and meaning, and keep certainty within what the evidence establishes.

## Incorporate findings into existing knowledge

Search for knowledge related to the subject and read promising results.

Create a note for a new subject, or update an existing note when the finding belongs there. Reflect changed facts and decisions while preserving necessary background and history.

Organize the canonical explanation around the question future work needs to answer, not one note per source file or tool call. Extend the relevant section and source context when the subject already has a home.

Use `maintain` to reconcile duplication or conflicts across notes, merge or split documents, or otherwise organize the knowledge base. Use `documentify` to systematically investigate sources and build or expand a knowledge base.

Connect related knowledge using actual document or block identifiers and explain the relationship.

## Write for future retrieval and understanding

Use a descriptive title and terms people will search for. Include the background, scope, and rationale needed to understand the note without reading the current conversation.

Link source-backed knowledge to its origin and location. For claims about the current state, include the checked version, environment, date, or other details needed to judge applicability.

Summarize work history around what was done, what was established, conclusions reached, and remaining follow-ups.

Extract relevant facts and context from raw logs and conversations, and leave out secrets.

## Save and verify

Save to the selected Space with agent attribution. Preserve document identity when updating existing notes. Do not re-import an existing note as a new document.

Read back the accepted revision and verify the target Space, title, body and
links. Check retrieval for a new note or a discovery repair using the selected
runtime's diagnostic policy. Reuse an already completed check for this revision;
do not search again merely to add activity. A content correction that does not
affect discovery needs read-back, not an invented search/use event.

Briefly tell the user what knowledge was saved and where.

For examples at completion, delegation, interruption or input-required boundaries,
use the [capture checkpoints](references/checkpoints.md). Return actual capture
evidence; keep ordinary supported capture separate from an unavailable atomic
operation.

## Honor applicable restrictions

Follow any explicit restrictions on Space, sources, storage, or uploads. Honor read-only and no-memory requests.

If saving is unavailable, disclose the relevant limitation and continue the original task.

Read [CLI usage](references/cli.md) for local authoring, or the remote MCP
reference above for hosted authoring. Preserve current document and block
revisions, request identity and selected Space in either path.

After an upgrade or an unexpected missing write command, use the [update checklist](https://github.com/obsdoghq/skills/blob/main/docs/SETUP.md#updating-cli-and-agent-guidance). A fresh shell does not update a running MCP connection.
