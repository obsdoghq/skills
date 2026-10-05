"""Check private identity mapping and portable resources without real accounts."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from bundle_private import build_bundle, PLUGIN


class PrivateBundleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="obsdog-bundle-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.registered = self.root / "registered"
        (self.registered / ".codex-plugin").mkdir(parents=True)
        (self.registered / ".codex-plugin" / "plugin.json").write_text(json.dumps({
            "name": "dev-fixture", "apps": "./.app.json", "version": "1.0.0",
        }))
        self.app = {"apps": {"fixture": {"id": "asdk_app_fixture"}}}
        self.write_app()

    def write_app(self):
        (self.registered / ".app.json").write_text(json.dumps(self.app))

    def test_preserves_registered_identity_without_extra_connections(self):
        output = self.root / "plugin.zip"
        build_bundle(PLUGIN, self.registered, output, "1.0.1")
        with zipfile.ZipFile(output) as archive:
            manifest = json.loads(archive.read(".codex-plugin/plugin.json"))
            self.assertEqual(manifest["name"], "dev-fixture")
            self.assertEqual(manifest["version"], "1.0.1")
            self.assertEqual(json.loads(archive.read(".app.json")), self.app)
            self.assertNotIn("mcpServers", manifest)
            self.assertNotIn(".mcp.json", archive.namelist())
            self.assertNotIn("mcp.json", archive.namelist())
            self.assertEqual({
                name.split("/")[1] for name in archive.namelist()
                if name.startswith("skills/") and name.endswith("/SKILL.md")
            }, {"find", "remember", "maintain", "documentify"})
            self.assertIn("hooks/session_start.py", archive.namelist())
            self.assertIn("hooks/context.md", archive.namelist())
            self.assertIn(manifest["hooks"][2:], archive.namelist())
            self.assertFalse(any("__pycache__" in p or p.endswith(".pyc")
                                 for p in archive.namelist()))
        with self.assertRaises(FileExistsError):
            build_bundle(PLUGIN, self.registered, output, "1.0.1")

    def test_extra_app_or_credential_fields_are_not_copied(self):
        for app in (
            {"apps": {"fixture": {"id": "asdk_app_fixture", "token": "synthetic"}}},
            {"apps": {"one": {"id": "asdk_app_one"}, "two": {"id": "asdk_app_two"}}},
            {"apps": {"fixture": {"id": "unexpected_provider_fixture"}}},
        ):
            with self.subTest(app=app):
                self.app = app
                self.write_app()
                output = self.root / "rejected.zip"
                with self.assertRaises(ValueError):
                    build_bundle(PLUGIN, self.registered, output, "1.0.1")
                self.assertFalse(output.exists())
