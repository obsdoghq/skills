---
name: remember
description: Save durable Markdown knowledge into a selected ObsDog Space with clear provenance and stable block identities. Use when the user asks to remember, capture, import, or preserve knowledge; do not import transient chat content without intent.
---

# Remember with ObsDog

Confirm the target Space and what should become durable. Preserve user-authored wording when supplied; distinguish facts, hypotheses, decisions, and follow-ups rather than silently upgrading certainty.

## Capture

- Prefer concise canonical Markdown with a descriptive title and source or decision context when available.
- On CLI v0.1.11+, import with `obsdog document import --path <space> --file <file> --actor-type agent --actor <agent-id> --format json`. Check installed help first; do not fall back to default human authorship if attribution flags are absent.
- Treat headings and leaf Markdown regions as stable addressable blocks after import. Do not fabricate block identifiers.
- Read the imported document back and verify its title, block count, and exact Space.
- Suggest labels only after discovering definitions. Agents normally use `--state suggested`, a rationale, and calibrated confidence. Protected verification remains subject to human or disclosed verifier review.
- Put explanations, questions, corrections, and evidence in metadata comments when they should not alter canonical prose.

Without an explicit boundary, v0.1.11 can capture into Personal from any directory
without `init`; its first capture lazily creates the local library. Respect an
existing project/Org binding and fail visibly if it is broken. Default selection
does not merge libraries or connect sync. Do not connect sync or import unrelated
files without authorization. Never place credentials, access tokens, or secret
values in remembered content. Keep capture usable without login or network.
