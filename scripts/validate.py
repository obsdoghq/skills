#!/usr/bin/env python3
"""Validate ObsDog plugin packaging and authorization boundaries."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from check_public_content import audit


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "obsdog"
EXPECTED_SKILLS = {"find", "remember", "maintain", "report", "documentify"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def verify_client_mcp_boundary(plugin: Path, codex: dict, claude: dict) -> dict:
    """Do not expose Codex opt-out flags to Claude's automatic discovery."""
    assert not (plugin / ".mcp.json").exists(), "Root MCP config is auto-loaded by Claude"
    assert "mcpServers" not in claude, "Claude must remain CLI-only by default"
    servers = codex.get("mcpServers")
    assert isinstance(servers, dict), "Codex MCP must be isolated inside its manifest"
    assert set(servers) == {"obsdog"}
    mcp = servers["obsdog"]
    assert mcp.get("enabled") is False, "Codex MCP must remain disabled by default"
    return mcp


def verify_live_mcp_boundary(mcp: dict) -> None:
    """Execute the declared command through a harmless stub and inspect scope."""
    with tempfile.TemporaryDirectory(prefix="obsdog-mcp-boundary-") as temporary:
        root = Path(temporary)
        selected_space = root / "selected-space"
        selected_space.mkdir()
        binary_dir = root / "bin"
        binary_dir.mkdir()
        capture = root / "capture.json"
        stub = binary_dir / "obsdog"
        stub.write_text(
            f"#!{sys.executable}\n"
            "import json, os, sys\n"
            f"open({str(capture)!r}, 'w', encoding='utf-8').write(json.dumps({{"
            "'argv': sys.argv[1:], 'cwd': os.getcwd(), 'env': sorted(os.environ)}))\n",
            encoding="utf-8",
        )
        stub.chmod(0o700)

        declared_environment = {name: str(binary_dir) for name in mcp["env_vars"]}
        completed = subprocess.run(
            [mcp["command"], *mcp["args"]],
            cwd=selected_space,
            env=declared_environment,
            check=False,
            capture_output=True,
            text=True,
            timeout=mcp["startup_timeout_sec"],
        )
        assert completed.returncode == 0, completed.stderr
        observed = json.loads(capture.read_text(encoding="utf-8"))
        assert observed["argv"] == ["mcp", "--space", "personal"]
        assert Path(observed["cwd"]).resolve() == selected_space.resolve()
        assert set(observed["env"]).issubset(
            {"PATH", "LC_CTYPE", "__CF_USER_TEXT_ENCODING"}
        ), observed
        assert "OBSDOG_SYNC_TOKEN" not in observed["env"]


def main() -> None:
    codex = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    claude = load_json(PLUGIN / ".claude-plugin" / "plugin.json")
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    mcp = verify_client_mcp_boundary(PLUGIN, codex, claude)

    assert codex["name"] == claude["name"] == "obsdog"
    assert codex["version"] == claude["version"]
    assert marketplace["name"] == "obsdog-skills"
    assert marketplace["plugins"][0]["source"]["path"] == "./plugins/obsdog"
    claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    assert claude_marketplace["plugins"][0]["version"] == codex["version"]
    assert mcp["enabled"] is False
    assert mcp["command"] == "obsdog"
    assert mcp["args"] == ["mcp", "--space", "personal"]
    assert "cwd" not in mcp, "The plugin directory must not select a Space"
    assert mcp["env_vars"] == ["PATH"]
    verify_live_mcp_boundary(mcp)

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
    for forbidden in ("api_key=", "access_token=", "bearer ey", "private_key=", "--path", "obsdog init"):
        assert forbidden not in repository_text

    problems, _, _ = audit(ROOT, [], False, [])
    for path, line, rule in problems:
        print(f"{path}:{line}: {rule} (matched value omitted)", file=sys.stderr)
    assert not problems, "Distributable content contains non-public information"

    subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests"], cwd=ROOT, check=True)

    print("ObsDog skills packaging and authorization-boundary checks passed.")


if __name__ == "__main__":
    main()
