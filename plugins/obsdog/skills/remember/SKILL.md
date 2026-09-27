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

A useful note serves one reader/job with scope, evidence and limitations. Keep
blocks independently revisable but context-complete: retain prerequisites,
warnings and code/table context. Do not atomize sentences or split for a token
quota. Update a canonical answer instead of adding another version as a new
note; route substantial split/merge or retirement to the maintenance workflow.

- Prefer concise canonical Markdown with a descriptive title and source or decision context when available.
- On CLI v0.1.11+, import with `obsdog document import --path <space> --file <file> --actor-type agent --actor <agent-id> --format json`. Check installed help first; do not fall back to default human authorship if attribution flags are absent.
- Treat headings and leaf Markdown regions as stable addressable blocks after import. Do not fabricate block identifiers.
- Read the imported document back and verify its title, block count, and exact Space.
- Suggest labels only after discovering definitions. Agents normally use `--state suggested`, a rationale, and calibrated confidence. Protected verification remains subject to human or disclosed verifier review.
- Put explanations, questions, corrections, and evidence in metadata comments when they should not alter canonical prose.

## Connect relevant knowledge

Search the selected Space for an existing note before creating a duplicate. Open
relevant results and, when they genuinely support the new note, cite their real
stable document/block IDs with Markdown links, e.g. `[Related decision](<returned-document-id>)`.
Do not guess IDs from titles. Keep citations proportionate; an isolated note is
better than a fabricated relationship.

For a plausible but unconfirmed connection, inspect `comment list` to avoid
duplicates and use an attributable `question` comment on the exact current block:

```sh
obsdog comment add --path <space> --type block --id <block-id> --relation question --body "Possible connection: [Related note](<document-id>). Explain the specific relationship and uncertainty." --actor-type agent --actor <agent-id> --format json
```

Read the comment back. The hosted graph separates current open question-comment
links as opt-in proposals; they do not increase reference strength or node size.
Use `evidence`/`explanation` only for an actual recorded citation with a concrete
reason, not to promote a guess. A link is not a correctness or usefulness rating.

Without an explicit boundary, v0.1.11 can capture into Personal from any directory
without `init`; its first capture lazily creates the local library. Respect an
existing project/Org binding and fail visibly if it is broken. Default selection
does not merge libraries or connect sync. Do not connect sync or import unrelated
files without authorization. Never place credentials, access tokens, or secret
values in remembered content. Keep capture usable without login or network.
