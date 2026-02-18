#!/usr/bin/env python3

# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator

SPLIT_PATTERN = re.compile(r"(\d+)")


def _convert(text: str) -> int | str:
    """Convert text for sorting: digits to int, strings to lowercase."""
    return int(text) if text.isdigit() else text.lower()


def _alphanum_key(item: dict[str, str], sort_key: str) -> list[int | str]:
    """Generate natural sort key for a dictionary item."""
    val = item.get(sort_key, "")
    return [_convert(part) for part in SPLIT_PATTERN.split(str(val))]


def natural_sort(iterable: list[dict[str, str]], sort_key: str) -> list[dict[str, str]]:
    """Sort an iterable using natural (alphanumeric) ordering with case-insensitive comparison."""
    return sorted(iterable, key=lambda item: _alphanum_key(item, sort_key))


class HostsParser:
    """Parser for extracting and sorting hosts from YAML content."""

    def __init__(self, lines: list[str], start_index: int, indent: str) -> None:
        """
        Initialize the parser.

        Args:
            lines: All lines in the YAML file
            start_index: Index to start parsing from (line after "hosts:")
            indent: Base indentation level for the hosts section
        """
        self.lines = lines
        self.index = start_index
        self.host_indent = indent + "  "
        self.property_indent = self.host_indent + "  "

    def parse(self) -> tuple[list[dict[str, str | list[str]]], int]:
        """
        Parse hosts and return sorted host blocks with final index.

        Returns:
            Tuple of (list of host dictionaries, final index position)
        """
        hosts_block: list[dict[str, str | list[str]]] = []
        pending_lines: list[str] = []

        while self.index < len(self.lines):
            line = self.lines[self.index]

            # Handle comments and blank lines
            if self._is_comment_or_blank(line):
                pending_lines.append(line)
                self.index += 1
                continue

            # Check for host entry
            if host_name := self._extract_host_name(line):
                host_lines = [*pending_lines, line]
                pending_lines = []
                self.index += 1

                # Collect host properties
                host_lines.extend(self._collect_properties())
                hosts_block.append({"name": host_name, "lines": host_lines})
            else:
                # End of hosts section
                break

        return hosts_block, self.index

    def _is_comment_or_blank(self, line: str) -> bool:
        """Check if line is a comment or blank at host indent level."""
        return line.strip() == "" or (line.strip().startswith("#") and line.startswith(self.host_indent))

    def _extract_host_name(self, line: str) -> str | None:
        """
        Extract host name from a line if it's a valid host entry.

        Returns:
            Host name if valid host entry, None otherwise
        """
        if not line.startswith(self.host_indent) or line.strip().startswith("#"):
            return None

        stripped = line[len(self.host_indent) :]
        # Check if it's a host entry (not a child key like "children:")
        if stripped and not stripped[0].isspace():
            return stripped.split(":")[0].strip()
        return None

    def _collect_properties(self) -> Iterator[str]:
        """Collect all property lines for the current host."""
        while self.index < len(self.lines):
            line = self.lines[self.index]
            if line.startswith(self.property_indent):
                yield line
                self.index += 1
            else:
                break


def sort_hosts_in_yaml(content: str) -> str:
    """
    Sort hosts in YAML content while preserving formatting, comments, and blank lines.

    Hosts are sorted using case-insensitive natural (alphanumeric) ordering.

    Args:
        content: YAML file content as a string

    Returns:
        Content with sorted hosts sections
    """
    lines = content.splitlines(keepends=True)
    result: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        result.append(line)

        # Check for "hosts:" line
        if hosts_match := re.match(r"^(\s*)hosts:\s*(?:#.*)?$", line):
            indent = hosts_match.group(1)
            parser = HostsParser(lines, i + 1, indent)
            hosts_block, i = parser.parse()

            # Sort and append hosts (case-insensitive)
            sorted_hosts = natural_sort(hosts_block, sort_key="name")
            for host in sorted_hosts:
                result.extend(host["lines"])
            continue

        i += 1

    return "".join(result)


def process_files(files: set[Path]) -> list[Path]:
    """
    Process and sort hosts in the given files.

    Args:
        files: Set of file paths to process

    Returns:
        List of modified files
    """
    modified_files: list[Path] = []

    for file_path in sorted(files):
        if not file_path.exists():
            print(f"Error: File not found: {file_path}", file=sys.stderr)  # noqa: T201
            sys.exit(1)

        try:
            original_content = file_path.read_text(encoding="utf-8")
            sorted_content = sort_hosts_in_yaml(original_content)

            if original_content != sorted_content:
                file_path.write_text(sorted_content, encoding="utf-8")
                modified_files.append(file_path)

        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)  # noqa: T201
            sys.exit(1)

    return modified_files


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Auto-sort host names in Ansible inventory hosts.yml files.")
    parser.add_argument("files", nargs="*", type=Path, help="Files to sort (passed by pre-commit)")
    parser.add_argument("--include-files", nargs="+", help="Glob pattern for hosts.yml files to sort.")
    parser.add_argument("--ignore-files", nargs="+", default=[], help="Glob pattern for hosts.yml files to ignore.")
    args = parser.parse_args()

    # Collect files to process
    if args.files:
        # Files passed directly (e.g., by pre-commit)
        include_files = {f.resolve() for f in args.files}
    elif args.include_files:
        # Files specified via glob patterns
        include_files = {p.resolve() for glob in args.include_files for p in Path().glob(glob)}
    else:
        # No files to process
        return 0

    ignore_files = {p.resolve() for glob in args.ignore_files for p in Path().glob(glob)}
    files_to_process = include_files - ignore_files

    if not files_to_process:
        return 0

    modified_files = process_files(files_to_process)

    if modified_files:
        print("\n--- Host Sorting: Files Modified ---", file=sys.stderr)  # noqa: T201
        print("The following files had unsorted hosts and have been automatically sorted:", file=sys.stderr)  # noqa: T201
        for file in modified_files:
            print(f"- {file}", file=sys.stderr)  # noqa: T201
        print("\nPlease review the changes and stage them.", file=sys.stderr)  # noqa: T201
        return 1

    # Silent success - no output when files are already sorted
    return 0


if __name__ == "__main__":
    sys.exit(main())
