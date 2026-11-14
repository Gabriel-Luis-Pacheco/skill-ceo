"""Static regressions for organic growth references; not an agent behavior test."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [
    "references/36-seo-tecnico-indexacao-semantic-search.md",
    "references/37-geo-aeo-ai-search-plataformas.md",
    "references/38-demanda-topical-conteudo-e-autoridade.md",
    "references/39-copywriting-cro-distribuicao-e-marca.md",
    "references/40-mensuracao-experimentos-organicos.md",
    "references/41-playbooks-organicos-por-negocio.md",
    "references/42-operacao-seo-geo-roadmap-e-governanca.md",
    "research/PESQUISA-SEO-GEO-AI-SEARCH-2026-11-14.md",
    "templates/organic-growth-audit.md",
    "templates/organic-growth-brief.md",
    "templates/ai-visibility-experiment.md",
    "tests/SEO-GEO-CEO-EVALS.md",
]

class OrganicGrowthDocs(unittest.TestCase):
    def test_docs_exist_and_are_substantial(self):
        for name in DOCS:
            with self.subTest(path=name):
                path = ROOT / name
                self.assertTrue(path.is_file(), name)
                self.assertGreater(len(path.read_text(encoding="utf-8")), 300)

    def test_routing_references_new_modules(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for name in DOCS[:7]:
            self.assertIn(name, skill)
        self.assertIn("POLICY.md", skill)

    def test_official_sources_and_anti_guarantee(self):
        geo = (ROOT / DOCS[1]).read_text(encoding="utf-8")
        self.assertIn("developers.openai.com/api/docs/bots", geo)
        self.assertIn("developers.google.com/search", geo)
        self.assertIn("Não confundir", geo)
        self.assertIn("não", geo.lower())

if __name__ == "__main__":
    unittest.main()
