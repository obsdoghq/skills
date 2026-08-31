---
name: documentify
description: Turn an authorized code repository into reviewable Markdown knowledge and import it into an ObsDog Space. Use for repository onboarding, architecture, operations, or issue-context documentation; do not claim undocumented behavior or ingest secrets.
---

# Documentify with ObsDog

Document the repository the user placed in scope. Inspect its agent instructions, authoritative docs, manifests, entry points, tests, deployment configuration, and a bounded sample of relevant issues when access is authorized.

## Build reviewable knowledge

- Prefer evidence from code and maintained configuration. Label inference as inference and unresolved behavior as a question or follow-up.
- Produce focused Markdown documents such as overview, architecture, data model, operational runbook, and contributor workflow only when the repository supports them. Avoid a file-by-file dump.
- Include exact source paths or public links where they make claims auditable. Do not copy credentials, environment values, private user data, or generated dependencies.
- Write drafts outside the Space first when substantial judgment is involved. Let the user review destructive replacements or broad imports.
- Import accepted Markdown through `obsdog document import`, verify the resulting documents and blocks, and suggest provenance or lifecycle labels if the Space definitions support them.
- Once a repository has a documented baseline, route future evolution and cleanup to `maintain` rather than regenerating everything.

Documentification does not imply benchmark or product comparison. Keep code truth and prose synchronized through attributable follow-up revisions.
