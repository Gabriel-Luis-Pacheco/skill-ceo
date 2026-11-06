#!/usr/bin/env python3
"""Offline validator for CEO planning DAGs; does not schedule OpenBot agents.

Checks structural consistency, conflicts, and dependencies. This is NOT a
transactional workflow engine or an authorization system.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

STATES = {"PROPOSED", "ACCEPTED", "RUNNING", "BLOCKED", "SUBMITTED",
          "REVIEW_CHANGES", "VERIFIED", "CANCELLED"}
RISK = {"internal", "external_requires_approval", "sensitive_requires_approval"}
FIELDS = {"id", "owner", "depends_on", "owned_resources", "deliverable",
          "acceptance", "status", "risk"}


def validate_plan(plan: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(plan, dict):
        return ["plan must be an object"]
    if not isinstance(plan.get("initiative_id"), str) or not plan["initiative_id"].strip():
        errors.append("initiative_id missing")
    tasks = plan.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        return errors + ["tasks must be a nonempty list"]
    by_id: dict[str, dict] = {}
    for index, task in enumerate(tasks, 1):
        if not isinstance(task, dict):
            errors.append(f"task {index} not object")
            continue
        missing = FIELDS - set(task)
        if missing:
            errors.append(f"task {index} missing fields: {sorted(missing)}")
            continue
        task_id = task["id"]
        if not isinstance(task_id, str) or not task_id.strip():
            errors.append(f"task {index} invalid id")
            continue
        if task_id in by_id:
            errors.append(f"duplicate task id: {task_id}")
            continue
        by_id[task_id] = task
        if not isinstance(task["owner"], str) or not task["owner"].strip():
            errors.append(f"{task_id}: owner required")
        if not isinstance(task["deliverable"], str) or not task["deliverable"].strip():
            errors.append(f"{task_id}: deliverable required")
        if not isinstance(task["acceptance"], str) or not task["acceptance"].strip():
            errors.append(f"{task_id}: acceptance required")
        if not isinstance(task["depends_on"], list) or any(
                not isinstance(x, str) or not x.strip() for x in task["depends_on"]):
            errors.append(f"{task_id}: depends_on must contain task ids")
        if not isinstance(task["owned_resources"], list) or any(
                not isinstance(x, str) or not x.strip() for x in task["owned_resources"]):
            errors.append(f"{task_id}: invalid owned_resources")
        if not isinstance(task["status"], str) or task["status"] not in STATES:
            errors.append(f"{task_id}: invalid status")
        if not isinstance(task["risk"], str) or task["risk"] not in RISK:
            errors.append(f"{task_id}: invalid risk")

    deps: dict[str, set[str]] = {}
    for key, task in by_id.items():
        if not isinstance(task["depends_on"], list):
            continue
        dep_set = set(x for x in task["depends_on"] if isinstance(x, str))
        if len(dep_set) != len(task["depends_on"]):
            errors.append(f"{key}: duplicate dependencies")
        if key in dep_set:
            errors.append(f"{key}: self dependency")
        for dep in dep_set:
            if dep not in by_id:
                errors.append(f"{key}: unknown dependency {dep}")
        deps[key] = dep_set

    visited: set[str] = set()
    active: set[str] = set()
    def walk(node: str) -> None:
        if node in active:
            errors.append(f"cycle detected at {node}")
            return
        if node in visited:
            return
        active.add(node)
        for dep in deps.get(node, ()):
            if dep in by_id:
                walk(dep)
        active.remove(node)
        visited.add(node)
    for task_id in by_id:
        walk(task_id)

    # Only dispatch tasks whose dependencies are actually verified.
    for key, task in by_id.items():
        if task.get("status") in {"RUNNING", "SUBMITTED", "VERIFIED"}:
            for dep in deps.get(key, ()):
                if dep in by_id and by_id[dep].get("status") != "VERIFIED":
                    errors.append(f"{key}: active/finished task depends on unverified {dep}")
        if (task.get("risk") in {"external_requires_approval", "sensitive_requires_approval"}
                and task.get("status") in {"RUNNING", "SUBMITTED", "VERIFIED"}
                and not isinstance(task.get("approval_reference"), str)):
            errors.append(f"{key}: external/sensitive task needs approval_reference before execution")

    def ancestor(earlier: str, later: str) -> bool:
        seen: set[str] = set()
        stack = list(deps.get(later, ()))
        while stack:
            dep = stack.pop()
            if dep == earlier:
                return True
            if dep not in seen:
                seen.add(dep)
                stack.extend(deps.get(dep, ()))
        return False

    by_resource: dict[str, list[str]] = defaultdict(list)
    for key, task in by_id.items():
        if isinstance(task["owned_resources"], list):
            for resource in task["owned_resources"]:
                if isinstance(resource, str) and resource.strip():
                    by_resource[resource].append(key)
    for resource, owners in by_resource.items():
        for i, task_a in enumerate(owners):
            for task_b in owners[i+1:]:
                if not ancestor(task_a, task_b) and not ancestor(task_b, task_a):
                    errors.append(f"concurrent resource conflict: {resource}: {task_a} vs {task_b}")

    # Do not perform side effects. Approval is only described in POLICY.md.
    return errors


def ready_tasks(plan: object) -> list[str]:
    """IDs that may be considered for assignment; does not dispatch or authorize."""
    if validate_plan(plan):
        return []
    if not isinstance(plan, dict):
        return []
    completed = {task["id"] for task in plan["tasks"] if task["status"] == "VERIFIED"}
    return [
        task["id"] for task in plan["tasks"]
        if task["status"] == "PROPOSED"
        and set(task["depends_on"]).issubset(completed)
        and (
            task["risk"] == "internal"
            or bool(task.get("approval_reference"))
        )
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a work plan JSON offline")
    parser.add_argument("plan", type=Path)
    parser.add_argument("--ready", action="store_true",
                        help="Print eligible task IDs; never dispatches agents")
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"Invalid plan: {exc}", file=sys.stderr)
        return 2
    errors = validate_plan(plan)
    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        return 1
    print("PASS: dependency graph, ownership, authorization references and state consistent.")
    if args.ready:
        print("READY_FOR_ASSIGNMENT:", ", ".join(ready_tasks(plan)) or "none")
    print("NOT A RUNTIME: no agent was assigned, executed or authorized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
