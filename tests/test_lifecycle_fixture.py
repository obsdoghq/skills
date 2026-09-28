"""Fixture integrity only; these tests do not measure agent behavior."""

import json
from pathlib import Path
import unittest


class LifecycleFixtureTest(unittest.TestCase):
    def test_cases_are_synthetic_and_explicitly_unevaluated(self):
        path = Path(__file__).parent / "fixtures" / "knowledge-lifecycle.json"
        fixture = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(fixture["schema"], "obsdog.skill-lifecycle-cases/v1")
        self.assertTrue(fixture["synthetic"])
        self.assertEqual(fixture["status"], "authored-not-behaviorally-evaluated")
        cases = fixture["cases"]
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertEqual({case["phase"] for case in cases}, {"entry", "completion"})
        decisions = {"entry": {"recall", "skip", "reuse", "defer"},
                     "completion": {"create", "update", "pointer", "skip", "defer"}}
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["prompt"].strip())
                self.assertTrue(case["context"].strip())
                expected = case["expected"]
                self.assertIn(expected["decision"], decisions[case["phase"]])
                required = expected["required_actions"]
                forbidden = expected["forbidden_actions"]
                self.assertTrue(required)
                self.assertTrue(forbidden)
                self.assertEqual(len(set(required)), len(required))
                self.assertEqual(len(set(forbidden)), len(forbidden))
                self.assertFalse(set(required) & set(forbidden))
                self.assertTrue(expected["rationale"].strip())
                if case["phase"] == "completion" and expected["decision"] in {"create", "update", "pointer"}:
                    self.assertIn("check_duplicates", required)
                    self.assertIn("readback", required)


if __name__ == "__main__":
    unittest.main()
