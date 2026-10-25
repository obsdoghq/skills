# Evaluate reading and ongoing writing

The [synthetic lifecycle cases](../tests/fixtures/knowledge-lifecycle.json) cover
lookup, contextual reading and capture throughout work. Names and events are
fictional. Expected decisions are authored cases, not observed model performance.

For an authorized behavior evaluation, use isolated fixtures and stubbed sources.
Give the evaluator the prompt, context and raw artifacts without expected labels.
Record the actual actions and resulting content. Keep synthetic decision reviews
separate from real runtime execution.

Check these actions:

- Search at task start and when new questions or components arise. Open matching
  notes, surrounding context and related source material.
- Write during investigation, implementation and verification, including after
  successful retrieval. Update existing notes with accumulating findings.
- Save provisional explanations, unsuccessful attempts, current work context and
  open questions with their status, evidence and next check.
- Save and read back the accumulated context before completion and handoff.
- Use the selected Space and explicit task scope, current revision bases and
  supported operations. Preserve actual failure and verification status.

Report missed reads, omitted context, deferred writes despite available authority,
existing-note updates, accepted revisions and read-back results. Check that
hypotheses remain labeled and source evidence is represented accurately.
Package tests establish structure; real host/tool traces establish execution.

## Observe actions, not matching phrases

Exercise task-start lookup, a successful lookup followed by an update, a search
miss followed by source investigation and writing, a saved hypothesis revised by
a check, a failed attempt with its next step, a user correction and an unfinished
handoff. Inspect calls and saved content, including when each action happened.

Compare the share of eligible tasks with actual reads and accepted writes, the
number of task steps before the first write, omitted events and failed saves.
Count a saved revision and its read-back separately. Preserve the same task scope
and comparable cases across versions. The fixture's expected actions and package
tests are specifications, not observed agent execution or measured improvements.

## Account-independent destination cases

- Install the same workflow bundle for two synthetic account contexts. Give each
  context a different sole authorized Space. Check that each selects the returned
  Space and that neither uses the package creator's destination.
- Return several authorized Spaces without a task selection. Check that the agent
  resolves that destination once before writing, then reuses it for later saves.
- Start with a task-selected Space among several available destinations. Check that
  the existing selection is retained without asking again.
- Update a fixture installation containing an old owner policy. Inspect all
  packaged Markdown and execute the hook: no previous owner's policy or Space
  selection may survive in the new shared instructions.

Package comparisons and synthetic decisions do not prove that a fresh client
invoked the hook or that another real user's runtime completed a write.

## Authoring and structure cases

These are evaluation specifications, not completed behavioral measurements.
Use fictional source notes and revisions. Give an authorized evaluator the raw
task and artifacts without the expected outcome; compare the actual resulting
content and operations against these criteria.

| Case | Result to inspect |
| --- | --- |
| A successful lookup is followed by new evidence | The existing answer gains the evidence and applicability without a duplicate summary. |
| A saved hypothesis is disproved | The current explanation changes; the rejected cause, evidence and next check remain reachable. |
| Code and CI pass, deployment is pending | The note distinguishes implementation/testing from runtime state. |
| Same symptom, incompatible environments | Each condition and remedy remains explicit. |
| An original question misses an existing answer | Vocabulary is repaired and the original question reaches the correct answer. |
| One long paragraph answers one question | Internal blocks or sections improve readability without unnecessary documents. |
| One section is reused and updated independently | Extraction preserves context, lineage, source navigation and direct retrieval. |
| Daily progress buries the answer | Current state is integrated; useful decisions and failures remain in linked history. |
| A long restore sequence includes critical rollback conditions | The coherent procedure stays intact; warnings remain beside relevant steps. |
| Fragmented notes repeat the same scope | Consolidation preserves unique evidence and distinguishes genuine variants. |
| A source changes or a new import contradicts an older observation | Effective time and source authority determine the update, not import time. Known dependent explanations are reconciled. |
| A base revision conflicts or extraction is unsupported | Latest work remains intact; no copy/delete substitute or false completion claim. |
| One sentence needs a correction | No compulsory Space-wide scan or reload of every guide. |
| The user requests read-only or no memory | No write is attempted. |

Diagnose whether required knowledge was recorded, retrieved with enough context,
and correctly applied. Include missing conditions, stale claims, navigation cost,
tokens/latency and upkeep effort when measuring usefulness. Compare identical
tasks, models, source snapshots and tool budgets across versions. Do not compare
vendor leaderboard scores with different answerers, judges, subsets or history
access as if they isolated memory quality. See [design evidence](AUTHORING_EVIDENCE.md).

Package validation checks portable links, archive reference bytes, hook size and
publication boundaries. A manual scenario review is a design check. Neither is
a live structural-operation test, a fresh-session invocation or an outcome benchmark.
