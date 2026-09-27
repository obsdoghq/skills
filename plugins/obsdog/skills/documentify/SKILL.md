---
name: documentify
description: Turn an authorized code repository into reviewable Markdown knowledge and import it into an ObsDog Space. Use for repository onboarding, architecture, operations, or issue-context documentation; do not claim undocumented behavior or ingest secrets.
---

# Documentify with ObsDog

Document the repository the user placed in scope. Inspect its agent instructions, authoritative docs, manifests, entry points, tests, deployment configuration, and a bounded sample of relevant issues when access is authorized.

## Build reviewable knowledge

Choose the reader's job first (how-to, explanation, reference or tutorial when
useful), without creating empty category folders. One focused topic should still
make sense when found through search. Preserve applicability, prerequisites and
source versions; block boundaries follow meaning and independent revision, not
fixed token length. Extraction/merge requires lineage and verified sync support,
not an ad hoc copy/delete cleanup. Use maintenance criteria for these decisions.

- Prefer evidence from code and maintained configuration. Label inference as inference and unresolved behavior as a question or follow-up.
- Produce focused Markdown documents such as overview, architecture, data model, operational runbook, and contributor workflow only when the repository supports them. Avoid a file-by-file dump.
- Include exact source paths or public links where they make claims auditable. Do not copy credentials, environment values, private user data, or generated dependencies.
- Stage drafts outside the Space when useful, then check their claims against sources yourself. The authorized repository scope does not require a separate human approval for every note. Ask before expanding to unrelated sources, new disclosure or destructive replacement; do not bulk-ingest just because files are reachable.
- Import source-checked, in-scope Markdown through `obsdog document import`, verify the resulting documents and blocks, and suggest provenance or lifecycle labels if the Space definitions support them. Report important results and uncertainty, not a mandatory manual draft-review queue.
- Preserve useful relative links when their exact imported targets exist in the same Space. For generated relationships between imported notes, read back their stable IDs and use explicit Markdown citations; do not fabricate IDs or bulk-connect every file. Record uncertain relationships as reasoned question comments, then route unresolved imports and stale citations to `maintain`.
- Once a repository has a documented baseline, route future evolution and cleanup to `maintain` rather than regenerating everything.

Documentification does not imply benchmark or product comparison. Keep code truth and prose synchronized through attributable follow-up revisions.
