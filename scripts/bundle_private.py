#!/usr/bin/env python3
"""Bundle workflows with one explicitly selected registered OpenAI app."""

from __future__ import annotations

import argparse
import copy
import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "obsdog"


def render_capture_policy(policy: dict, app: dict) -> str:
    """Render bounded owner-supplied preferences, never arbitrary instructions."""
    if not isinstance(policy, dict) or set(policy) != {"schema", "app_id", "space_id", "allow"}:
        raise ValueError("Capture policy requires schema, app_id, space_id and allow")
    if policy["schema"] != "obsdog.private-capture-policy/v1":
        raise ValueError("Unsupported private capture policy schema")
    app_id = next(iter(app["apps"].values()))["id"]
    if policy["app_id"] != app_id:
        raise ValueError("Capture policy must match the existing registered app")
    space = policy["space_id"]
    if not isinstance(space, str) or not re.fullmatch(r"spc_[A-Za-z0-9_-]+", space):
        raise ValueError("Capture policy needs one exact Space ID")
    allowed = policy["allow"]
    if (not isinstance(allowed, list) or not allowed
            or any(not isinstance(value, str) for value in allowed)
            or len(set(allowed)) != len(allowed)
            or not set(allowed) <= {"capture", "maintenance", "feedback"}):
        raise ValueError("Use distinct supported capture policy operations")
    actions = {
        "capture": "Capture established reusable findings and update matching notes during authorized work, without another per-note save request.",
        "maintenance": "Apply ordinary supported, evidence-backed maintenance within the same scope.",
        "feedback": "Record attributable evaluations supported by inspected evidence and real use, without a rating quota.",
    }
    lines = [
        "# Owner-approved standing instructions (private bundle)",
        "",
        "These owner-supplied preferences carry existing authorization; installation alone grants none.",
        f"Use only the existing registered app `{app_id}` and selected Space `{space}` through hosted MCP.",
        "Preserve this selection; an unavailable connection is not permission to switch accounts, Spaces or runtimes.",
        "",
        *["- " + actions[value] for value in ("capture", "maintenance", "feedback") if value in allowed],
        "",
        "Use only sources authorized for the current task. Existing source/upload restrictions, explicit no-memory/read-only requests and later user changes override these preferences. Keep secrets and raw transcripts out. Do not change sync, enroll Spaces or install a local CLI.",
        "Operations not listed here need their own authorization. Server scopes and current capabilities still apply.",
        "",
    ]
    return "\n".join(lines)


def build_bundle(plugin: Path, registered: Path, output: Path, version: str,
                 capture_policy: dict | None = None) -> int:
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise ValueError("Use a three-part plugin version")
    original = json.loads(
        (registered / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    if original.get("apps") != "./.app.json":
        raise ValueError("The selected registered plugin must map ./.app.json")
    name = original.get("name", "")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,127}", name):
        raise ValueError("The registered plugin needs a valid existing name")
    app = json.loads((registered / ".app.json").read_text(encoding="utf-8"))
    if set(app) != {"apps"} or not isinstance(app["apps"], dict) or len(app["apps"]) != 1:
        raise ValueError("Select exactly one registered app mapping")
    for entry in app["apps"].values():
        if not isinstance(entry, dict) or set(entry) != {"id"}:
            raise ValueError("App mappings must contain only the registered ID")
        if not isinstance(entry["id"], str) or not re.fullmatch(
            r"asdk_app_[A-Za-z0-9_-]+", entry["id"]
        ):
            raise ValueError("Use an existing registered OpenAI app ID")

    if (registered / "owner-capture-policy.md").exists() and capture_policy is None:
        raise ValueError("Explicitly supply the reviewed capture policy when updating this private bundle")
    policy_text = render_capture_policy(capture_policy, app) if capture_policy is not None else None

    manifest = copy.deepcopy(json.loads(
        (plugin / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
    ))
    manifest.update(name=name, version=version, apps="./.app.json")
    # The registered hosted app supplies tools and authentication. The private
    # package must not add a local process or a second HTTP OAuth connection.
    manifest.pop("mcpServers", None)
    payloads = {}
    for path in sorted(plugin.rglob("*")):
        if path.is_symlink():
            raise ValueError("Plugin resources must not be symbolic links")
        if not path.is_file():
            continue
        relative = path.relative_to(plugin).as_posix()
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if relative.startswith(".claude-plugin/"):
            continue
        if relative in {".app.json", ".codex-plugin/plugin.json"}:
            continue
        if relative in {".mcp.json", "mcp.json"}:
            raise ValueError("A private registered-app bundle cannot add MCP servers")
        payloads[relative] = path.read_bytes()
    if policy_text is not None:
        payloads["owner-capture-policy.md"] = policy_text.encode("utf-8")
        for relative in list(payloads):
            if relative.startswith("skills/") and relative.endswith("/SKILL.md"):
                text = payloads[relative].decode("utf-8")
                frontmatter, body = text.split("\n---\n", 1)
                routing = ("\nRead the [owner-approved standing instructions](../../owner-capture-policy.md) "
                           "for this private connection before choosing a Space or deciding whether to capture.\n")
                payloads[relative] = (frontmatter + "\n---\n" + routing + body).encode("utf-8")
        payloads["hooks/context.md"] += ("\n" + policy_text).encode("utf-8")
        hook = json.loads(payloads["hooks/codex.json"])
        limit = hook["hooks"]["SessionStart"][0]["hooks"][0]["additionalContextLimit"]
        if len(payloads["hooks/context.md"]) >= limit:
            raise ValueError("Private capture context exceeds the declared hook limit")
    payloads[".codex-plugin/plugin.json"] = (
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    payloads[".app.json"] = (
        json.dumps(app, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as stream:
        output.chmod(0o600)
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, content in sorted(payloads.items()):
                archive.writestr(name, content)
    return len(payloads)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registered-plugin-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--version", required=True)
    parser.add_argument("--capture-policy", type=Path,
                        help="Optional owner-reviewed private policy JSON; never infer permission")
    args = parser.parse_args()
    policy = json.loads(args.capture_policy.read_text(encoding="utf-8")) if args.capture_policy else None
    count = build_bundle(PLUGIN, args.registered_plugin_dir, args.output, args.version, policy)
    print(json.dumps({"output": str(args.output), "files": count, "version": args.version}))


if __name__ == "__main__":
    main()
