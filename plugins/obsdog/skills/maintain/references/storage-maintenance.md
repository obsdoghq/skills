# Local storage maintenance

Use CLI v0.2.36+ only after installed help/capability checks. A size report alone
does not authorize cleanup of a user's DB. Keep the selected Space and the user's
actual maintenance scope; local commands are not hosted-policy fallbacks.

`space compact --space SPACE_ID --format json` is a read-only physical inventory
of database/WAL bytes, pages and sampled freelist bytes. For an authorized apply,
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

Command elapsed time is wall time. Admission budget is the allowance at that
operation's entry; attempts show actual reservation waits/backoff, including on
success. Prior admission spent is already included in command elapsed time.
Phases can overlap, so do not sum them as exclusive durations. A budget is not
an ETA. Each long-lived MCP request gets a fresh allowance. Search/open known
prewrite refusal returns real content with `not_recorded` and exact `next_read`.
Other local MCP errors carry `obsdog.mcp-error/v1`, `error_code`, `message` and
diagnostics in structuredContent and omit the normal `result`. Never interpret
an error as no matching knowledge or call use/evaluation on an unopened result.

## Sampled sizes and backup coverage (CLI v0.2.39+)



space compact is a read-only preview unless --apply is passed. Its
reclaimable_free_page_bytes is exactly page_size * free_pages: a sampled freelist,
not a forecast of VACUUM savings or runtime. Zero freelist does not mean zero
unused bytes inside allocated pages. Database growth alone does not prove that
growth can be reclaimed.

The apply sequence is before sample, one bounded eligible unobserved-snapshot
cleanup, after_snapshot_cleanup sample, VACUUM, checkpoint and after sample.
Cleanup may free pages not counted by before. Concurrent sessions and checkpoint
timing can change database/WAL sizes between samples. Separate previews are not
reserved plans. Samples include sampled_at; duration_estimate_status=not_estimated
and vacuum_savings_estimate_status is explicitly unknown. Use actual timings to
plan later maintenance under similar conditions, without treating them as an ETA.

```sh
obsdog space compact --space SPACE_ID --storage-details --format json
```

This opt-in read-only dbstat scan has a 2s budget and at most 1024 object rows.
Check storage_details.complete/status. Allocated, payload and unused page bytes
are shown per B-tree/table/index with categorized totals. This is metadata,
not document contents. The categories group object names and do not allocate
each byte to a user action. Freelist, WAL and file length are separate; partial/
unavailable is unknown rather than zero. Unused page bytes are not guaranteed
VACUUM savings.

Do not VACUUM repeatedly just because a DB is large. Inspect the object breakdown:
live history, frozen/pinned snapshots and retained observations cannot all be
freed by physical compaction. Where installed help supports it, history retention
without --apply previews its existing policy; applying/preparing retention is a
separate explicit operation with compatibility and recovery consequences.
This release does not silently shorten retention or delete authored history.
Keep an accepted backup and use an idle window for an authorized compact --apply.

## Compare like-for-like backup bytes

space backup creates a ZIP/DEFLATE archive with manifest.json and an internally
consistent retained SQLite database from VACUUM INTO. All database-resident
tables, indexes, snapshots, events and retained history are copied. It is not a
current-document-only export. Archive bytes and compressed DB entry bytes can
be much smaller than database_uncompressed_bytes or the live file. This is not
evidence of lost history or a DB leak. A same-time internal DB/object comparison
is needed to explain a particular gap.

```sh
obsdog --timeout 5m space backup --space SPACE_ID --output NEW_BACKUP   --include-drafts --format json
```

The default backup omits private capture-drafts and correction-drafts. The explicit
--include-drafts option copies those two trees and a versioned SHA256/size inventory.
It detects changed file sets/content during copying and refuses symlinks/special
files. Stop all writers using that profile first: the DB and draft files are
not one atomic cross-file snapshot, and rechecks cannot prove absence of every
race. Limits: 10000 files, 64MiB per draft file and 512MiB combined. Failures remove
the new incomplete archive; an existing output is never overwritten.

Both modes omit profile identity, authentication material and dashboard runtime
controls. Database replica/history metadata is retained; restoration does not
authenticate or enroll a device. This is a Space data backup, not an authenticated
profile clone. Preserve it privately. Never publish draft contents or credentials.

## Restore privately without overwriting a library

Restore supports old DB-only archives and the new draft-bearing format; old CLIs
may reject draft-bearing archives. It validates paths, counts, sizes, hashes,
SQLite integrity and existing recovery constraints before publishing a fresh
Space. It refuses an already existing destination and does not erase a current
profile or select a new Personal Space.

```sh
# Use a NEW private recovery profile and an already accepted backup.
OBSDOG_HOME=NEW_RECOVERY_PROFILE obsdog --timeout 5m space restore   --backup BACKUP --format json
```

The default uncompressed DB entry limit remains 2GiB. For an intentionally larger
accepted backup, explicitly pass --max-database-bytes BYTES, up to 68719476736
(64GiB), and ensure adequate disk space. This option does not raise draft limits.
Restored drafts keep original IDs/actors/revision bases; inspect before recovery.
No sync, automatic draft replay, credential restoration or existing-file overwrite
is performed.
