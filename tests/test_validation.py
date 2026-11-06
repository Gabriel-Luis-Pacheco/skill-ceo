"""Mutation/regression tests for the structural validator (not CEO behavior)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_skill as skill_validator


class ValidatorTests(unittest.TestCase):
    def test_quota_is_rejected(self):
        self.assertTrue(skill_validator.check_quotas(
            "Crie no máximo 18 agentes ativos.", "sample"
        ))
        self.assertTrue(skill_validator.check_quotas(
            "Só até 3 frentes estratégicas.", "sample"
        ))

    def test_dynamic_organization_is_not_a_quota(self):
        self.assertEqual([], skill_validator.check_quotas(
            "CEO decide quantos agentes criar conforme o orçamento delegado.", "sample"
        ))

    def test_missing_and_escaping_markdown_links(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text(
                "[Guia](missing.md)\n[Escapar](../../outside.md)\n"
                "[Ok](https://openbot.run)\n", encoding="utf-8"
            )
            problems = skill_validator.check_local_links(root)
            self.assertEqual(2, len(problems))

    def test_valid_local_markdown_link(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "POLICY.md").write_text("# Policy", encoding="utf-8")
            (root / "README.md").write_text(
                "[Política](POLICY.md)\n", encoding="utf-8"
            )
            self.assertEqual([], skill_validator.check_local_links(root))

    def test_jsonl_duplicate_and_missing_ids(self):
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / "cases.jsonl"
            row = {"id": "E01", "input": "x", "expected": "y", "bad_pattern": "z"}
            file.write_text(
                json.dumps(row) + "\n" + json.dumps(row) + "\n",
                encoding="utf-8",
            )
            errors = skill_validator.check_jsonl(
                file, ("id", "input", "expected", "bad_pattern"), {"E01", "E02"}
            )
            self.assertTrue(any("duplicado" in e for e in errors))
            self.assertTrue(any("faltando" in e for e in errors))

    def test_invalid_schema(self):
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / "cases.jsonl"
            file.write_text('{"id":"E01","input":"x"}\n', encoding="utf-8")
            self.assertTrue(skill_validator.check_jsonl(
                file, ("id", "input", "expected", "bad_pattern"), {"E01"}
            ))

    def test_repository_static_checks(self):
        self.assertEqual([], skill_validator.validate(), "Current files must pass integrity checks")


if __name__ == "__main__":
    unittest.main()
