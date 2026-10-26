# Split, consolidate or keep a note

Read this when a note grows beyond its question, history obscures the current
answer, or related notes overlap. Apply it to the affected notes and known links;
a local edit does not require a whole-Space audit.

## When to reconsider the boundary

Review the boundary while adding a new topic, after a correction exposes several
versions of the same fact, when a lookup returns a broad note with buried detail,
and at a phase change if progress records are accumulating. Do not wait for an
arbitrary length limit or postpone capture until a cleanup finishes.

Use these signals to choose the smallest helpful change:

| What you observe | Appropriate response |
| --- | --- |
| One question, but a paragraph mixes several steps or claims | Split paragraphs or blocks; add headings inside the same note. |
| A section answers a distinct question, is reused on its own, or changes independently | Extract it into a focused note with its own answer and context. |
| Background, current procedure and extensive incident history compete | Keep the current answer visible; separate the independently useful history or procedure and connect them. |
| Several notes repeat the same answer for the same scope | Choose the existing canonical home and consolidate unique evidence through supported operations. |
| Similar symptoms apply to different versions or environments | Keep the variants explicit; split if each needs an independent procedure. Do not merge by keyword alone. |
| A recovery sequence, contract table or argument must be read together | Keep it together, even when long. Headings or bounded reads may be enough. |
| Many tiny pages require repeated prerequisite lookups to answer one question | Consolidate the fragments or restore enough local context. |

Size and repeated read truncation are inspection signals, not semantic boundaries.
No universal byte, line or page count establishes quality. Runtime input/output
limits still apply; consult the current tool contract for those limits. A tool
limit does not authorize deleting evidence or inventing a split operation.

## Choose the units before moving content

For each proposed destination, state its reader question, answer, applicability
and expected updates. If two destinations cannot be described independently,
sections may be better. Search for an existing home before proposing a new one.
Keep prerequisites, exceptions, causal explanation and evidence with the claim
or step that needs them. Preserve contrasting environments instead of flattening
them into one generic rule.

Separate the maintained answer from the chronological record. Fold repeated
progress statements into current state, while keeping decisions, rejected causes,
failed attempts and reasons in a readable linked record where needed. A summary
on top of an unchanged growing log does not resolve the structure problem.

## Carry out a bounded restructure

1. Read the affected notes and their current revisions. Identify the content
   being moved, retained or consolidated and the known links that depend on it.
2. Choose the supported operation. Read
   [care execution](../../maintain/references/care-execution.md) before an extract,
   split, merge, move or supersede. Follow its exact revision and check/apply
   contract; a successful check does not reserve the base revision.
   A CLI with `document split` can construct the extraction receipt directly.
   On older care-capable CLIs, use the existing `extract-document` plan rather
   than treating the missing shorthand as proof extraction is unavailable.
   Read document-scoped identities with `document read --structure --format json`.
   The [execution guide](../../maintain/references/care-execution.md) distinguishes
   unreleased shortcuts, installed support and connected preparation.
3. Preserve the source note's useful identity. Leave a brief answer at its level
   and a descriptive link to the new home where the old detail was expected.
   Give the destination a self-contained opening, scope and source/history links.
   Keep a short prerequisite near the procedure even if its fuller explanation
   has another home; necessary local context is not harmful duplication.
4. Use returned identities to repair the affected overview and known inbound
   references. Record provenance and lineage through the supported operation;
   do not assume titles, anchors, identifiers or history transfer automatically.
5. Read back every affected document and changed link destination. Check both
   the old reader path and a direct lookup for each new question. Confirm that
   conditions, exceptions, evidence and unresolved work are still reachable.

If a conflict occurs, reread the latest revision and reconsider the bounded plan.
If the operation is unsupported or refused, keep the accepted explanation intact,
record the proposed boundary and precise unfinished action, and report the limit.
Do not simulate a move by creating a copy and deleting or clearing the source.
Do not call a proposed split complete before both content and navigation verify.

## Stop splitting when it stops helping

A successful split makes the next question easier to answer and the next update
easier to place. It does not simply reduce bytes. If readers need every new note
for every use, the boundary is probably too fine. Retain a coherent procedure;
merge fragments when they repeatedly change together. Avoid empty hubs, mandatory
categories, link quotas or one-page-per-entity rules.

See [worked choices](authoring-examples.md) for a section split, an extraction,
current/history separation and a case that should remain intact.

## References and limits

Reviewed 2026-10-25. [Basic Memory's defrag workflow](https://github.com/basicmachines-co/basic-memory/blob/main/skills/memory-defrag/SKILL.md)
offers split/consolidate/dated-correction patterns. Its scheduled whole-project
audit and product-specific permissions are not defaults for ordinary ObsDog edits.
[Letta's core-memory guidance](https://github.com/letta-ai/letta-code/blob/main/src/skills/builtin/maintaining-core-memory/SKILL.md)
motivates revising existing principles and opening detailed memory when needed.
ObsDog explanations still need provenance; do not copy its prompt-only advice to
omit incident history from all knowledge notes. Neither source establishes a
universal split threshold or measured ObsDog performance.
