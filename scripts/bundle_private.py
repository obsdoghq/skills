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


def build_bundle(plugin: Path, registered: Path, output: Path, version: str) -> int:
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
    args = parser.parse_args()
    count = build_bundle(PLUGIN, args.registered_plugin_dir, args.output, args.version)
    print(json.dumps({"output": str(args.output), "files": count, "version": args.version}))


if __name__ == "__main__":
    main()
