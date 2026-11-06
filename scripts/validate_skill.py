#!/usr/bin/env python3
"""Checks that the BataTalk CEO skill remains installable and structurally sound."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "SKILL.md", "CEO_SYSTEM_PROMPT.md",
    "setup/CEO-first-message.md", "setup/routines.md",
    "config/policy.example.yaml", "tests/CEO-BEHAVIOR-EVALS.md",
    "tests/test_cases.jsonl", "tests/all-30-scenarios.jsonl", "tests/REVIEW-PROTOCOL.md",
    *[f"references/{n:02d}-{name}.md" for n, name in enumerate([
        "principios-de-ceo",
        "sistema-operacional",
        "equipe-e-organograma",
        "diagnostico-e-autoaperfeicoamento",
        "growth-competidores-seo-geo-cro",
        "produto-pedagogia-dados-financas",
        "safety-controles",
        "rituais-rotinas",
        "playbooks-de-situacoes",
        "fontes",
        "openbot-integracao",
    ], start=1)],
    *[f"references/{i:02d}-{name}.md" for i, name in enumerate([
        "ceo-autonomous-loop", "deep-product-audit", "competitive-advantage",
        "growth-profit-engine", "team-culture-organization",
        "deep-research-and-learning", "runtime-guardrails",
        "executive-scenarios", "executive-memory",
    ], start=12)],
]
errors = []
for name in REQUIRED:
    path = ROOT / name
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"Missing or empty: {name}")

skill_path = ROOT / "SKILL.md"
if skill_path.exists():
    skill = skill_path.read_text(encoding="utf-8")
    if not skill.startswith("---\n") or not re.search(
        r"(?m)^name:\s*batatalk-ceo-operator\s*$", skill
    ):
        errors.append("Invalid SKILL.md frontmatter/name")
    if not re.search(r"(?m)^description:\s*\S", skill):
        errors.append("Missing skill description")
    for ref in set(re.findall(
        r"(?<![A-Za-z0-9_./])(?:references|templates|setup|tests|config)/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*",
        skill,
    )):
        if not (ROOT / ref).exists():
            errors.append(f"SKILL.md references nonexistent path: {ref}")

test_file = ROOT / "tests/test_cases.jsonl"
if test_file.exists():
    seen = set()
    for lineno, line in enumerate(test_file.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            case = json.loads(line)
            if not isinstance(case, dict):
                raise ValueError("expected an object")
            if not all(k in case for k in ("id", "input", "must", "must_not")):
                raise ValueError("missing required fields")
            if case["id"] in seen:
                raise ValueError("duplicate test id")
            seen.add(case["id"])
        except (ValueError, TypeError) as exc:
            errors.append(f"Invalid test case line {lineno}: {exc}")
    if len(seen) < 5:
        errors.append("Need at least five unique behavior test cases")

full_path = ROOT / "tests/all-30-scenarios.jsonl"
if full_path.exists():
    found = set()
    for lineno, raw in enumerate(full_path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
            if not isinstance(item, dict):
                raise ValueError("not an object")
            if any(not isinstance(item.get(k), str) or not item[k].strip()
                   for k in ("id", "input", "expected", "bad_pattern")):
                raise ValueError("missing/non-string case field")
            if item["id"] in found:
                raise ValueError("duplicate id")
            found.add(item["id"])
        except (ValueError, TypeError) as exc:
            errors.append(f"Invalid full test case line {lineno}: {exc}")
    missing = {f"E{i:02d}" for i in range(1, 31)} - found
    if len(found) != 30 or missing:
        errors.append(f"Expected exactly E01-E30 in full cases; got {len(found)} missing={sorted(missing)}")

if skill_path.exists() and skill.count("\n") > 500:
    errors.append("SKILL.md exceeds 500-line progressive-disclosure guideline")

if errors:
    for err in errors:
        print("ERROR:", err, file=sys.stderr)
    sys.exit(1)
print("OK: skill structure, declared references, frontmatter, and behavior cases validated.")
