# Test a private connected ObsDog plugin

Keep the four workflows together. A private package contains:

```text
.codex-plugin/plugin.json  Existing private plugin name, new version
.app.json                 Exact existing registered app mapping
skills/find/              Search and apply context
skills/remember/          Authorized capture and updates
skills/maintain/          Supported care and proposals
skills/documentify/       Source investigation and connected explanations
hooks/codex.json          Optional local Codex SessionStart command
hooks/session_start.py    Static context reader
hooks/context.md          Short routing guidance
```

The existing registered app supplies its remote MCP tools and OAuth connection.
The bundle adds no local MCP process or second HTTP OAuth connection. It does
not include credentials or grant access to another Space. This is a private
test path, not public marketplace publication.

## Build from an existing registration

First connect and register the intended ObsDog app in a supported client. Select
the installed private plugin directory whose manifest references `./.app.json`.
Inspect that exact app mapping; do not substitute a plugin ID for a registered
app ID or select an unrelated connected app. Keep all real mappings and output
archives outside this public repository.

Validate the source, then build a new version into a private output location:

```sh
python3 scripts/validate.py
python3 scripts/bundle_private.py \
  --registered-plugin-dir <existing-private-plugin-directory> \
  --output <private-output-zip> \
  --version <new-three-part-version>
```

The bundler copies exactly one ID-only app mapping, preserves the registered
plugin's technical name, adds the four workflows and hook, and removes the
public package's disabled local MCP declaration. It rejects symlinks, extra
app mappings and credential fields. Output is created once with private file
permissions; an existing archive is not overwritten. Real IDs do not enter
the source manifest or Git history.

Upload the ZIP as a new version of that same personal plugin using the client's
supported version-upload flow. Confirm the accepted version, four skills and
existing app connection. If a client does not offer this flow, use its documented
private plugin builder; do not claim a source checkout is already installed.

## Optional owner-approved capture preferences

A plugin-only installation can carry existing owner-approved capture preferences
without a second local skill or AGENTS.md snippet. This is optional, private
operator configuration, not consent inferred from installation, OAuth scopes,
an allow-actions setting or a retrieved note. Only supply it when the owner
has authorized these operations and the selected hosted Space/upload scope.

Keep a reviewed JSON file outside this public checkout:

```json
{
  "schema": "obsdog.private-capture-policy/v1",
  "app_id": "asdk_app_FROM_REGISTRATION",
  "space_id": "spc_FROM_OWNER_SELECTION",
  "allow": ["capture", "maintenance", "feedback"]
}
```

Pass it with `--capture-policy <private-policy-json>` to the bundler. Choose only
the authorized operations; feedback is separate from capture. The bundler checks
the app binding and allowed fields, renders fixed bounded instructions, links
them from all four skill entrypoints, and includes them in the optional static
Codex context. It rejects arbitrary instruction fields and an oversized hook
context. Existing user restrictions override the preferences. The server still
enforces access and capabilities; this file is not an access token.

When updating a package that already contains `owner-capture-policy.md`, explicitly
provide its reviewed policy source again. The bundler refuses to silently drop
it. Change or remove standing preferences only at the owner's direction. Ordinary
updates within unchanged authorization need no fresh per-note consent.

The four skills can read the same packaged preference in clients without command
hooks, but package presence does not prove a host loaded it. Check actual skill
selection and the interpreted scope on each host. Never turn a generic public
package into a grant of permission for all users.

## Check each client separately

In ChatGPT, select the installed plugin for a harmless read-only task. Confirm
the skill actually loads and uses the connected app's search/open tools. The
same account's dots can use supported installed/enabled plugins with their
connections and permissions; verify with an explicitly instructed task rather
than assuming every dot has invoked it.

In local Codex, confirm the updated package is discovered in a fresh session.
Review the actual hook command and its packaged context in the client's hook
trust flow before running it. The hook adds guidance without editing AGENTS.md.
It requires `python3` on a POSIX client; native Windows hook operation has not
been qualified. ChatGPT and dots do not execute this personal command hook.

For authorized remote writes, use a bounded note or block update, inspect the
actual receipt and read the accepted exact revision back. Preserve request
identity after an uncertain response and use receipt lookup before retrying.
Capability or policy refusal does not authorize a CLI fallback.

Record package validation, upload, client discovery, hook trust, actual skill
invocation and read/write acceptance as distinct outcomes. Passing one does not
prove the others. No-memory/read-only tasks remain read-only; installing or
testing the hook never starts transcript capture, sync or background jobs.

Compare the uploaded archive's manifest version and workflow bytes with the
client-managed installed package. Do not patch a versioned cache to simulate an
update. A running chat can retain old instructions; verify a fresh invocation
when available and report that layer as unverified otherwise.

## References

- [Official plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Skill selection and loading](https://developers.openai.com/plugins/build/skills)
- [Hook support and trust review](https://learn.chatgpt.com/docs/hooks)
- [dots app and computer support](https://learn.chatgpt.com/docs/dots/computers-and-apps)
