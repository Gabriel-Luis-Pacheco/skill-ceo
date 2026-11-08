#!/usr/bin/env python3
"""Compare human-reviewed CEO skill evaluation scorecards on common scenarios.

No claim of causal improvement or real OpenBot execution is made by this script.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from score_evaluations import evaluate


def read_scores(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def compare_records(baseline: list[dict], candidate: list[dict]) -> dict:
    base_report = evaluate(baseline)
    new_report = evaluate(candidate)
    if base_report["errors"] or new_report["errors"]:
        return {
            "status": "INVALID",
            "baseline_errors": base_report["errors"],
            "candidate_errors": new_report["errors"],
        }
    base = {row["case_id"]: row["score"] for row in baseline}
    new = {row["case_id"]: row["score"] for row in candidate}
    common = sorted(base.keys() & new.keys())
    improved = [k for k in common if new[k] > base[k]]
    regressed = [k for k in common if new[k] < base[k]]
    unchanged = [k for k in common if new[k] == base[k]]
    mean_base = sum(base[k] for k in common) / len(common) if common else None
    mean_new = sum(new[k] for k in common) / len(common) if common else None
    safety = bool(new_report["safety_violations"])
    complete = base_report["coverage"] == base_report["total"] and new_report["coverage"] == new_report["total"]
    return {
        "status": "SAFETY_BLOCK" if safety else ("COMPLETE_FOR_HUMAN_REVIEW" if complete else "INCOMPLETE"),
        "shared_cases": len(common),
        "baseline_coverage": base_report["coverage"],
        "candidate_coverage": new_report["coverage"],
        "baseline_mean_common": round(mean_base, 3) if mean_base is not None else None,
        "candidate_mean_common": round(mean_new, 3) if mean_new is not None else None,
        "delta_mean_common": round(mean_new - mean_base, 3) if mean_base is not None else None,
        "improved": improved,
        "regressed": regressed,
        "unchanged_count": len(unchanged),
        "candidate_safety_violations": new_report["safety_violations"],
        "note": "Review trace provenance, environment equivalence, actual artifacts and business results manually.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare two human-reviewed CEO evaluations.")
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--allow-partial", action="store_true", help="Analyze overlap despite incomplete coverage.")
    args = parser.parse_args()
    try:
        result = compare_records(read_scores(args.baseline), read_scores(args.candidate))
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Cannot read scores: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] in ("INVALID", "SAFETY_BLOCK"):
        return 2
    if result["status"] == "INCOMPLETE" and not args.allow_partial:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
