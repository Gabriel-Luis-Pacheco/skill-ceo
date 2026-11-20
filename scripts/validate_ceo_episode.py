#!/usr/bin/env python3
"""Validate a CEO decision episode, without executing it or authenticating evidence.

This is a narrow structural guard: strings called "proof" or "approval" are
NOT independently verified. Keep customer/PII traces out of public Git.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

OBSERVATION = {"VERIFICADO", "RELATADO", "HIPOTESE", "SEM_DADOS", "SEM_ACESSO"}
EFFECT = {"PREPARADO", "EXECUTADO", "VERIFICADO", "BLOQUEADO", "NAO_EXECUTADO"}
RISK = {"internal", "external_requires_approval", "sensitive_requires_approval"}


def _string(obj: dict, key: str, where: str, errors: list[str]) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{where}.{key}: nonempty text required")
        return ""
    return value.strip()


def _timestamp(value: str, where: str, errors: list[str]) -> None:
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None or dt.utcoffset() is None:
            raise ValueError("timezone required")
    except ValueError:
        errors.append(f"{where}: timestamp must be ISO-8601 with timezone")


def validate_episode(episode: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(episode, dict):
        return ["episode must be an object"]

    for key in ("episode_id", "issue", "owner", "next_trigger"):
        _string(episode, key, "episode", errors)
    date = _string(episode, "observed_at", "episode", errors)
    if date:
        _timestamp(date, "episode.observed_at", errors)

    if episode.get("mode") not in {"M0", "M1", "M2"}:
        errors.append("episode.mode: expected M0/M1/M2")

    observations = episode.get("observations")
    if not isinstance(observations, list) or not observations:
        errors.append("observations: nonempty array required")
    else:
        for i, item in enumerate(observations):
            where = f"observations[{i}]"
            if not isinstance(item, dict):
                errors.append(f"{where}: object required")
                continue
            _string(item, "claim", where, errors)
            status = item.get("status")
            if status not in OBSERVATION:
                errors.append(f"{where}.status: unsupported evidence classification")
            source = item.get("source", "")
            if status == "VERIFICADO" and (not isinstance(source, str) or not source.strip()):
                errors.append(f"{where}.source: verified claim needs inspectable source")
            if source is not None and not isinstance(source, str):
                errors.append(f"{where}.source: text expected")

    hypothesis = episode.get("hypothesis")
    if not isinstance(hypothesis, dict):
        errors.append("hypothesis: object required")
    else:
        for key in ("main", "rival", "discriminator"):
            _string(hypothesis, key, "hypothesis", errors)

    decision = episode.get("decision")
    if not isinstance(decision, dict):
        errors.append("decision: object required")
    else:
        for key in ("action", "not_do", "reason"):
            _string(decision, key, "decision", errors)

    effect = episode.get("effect")
    if not isinstance(effect, dict):
        errors.append("effect: object required")
        status, risk = None, None
    else:
        status, risk = effect.get("status"), effect.get("risk")
        if status not in EFFECT:
            errors.append("effect.status: unsupported execution state")
        if risk not in RISK:
            errors.append("effect.risk: unsupported risk state")
        _string(effect, "target", "effect", errors)
        if status in {"EXECUTADO", "VERIFICADO"}:
            _string(effect, "evidence", "effect", errors)
        if status == "VERIFICADO":
            verified_at = _string(effect, "verified_at", "effect", errors)
            if verified_at:
                _timestamp(verified_at, "effect.verified_at", errors)
        if risk in {"external_requires_approval", "sensitive_requires_approval"} and status in {"EXECUTADO", "VERIFICADO"}:
            _string(effect, "approval_reference", "effect", errors)

    impact = episode.get("impact")
    if not isinstance(impact, dict) or impact.get("status") not in {"NAO_MEDIDO", "MEDIDO"}:
        errors.append("impact.status: expected NAO_MEDIDO or MEDIDO")
    elif impact["status"] == "MEDIDO":
        if status != "VERIFICADO":
            errors.append("impact: measured outcome cannot be attributed to unverified execution")
        for key in ("metric", "unit", "window", "population", "source"):
            _string(impact, key, "impact", errors)
        for key in ("baseline", "after"):
            number = impact.get(key)
            if isinstance(number, bool) or not isinstance(number, (int, float)):
                errors.append(f"impact.{key}: finite numeric value required")
            elif number != number or number in (float("inf"), float("-inf")):
                errors.append(f"impact.{key}: must be finite")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episode", type=Path, help="JSON of one decision/verification episode")
    args = parser.parse_args()
    try:
        doc = json.loads(args.episode.read_text(encoding="utf-8"))
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"Invalid episode file: {exc}", file=sys.stderr)
        return 2
    problems = validate_episode(doc)
    for p in problems:
        print("ERROR:", p, file=sys.stderr)
    if problems:
        return 1
    print("PASS: episode schema is consistent. Evidence and approval NOT authenticated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
