"""Offline contract checks; these do not establish authenticity of CEO behavior."""
from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_ceo_episode import validate_episode


def sample() -> dict:
    return json.loads((ROOT / "templates/ceo-episode.example.json").read_text(encoding="utf-8"))


class EpisodeContractTests(unittest.TestCase):
    def test_sample_is_valid_but_not_issued_as_real_execution(self):
        doc = sample()
        self.assertEqual([], validate_episode(doc))
        self.assertEqual("PREPARADO", doc["effect"]["status"])
        self.assertEqual("NAO_MEDIDO", doc["impact"]["status"])

    def test_verified_claim_needs_source(self):
        doc = sample()
        doc["observations"][0]["status"] = "VERIFICADO"
        doc["observations"][0]["source"] = ""
        self.assertIn("verified claim needs inspectable source", " ".join(validate_episode(doc)))

    def test_no_execution_without_external_approval_reference(self):
        doc = sample()
        doc["effect"].update({"status": "EXECUTADO", "risk": "external_requires_approval", "evidence": "trace://example"})
        self.assertIn("effect.approval_reference", " ".join(validate_episode(doc)))

    def test_unverified_effect_cannot_claim_measured_outcome(self):
        doc = sample()
        doc["impact"] = {
            "status": "MEDIDO", "metric": "first_voice_use", "unit": "people",
            "window": "7 days", "population": "external users", "source": "trace://example",
            "baseline": 2, "after": 4
        }
        self.assertIn("cannot be attributed", " ".join(validate_episode(doc)))

    def test_verified_effect_and_measured_values_require_proof_fields(self):
        doc = sample()
        doc["effect"] = {
            "status": "VERIFICADO", "risk": "internal", "target": "sandbox",
            "evidence": "", "verified_at": "2026-11-20T20:05:00-03:00"
        }
        self.assertIn("effect.evidence", " ".join(validate_episode(doc)))
        doc["effect"]["evidence"] = "trace://synthetic-fixture"
        self.assertEqual([], validate_episode(doc))

    def test_naive_date_and_nan_are_rejected(self):
        doc = sample()
        doc["observed_at"] = "2026-11-20T20:00:00"
        self.assertIn("timezone", " ".join(validate_episode(doc)))
        doc["observed_at"] = "2026-11-20T20:00:00-03:00"
        doc["effect"].update({
            "status": "VERIFICADO", "evidence": "trace://synthetic-fixture",
            "verified_at": "2026-11-20T20:05:00-03:00"
        })
        doc["impact"] = {
            "status": "MEDIDO", "metric": "conversations", "unit": "people",
            "window": "7 days", "population": "test cohort", "source": "trace://fixture",
            "baseline": 1, "after": float("nan")
        }
        self.assertIn("must be finite", " ".join(validate_episode(doc)))


if __name__ == "__main__":
    unittest.main()
