# Active reading and writing guidance

## Product purpose

The [canonical mission](https://github.com/obsdoghq/obsdog/blob/main/docs/MISSION.md)
from [central PR #127](https://github.com/obsdoghq/obsdog/pull/127) is
**Knowledge, made observable.** and **Make memory truly useful.**
This alignment was checked against merge commit
`e334027ebfe94906da4db62e53d9061cb3100d6b` on 2026-10-22.

The owner's current priority is active knowledge use: read extensively for the
task and write what the work produces throughout its progress. The mission
explains why agents do this. Entry instructions specify the concrete lookup and
writing actions, with runtime mechanics in the relevant references.

## Translate the mission into actions

| Loop | Action during work |
| --- | --- |
| Observe | Search at task start and as questions arise. Open notes, surrounding context, related decisions and source links. Apply them to the task. |
| Diagnose | Compare the explanation with current sources. Write observations, differences, preliminary explanations and the next checks. |
| Improve | Update the existing note as findings develop. Add decisions, rationale, attempted approaches, results and work context. Create a home for a new subject and connect related explanations. |
| Observe again | Read back saved content. Check discovery for a new note or repaired lookup. Record actual use and supported feedback as work applies the knowledge, then incorporate further findings. |

Capture happens during investigation, implementation and verification, including
after successful retrieval. Save accumulated context at phase transitions,
completion, pauses and handoffs. Record an unfinished investigation with its
current status and open questions, then revise the same explanation as evidence
arrives. Confirmation is a claim status to record, not a prerequisite for writing
an observation or hypothesis.

Use direct instructions such as “write the observation and next check” and
“update the matching note.” Avoid subjective save gates such as “only if valuable
enough,” “only fully established findings,” or “skip uncertain content.” The
entrypoint should make the next read or write clear.

## Runtime and delivery

Reuse the user's existing capture permission, selected Space and source scope.
Explicit read-only/no-memory instructions still define the task boundary.
Private bundles preserve the owner's existing policy; keep real identifiers
outside this public repository. Exact revisions, idempotent requests, supported
operations and read-back belong in runtime references.

The optional SessionStart hook supplies these instructions in supported local
Codex sessions. The same four entrypoints guide other supported clients. Package
validation, installed files, actual host invocation and real saved content are
separate acceptance checks; use the [private bundle guide](PRIVATE_PLUGIN.md).

## Authoring references

The following sources informed the concise trigger/body/reference structure
checked on 2026-10-21; they do not establish measured model outcomes:

- [OpenAI skill authoring](https://developers.openai.com/plugins/build/skills)
  separates activation, workflow and live authorization.
- [Codex discovery](https://learn.chatgpt.com/docs/build-skills) loads descriptions
  before the body, so concrete lookup/write triggers come first.
- [Agent Skills guidance](https://agentskills.io/skill-creation/best-practices)
  favors task-specific instructions and execution-based validation.
- [Anthropic context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  supports concise routing and relevant progressive detail.

## Acceptance

Use the [lifecycle cases](../tests/fixtures/knowledge-lifecycle.json) and
[evaluation method](EVALUATION.md). Check that the agent reads across related
components, continues writing after a successful lookup, saves provisional
investigation context and failed attempts with their status, and finishes writes
before handing work over. Test actual saved content and revision read-back when
a runtime exercise is authorized. Keep synthetic decision reviews distinct from
real tool execution and subsequent task outcomes.
