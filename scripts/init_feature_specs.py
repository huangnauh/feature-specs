#!/usr/bin/env python3
"""Safely initialize the core feature-specs files in a repository."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the core evidence-driven specs templates without overwriting files."
    )
    parser.add_argument(
        "repo_root",
        nargs="?",
        default=".",
        help="Repository root to initialize (default: current directory).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report planned changes without creating files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).expanduser().resolve()
    if not repo_root.is_dir():
        print(f"error: repository root is not a directory: {repo_root}", file=sys.stderr)
        return 2

    skill_root = Path(__file__).resolve().parent.parent
    source_root = skill_root / "assets" / "specs"
    if not source_root.is_dir():
        print(f"error: bundled specs assets are missing: {source_root}", file=sys.stderr)
        return 2

    sources = sorted(path for path in source_root.rglob("*") if path.is_file())
    conflicts: list[Path] = []
    unchanged: list[Path] = []
    pending: list[tuple[Path, Path]] = []

    for source in sources:
        relative = source.relative_to(source_root)
        target = repo_root / "specs" / relative
        if target.exists():
            if target.is_file() and target.read_bytes() == source.read_bytes():
                unchanged.append(target)
            else:
                conflicts.append(target)
        else:
            pending.append((source, target))

    if conflicts:
        print("error: refusing to overwrite differing paths:", file=sys.stderr)
        for target in conflicts:
            print(f"  {target}", file=sys.stderr)
        return 2

    action = "would create" if args.dry_run else "created"
    for source, target in pending:
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        print(f"{action}: {target}")

    for target in unchanged:
        print(f"unchanged: {target}")

    if not pending:
        print("feature specs are already initialized")
    elif not args.dry_run:
        print("next: adapt specs/README.md and add a project AGENTS.md routing rule if needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
