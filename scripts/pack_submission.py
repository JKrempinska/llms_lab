#!/usr/bin/env python3
"""Submission Packager for LLM Lab Lists.

Usage:
    uv run python scripts/pack_submission.py list01
"""

import argparse
import json
import os
import sys
import zipfile
from pathlib import Path


def check_notebook_outputs(nb_path: Path) -> None:
    """Warn if the notebook seems not to have been executed."""
    try:
        data = json.loads(nb_path.read_text(encoding="utf-8"))
        code_cells = [c for c in data.get("cells", []) if c.get("cell_type") == "code"]
        unexecuted = [c for c in code_cells if not c.get("outputs") and c.get("execution_count") is None]
        if code_cells and len(unexecuted) == len(code_cells):
            print("\n⚠️  WARNING: All code cells in your notebook appear UNEXECUTED!")
            print("   Remember the instruction: 'Submit this notebook run from top to bottom with outputs'.")
            print("   Please execute the notebook before final submission.\n")
        elif unexecuted:
            print(f"\nℹ️  Notice: {len(unexecuted)} of {len(code_cells)} code cells have no outputs saved.")
    except Exception as e:
        print(f"Could not inspect notebook: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Package an exercise list for submission.")
    parser.add_argument("list_name", help="Name of list folder (e.g. list01)")
    parser.add_argument(
        "--output",
        "-o",
        help="Custom output zip path (default: <list_name>_submission.zip)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    list_dir = repo_root / args.list_name

    if not list_dir.is_dir():
        print(f"Error: Directory '{list_dir}' does not exist.")
        sys.exit(1)

    nb_candidates = list(list_dir.glob("*.ipynb"))
    if not nb_candidates:
        print(f"Warning: No .ipynb file found inside {list_dir}")
    else:
        for nb in nb_candidates:
            check_notebook_outputs(nb)

    out_name = args.output or f"{args.list_name}_submission.zip"
    out_path = repo_root / out_name

    # Files to exclude from the submission zip
    ignored_patterns = {
        ".ipynb_checkpoints",
        ".DS_Store",
        "__pycache__",
        ".venv",
    }

    files_added = []
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(list_dir):
            # prune ignored directories
            dirs[:] = [d for d in dirs if d not in ignored_patterns and not d.startswith(".")]

            for file in files:
                if any(ignored in file for ignored in ignored_patterns) or file.startswith("."):
                    continue
                # Skip source pdf materials if large, but keep assignments if desired
                # Keep everything inside list_dir
                full_path = Path(root) / file
                rel_path = full_path.relative_to(repo_root)
                zipf.write(full_path, arcname=str(rel_path))
                files_added.append(str(rel_path))

    size_kb = out_path.stat().st_size / 1024
    print(f"\n✅ Packaged submission archive: {out_path.name} ({size_kb:.1f} KB)")
    print("Files included:")
    for f in sorted(files_added):
        print(f"  - {f}")
    print(f"\nYou can now submit '{out_path.name}' to your professor / e-portal!")


if __name__ == "__main__":
    main()
