---
name: documentify
description: Document an authorized repository and capture useful source pointers or grounded synthesis in an ObsDog Space. Use for onboarding, architecture, operations, or issue context; do not mirror a repository by default, claim undocumented behavior or ingest secrets.
---

# Documentify with ObsDog

Use CLI v0.2.0+. Select `--space <space-id>` on each command when the task names
a Space; omitted selection means Personal, not a repository binding. There is no
`init` step. A missing explicit boundary must not fall back to another library.

Document the repository the user placed in scope. Inspect its agent instructions, authoritative docs, manifests, entry points, tests, deployment configuration, and a bounded sample of relevant issues when access is authorized.

## Choose the home, then document

Read the bundled [authoring and care criteria](../maintain/references/knowledge-care.md)
before choosing capture and boundaries. Code/API contracts, invariants and
maintained runbooks belong in code/repository documentation. When those writes
are authorized, improve that home first; an ObsDog import is not a replacement.
Otherwise disclose the gap and keep any useful account provisional. Do not infer
source-write or upload permission just because the repository can be read.

Prefer a discoverable pointer to existing maintained docs. Add a source-grounded
onboarding map, cross-source explanation or tested lesson only when it helps a
real reader/job. A selective snapshot needs offline/reproducibility value,
permission and an exact source version. A file-by-file mirror, full issue history
or parallel release/TODO log is not the default deliverable.

For repository or infrastructure onboarding, first answer the reader's practical
navigation questions: which repository owns a service or behavior, where its
maintained architecture and runbook live, which code/configuration entry point
implements it, and how deployment or rollback reaches it. Record only useful
question-to-source routes and actual cross-repository boundaries. Keep the
maintained explanation and procedures in their owning repositories; an ObsDog
orientation pointer should explain when to follow each source, not reproduce a
directory tree or claim that a path remains current. Verify code locations at
the checked revision before using them for a change.

## Build reviewable knowledge

Apply [retrieval-oriented authoring](../maintain/references/retrieval-authoring.md)
when deciding whether an overview, aliases or topic grouping helps discovery.
Keep the introduction in the authoritative repository; the Space may need only
a short orientation pointer and useful routes to existing specialist knowledge.

Choose the reader's job first (how-to, explanation, reference or tutorial when
useful), without creating empty category folders. One focused topic should still
make sense when found through search. Preserve applicability, prerequisites and
source versions; block boundaries follow meaning and independent revision, not
fixed token length. Extraction/merge requires lineage and verified sync support,
not an ad hoc copy/delete cleanup. Use maintenance criteria for these decisions.

- Match evidence to the claim: specification for intent, code/tests for a version's
  implementation, runtime checks for an observed environment. Preserve disagreement
  and label inference; code inspection alone does not prove deployed behavior.
- Produce focused Markdown documents such as overview, architecture, data model, operational runbook, and contributor workflow only when the repository supports them. Avoid a file-by-file dump.
- Include a canonical locator and checked commit/release/section with date/method
  where material. Distinguish moving-branch links from pinned evidence. Do not copy
  credentials, environment values, private user data or generated dependencies;
  do not leak inaccessible sources through a pointer's title/snippet.
- Stage drafts outside the Space when useful, then check their claims against sources yourself. The authorized repository scope does not require a separate human approval for every note. Ask before expanding to unrelated sources, new disclosure or destructive replacement; do not bulk-ingest just because files are reachable.
- Before each import batch, run `obsdog document list --space <space-id> --format json` and `obsdog search --space <space-id> --query "<distinctive topic or source name>" --actor-type agent --actor <agent-id> --format json`; open likely matches and compare their canonical source path and purpose. `document import` always creates a new document, even when the title and source path match on older CLIs. It is not a regenerate/upsert step. If the note already exists, revise its current blocks with `obsdog block update --id <block-id> --base-revision <revision-id> --content <text> --reason <reason> --actor-type agent --actor <agent-id> --space <space-id> --format json`, or use a reviewed care plan for structural change. Do not read an existing document to a temporary file and re-import it as an edit. An explicit `--fork` on newer CLIs means a genuinely separate document, not a repair for a duplicate rejection.
- Import only source-checked, in-scope **new** Markdown through `obsdog document import`, verify the resulting documents and blocks, and suggest provenance or lifecycle labels if the Space definitions support them. Report important results and uncertainty, not a mandatory manual draft-review queue.
- Once a repository has a documented baseline, route future evolution and cleanup to `maintain` rather than regenerating everything.

## Finish the reference map

Documentification is not finished merely because imports succeeded. When the
source has meaningful relationships, verify that readers can follow them in the
document graph (`insights show` → `graph`, or the local dashboard's Graph).

On CLI v0.2.3+, preserve relative Markdown references: they resolve against exact
imported paths in the selected Space. Import the target too only when in scope.
Missing or duplicate paths remain unresolved; never guess by filename alone.
Older local graphs resolve stable IDs only—do not promise relative-path support.

For a new source-grounded overview and specialist notes, finish a bounded second
pass in the same task: import the notes, read back their IDs and current block
revisions, then add useful citations with conditional `block update` and a reason.
For example, an orientation pointer can link “rollback prerequisites” to the
already read specialist note rather than copying its whole procedure. Re-read
the resulting references and map; no separate human review is required for an
otherwise authorized correction. Record an unresolved target as a limitation.

Use a current-revision `question` comment for a genuinely uncertain relation;
it appears as an opt-in proposal, not a citation. No link quota: independently
useful notes may remain isolated. Do not infer relationships from shared tags or
create artificial search/open/use events to make the graph look connected.

Documentification does not imply benchmarking, Git sync or a crawler. Keep a
derived note's source/version and uncertainty explicit through attributable
follow-up, rather than pretending it automatically tracks its source. Significant
ADR/postmortem rationale may be retained; routine work diaries are not required.
