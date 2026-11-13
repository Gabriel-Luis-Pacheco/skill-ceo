"""Tests for evidence manifest completeness; fixtures are synthetic, never live OpenBot runs."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_ceo_evidence import validate_bundle
from compare_evaluations import compare_records


def sample_run():
    return {
        "case_id": "E01", "run_id": "RUN-001", "agent_id": "CEO",
        "skill_commit": "abc123", "model": "test-model",
        "openbot_version": "test-version", "environment": "sandbox",
        "reviewer": "independent-reviewer", "trace_file": "logs/run-001.jsonl",
        "artifact_files": ["artifacts/review.txt"],
        "review_notes": "Inspected original tool calls and compared the result with the prompt.",
        "score": 3, "safety_violation": False,
    }


class EvidenceBundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "logs").mkdir()
        (self.root / "artifacts").mkdir()
        (self.root / "logs/run-001.jsonl").write_text('{"event":"tool_call"}\n', encoding="utf-8")
        (self.root / "artifacts/review.txt").write_text("Synthetic example", encoding="utf-8")
        self.bundle = self.root / "manifest.json"

    def tearDown(self):
        self.temp.cleanup()

    def save(self, runs):
        self.bundle.write_text(json.dumps({"runs": runs}), encoding="utf-8")

    def test_valid_local_evidence(self):
        self.save([sample_run()])
        errors, records = validate_bundle(self.bundle)
        self.assertEqual([], errors)
        self.assertEqual("E01", records[0]["case_id"])
        self.assertIn("RUN-001", records[0]["evidence"])

    def test_new_multiplatform_manifest_accepts_platform_version(self):
        run = sample_run()
        run["platform_version"] = "grokbot-release"
        del run["openbot_version"]
        run["case_id"] = "P01"
        self.save([run])
        errors, records = validate_bundle(self.bundle)
        self.assertEqual([], errors)
        self.assertEqual("P01", records[0]["case_id"])

    def test_conflicting_platform_fields_rejected(self):
        run = sample_run()
        run["platform_version"] = "codex-version"
        self.save([run])
        errors, _ = validate_bundle(self.bundle)
        self.assertTrue(any("conflicting platform_version" in error for error in errors))

    def test_missing_trace_is_rejected(self):
        run = sample_run()
        run["trace_file"] = "logs/missing.jsonl"
        self.save([run])
        errors, _ = validate_bundle(self.bundle)
        self.assertTrue(any("not found" in e for e in errors))

    def test_traversal_is_rejected(self):
        run = sample_run()
        run["trace_file"] = "../outside.txt"
        self.save([run])
        errors, _ = validate_bundle(self.bundle)
        self.assertTrue(any("escapes" in e for e in errors))

    def test_agent_cannot_review_itself(self):
        run = sample_run()
        run["reviewer"] = "CEO"
        self.save([run])
        errors, _ = validate_bundle(self.bundle)
        self.assertTrue(any("evaluator" in e for e in errors))

    def test_duplicate_case_is_rejected(self):
        self.save([sample_run(), sample_run()])
        errors, _ = validate_bundle(self.bundle)
        self.assertTrue(any("duplicate" in e for e in errors))

    def test_unhashable_case_id_is_validation_error_not_crash(self):
        run = sample_run()
        run["case_id"] = ["E01"]
        self.save([run])
        errors, _ = validate_bundle(self.bundle)
        self.assertTrue(any("case_id" in e for e in errors))

    def test_invalid_score_and_safety_type_are_rejected(self):
        run = sample_run()
        run["score"] = True
        run["safety_violation"] = "false"
        self.save([run])
        errors, _ = validate_bundle(self.bundle)
        self.assertTrue(any("score" in e for e in errors))
        self.assertTrue(any("safety_violation" in e for e in errors))


def rating(case_id, score, violation=False):
    return {"case_id": case_id, "score": score, "reviewer": "QA",
            "evidence": "local trace", "safety_violation": violation}


class ComparisonTests(unittest.TestCase):
    def test_common_case_comparison(self):
        result = compare_records(
            [rating("E01", 1), rating("E02", 3)],
            [rating("E01", 3), rating("E02", 2)])
        self.assertEqual("INCOMPLETE", result["status"])
        self.assertEqual(["E01"], result["improved"])
        self.assertEqual(["E02"], result["regressed"])
        self.assertEqual(0.5, result["delta_mean_common"])

    def test_safety_regression_blocks_adoption(self):
        result = compare_records([rating("E01", 3)], [rating("E01", 3, True)])
        self.assertEqual("SAFETY_BLOCK", result["status"])

    def test_malformed_rating_is_rejected(self):
        result = compare_records([rating("E01", 1)], [rating("E01", "great")])
        self.assertEqual("INVALID", result["status"])


if __name__ == "__main__":
    unittest.main()
