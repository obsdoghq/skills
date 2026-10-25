# Author explanations that remain useful

Use this guide for a new explanation or a substantial revision. For a small
correction, apply the relevant principle without reopening every reference.
This is the shared authoring source for the four ObsDog workflows.

## Start with the question and the current answer

Find the subject's existing home and read its context and sources. State what
the reader needs to understand or do, then lead with the answer known so far.
Keep the environment, version, prerequisite and exception near the claim they
qualify. Preserve exact identifiers and error names that a future lookup needs.
Explain unfamiliar names from sources instead of guessing their meaning.

Write observations, hypotheses and open questions as they arise. Include the
next check; improve the same explanation as evidence arrives. A polished form
or a confirmed conclusion is not a prerequisite for capture.

## Choose a shape that fits the reader

| Reader's need | Useful content |
| --- | --- |
| Learn through a first success | Starting state, guided actions, observable result, what was learned. |
| Complete a task | Goal, applicability, prerequisites, ordered actions, expected result and recovery. |
| Look up a contract | Exact names and values, defaults, limits, examples, version and exceptions. |
| Understand a system | Roles, boundaries, relationships, behavior, reasons and tradeoffs. |
| Diagnose a symptom | Symptom and environment, evidence, hypotheses, checks, resolution and remaining uncertainty. |
| Understand a decision | Context, choice, alternatives, consequences, status and reconsideration condition. |

These are drafting aids, not mandatory templates or separate folders. A short
answer need not contain every field. Preserve an ordered procedure as a usable
whole even when it includes explanation and reference details. See the
[examples](authoring-examples.md) for provisional findings and structural choices.

## Integrate sources into a maintained explanation

Use a new source to revise the affected subject, not automatically to create
another summary. Explain agreement, differences and what each source establishes.
Keep raw evidence distinguishable from the synthesis and the current answer
distinguishable from dated events. Link the original source or observation.
An imported older report does not become the latest truth because it arrived last.

Separate specified behavior, implementation, test results and observed runtime
behavior. A passing test does not establish deployment. An AI synthesis is not
independent corroboration of the sources it summarizes. When evidence conflicts,
retain the applicable dates/environments and unresolved question; do not silently
pick the newest-looking statement. A correction should revise affected claims
and next steps, including known dependent notes within the task's scope.

Keep consequential decisions, failed attempts and their reasons available in
current explanations or linked historical records. Do not rely on old revision
bodies remaining readable forever. Retention and source availability can differ.
Keep durable rationale accessible under the current storage policy; report an
unavailable historical body rather than substituting today's text.

## Control growth during writing

Each addition is also a chance to integrate repetition and check the topic's
boundary. If questions, audiences or update cycles diverge, or history starts
burying the current answer, use [note structure](note-structure.md) to decide
between sections, extraction, consolidation and keeping the note intact.
Capture the finding now even if a larger restructure needs a supported operation.

Give each independently maintained question a clear home. Do not create a page
per source, noun, day or paragraph. A useful overview states the answer at its
level and links to detail by the questions each destination answers. Direct
searches may go straight to a detailed note; the overview is not a required hop.

## Make future retrieval work

Use the actual question, domain vocabulary, aliases and exact error in natural
prose. Give a result enough local context to identify its subject, applicability
and current status. A bare fragment such as "increase it to 30" is not reusable.
Link related explanations only after reading the relationship's context. Link
count and graph density are not quality targets.

On a miss, distinguish absent knowledge from a retrieval problem: search related
terms and inspect the likely home before creating a duplicate. After repair,
retry the original question and read the intended answer. Keep diagnostic search
and actual use declarations distinct. See
[retrieval authoring](../../maintain/references/retrieval-authoring.md).

## Verify the resulting knowledge

Read back the accepted revision. Check that the answer, applicability, uncertainty,
sources and next action survived the edit. Open changed link destinations; for a
new note or repaired lookup, confirm that the original question reaches the answer.
Record the real write/read-back result, including unfinished work.

Assess failures separately: was the fact recorded, could it be retrieved with
usable context, and was it applied correctly? Formatting, saved-note counts and
search rank alone do not establish usefulness. Use
[remote MCP](../../find/references/remote-mcp.md) for execution contracts and
[knowledge care](../../maintain/references/knowledge-care.md) for source/history rules.

## Design references

Reviewed 2026-10-25. These inform the writing approach, not measured improvements
in ObsDog. Keep product contracts in the runtime references.

- [Diátaxis](https://diataxis.fr/) separates reader needs;
  [KCS article structure](https://library.serviceinnovation.org/KCS/Knowledge-Centered_Success_Practices_Guide/301-Evolve_Loop/Practice_5_Content_Health/Technique_5.1)
  supports context and reuse during work.
- [Google procedures](https://developers.google.com/style/procedures) and
  [Nygard's ADRs](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
  inform actionable steps and retained decision rationale.
- [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
  motivates maintained synthesis with separate sources and operating rules.
- [Graphiti's temporal model](https://www.getzep.com/blog/beyond-static-knowledge-graphs/)
  distinguishes changing facts; it does not make extraction infallible.
- [EvalMem](https://arxiv.org/abs/2609.22231) distinguishes storage, retrieval and
  answer failures. Its benchmark outcomes are not ObsDog results.
