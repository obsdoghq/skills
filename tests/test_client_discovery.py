"""Guard the default-disabled boundary without connecting to any real Space."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate import verify_client_mcp_boundary


class ClientDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="obsdog-discovery-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.configuration = {"mcpServers": {"obsdog": {"enabled": False}}}
        self.codex = self.configuration

    def test_codex_disabled_claude_without_server(self):
        self.assertIs(verify_client_mcp_boundary(self.root, self.codex, {})["enabled"], False)

    def test_root_auto_discovery_rejected_even_with_disabled_flag(self):
        (self.root / ".mcp.json").write_text(json.dumps(self.configuration), encoding="utf-8")
        with self.assertRaises(AssertionError):
            verify_client_mcp_boundary(self.root, self.codex, {})

    def test_claude_inline_or_file_server_rejected(self):
        for value in ({}, "./.mcp.json"):
            with self.subTest(value=value), self.assertRaises(AssertionError):
                verify_client_mcp_boundary(self.root, self.codex, {"mcpServers": value})

    def test_missing_or_enabled_codex_opt_out_rejected(self):
        for server in ({}, {"enabled": True}, {"enabled": "false"}):
            self.codex["mcpServers"]["obsdog"] = server
            with self.subTest(server=server), self.assertRaises(AssertionError):
                verify_client_mcp_boundary(self.root, self.codex, {})

    def test_unexpected_path_or_server_rejected(self):
        with self.assertRaises(AssertionError):
            verify_client_mcp_boundary(self.root, {"mcpServers": "../other.json"}, {})
        self.configuration["mcpServers"]["extra"] = {"enabled": False}
        with self.assertRaises(AssertionError):
            verify_client_mcp_boundary(self.root, self.codex, {})


if __name__ == "__main__":
    unittest.main()
