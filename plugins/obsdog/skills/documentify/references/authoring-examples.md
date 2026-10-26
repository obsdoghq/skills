# Worked authoring choices

All names, events and values below are fictional. They illustrate writing
decisions, not live service state or an executable ObsDog API contract.

## Save an unfinished investigation, then revise it

Initial evidence: a test worker reports `LEASE_EXPIRED` after a restart. The
request finished in four seconds; the configured timeout is thirty seconds.

Write now in the existing worker investigation:

> The restart test returned `LEASE_EXPIRED` before the configured timeout.
> Timeout exhaustion is not established. A stale lease after restart is a
> hypothesis. Next, compare the saved lease revision with the revision used by
> the retry. Evidence: the restart test log and worker timeout configuration.

Later evidence: a trace shows the retry reused an old lease revision. A fixture
passes after the retry reads the current revision.

Update the same explanation:

> In the restart fixture, the retry reused an old lease revision and produced
> `LEASE_EXPIRED`. Reading the current revision before retrying fixed that
> fixture. The timeout hypothesis was rejected because the failure occurred
> before the deadline and the trace identified the stale lease. Production
> behavior remains unverified; next, check the same revision transition there.

Keep the original evidence and failed hypothesis reachable. Do not add a second
"timeout solved" note or describe the fixture result as a production deployment.

## Turn a progress log into a current explanation

A fictional release note contains daily messages about build success, signature
failure, a corrected signing setting and a successful staging check.

Keep its current answer short: the staging artifact is verified; production
promotion is pending. Put the current promotion procedure beside its required
signing check. If the troubleshooting chronology is independently useful, move
it through a supported extraction into "Why the staging signature failed".
Preserve the failed setting, evidence and correction there. Link the procedure
to that explanation and leave a summary/link in the former history section.

The acceptance question is whether a reader can both perform the current
procedure and find why the setting changed. A shorter note that loses the
failure evidence is not an improvement.

## Split a block without creating a new document

An onboarding paragraph combines prerequisites, connecting a client and checking
the first response. All three serve one first-use goal and change together.
Use a prerequisites paragraph and an ordered procedure in the same note, with
the expected response next to the final step. Use supported block operations
if the runtime requires them. Three new notes would add navigation cost without
creating independently useful explanations.

## Extract an independently changing question

An "Atlas operations" overview contains service roles, a reusable credential
rotation procedure and an expanding incident history. Rotation now has its own
readers, prerequisites, rollback conditions and release-dependent updates.

Read the overview, rotation material and existing related notes. If no rotation
home exists, extract the coherent rotation section using the supported operation.
The destination opens with who should rotate which fictional credential, under
what conditions, and how success is checked. Move its exceptions, rollback and
source references together. The overview keeps the service roles and a short
"Rotate credentials" summary/link. Update known links and verify both overview
navigation and a direct "Atlas credential rotation" lookup.

Do not also split every individual command, create a new Space, or create a
daily incident page just because the overview has grown.

## Keep a long recovery sequence intact

A restore procedure needs its snapshot compatibility check, restore steps,
validation and rollback decision together. Readers use the whole sequence under
one set of conditions. Keep that procedure intact, use useful headings, and link
its separately maintained architecture background. Do not separate the rollback
warning from the step that can require it to meet a byte target.

## Consolidate without erasing a scope difference

Two cache notes repeat the same current setting for the same environment. Merge
their unique evidence into the canonical home with supported lineage and links.
A third note describes a different cache generation with an incompatible setting;
retain the version distinction and connect it as a variant. A newer import time
does not make its setting correct for every version.

## Repair a miss and check the original question

The question "Why does Atlas reject a renewed lease?" misses an existing note
titled "Worker restart". A follow-up search finds the explanation and trace.
Add the renewal question, `LEASE_EXPIRED`, and the restart condition naturally
to that explanation. Read back the change, rerun the original question and open
the intended answer. A search hit alone does not prove the answer was applied
or that the underlying service was repaired.

## Repair a successful lookup that needed a detour

A fictional task asks why the Atlas worker "loses its job after restart". That
query misses the existing investigation. Searching the log's `LEASE_EXPIRED`
finds it; the current-revision check is explained in a separate retry note.

Update the existing investigation with a direct answer:

> In the restart fixture, the Atlas worker lost its job after restart because
> the retry reused an old lease revision and returned `LEASE_EXPIRED`. Reading
> the current revision before retrying fixed this fixture. Production behavior
> remains unverified. Evidence: the restart trace and corrected fixture result.

Link the retry note with what it explains: "How retries read the current lease
revision". Preserve that note's prerequisites rather than duplicating its whole
procedure. Check the original symptom wording and the observed error term; open
the results and verify that the answer retains its fixture-only scope.

Do not create separate symptom and error pages for the same explanation, invent
additional aliases, or call diagnostic retrieval a successful production fix.
