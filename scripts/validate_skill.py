#!/usr/bin/env python3
"""Static integrity checks for the BataTalk CEO skill.

Does NOT run the CEO, approve actions, or measure business outcomes.
Stdlib-only: Python >= 3.11.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_E = {f"E{i:02d}" for i in range(1, 31)}
EXPECTED_ORG = {f"ORG{i:02d}" for i in range(1, 17)}
EXPECTED_O = {f"O{i:02d}" for i in range(1, 25)}
REQUIRED = (
    "README.md", "INSTALL.md", "AGENTS.md", "SKILL.md",
    "CEO_SYSTEM_PROMPT.md", "POLICY.md", "config/policy.example.yaml",
    "setup/CEO-first-message.md", "setup/routines.md",
    "tests/CEO-BEHAVIOR-EVALS.md", "tests/REVIEW-PROTOCOL.md",
    "tests/all-30-scenarios.jsonl", "tests/org-autonomy-cases.jsonl",
    "tests/test_cases.jsonl", "tests/orchestration-cases.jsonl",
    "research/ORCHESTRATION-RESEARCH-2026.md",
    "scripts/validate_work_graph.py",
    "templates/orchestration-task.md", "templates/orchestration-plan.example.json",
    "templates/CEO-dashboard.md", "templates/task-handoff.md",
    "templates/agent-charter.md", "templates/organizational-decision.md",
    "references/03-equipe-e-organograma.md",
    "references/05-growth-competidores-seo-geo-cro.md",
    "references/06-produto-pedagogia-dados-financas.md",
    "references/07-safety-controles.md", "references/11-openbot-integracao.md",
    "references/12-ceo-autonomous-loop.md", "references/18-runtime-guardrails.md",
    "references/20-executive-memory.md", "references/21-organizacao-autonoma.md",
    *tuple(f"references/{i:02d}-{name}.md" for i, name in enumerate((
        "orquestracao-padroes", "contratos-dags-handoffs", "recuperacao-confiabilidade",
        "contexto-e-comunicacao", "qualidade-e-observabilidade", "ceo-sistema-estrategico",
        "openbot-playbook-operacional", "modelos-custo-capacidade"
    ), start=22)),
)
LOCAL_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
REQUIRED_PATH = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:references|templates|setup|tests|config)/[A-Za-z0-9_./-]+"
)
QUOTA = re.compile(
    r"(?i)\b(?:no\s+m[aá]ximo|at[eé]|limite\s+de|teto\s+de)\s+"
    r"\d+\s+(?:agentes|subagentes|frentes|projetos|pesquisas|novos\s+agentes)"
    r"|\b\d+\s+agentes(?:-piloto)?\s+por\s+semana"
    r"|\b1[–-]3\s+frentes\s+ativas"
)
NORMATIVE_DOCS = (
    "SKILL.md", "CEO_SYSTEM_PROMPT.md", "config/policy.example.yaml",
    "references/02-sistema-operacional.md", "references/03-equipe-e-organograma.md",
    "references/04-diagnostico-e-autoaperfeicoamento.md",
    "references/07-safety-controles.md", "references/08-rituais-rotinas.md",
    "references/12-ceo-autonomous-loop.md",
    "references/16-team-culture-organization.md",
    "references/18-runtime-guardrails.md",
    "setup/CEO-first-message.md", "setup/routines.md",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def check_jsonl(path: Path, required_fields: tuple[str, ...], expected: set[str]) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"Ausente: {path.name}"]
    seen: set[str] = set()
    for lineno, raw in enumerate(read_text(path).splitlines(), 1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
            if not isinstance(item, dict):
                raise ValueError("registro deve ser um objeto")
            for key in required_fields:
                if not isinstance(item.get(key), str) or not item[key].strip():
                    raise ValueError(f"campo inválido: {key}")
            item_id = item["id"]
            if item_id in seen:
                raise ValueError(f"id duplicado: {item_id}")
            seen.add(item_id)
        except (ValueError, TypeError) as exc:
            errors.append(f"{path.name}:{lineno}: {exc}")
    if seen != expected:
        errors.append(f"{path.name}: faltando={sorted(expected - seen)} inesperados={sorted(seen - expected)}")
    return errors


def check_smoke_cases(path: Path) -> list[str]:
    """Small regression subset with machine-readable must/must_not checks."""
    if not path.is_file():
        return [f"Ausente: {path.name}"]
    errors: list[str] = []
    found: set[str] = set()
    for lineno, raw in enumerate(read_text(path).splitlines(), 1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
            if not isinstance(item, dict):
                raise ValueError("expected object")
            ident = item.get("id")
            if ident not in EXPECTED_E or ident in found:
                raise ValueError("unknown/duplicate E-id")
            if not isinstance(item.get("input"), str) or not item["input"].strip():
                raise ValueError("missing input")
            for key in ("must", "must_not"):
                values = item.get(key)
                if not isinstance(values, list) or not values or any(
                    not isinstance(v, str) or not v.strip() for v in values
                ):
                    raise ValueError(f"invalid {key}")
            found.add(ident)
        except (ValueError, TypeError) as exc:
            errors.append(f"{path.name}:{lineno}: {exc}")
    if not found:
        errors.append(f"{path.name}: empty smoke suite")
    return errors


def check_local_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = read_text(path)
        for target in LOCAL_LINK.findall(content):
            target = target.strip().strip("<>")
            if target.startswith(("https://", "http://", "mailto:", "data:", "#")):
                continue
            target = unquote(target.split("#", 1)[0]).strip()
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(root)}: link escapa do repositório: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(root)}: link local inexistente: {target}")
    return errors


def check_quotas(text: str, source: str) -> list[str]:
    errors: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        # Negative examples inside quoted policy explanations are not policy.
        if "proibid" in line.lower() and "artificial" in line.lower():
            continue
        if QUOTA.search(line):
            errors.append(f"{source}:{lineno}: possível teto arbitrário: {line.strip()[:150]}")
    return errors


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED:
        path = root / rel
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Arquivo obrigatório ausente/vazio: {rel}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        skill = read_text(skill_path)
        parts = skill.split("---", 2)
        if len(parts) < 3 or not skill.startswith("---\n"):
            errors.append("SKILL.md: YAML frontmatter ausente")
        else:
            header = parts[1]
            if not re.search(r"(?m)^name:\s*batatalk-ceo-operator\s*$", header):
                errors.append("SKILL.md: name inválido")
            description = re.search(r"(?m)^description:\s*(.+)$", header)
            if not description or len(description.group(1)) > 1024:
                errors.append("SKILL.md: description ausente ou muito longa")
            example = re.search(r"(?m)^example-prompt:\s*(.+)$", header)
            if example and len(example.group(1)) > 1000:
                errors.append("SKILL.md: example-prompt ultrapassa limite OpenBot")
        if len(skill.splitlines()) > 500:
            errors.append("SKILL.md: núcleo enorme; considerar progressão por referências")
        if "POLICY.md" not in skill or "references/21-organizacao-autonoma.md" not in skill:
            errors.append("SKILL.md: política ou governança organizacional não referenciada")
        for ref in set(REQUIRED_PATH.findall(skill)):
            if not (root / ref).exists():
                errors.append(f"SKILL.md: referência inexistente: {ref}")

    policy_path = root / "POLICY.md"
    if policy_path.is_file():
        policy = read_text(policy_path)
        for phrase in ("Reels Creator", "orçamento", "autorização", "subagentes"):
            if phrase not in policy:
                errors.append(f"POLICY.md: proteções obrigatórias não mencionam {phrase!r}")
        if "aprovação do fundador" not in policy:
            errors.append("POLICY.md: mudança de alçada exige aprovação humana")

    if skill_path.is_file():
        skill = read_text(skill_path)
        if "Reels Creator" not in skill or "PAUSADO" not in skill:
            errors.append("SKILL.md: decisão de pausa do Reels Creator ausente")
        if "não há teto" not in skill.lower() and "não existem cotas" not in skill.lower():
            errors.append("SKILL.md: liberdade de dimensionamento não está explícita")

    for rel in NORMATIVE_DOCS:
        path = root / rel
        if path.is_file():
            errors += check_quotas(read_text(path), rel)

    errors += check_local_links(root)
    errors += check_smoke_cases(root / "tests/test_cases.jsonl")
    errors += check_jsonl(
        root / "tests/all-30-scenarios.jsonl",
        ("id", "input", "expected", "bad_pattern"), EXPECTED_E,
    )
    errors += check_jsonl(
        root / "tests/org-autonomy-cases.jsonl",
        ("id", "scenario", "expected", "forbidden"), EXPECTED_ORG,
    )

    errors += check_jsonl(
        root / "tests/orchestration-cases.jsonl",
        ("id", "scenario", "expected", "forbidden"), EXPECTED_O,
    )

    # Planning test checks the example with the same validator used by operators.
    try:
        from validate_work_graph import validate_plan
        plan = json.loads(read_text(root / "templates/orchestration-plan.example.json"))
        errors += [f"orchestration example: {err}" for err in validate_plan(plan)]
    except (OSError, ValueError, ImportError) as exc:
        errors.append(f"orchestration example invalid: {exc}")

    eval_doc = root / "tests/CEO-BEHAVIOR-EVALS.md"
    if eval_doc.is_file():
        ids = re.findall(r"(?m)^\|\s*(E\d{2})\s*\|", read_text(eval_doc))
        if set(ids) != EXPECTED_E or len(ids) != len(EXPECTED_E):
            errors.append("CEO-BEHAVIOR-EVALS.md: tabela diverge de E01..E30")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for message in errors:
            print("FAIL:", message, file=sys.stderr)
        return 1
    print("PASS: integridade da skill, contratos, DAG offline, política e 70 cenários estruturados.")
    print("OBS: não executa agentes, não valida decisões reais e não autoriza ações.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
