---
name: documentify
description: Investigate sources and write connected explanations in ObsDog. Read code, documents, configuration and work records to explain the task's questions, then expand existing notes and record findings as the investigation progresses.
---

# Documentify with ObsDog

Make memory truly useful by connecting source investigation to written knowledge.
Follow the [mission](https://github.com/obsdoghq/obsdog/blob/main/docs/MISSION.md)
through reading, explanation, updates and verification.

## Find and read the existing context

Identify the subject and questions from the user's request and ongoing work.
Search ObsDog for existing explanations, prior decisions, related investigations
and source pointers. Open them and read the context and linked sources.

Use terms discovered in the sources to search additional questions. Follow
relevant code, documents, configuration, tests, issues and work records to explain
component roles, behavior, data flow, procedures and rationale.

## Write while investigating

Update the existing explanation as each part of the subject becomes understood.
Create a document for a subject that has no existing home. Include source
locations, roles, relationships, observed behavior, decisions and their reasons.

Write preliminary explanations and unresolved questions with their current
status, supporting observations and next checks. Distinguish intended behavior
in specifications, implemented behavior in code and observations from a running
environment. Revisit those sections as further evidence arrives.

Organize the explanation around readers' questions and tasks. Connect the
overview, procedures and detailed knowledge with links that explain what each
destination answers. When several sources are needed, write their combined
explanation and cite each source's contribution.

## Integrate and verify

Use `remember` for individual saves and `maintain` to reconcile overlapping notes
or apply structural changes. Preserve existing document identities and include
source versions, dates, environments and the context needed to apply the answer.

Read back saved documents and follow their links. Search representative task
questions, open the results and follow the navigation to the detailed answer
using the runtime's diagnostic policy. At completion or handoff, save the current
explanation and open questions, and return the saved locations and checks.

## Runtime

Use [remote MCP](../find/references/remote-mcp.md) for the selected hosted
connection, or [CLI usage](references/cli.md) for a selected local library.
Investigate with the available source tools and write within the user's selected
Space and source/upload scope. Honor explicit read-only/no-memory instructions
and keep secrets out of documents and queries.
