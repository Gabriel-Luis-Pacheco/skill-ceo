#!/usr/bin/env python3
"""Check role coverage and bibliographic consistency. Does not verify actual books."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "references/53-biblioteca-expandida-140-obras-19-cargos.md"
EXPECTED_ROLES = 19
EXPECTED_BOOKS = 140

def validate(text: str) -> list[str]:
    errors: list[str] = []
    books = re.findall(r"(?m)^\| (D\d{2,3}) \| \*\*", text)
    if len(books) != EXPECTED_BOOKS:
        errors.append(f"Expected {EXPECTED_BOOKS} catalog rows, got {len(books)}")
    if len(set(books)) != len(books):
        errors.append("Duplicate catalog IDs")
    role_section = text.split("## Trilha por função", 1)
    if len(role_section) < 2:
        return errors + ["Role matrix missing"]
    role_section = role_section[1].split("## Catálogo de obras", 1)[0]
    role_rows = re.findall(r"(?m)^\| ([^|]+) \| ([^|]+) \| (\d+) \|$", role_section)
    role_rows = [(r, ids, count) for r, ids, count in role_rows if re.search(r"D\d{2,3}", ids)]
    if len(role_rows) != EXPECTED_ROLES:
        errors.append(f"Expected {EXPECTED_ROLES} role rows, got {len(role_rows)}")
    seen_roles: set[str] = set()
    for name, values, declared in role_rows:
        if name in seen_roles:
            errors.append(f"Duplicate role: {name}")
        seen_roles.add(name)
        ids = re.findall(r"\bD\d{2,3}\b", values)
        if len(ids) < 20:
            errors.append(f"{name}: fewer than 20 titles")
        if int(declared) != len(ids):
            errors.append(f"{name}: declared count mismatch")
        if len(set(ids)) != len(ids):
            errors.append(f"{name}: duplicated IDs")
        for ident in ids:
            if ident not in books:
                errors.append(f"{name}: missing catalog title {ident}")
    if "não" not in text.lower() or "leitura integral" not in text.lower():
        errors.append("Missing explicit bibliographic limitation")
    return errors

def main() -> int:
    if not DOC.is_file():
        print(f"FAIL missing {DOC}", file=sys.stderr)
        return 1
    errors = validate(DOC.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: 140 unique titles, 19 roles, at least 20 role-specific references each.")
    print("NOTE: validates structure, not full-text book access or business outcomes.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
