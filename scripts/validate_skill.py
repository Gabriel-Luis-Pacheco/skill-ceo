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
    "tests/test_cases.jsonl",
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

if errors:
    for err in errors:
        print("ERROR:", err, file=sys.stderr)
    sys.exit(1)
print("OK: skill structure, declared references, frontmatter, and behavior cases validated.")
