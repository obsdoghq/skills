---
name: remember
description: Save durable Markdown knowledge into a selected ObsDog Space with clear provenance and stable block identities. Use when the user asks to remember, capture, import, or preserve knowledge; do not import transient chat content without intent.
---

# Remember with ObsDog

Confirm the target Space and what should become durable. Preserve user-authored wording when supplied; distinguish facts, hypotheses, decisions, and follow-ups rather than silently upgrading certainty.

## Capture

- Prefer concise canonical Markdown with a descriptive title and source or decision context when available.
- Import a prepared file with `obsdog document import --path <space> --file <file> --actor <id> --format json` using the installed help as the contract. The current import surface records human authorship; do not relabel agent-authored prose as human-authored without review.
- Treat headings and leaf Markdown regions as stable addressable blocks after import. Do not fabricate block identifiers.
- Read the imported document back and verify its title, block count, and exact Space.
- Suggest labels only after discovering definitions. Agents normally use `--state suggested`, a rationale, and calibrated confidence. Protected verification remains subject to human or disclosed verifier review.
- Put explanations, questions, corrections, and evidence in metadata comments when they should not alter canonical prose.

Do not initialize a Space, connect sync, or import unrelated repository files unless requested. Never place credentials, access tokens, or secret values in remembered content. Keep local capture functional without login or network access.
