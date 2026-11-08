"""Offline planner validation and adversarial tests."""
import sys
import unittest
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_work_graph import validate_plan, ready_tasks


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

    def test_active_task_with_unverified_dependency_rejected(self):
        first = task("A")
        second = task("B", ["A"])
        second["status"] = "RUNNING"
        errors = validate_plan(dict(initiative_id="A", tasks=[first, second]))
        self.assertTrue(any("unverified" in e for e in errors))

    def test_external_execution_requires_approval_reference(self):
        t = task("SEND", risk="external_requires_approval")
        t["status"] = "RUNNING"
        failures = validate_plan(dict(initiative_id="A", tasks=[t]))
        self.assertTrue(any("approval_reference" in e for e in failures))
        t["approval_reference"] = "APPROVAL-123"
        self.assertEqual([], validate_plan(dict(initiative_id="A", tasks=[t])))

    def test_ready_tasks_respect_dependencies(self):
        a = task("A")
        b = task("B", ["A"])
        plan = dict(initiative_id="A", tasks=[a, b])
        self.assertEqual(["A"], ready_tasks(plan))
        a["status"] = "VERIFIED"
        self.assertEqual(["B"], ready_tasks(plan))

    def test_ready_external_task_needs_approval(self):
        t = task("PUBLISH", risk="external_requires_approval")
        plan = dict(initiative_id="A", tasks=[t])
        self.assertEqual([], ready_tasks(plan))
        t["approval_reference"] = "approval:founder"
        self.assertEqual(["PUBLISH"], ready_tasks(plan))

    def test_invalid_type_in_status_is_validation_failure(self):
        t = task("A")
        t["status"] = []
        self.assertTrue(any("invalid status" in e for e in validate_plan(
            dict(initiative_id="A", tasks=[t]))))

    def test_cancelled_resource_does_not_block_new_task(self):
        old = task("OLD", resources=["index.ts"])
        old["status"] = "CANCELLED"
        new = task("NEW", resources=["index.ts"])
        self.assertEqual([], validate_plan(dict(initiative_id="A", tasks=[old, new])))

    def test_verified_resource_does_not_block_new_task(self):
        old = task("OLD", resources=["index.ts"])
        old["status"] = "VERIFIED"
        new = task("NEW", resources=["index.ts"])
        self.assertEqual([], validate_plan(dict(initiative_id="A", tasks=[old, new])))

    def test_whitespace_approval_is_not_authorization(self):
        t = task("PUBLISH", risk="external_requires_approval")
        t["approval_reference"] = "   "
        plan = dict(initiative_id="A", tasks=[t])
        self.assertEqual([], ready_tasks(plan))
        t["status"] = "RUNNING"
        self.assertTrue(any("approval_reference" in e for e in validate_plan(plan)))

    def test_example_plan(self):
        import json
        root = Path(__file__).resolve().parents[1]
        plan = json.loads((root / "templates/orchestration-plan.example.json").read_text())
        self.assertEqual([], validate_plan(plan))


if __name__ == "__main__":
    unittest.main()
