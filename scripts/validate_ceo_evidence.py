#!/usr/bin/env python3
"""Validate a locally collected OpenBot CEO evidence bundle.

Checks completeness and file references, NOT the authenticity of a trace,
the behavior of a live agent, or the reviewer's independent judgment.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from score_evaluations import KNOWN, evaluate

REQUIRED_TEXT = (
    "case_id", "run_id", "agent_id", "skill_commit", "model",
    "openbot_version", "environment", "reviewer", "trace_file",
    "review_notes",
)


def _local_evidence(root: Path, relative: object, name: str) -> list[str]:
    if not isinstance(relative, str) or not relative.strip():
        return [f"{name}: relative file path required"]
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        return [f"{name}: path escapes bundle directory"]
    if not path.is_file():
        return [f"{name}: file not found: {relative}"]
    if path.stat().st_size == 0:
        return [f"{name}: empty file: {relative}"]
    return []


def validate_bundle(bundle_path: Path) -> tuple[list[str], list[dict]]:
    errors: list[str] = []
    records: list[dict] = []
    try:
        source = json.loads(bundle_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        return [f"Cannot read bundle: {exc}"], []
    if not isinstance(source, dict) or not isinstance(source.get("runs"), list):
        return ["Bundle must contain a runs array"], []
    if not source["runs"]:
        return ["Bundle has no runs"], []
    root = bundle_path.resolve().parent
    seen_cases: set[str] = set()
    for idx, run in enumerate(source["runs"], 1):
        prefix = f"run {idx}"
        if not isinstance(run, dict):
            errors.append(f"{prefix}: expected an object")
            continue
        valid = True
        for key in REQUIRED_TEXT:
            if not isinstance(run.get(key), str) or not run[key].strip():
                errors.append(f"{prefix}: missing {key}")
                valid = False
        case_id = run.get("case_id")
        if not isinstance(case_id, str) or case_id not in KNOWN:
            errors.append(f"{prefix}: unknown case_id {case_id!r}")
            valid = False
        if isinstance(case_id, str):
            if case_id in seen_cases:
                errors.append(f"{prefix}: duplicate case_id {case_id}")
                valid = False
            seen_cases.add(case_id)
        if isinstance(run.get("agent_id"), str) and isinstance(run.get("reviewer"), str):
            if run["agent_id"].strip().casefold() == run["reviewer"].strip().casefold():
                errors.append(f"{prefix}: evaluator must not be the evaluated agent")
                valid = False
        score = run.get("score")
        if type(score) is not int or score not in (0, 1, 2, 3):
            errors.append(f"{prefix}: score must be 0..3")
            valid = False
        if type(run.get("safety_violation")) is not bool:
            errors.append(f"{prefix}: safety_violation must be boolean")
            valid = False
        if isinstance(run.get("trace_file"), str):
            found = _local_evidence(root, run["trace_file"], f"{prefix} trace_file")
            errors.extend(found)
            if found:
                valid = False
        artifacts = run.get("artifact_files", [])
        if not isinstance(artifacts, list) or any(not isinstance(x, str) for x in artifacts):
            errors.append(f"{prefix}: artifact_files must be a list of paths")
            valid = False
        else:
            for file_name in artifacts:
                found = _local_evidence(root, file_name, f"{prefix} artifact")
                errors.extend(found)
                if found:
                    valid = False
        if not valid:
            continue
        evidence = f"run={run['run_id']}; trace={run['trace_file']}"
        if artifacts:
            evidence += "; artifacts=" + ", ".join(artifacts)
        records.append({
            "case_id": case_id,
            "score": score,
            "reviewer": run["reviewer"],
            "evidence": evidence,
            "safety_violation": run["safety_violation"],
        })
    return errors, records


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a local OpenBot CEO evidence manifest.")
    parser.add_argument("bundle", type=Path, help="JSON manifest with runs and relative evidence paths.")
    parser.add_argument("--out", type=Path, help="Write scores JSONL for score_evaluations/compare_evaluations.")
    parser.add_argument("--allow-partial", action="store_true", help="Permit incomplete coverage for iteration only.")
    args = parser.parse_args()
    errors, records = validate_bundle(args.bundle)
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        return 2
    result = evaluate(records)
    if result["errors"]:
        for error in result["errors"]:
            print("ERROR:", error, file=sys.stderr)
        return 2
    if args.out is not None:
        # Do not write review artifacts into a public repo without checking their contents.
        args.out.write_text(
            "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in records),
            encoding="utf-8",
        )
    print(f"Reviewed local files for {result['coverage']}/{result['total']} scenarios.")
    print("Evaluation status:", result["status"])
    print("NOTE: files can be synthetic/edited; human review of original OpenBot runs is required.")
    if result["safety_violations"]:
        return 1
    if result["status"] == "AVALIACAO_INCOMPLETA" and not args.allow_partial:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
