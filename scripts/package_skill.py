#!/usr/bin/env python3
"""Build a portable Agent Skills directory, without changing any active agent.

The repository is named skill-ceo; the distributable directory MUST match the
frontmatter name batatalk-ceo-operator. Building a bundle is not installation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "batatalk-ceo-operator"
FILES = (
    "SKILL.md", "POLICY.md", "CEO_SYSTEM_PROMPT.md", "AGENTS.md",
    "INSTALL.md", "README.md", "AUDIT.md",
)
FOLDERS = (
    "references", "adapters", "setup", "templates", "scripts",
    "tests", "research", "config",
)
MANIFEST = ".skill-bundle-manifest.json"


def package_skill(output_root: Path, source_root: Path = SOURCE_ROOT, *, replace: bool = False) -> Path:
    source_root = source_root.resolve()
    output_root = output_root.resolve()
    dest = output_root / SKILL_NAME
    if dest == source_root or source_root.is_relative_to(dest):
        raise ValueError("Destination would overwrite the canonical source repository")
    if dest.exists():
        if not replace:
            raise FileExistsError(f"{dest} exists; pass --replace to rebuild an existing generated bundle")
        if not dest.is_dir() or not (dest / MANIFEST).is_file():
            raise ValueError("Refusing to replace a directory without the generated bundle manifest")
        existing = json.loads((dest / MANIFEST).read_text(encoding="utf-8"))
        if existing.get("skill") != SKILL_NAME:
            raise ValueError("Refusing to replace a bundle with a different identity")
        shutil.rmtree(dest)
    output_root.mkdir(parents=True, exist_ok=True)
    dest.mkdir()
    for name in FILES:
        src = source_root / name
        if not src.is_file():
            raise FileNotFoundError(f"Required source file missing: {name}")
        shutil.copy2(src, dest / name)
    for dirname in FOLDERS:
        src = source_root / dirname
        if not src.is_dir():
            raise FileNotFoundError(f"Required source directory missing: {dirname}")
        shutil.copytree(
            src, dest / dirname,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo", ".DS_Store", ".env*"),
        )
    skill_text = (dest / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\nname: " + SKILL_NAME + "\n"):
        raise ValueError("SKILL.md name does not match the distributable directory")
    from validate_skill import check_local_links
    broken = check_local_links(dest)
    if broken:
        raise ValueError("Generated bundle contains broken relative links: " + "; ".join(broken[:5]))
    (dest / MANIFEST).write_text(json.dumps({
        "skill": SKILL_NAME,
        "skill_sha256": hashlib.sha256((dest / "SKILL.md").read_bytes()).hexdigest(),
        "purpose": "Generated skill bundle; not proof of installation or runtime activity",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return dest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SOURCE_ROOT / "dist",
                        help="Parent folder where batatalk-ceo-operator/ will be generated")
    parser.add_argument("--replace", action="store_true",
                        help="Replace only a previously generated, manifest-verified bundle")
    args = parser.parse_args()
    try:
        dest = package_skill(args.output, replace=args.replace)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(f"OK: bundle at {dest}")
    print("Not installed. Copy this folder into the host's verified skill directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
