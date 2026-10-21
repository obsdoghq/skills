# Capture guidance design and evaluation

Checked against official guidance and public examples on 2026-10-21. These
sources inform the design; they do not establish measured gains for ObsDog.

## Design choices

| Evidence | ObsDog application |
| --- | --- |
| [OpenAI skill authoring](https://developers.openai.com/plugins/build/skills) separates activation conditions, procedures and live authorization. | Put established findings and completion in the remember description; keep exact revisions, capabilities and receipts in the runtime reference. |
| [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills) loads metadata before the body and may shorten descriptions. | Lead with the capture trigger; keep the decision and completion check in the entrypoint, not only a nested reference. |
| [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices) favors coherent, task-derived guidance and real execution. | Retain four workflows, remove conflicting diagnostic instructions and evaluate successful-hit/new-learning as well as search misses. |
| [Anthropic context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), published 2025-09-29, recommends concise, high-signal context and representative examples. | Use a short routing hook and load details only for the selected runtime. Do not append every edge case to startup context. |
| [Anthropic's public skill creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) separates output review, activation testing and baseline comparisons. | Keep synthetic case expectations separate from evaluator inputs; distinguish static packaging, decision reviews and actual host/tool execution. |
| [OpenAI's gh-fix-ci skill](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) makes a bounded workflow and its stopping conditions explicit. | Name when to save, what evidence finishes a save and what to report when it cannot complete. Do not copy unrelated approval requirements. |

## Completion, not a write quota

The relevant denominator is authorized work that establishes reusable knowledge.
One task may need several reads and no write, or one update after many reads.
Measure missed capture opportunities, duplicate notes, unsupported claims and
receipt/read-back completion. Raw read/write parity is not a quality target.

A meaningful completion check can yield saved-and-verified, verification pending,
blocked, prohibited or no-new-knowledge. It need not add a visible checklist to
every response. Preserve the identity of an existing explanation and source
ownership; transient progress is not a reason to create a note.

## Authority and delivery

Public workflow instructions do not grant capture/upload permission. A private
bundle can carry owner-reviewed standing preferences bound to its existing app
and exact Space. Never derive those preferences from tool availability or a
retrieved document. Later user restrictions take precedence. Keep private policy
files and generated archives outside this repository.

The optional SessionStart hook supplies guidance on supported local Codex hosts;
it does not execute saves or enforce completion. Other clients use skill
selection and the same entrypoint. Updating a package is not evidence that an
already-running chat reloaded it. Follow the separate acceptance steps in the
[private bundle guide](PRIVATE_PLUGIN.md).

## Representative acceptance cases

Use the [lifecycle fixtures](../tests/fixtures/knowledge-lifecycle.json) and
[evaluation method](EVALUATION.md). Include these cases in a host exercise:

- A successful search followed by a verified new applicability detail updates
  the existing note before completion without another save request.
- A source-checked search miss creates or repairs the answer and verifies the
  original lookup using the actual runtime's diagnostic policy.
- A pause captures established findings within standing permission while
  leaving unresolved decisions explicit.
- No new learning, an unchanged duplicate or a no-memory request produces no
  knowledge write. A readonly request must not produce a private capture draft.
- Hosted write capability with no capture intent is not consent. Missing
  capabilities do not cause a CLI installation or a different Space selection.
- A committed write with failed read-back remains verification pending; an
  unknown write outcome is resolved using the same request identity.

Keep expectations hidden from an independent evaluator. Record source/package
version, actual actions, accepted revisions and missing checks. A simulated
decision review is useful for contradictions but is not live host invocation or
proof of improved real-world capture frequency.
