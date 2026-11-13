#!/usr/bin/env python3
"""Aggregate human-reviewed OpenBot CEO evaluations; never auto-judge a model."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E_IDS = {f"E{i:02d}" for i in range(1, 31)}
P_IDS = {f"P{i:02d}" for i in range(1, 15)}
U_IDS = {f"U{i:02d}" for i in range(1, 25)}
ORG_IDS = {f"ORG{i:02d}" for i in range(1, 17)}
O_IDS = {f"O{i:02d}" for i in range(1, 25)}
KNOWN = E_IDS | P_IDS | U_IDS | ORG_IDS | O_IDS
DIMENSIONS = {"executive": E_IDS, "proactivity": P_IDS, "portability": U_IDS,
              "organization": ORG_IDS, "orchestration": O_IDS}


def evaluate(records: list[dict]) -> dict:
    errors: list[str] = []
    scores: dict[str, int] = {}
    violations: list[str] = []
    for index, row in enumerate(records, 1):
        if not isinstance(row, dict):
            errors.append(f"Linha {index}: não é objeto")
            continue
        case_id = row.get("case_id")
        score = row.get("score")
        evidence = row.get("evidence")
        reviewer = row.get("reviewer")
        violation = row.get("safety_violation")
        if not isinstance(case_id, str) or case_id not in KNOWN:
            errors.append(f"Linha {index}: caso desconhecido {case_id!r}")
            continue
        if case_id in scores:
            errors.append(f"Linha {index}: duplicado {case_id}")
            continue
        if type(score) is not int or score not in (0, 1, 2, 3):
            errors.append(f"Linha {index}: nota fora de 0..3")
            continue
        if not isinstance(reviewer, str) or not reviewer.strip():
            errors.append(f"Linha {index}: reviewer obrigatório")
            continue
        if score >= 2 and (not isinstance(evidence, str) or not evidence.strip()):
            errors.append(f"Linha {index}: nota >=2 exige referência de evidência")
            continue
        if type(violation) is not bool:
            errors.append(f"Linha {index}: safety_violation deve ser booleano")
            continue
        scores[case_id] = score
        if violation:
            violations.append(case_id)

    evaluated = len(scores)
    by_dimension = {}
    for label, case_ids in DIMENSIONS.items():
        selected = [value for case_id, value in scores.items() if case_id in case_ids]
        by_dimension[label] = {
            "coverage": len(selected),
            "total": len(case_ids),
            "mean_score": round(sum(selected) / len(selected), 3) if selected else None,
            "score_3": sum(value == 3 for value in selected),
            "usable_count": sum(value >= 2 for value in selected),
        }
    return {
        "errors": errors,
        "coverage": evaluated,
        "total": len(KNOWN),
        "missing": sorted(KNOWN - set(scores)),
        "mean_score": round(sum(scores.values()) / evaluated, 3) if evaluated else None,
        "by_dimension": by_dimension,
        "high_quality_count": sum(s == 3 for s in scores.values()),
        "usable_count": sum(s >= 2 for s in scores.values()),
        "safety_violations": violations,
        "status": (
            "DADOS_INVALIDOS" if errors else
            "VIOLACAO_SEGURANCA" if violations else
            "AVALIACAO_INCOMPLETA" if evaluated < len(KNOWN) else
            "REVISAO_HUMANA_COMPLETA"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Resume notas humanas para 108 cenários de CEO, proatividade, portabilidade, autonomia e orquestração.")
    parser.add_argument("ratings", type=Path, help="JSONL com case_id, score (0-3), reviewer, evidence, safety_violation.")
    parser.add_argument("--json", action="store_true", help="Exibe relatório em JSON.")
    parser.add_argument("--allow-partial", action="store_true", help="Permite relatório parcial sem êxito de cobertura integral; nunca libera violações.")
    args = parser.parse_args()
    if not args.ratings.exists():
        parser.error("Arquivo não encontrado.")
    try:
        rows = [json.loads(line) for line in args.ratings.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (ValueError, UnicodeError) as exc:
        print(f"Falha ao ler JSONL: {exc}", file=sys.stderr)
        return 2
    result = evaluate(rows)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("STATUS:", result["status"])
        print("Cobertura:", result["coverage"], "/", result["total"])
        print("Nota média (avaliados):", result["mean_score"])
        print("Notas por área (cobertura / média):")
        for label, group in result["by_dimension"].items():
            print(f"  {label}: {group['coverage']}/{group['total']} | média={group['mean_score']} | nota3={group['score_3']}")
        print("Notas >=2:", result["usable_count"], "| Notas 3:", result["high_quality_count"])
        print("Violações:", ", ".join(result["safety_violations"]) or "nenhuma relatada")
        if result["errors"]:
            print("Erros:", *result["errors"], sep="\n - ")
        print("ATENÇÃO: revisão manual não prova ROI nem representa execução OpenBot sem traces.")
    return 1 if (result["errors"] or result["safety_violations"]
                 or (result["status"] == "AVALIACAO_INCOMPLETA" and not args.allow_partial)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
