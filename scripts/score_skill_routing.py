#!/usr/bin/env python3
"""Evaluate *observed* skill triggering, never simulate a host invocation.

Expected suites describe inputs. Observations must come from captured host runs.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

CASES = Path(__file__).resolve().parents[1] / "tests/skill-trigger-evals.jsonl"


def load_jsonl(path: Path) -> list[dict]:
    values = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        obj = json.loads(line)
        if not isinstance(obj, dict):
            raise ValueError(f"{path}:{lineno}: expected object")
        values.append(obj)
    return values


def score_routing(cases: list[dict], observations: list[dict]) -> dict:
    expectations = {}
    errors = []
    for case in cases:
        ident = case.get("id")
        if not isinstance(ident, str) or ident in expectations or not isinstance(case.get("should_activate"), bool):
            errors.append(f"Invalid or duplicate case: {ident}")
            continue
        expectations[ident] = case["should_activate"]
    observed = {}
    for item in observations:
        ident = item.get("id")
        if ident not in expectations or ident in observed:
            errors.append(f"Unknown or duplicate observation: {ident}")
            continue
        if not isinstance(item.get("activated"), bool) or not isinstance(item.get("evidence"), str) or not item["evidence"].strip():
            errors.append(f"Invalid observation evidence/activated: {ident}")
            continue
        observed[ident] = item["activated"]
    missing = sorted(expectations.keys() - observed.keys())
    tp = sum(expectations[k] and v for k, v in observed.items())
    fp = sum(not expectations[k] and v for k, v in observed.items())
    fn = sum(expectations[k] and not v for k, v in observed.items())
    tn = sum(not expectations[k] and not v for k, v in observed.items())
    return {
        "status": "INVALID" if errors else ("INCOMPLETE" if missing else "COMPLETE"),
        "errors": errors, "missing": missing,
        "coverage": len(observed), "total": len(expectations),
        "true_positive": tp, "false_positive": fp, "false_negative": fn, "true_negative": tn,
        "precision": round(tp / (tp + fp), 3) if tp + fp else None,
        "recall": round(tp / (tp + fn), 3) if tp + fn else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observations", type=Path, help="JSONL of {id, activated, evidence} from real host traces")
    parser.add_argument("--cases", type=Path, default=CASES)
    args = parser.parse_args()
    try:
        result = score_routing(load_jsonl(args.cases), load_jsonl(args.observations))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
