#!/usr/bin/env python3
"""Validate ObsDog plugin packaging and authorization boundaries."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "obsdog"
EXPECTED_SKILLS = {"find", "remember", "maintain", "report", "documentify"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    codex = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    claude = load_json(PLUGIN / ".claude-plugin" / "plugin.json")
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    mcp = load_json(PLUGIN / ".mcp.json")["mcpServers"]["obsdog"]

    assert codex["name"] == claude["name"] == "obsdog"
    assert codex["version"] == claude["version"]
    assert marketplace["name"] == "obsdog-skills"
    assert marketplace["plugins"][0]["source"]["path"] == "./plugins/obsdog"
    claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    assert claude_marketplace["plugins"][0]["version"] == codex["version"]
    assert mcp["enabled"] is False
    assert mcp["command"] == "obsdog"
    assert mcp["args"] == ["mcp", "--path", "."]
    assert mcp["env_vars"] == ["PATH"]

    skill_directories = {
        path.name for path in (PLUGIN / "skills").iterdir() if path.is_dir()
    }
    assert skill_directories == EXPECTED_SKILLS
    for name in EXPECTED_SKILLS:
        text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        assert f"name: {name}\n" in text
        assert "[TODO:" not in text
        assert "Space" in text
        prompt = (PLUGIN / "skills" / name / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )
        assert f"${name}" in prompt

    repository_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in PLUGIN.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ).lower()
    for forbidden in ("api_key=", "access_token=", "bearer ey", "private_key="):
        assert forbidden not in repository_text

    print("ObsDog skills packaging and authorization-boundary checks passed.")


if __name__ == "__main__":
    main()
