---
name: remember
description: Save durable, source-grounded knowledge in an ObsDog Space when explicitly requested or when standing capture permission covers reusable learning from ordinary work. At meaningful milestones consider tested fixes, operating lessons and durable decisions; skip duplicates, transient chat and unsupported claims. Plugin installation alone does not authorize capture.
---

# Remember with ObsDog

Resolve the target Space and durable intent from the request and existing scope;
ask only if either is materially ambiguous. With capture already authorized, check,
import and read back the note yourself rather than asking for each routine save.
Preserve user-authored wording when supplied; distinguish facts, hypotheses,
decisions and follow-ups rather than silently upgrading certainty.

## Consider capture at a meaningful milestone

An existing instruction authorizing proactive capture is sufficient intent; do
not require another "remember this" after each relevant fix or investigation.
Without that permission or an explicit capture request, do not write. Search-only
and no-memory instructions take precedence. Inspect the exact Space's existing
sync status/permission: a nominally local write to a connected Space can upload.
Permission in one project/client/Space does not grant it in another.

For proactive capture, select a verified reusable finding, tested procedure or
explicit durable decision. Check whether it would change a future answer or
prevent a repeated mistake, and whether a canonical note already covers it.
Prefer a bounded update or source pointer when the authoritative content lives
elsewhere. Keep checked source/version/date, applicability and limitations.

Do not convert raw transcripts, logs, temporary progress, secrets or untested
hypotheses into factual memory. An explicit request to retain a hypothesis can
preserve it clearly labeled; proactive speculation is not verified learning.
Nothing useful or new means no write, not a forced summary, rating or approval
question. Briefly disclose material captures without adding routine housekeeping
noise to every response. Continue the user's task if memory is unavailable.

## Capture

Before choosing what to store, read the bundled
[authoring and care criteria](../maintain/references/knowledge-care.md).
Find the authoritative home: code-local contracts/runbooks stay in their source
repository; a Space-owned lesson can be native. Choose a useful pointer, an
attributed synthesis or a justified minimal snapshot when the original lives
elsewhere. No reuse/discovery value means no extra note. Explicit preservation
intent is respected; read access alone does not authorize a private-source copy.
Do not create a parallel task log, API manual or repository mirror.

### Check identity before creating

`document import` **always creates a new document**; it is not an upsert by
title, file path or Markdown heading. A `document read` → edit temporary file
→ `document import` round trip creates a second document and changes the source
path. Before a new note, query the selected Space for its distinctive subject
and inspect likely documents, for example:

```sh
obsdog search --space <space-id> --query "<subject or source name>" --actor-type agent --actor <agent-id> --format json
obsdog document list --space <space-id> --format json
obsdog document read --space <space-id> --id <candidate-document-id> --format json
```

Search results are candidates, not proof of absence; a bounded reformulation
or source-path comparison may be needed. If the same canonical answer exists,
read its current revision. For a small correction, use `obsdog block update`
with that block's exact base revision and agent attribution. On CLI v0.2.9+,
`obsdog document update --id <document-id> --base-revision
<document-revision-id> --file <edited-markdown> --reason <reason> --actor-type
agent --actor <agent-id> --space <space-id> --format json` replaces the full
Markdown without creating a second document, provided its block structure is
unchanged. `document rename` changes the stored title independently of the H1.
Use a reviewed care plan for structural change; never re-import an existing
note to "fix" its content or title. Only
when there is no existing canonical note should the new-note import below run.
CLI versions with duplicate protection fail on the same source/content and
report an existing ID; do not bypass that result with `--fork` unless the
user actually intends a distinct document. Read back the **existing or newly
updated** document, not only a newly imported one.

A useful note serves one reader/job with scope, evidence and limitations. Keep
blocks independently revisable but context-complete: retain prerequisites,
warnings and code/table context. Do not atomize sentences or split for a token
quota. Update a canonical answer instead of adding another version as a new
note; route substantial split/merge or retirement to the maintenance workflow.

- Prefer concise canonical Markdown with a descriptive title and source or decision context when available.
- For externally grounded claims, distinguish the current source link from the
  exact checked version/section, observation date/method and applicability.
  Preserve necessary qualifications in the body. Import/edit time is not source
  freshness; a copied source is not another independent confirmation.
- On CLI v0.2.0+, create a genuinely new note with `obsdog document import --space <space-id> --file <file> --actor-type agent --actor <agent-id> --format json`. Check installed help first; do not fall back to default human authorship if attribution flags are absent.
- Treat headings and leaf Markdown regions as stable addressable blocks after import. Do not fabricate block identifiers.
- Read the imported document back and verify its title, block count, and exact Space.
- Suggest labels only after discovering definitions. Agents normally use `--state suggested`, a rationale, and calibrated confidence. Protected verification remains subject to human or disclosed verifier review.
- Put explanations, questions, corrections, and evidence in metadata comments when they should not alter canonical prose.
- Keep current guidance separate from selected historical rationale. Skip routine
  progress chatter; never prune revisions or evaluations as "unnecessary history".
  No new source-role flags, automatic archive filter or retention policy is added.

## Connect relevant knowledge

When recurring specialist notes lack orientation, apply the optional entity
overview in [retrieval-oriented authoring](../maintain/references/retrieval-authoring.md).
Capture a small, sourced introduction and selective question-to-note routes,
not a new document/category for every entity or a keyword-filled hub.

Search the selected Space for an existing note before creating a duplicate. Open
relevant results and, when they genuinely support the new note, cite their real
stable document/block IDs with Markdown links, e.g. `[Related decision](<returned-document-id>)`.
Do not guess IDs from titles. Keep citations proportionate; an isolated note is
better than a fabricated relationship.

For a plausible but unconfirmed connection, inspect `comment list` to avoid
duplicates and use an attributable `question` comment on the exact current block:

```sh
obsdog comment add --space <space-id> --type block --id <block-id> --relation question --body "Possible connection: [Related note](<document-id>). Explain the specific relationship and uncertainty." --actor-type agent --actor <agent-id> --format json
```

Read the comment back. The hosted graph separates current open question-comment
links as opt-in proposals; they do not increase reference strength or node size.
Use `evidence`/`explanation` only for an actual recorded citation with a concrete
reason, not to promote a guess. A link is not a correctness or usefulness rating.

Without an explicit boundary, v0.2.0 can capture into Personal from any directory
without `init`; its first capture lazily creates the local library. Respect an
existing project/Org binding and fail visibly if it is broken. Default selection
does not merge libraries or connect sync. Do not connect sync or import unrelated
files without authorization. Never place credentials, access tokens, or secret
values in remembered content. Keep capture usable without login or network.
