"""Check shipped local Markdown routes, not instruction wording or behavior."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote


class ReferenceLinksTest(unittest.TestCase):
    def test_skill_references_resolve_inside_the_distributable_plugin(self):
        plugin = Path(__file__).resolve().parents[1] / "plugins" / "obsdog"
        for document in plugin.rglob("*.md"):
            for link in re.findall(r"\]\(([^\s)]+)\)", document.read_text(encoding="utf-8")):
                if ":" in link or link.startswith("#") or "<" in link or "$" in link:
                    continue
                target = (document.parent / unquote(link.split("#", 1)[0])).resolve()
                with self.subTest(document=document.relative_to(plugin), link=link):
                    self.assertTrue(target.is_relative_to(plugin.resolve()))
                    self.assertTrue(target.is_file(), f"Missing shipped reference: {link}")


if __name__ == "__main__":
    unittest.main()
