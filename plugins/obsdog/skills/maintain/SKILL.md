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
- A lookup misses, needs alternate wording or requires scattered notes: improve
  the matching explanation and its navigation, then check the original lookup
  after saving. See [retrieval authoring](references/retrieval-authoring.md).

## Connect and organize

Read both ends of a relationship and link the notes with the question the link
answers. Connect overviews to procedures, source locations and detailed explanations.
Combine overlapping explanations around their subject. When additions introduce
independent questions, different update cycles or accumulating history, read
[note structure](../documentify/references/note-structure.md) for split timing,
boundaries and verification. Keep a coherent procedure together and preserve
decision history, conditions, evidence and navigation through supported operations.

For substantial changes to an explanation, read the shared
[authoring guide](../documentify/references/authoring-guide.md); use its
[examples](../documentify/references/authoring-examples.md) when a boundary is unclear.
Small corrections do not require loading every reference or auditing the Space.

## Apply and verify

Read the current revision, apply the update, then read back the accepted revision.
Check the explanation, structure and links. After a search repair, check the
original lookup. Return saved locations and any unfinished verification.

## Tools and destination

Use [remote MCP](../find/references/remote-mcp.md) when connected ObsDog tools are available,
keeping the selected account and Space. For an explicitly selected local library,
use [CLI usage](references/cli.md). When no connected ObsDog tools exist in the
session, use an already installed `obsdog` CLI for the same authorized Space;
verify `obsdog space status --space <space-id> --format json` and follow that
CLI reference. A hosted denial, lost permission or broken selection is not tool
absence and does not authorize a local/account fallback. Do not install, log in,
migrate or broaden access just to capture. Keep source/upload and read-only or
no-memory restrictions. Resolve an unclear Space once; use returned identifiers
and current exact revisions for writes.
