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
