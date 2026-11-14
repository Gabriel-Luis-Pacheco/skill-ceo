"""Regressão estática da biblioteca de competência executiva; não mede comportamento do agente."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ExecutiveKnowledgeTests(unittest.TestCase):
    def test_modules_exist_and_are_routed(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for idx in range(36, 46):
            matches = list((ROOT / "references").glob(f"{idx:02d}-*.md"))
            self.assertEqual(len(matches), 1, f"referência {idx} ausente ou ambígua")
            self.assertIn("references/" + matches[0].name, skill)
            self.assertGreater(len(matches[0].read_text(encoding="utf-8")), 500)

    def test_books_are_distinct_catalog_entries(self):
        doc = (ROOT / "references/42-biblioteca-executiva-auditavel.md").read_text(encoding="utf-8")
        ids = re.findall(r"(?m)^\| (B\d{2}) \|", doc)
        self.assertEqual(ids, [f"B{i:02d}" for i in range(1, 51)])
        self.assertIn("Não é comprovação de leitura integral", doc)

    def test_research_and_eval_coverage(self):
        research = (ROOT / "research/CEO-CSUITE-PESQUISA-E-FONTES-2026-11-14.md").read_text(encoding="utf-8")
        evals = (ROOT / "tests/CEO-CSUITE-COMPETENCY-EVALS.md").read_text(encoding="utf-8")
        ids = re.findall(r"(?m)^\| (XC\d{2}) \|", evals)
        self.assertEqual(ids, [f"XC{i:02d}" for i in range(1, 17)])
        for idx in range(36, 46):
            self.assertIn(f"../references/{idx:02d}-", research)
        self.assertIn("POLICY.md", (ROOT / "SKILL.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
