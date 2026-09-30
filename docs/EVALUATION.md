# Evaluate recall and capture decisions

The [synthetic lifecycle cases](../tests/fixtures/knowledge-lifecycle.json) cover
entry decisions and selective capture separately from search ranking. All names,
events and findings are fictional; there are no customer sessions or knowledge.
These are authored expectations, not observed model results or a quality claim.

Each case supplies a phase, prompt, context, expected decision, necessary actions
and forbidden actions. When behavior evaluation is authorized, run in an isolated
temporary Space with stubbed sources and no real credentials, network publication
or production writes. Give the host only prompt/context and fixture inputs, not
the expected labels. Record the actual skill/tool actions and resulting content;
do not accept "I checked memory" as proof without its trace.

For entry cases, check recall when a new question arises at startup or mid-task,
opening relevant results, source verification and fallback on no-hit/unavailability.
For completion cases, supply candidate evidence and existing-note/source fixtures;
check permission, exact Space, duplicate handling, source/verification metadata,
readback and excluded content. Reuse existing evidence when the same task already
performed the relevant check. Do not reward extra searches, notes or ratings.
Check capture after successful retrieval as well as after a miss. Remember
creates and updates individual findings; maintain handles broader reconciliation
and discoverability. Verify actual content and read-back, not a mandated report
template. A retrieval repair also needs an original-query diagnostic rerun.
These cases test workflows, not invocation performance or the search index.

Report denominators and exclusions, not just a pass percentage:

- Recall misses among eligible cases; unnecessary recall among ineligible cases.
- Unauthorized, sensitive or cross-boundary writes and unsupported factual claims.
- Duplicate/unnecessary captures among writes; omitted reusable findings among
  authorized capture opportunities. No durable finding is an expected no-write.
- Source-check completion, task continuation after no-hit/stale/unavailable data,
  and extra latency/context. Real later usefulness needs separate outcome evidence.

Keep skill/package and fixture versions, host/model configuration, repeated-run
variability and missing traces with results. Static fixture and package checks
only establish integrity; they cannot establish invocation recall, precision or
knowledge quality. This repository includes no model runner, automatic production
evaluation, collection hook or background job.
