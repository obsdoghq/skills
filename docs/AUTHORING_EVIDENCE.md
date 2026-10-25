# Evidence behind the authoring guidance

Reviewed 2026-10-25. This is a design rationale, not a product ranking, installation
recommendation or ObsDog benchmark. Source documentation describes intended
mechanisms; firsthand reports describe use; papers measure bounded experiments.
Popularity is not satisfaction, and published scores are not interchangeable.

## Closest operational references

| Reference | Relevant evidence | Decision for ObsDog |
| --- | --- | --- |
| [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | An author's workflow separating sources, maintained synthesis and operating conventions. | Revise the existing explanation as sources and questions arrive; keep provenance and navigation. Do not require a new page per source or an index-first hop. |
| [Basic Memory assistant guide](https://docs.basicmemory.com/reference/ai-assistant-guide) and [defrag skill](https://github.com/basicmachines-co/basic-memory/blob/main/skills/memory-defrag/SKILL.md) | Executable guidance for recurring lookup/writing, splitting mixed topics, consolidation and dated corrections. | Review topic boundaries during relevant work. A whole-project maintenance schedule and its permissions are not imported into ordinary edits. |
| [Letta core memory](https://github.com/letta-ai/letta-code/blob/main/src/skills/builtin/maintaining-core-memory/SKILL.md) | Maintained principles and deferred detail with explicit retrieval cues. | Keep the hook concise and load the needed guide. Preserve evidence in knowledge notes even where a prompt-only memory system omits it. |
| [Graphiti temporal model](https://www.getzep.com/blog/beyond-static-knowledge-graphs/) | Distinguishes when facts hold from when they are recorded. | Write applicability and effective time near claims; reconcile changed facts without silently losing their history. This does not require adding a graph engine. |
| [Mem0 paper](https://arxiv.org/abs/2504.19413) | Vendor-authored LoCoMo evaluation of extraction, consolidation and retrieval. | Treat consolidation as a first-class decision. Its QA, latency and token claims do not prove performance for ObsDog's documentation tasks. |
| [Hindsight memory workflow](https://github.com/vectorize-io/hindsight/blob/main/hindsight-integrations/agent-plugin/skills/hindsight-memory/SKILL.md) | Separates recall, retention and synthesis. | Distinguish retrieving facts from reconciling an explanation. Preserve ObsDog's immediate provisional capture instead of adopting a durable-only save gate. |

The documentation foundation remains reader-purpose separation from
[Diátaxis](https://diataxis.fr/), context and reuse from
[KCS](https://library.serviceinnovation.org/KCS/Knowledge-Centered_Success_Practices_Guide/301-Evolve_Loop/Practice_5_Content_Health/Technique_5.1),
actionable [procedures](https://developers.google.com/style/procedures), and
[decision rationale](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
The result is shared authoring guidance plus targeted skill routing, with the
existing runtime contracts still controlling actual operations.

## Favorable experience with concrete limits

[Thoughtworks' April 2026 Graphiti assessment](https://www.thoughtworks.com/radar/platforms/graphiti)
reports team use and moves it to Trial. It also calls out extraction cost and
dependency management. This is relevant external adoption experience, not an
independent head-to-head measurement of every memory system.

[Brian Buntz's month-long LLM Wiki account](https://www.rdworldonline.com/is-karpathys-viral-llm-wiki-helpful-mostly-yes-one-month-in/)
describes useful synthesis across covered topics in a roughly 760-page wiki.
At that point maintenance time roughly balanced time saved. This supports paying
attention to upkeep and coverage; it does not establish a general productivity gain.

[Letta's filesystem evaluation](https://www.letta.com/blog/benchmarking-ai-agent-memory/)
reports 74.0% LoCoMo accuracy with GPT-4o mini. The setup includes parsed/embedded
files, semantic search and tool rules. It is a vendor-run agent evaluation, not
proof that plain files alone outperform all memory services. It reinforces the
need to evaluate the agent's use of retrieval, not only a storage architecture.

## Research that changes how to evaluate

- [Single-Round Vector RAG vs an LLM-Compiled Wiki, v3](https://arxiv.org/abs/2605.18490v3)
  compares 13 questions over 24 papers with one answer model. Synthesis benefited,
  but query tokens were much higher. The October correction removes the earlier
  citation-support advantage after fixing truncated evidence and checking human
  judgments. Do not cite the earlier result as current confirmation.
- [Progressive disclosure, v2](https://arxiv.org/abs/2607.04576v2) studies access to
  an unchanged 709-page wiki. It reports lower cost but weak human/judge agreement
  and exceptions to quality non-inferiority. It does not test whether splitting
  the page content itself improves answers or establish a universal size limit.
- [LongMemEval](https://arxiv.org/abs/2410.10813) separates extraction, multi-session
  and temporal reasoning, knowledge updates and abstention. Test changed facts
  and insufficient evidence, not only successful recall.
- [EvalMem](https://arxiv.org/abs/2609.22231) diagnoses encoding, retrieval and
  generation separately. Its auxiliary MemWiki improves mean accuracy on its
  evaluated systems; this is motivation for diagnosing missed answers, not a
  forecast for ObsDog.

These sources favor a measured approach: keep original evidence, maintain useful
explanations, retrieve only needed detail and verify the original question after
repair. Record the model, snapshot, question set, judge, source access, tool budget,
upkeep cost and failure categories for any outcome comparison. See
[evaluation cases](EVALUATION.md). No outcome benchmark was run for this release.
