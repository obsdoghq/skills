# Active reading and writing guidance

## Product purpose

The [canonical mission](https://github.com/obsdoghq/obsdog/blob/main/docs/MISSION.md)
from [central PR #127](https://github.com/obsdoghq/obsdog/pull/127) is
**Knowledge, made observable.** and **Make memory truly useful.**
This alignment was checked against merge commit
`e334027ebfe94906da4db62e53d9061cb3100d6b` on 2026-10-22.

The workflow priority is active knowledge use: read extensively for the
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

## Trigger the next action

The shared hook follows the task's events rather than asking the agent to choose
among skill names first. The skills explain how to carry out each action.

| Event | Action |
| --- | --- |
| Task start; new question, component, error or source | Search, open the explanation, follow sources and apply the context. |
| Requirement, preference or correction | Record the current requirement, scope and reason; update affected steps. |
| Answer found or source read | Write what was learned and how it applies to this task. |
| Decision, attempt or check | Record the choice or attempt, conditions, result and next action. |
| Incomplete understanding | Save observations, hypotheses and questions now, then revise as checks progress. |
| Phase change or final response | Finish accumulated saves, record next actions and read back. |

Capture and integration are a continuous writing flow. Keep the subject's existing
home current and create one when absent. The entrypoints include examples of a
successful lookup followed by writing, a failed attempt, a user correction and a
hypothesis changed by a later check. Scope and runtime mechanics remain in the
selected runtime reference.

This structure draws on [Basic Memory's assistant guide](https://docs.basicmemory.com/reference/ai-assistant-guide)
and [Graphiti's agent rules](https://github.com/getzep/graphiti/blob/main/mcp_server/docs/cursor_rules.md),
reviewed on 2026-10-22. These are design references, not evidence of measured
improvement in ObsDog behavior. The static hook still supplies instructions;
it does not run searches or save transcripts itself.

## Maintain explanations as they grow

The packaged [authoring guide](../plugins/obsdog/skills/documentify/references/authoring-guide.md)
is the common source for reader purpose, evidence, current state and retrieval.
[Note structure](../plugins/obsdog/skills/documentify/references/note-structure.md)
owns split/consolidation timing and mechanics; the
[fictional examples](../plugins/obsdog/skills/documentify/references/authoring-examples.md)
show the decisions. Documentify reads the guide for substantial writing; maintain
loads structure guidance when boundaries change. Remember and find keep the small
criteria needed in daily work. The hook carries only the shared behavior.

Write for later tasks that ask the same question or express the same intent
differently. Actual symptom wording and source-confirmed names belong near the
answer and its conditions, not in a keyword list. A successful lookup that needed
detours or scattered notes is also an authoring opportunity. The retrieval
reference owns bounded checks; the hook and global snippet state the purpose.

Review boundaries during additions and corrections, when retrieval exposes buried
answers, and at phase changes. Separate independent questions and update cycles;
use internal sections for a single coherent task. Preserve conditions, exceptions,
source identity and useful history, then verify both old navigation and direct
lookup. A byte threshold is an inspection signal, never a reason to cut meaning.
Keep runtime operations in the existing Care references and use the current
capability contract. Guidance does not add an unsupported structural operation.

The design draws on the sources linked in those references, including LLM Wiki,
Basic Memory and Letta. It adopts maintained synthesis and progressive detail,
without importing full-project scans, raw transcript collection, fixed page
quotas or source-removal rules. Published memory benchmarks and favorable user
reports motivate evaluation; they do not establish ObsDog outcomes.

## Runtime and delivery

Reuse the user's existing capture permission, selected Space and source scope.
Explicit read-only/no-memory instructions still define the task boundary.
Resolve account and Space selection from the current connection. Reuse the
user's selected destination or the sole available Space; resolve a choice among
several destinations before writing. Shared workflows carry no personal Space
IDs or packaged owner permission. The registered app mapping stays in its
manifest. Exact revisions, idempotent requests, supported operations and read-back
belong in runtime references.

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
