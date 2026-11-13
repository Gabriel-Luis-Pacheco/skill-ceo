"""Static evaluator tests, not proof of a host's real invocation behavior."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from score_skill_routing import load_jsonl, score_routing, CASES


class RoutingTests(unittest.TestCase):
    def test_complete_perfect_observations(self):
        cases = load_jsonl(CASES)
        observations = [{"id": c["id"], "activated": c["should_activate"],
                         "evidence": "trace://case"} for c in cases]
        result = score_routing(cases, observations)
        self.assertEqual("COMPLETE", result["status"])
        self.assertEqual(1, result["precision"])
        self.assertEqual(1, result["recall"])

    def test_false_positives_and_negatives_are_visible(self):
        cases = load_jsonl(CASES)
        observations = [{"id": c["id"], "activated": c["should_activate"],
                         "evidence": "trace://case"} for c in cases]
        observations[0]["activated"] = False
        observations[-1]["activated"] = True
        result = score_routing(cases, observations)
        self.assertEqual(1, result["false_negative"])
        self.assertEqual(1, result["false_positive"])
        self.assertLess(result["precision"], 1)
        self.assertLess(result["recall"], 1)

    def test_missing_is_incomplete_and_no_fake_pass(self):
        result = score_routing(load_jsonl(CASES), [])
        self.assertEqual("INCOMPLETE", result["status"])
        self.assertEqual(0, result["coverage"])


if __name__ == "__main__":
    unittest.main()
