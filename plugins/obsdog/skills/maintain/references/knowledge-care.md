# Knowledge care in an active task

Use these criteria when a capture or maintenance task needs judgment about
document boundaries, relationships or quality. They are ObsDog's
`knowledge-care/v1` rubric, not a universal standard or automatic ranking policy.

## Choose an operation from an observed need

- Add only durable knowledge with no existing canonical answer. Search first.
- Update an existing block when the subject is the same and evidence changed.
- Split distinct questions or independently changing claims; keep the minimum
  context needed to understand each successor. A long procedure, warning plus
  command, table, or code example can be one coherent unit. Do not split solely
  to hit a token target: retrieval chunks are derived, not authored identities.
- Merge true duplicates or inseparable fragments with compatible scope/version.
  Reconcile differences explicitly; do not erase conflicting evidence or merge
  a how-to and an explanation merely because their words overlap.
- Link only after reading both ends. Explain the next-step purpose: prerequisite,
  evidence, explanation, example, qualification, contradiction or replacement.
  These are prose rationale categories, not supported typed-edge CLI options.
  Generic relatedness is not support, equality or a transitive relation.
- Retire demonstrably superseded/duplicate material with a reason, replacement
  pointer and recoverable history. Never delete for age, low use or zero links.
  Hard removal needs explicit scope and a supported recoverable procedure.

Use only capabilities exposed by the installed runtime. Stable block split/merge
does not imply atomic cross-document merge/redirect support. For connected Spaces,
verify sync and recovery support for structural operations before applying them.
If unsupported, leave a review proposal; no DB edit, copy-delete workaround or
experimental upgrade. On the currently deployed history-adoption transport,
structural round-trip acceptance is still pending: use comments/revisions only.

## Review without a magical score

Inspect dimensions independently, with `pass / needs_work / unknown /
not_applicable`, reason and cited evidence:

- Document: reader/job, scope/version, source, title/discoverability, duplication.
- Block: focused idea, sufficient context, independent revisability, source
  faithfulness, intact prerequisite/code/table boundaries.
- Link: exact target/scope, useful purpose/direction, supported rationale,
  current revision, duplication and contradiction.
- Outcome: relevance/noise when actually opened; usefulness only after real use;
  correctness/freshness only against evidence. Unexamined is not bad.

A short attributable comment may record `knowledge-care/v1` dimensions and a
proposed operation. This is a review note, not a machine-aggregated metric.
Existing `feedback add` kinds retain their real meanings; do not invent rubric
values or claim a comment alone trains the ranker. Keep AI/human attribution.
Repeated praise from the same agent/task is not independent corroboration.

## Close the loop with a small, auditable change

1. Search/open in the selected Space; preserve scope and existing IDs.
2. Do the actual user task. Record use only when the evidence genuinely helped.
3. Evaluate relevant outcomes with a concrete reason, not every returned hit.
4. Select a bounded improvement justified by those observations or current source.
   Check current revisions and existing proposals, including rejected ones.
5. Apply the smallest authorized change using actor/base-revision/reason flags.
   Keep uncertain connections in question comments; actual citations in
   evidence/explanation or canonical prose. Closing a proposal is not promotion.
6. Verify Markdown, identity/history, context and incoming/outgoing links. Search
   again when relevant; a maintenance replay is not a fabricated task use.
   Preserve old evaluation against old revisions and do not inherit verification
   across split/merge.
7. Sync only the already authorized Space and report material changes/limits.

Strengthening means preserving and improving useful evidence, not accumulating
links. Weakening means reviewing applicability, rejecting a bad proposal or
retiring proven obsolete material—not an untested automatic decay/delete rule.
Current graph width counts distinct citing blocks, not usefulness.

## Counterexamples to check

- A long self-contained deployment procedure: keep prerequisites and warnings;
  adjust retrieval context before fragmenting its authoring blocks.
- A rare but correct disaster-recovery note: preserve it despite zero usage.
- Two similarly titled notes about different versions: do not merge by title.
- A link that was opened but not used: no usefulness/use event.
- A plausible relation with no source proof: question proposal, not evidence.
- Rejected proposal or changed source revision: do not reopen/rebind without new
  evidence. Keep history; write a new justified record if needed.
- A wrong current command: correct promptly against the authoritative version;
  do not wait for a popularity threshold.

## Sources

Reviewed 2026-09-28; these inform the rubric, not a claim of external certification.

- [Diátaxis](https://www.diataxis.fr/start-here/) and
  [incremental workflow](https://www.diataxis.fr/how-to-use-diataxis/): reader needs
  and small improvements; do not impose empty taxonomy scaffolding.
- [OASIS DITA topics](https://docs.oasis-open.org/dita/v1.1/CS01/archspec/topics.html):
  focused yet context-complete authoring units (historical reference).
- [Obsidian Note composer](https://obsidian.md/help/plugins/note-composer):
  extraction/merge as editing workflows; ObsDog additionally preserves lineage.
- [W3C SKOS](https://www.w3.org/TR/skos-primer/) and
  [PROV](https://www.w3.org/TR/prov-primer/): relation semantics and attribution.
- [Unbiased Learning-to-Rank with Biased Feedback](https://arxiv.org/abs/1608.04468):
  clicks have presentation bias; no raw popularity-equals-quality policy.
- [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/): measure context
  cost and task outcomes, not a universal model-independent block size.
