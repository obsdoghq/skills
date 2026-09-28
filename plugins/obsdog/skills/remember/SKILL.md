---
name: remember
description: Save durable Markdown knowledge into a selected ObsDog Space with clear provenance and stable block identities. Use when the user asks to remember, capture, import, or preserve knowledge; do not import transient chat content without intent.
---

# Remember with ObsDog

Resolve the target Space and durable intent from the request and existing scope;
ask only if either is materially ambiguous. With capture already authorized, check,
import and read back the note yourself rather than asking for each routine save.
Preserve user-authored wording when supplied; distinguish facts, hypotheses,
decisions and follow-ups rather than silently upgrading certainty.

## Capture

Before choosing what to store, read the bundled
[authoring and care criteria](../maintain/references/knowledge-care.md).
Find the authoritative home: code-local contracts/runbooks stay in their source
repository; a Space-owned lesson can be native. Choose a useful pointer, an
attributed synthesis or a justified minimal snapshot when the original lives
elsewhere. No reuse/discovery value means no extra note. Explicit preservation
intent is respected; read access alone does not authorize a private-source copy.
Do not create a parallel task log, API manual or repository mirror.

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
- On CLI v0.2.0+, import with `obsdog document import --space <space-id> --file <file> --actor-type agent --actor <agent-id> --format json`. Check installed help first; do not fall back to default human authorship if attribution flags are absent.
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
