"""Offline planner validation and adversarial tests."""
import sys
import unittest
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_work_graph import validate_plan


def task(task_id: str, deps=None, resources=None, risk="internal"):
    return dict(id=task_id, owner="CTO", depends_on=deps or [],
                owned_resources=resources or [f"owned/{task_id}"],
                deliverable=f"outputs/{task_id}.md", acceptance="verifiable result",
                status="PROPOSED", risk=risk)


class WorkGraphTests(unittest.TestCase):
    def test_sequential(self):
        self.assertEqual([], validate_plan(dict(initiative_id="A", tasks=[
            task("A"), task("B", ["A"]), task("C", ["B"])
        ])))

    def test_parallel_distinct_resources(self):
        self.assertEqual([], validate_plan(dict(initiative_id="A", tasks=[
            task("A"), task("B")
        ])))

    def test_cycle_rejected(self):
        plan = dict(initiative_id="A", tasks=[task("A", ["B"]), task("B", ["A"])])
        self.assertTrue(any("cycle" in e for e in validate_plan(plan)))

    def test_unknown_dependency_rejected(self):
        self.assertTrue(any("unknown" in e for e in validate_plan(
            dict(initiative_id="A", tasks=[task("A", ["NOT_EXISTS"])]))))

    def test_duplicate_id_rejected(self):
        self.assertTrue(any("duplicate task" in e for e in validate_plan(
            dict(initiative_id="A", tasks=[task("A"), task("A")]))))

    def test_parallel_same_resource_rejected(self):
        self.assertTrue(any("resource conflict" in e for e in validate_plan(
            dict(initiative_id="A", tasks=[
                task("A", resources=["index.ts"]), task("B", resources=["index.ts"])
            ]))))

    def test_sequential_same_resource_allowed(self):
        self.assertEqual([], validate_plan(dict(initiative_id="A", tasks=[
            task("A", resources=["index.ts"]),
            task("B", ["A"], ["index.ts"]),
        ])))

    def test_missing_owner_and_acceptance(self):
        t = task("A")
        t["owner"] = ""
        t["acceptance"] = ""
        failures = validate_plan(dict(initiative_id="A", tasks=[t]))
        self.assertTrue(any("owner required" in e for e in failures))
        self.assertTrue(any("acceptance required" in e for e in failures))

    def test_unknown_risk_rejected(self):
        self.assertTrue(any("invalid risk" in e for e in validate_plan(
            dict(initiative_id="A", tasks=[task("A", risk="autonomous_prod")]))))

    def test_self_dependency_rejected(self):
        self.assertTrue(any("self dependency" in e for e in validate_plan(
            dict(initiative_id="A", tasks=[task("A", ["A"])]))))

    def test_example_plan(self):
        import json
        root = Path(__file__).resolve().parents[1]
        plan = json.loads((root / "templates/orchestration-plan.example.json").read_text())
        self.assertEqual([], validate_plan(plan))


if __name__ == "__main__":
    unittest.main()
