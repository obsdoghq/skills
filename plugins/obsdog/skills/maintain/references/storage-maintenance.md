# Local storage maintenance

Use CLI v0.2.36+ only after installed help/capability checks. A size report alone
does not authorize cleanup of a user's DB. Keep the selected Space and the user's
actual maintenance scope; local commands are not hosted-policy fallbacks.

`space compact --space SPACE_ID --format json` is a read-only physical inventory
of database/WAL bytes, pages and free-page estimates. For an authorized apply,
keep an accepted backup and choose an idle window, then use `space compact
--space SPACE_ID --apply --format json`. It performs one existing safe bounded
unobserved-snapshot cleanup batch, SQLite VACUUM and a bounded checkpoint attempt.
Read actual before/after sizes and checkpoint status. Readers/writers may defer
checkpoint. Repeating explicit maintenance may be needed for a backlog.

Compaction preserves source history, pinned runs, receipts, schema/floors and
private drafts. VACUUM cannot reclaim live historical rows; retirement preserves
that history. Schema13 sharing requires its separate backed-up transition from12.
Do not activate a new retention policy, delete DB/WAL/shm files, rewrite SQLite,
kill a writer or enable sync to force reclamation. An unexpected integrity error
requires preserving the DB and accepted backup before further writes.

Ordinary reads/edits do not run unrelated snapshot cleanup. General status is a
read-only snapshot; write-readiness is an instantaneous rollback-only probe.
SQLite has one physical writer per DB, even for different documents; revision
checks separately decide conflicting edits. Observe phase/admission diagnostics
and let an owned operation finish/cancel normally. Missing lock age is unknown,
not evidence of corruption or a reason to restart another process.
