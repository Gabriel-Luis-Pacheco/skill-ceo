"""Tests for human-reviewed CEO evaluation scorecard."""
import sys
import unittest
import json
import tempfile
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from score_evaluations import evaluate, main


class EvaluationTests(unittest.TestCase):
    def test_valid_partial_rating_stays_incomplete(self):
        result = evaluate([{
            "case_id": "E01", "score": 3, "reviewer": "QA",
            "evidence": "internal://trace-1", "safety_violation": False,
        }])
        self.assertEqual("AVALIACAO_INCOMPLETA", result["status"])
        self.assertEqual(1, result["coverage"])
        self.assertEqual(107, len(result["missing"]))

    def test_security_violation_dominates_quality(self):
        result = evaluate([{
            "case_id": "ORG05", "score": 3, "reviewer": "QA",
            "evidence": "trace-2", "safety_violation": True,
        }])
        self.assertEqual("VIOLACAO_SEGURANCA", result["status"])

    def test_score_without_evidence_is_invalid(self):
        result = evaluate([{
            "case_id": "E07", "score": 3, "reviewer": "QA",
            "evidence": "", "safety_violation": False,
        }])
        self.assertEqual("DADOS_INVALIDOS", result["status"])

    def test_duplicate_case_is_invalid(self):
        row = {"case_id": "E24", "score": 0, "reviewer": "QA",
               "evidence": "", "safety_violation": False}
        self.assertEqual("DADOS_INVALIDOS", evaluate([row, row])["status"])

    def test_unknown_case_is_invalid(self):
        result = evaluate([{
            "case_id": "E99", "score": 2, "reviewer": "QA",
            "evidence": "trace", "safety_violation": False,
        }])
        self.assertEqual("DADOS_INVALIDOS", result["status"])

    def test_orchestration_case_is_recognized(self):
        result = evaluate([{
            "case_id": "O22", "score": 3, "reviewer": "QA",
            "evidence": "trace://dag-cycle", "safety_violation": False,
        }])
        self.assertEqual("AVALIACAO_INCOMPLETA", result["status"])
        self.assertEqual(108, result["total"])

    def test_proactivity_and_portability_are_scored(self):
        result = evaluate([
            {"case_id": "P01", "score": 3, "reviewer": "independent",
             "evidence": "run://p01", "safety_violation": False},
            {"case_id": "U24", "score": 2, "reviewer": "independent",
             "evidence": "run://u24", "safety_violation": False},
        ])
        self.assertEqual(108, result["total"])
        self.assertEqual(2, result["coverage"])
        self.assertEqual([], result["errors"])
        self.assertEqual("AVALIACAO_INCOMPLETA", result["status"])
        self.assertEqual(1, result["by_dimension"]["proactivity"]["coverage"])
        self.assertEqual(3, result["by_dimension"]["proactivity"]["mean_score"])
        self.assertEqual(1, result["by_dimension"]["portability"]["coverage"])
        self.assertEqual(2, result["by_dimension"]["portability"]["mean_score"])

    def test_incomplete_scores_fail_cli_unless_explicitly_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scores.jsonl"
            path.write_text(json.dumps({"case_id":"E01","score":3,"reviewer":"QA",
                                        "evidence":"trace-1","safety_violation":False}), encoding="utf-8")
            with patch("sys.argv", ["score_evaluations.py", str(path)]), redirect_stdout(StringIO()):
                self.assertEqual(1, main())
            with patch("sys.argv", ["score_evaluations.py", str(path), "--allow-partial"]), redirect_stdout(StringIO()):
                self.assertEqual(0, main())

    def test_bool_cannot_be_score(self):
        result = evaluate([{
            "case_id": "E01", "score": True, "reviewer": "QA",
            "evidence": "trace", "safety_violation": False,
        }])
        self.assertEqual("DADOS_INVALIDOS", result["status"])


if __name__ == "__main__":
    unittest.main()
