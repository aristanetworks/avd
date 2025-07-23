#!/usr/bin/env python3

# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Checks that all table markdown files are referenced in global documentation.")
    parser.add_argument("--root-path", type=Path, required=True, help="The relative path to the project's root directory from where pre-commit is run.")
    parser.add_argument("--table-files", nargs="+", required=True, help="Glob pattern for table markdown files.")
    parser.add_argument("--global-docs", nargs="+", required=True, help="Glob pattern for global documentation files.")
    parser.add_argument("--ignore-files", nargs="+", default=[], help="Glob pattern for table files to ignore.")
    args = parser.parse_args()

    project_root = args.root_path.resolve()

    table_files = {p.resolve() for glob in args.table_files for p in Path().glob(glob)}
    global_docs = {p.resolve() for glob in args.global_docs for p in Path().glob(glob)}
    ignored_files = {p.resolve() for glob in args.ignore_files for p in Path().glob(glob)}

    files_to_check = table_files - ignored_files

    if not files_to_check:
        print("No table files to check after ignoring. Skipping.", file=sys.stderr)  # noqa: T201
        return 0

    global_content = ""
    for doc_file in global_docs:
        global_content += doc_file.read_text(encoding="utf-8")

    unlinked_files: list[Path] = []
    for table_file in files_to_check:
        relative_path = table_file.relative_to(project_root)
        path_to_check = str(relative_path.as_posix())
        if path_to_check not in global_content:
            unlinked_files.append(table_file)

    if unlinked_files:
        print("\n--- Table Documentation Link Check: FAILED ---", file=sys.stderr)  # noqa: T201
        print("Error: The following table files are not linked by their relative path:", file=sys.stderr)  # noqa: T201
        for file in sorted(unlinked_files):
            print(f"- {file.relative_to(project_root).as_posix()}", file=sys.stderr)  # noqa: T201
        return 1

    print("Success: All table documentation files are linked.")  # noqa: T201
    return 0


if __name__ == "__main__":
    sys.exit(main())
