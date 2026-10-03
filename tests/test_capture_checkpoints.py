"""Static workflow regressions, not actual host/capture acceptance."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins/obsdog/skills"
REFERENCE = SKILLS / "remember/references/checkpoints.md"


class CaptureCheckpointTests(unittest.TestCase):
    def test_six_distinct_handoff_examples(self):
        text = REFERENCE.read_text()
        for heading in ("Successful hit with new learning", "Repaired search miss", "Pause or input required", "Delegated result", "No-memory or read-only request", "Unavailable atomic preparation"):
            self.assertIn("### " + heading, text)

    def test_skills_route_to_existing_packaged_reference(self):
        for name in ("find", "remember"):
            source = SKILLS / name / "SKILL.md"
            match = re.search(r"\[capture checkpoints\]\(([^)]+)\)", source.read_text())
            self.assertIsNotNone(match)
            self.assertEqual((source.parent / match.group(1)).resolve(), REFERENCE.resolve())

    def test_parent_acceptance_requires_actual_evidence(self):
        text = REFERENCE.read_text()
        self.assertIn("The parent checks the actual receipt and saved content", text)
        self.assertIn("not just \"parent will save\"", text)
        self.assertIn("draft-only", text)
        self.assertIn("saved-readback-pending", text)

    def test_no_memory_does_not_create_private_draft(self):
        section = REFERENCE.read_text().split("### No-memory or read-only request")[1].split("###")[0]
        self.assertIn("Do not save or persist a capture draft.", section)
        self.assertIn("prohibited", section)

    def test_atomic_unavailability_does_not_block_all_capture(self):
        text = REFERENCE.read_text()
        self.assertIn("Ordinary authorized capture must not wait", text)
        self.assertIn("exact target/base revision", text)
        self.assertIn("Revalidate that base", text)
        self.assertIn("Do not substitute re-import", text)

    def test_original_miss_and_unrun_verification_remain_distinct(self):
        text = REFERENCE.read_text()
        self.assertIn("original lookup cue/run", text)
        self.assertIn("supported no-observe diagnostic path", text)
        self.assertIn("not run rather than manufacture observations", text)
        self.assertIn("Static contract tests", text)

    def test_host_guide_uses_compact_handoff_not_new_hooks(self):
        text = (ROOT / "docs/AI_CLIENT_INTEGRATION.md").read_text()
        self.assertIn("## Capture at delegated and interrupted boundaries", text)
        self.assertIn("capture disposition", text)
        self.assertIn("not a new automatic hook", text)


if __name__ == "__main__":
    unittest.main()
