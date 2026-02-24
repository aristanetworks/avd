#!/usr/bin/env python3

# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Override global path to load pyavd from pwd instead of any installed version.
sys.path.insert(0, str(Path(__file__).parent.parent / "python-avd"))

from pyavd.j2filters.natural_sort import natural_sort

# Pre-compile regex patterns for better performance
HOSTS_PATTERN = re.compile(r"^(\s*)hosts:\s*(?:#.*)?$")
CHILDREN_PATTERN = re.compile(r"^(\s*)children:\s*(?:#.*)?$")


class EntriesParser:
    """Parser for extracting and sorting entries (hosts or groups) from YAML content."""

    def __init__(self, lines: list[str], start_index: int, indent: str) -> None:
        """
        Initialize the parser.

        Args:
            lines: All lines in the YAML file
            start_index: Index to start parsing from (line after "hosts:" or "children:")
            indent: Base indentation level for the section
        """
        self.lines = lines
        self.index = start_index
        self.entry_indent = indent + "  "
        self.property_indent = self.entry_indent + "  "

    def parse(self) -> tuple[list[dict[str, str | list[str]]], int]:
        """
        Parse entries and return sorted entry blocks with final index.

        Returns:
            Tuple of (list of entry dictionaries, final index position)
        """
        entries_block: list[dict[str, str | list[str]]] = []
        pending_lines: list[str] = []

        while self.index < len(self.lines):
            line = self.lines[self.index]

            # Handle comments and blank lines
            if self._is_comment_or_blank(line):
                pending_lines.append(line)
                self.index += 1
                continue

            # Check for entry
            if entry_name := self._extract_entry_name(line):
                entry_lines = [*pending_lines, line]
                pending_lines = []
                self.index += 1

                # Collect entry properties
                entry_lines.extend(self._collect_properties())
                entries_block.append({"name": entry_name, "lines": entry_lines})
            else:
                # End of section
                break

        return entries_block, self.index

    def _is_comment_or_blank(self, line: str) -> bool:
        """Check if line is a comment or blank at entry indent level."""
        stripped_line = line.strip()
        return not stripped_line or stripped_line.startswith("#")

    def _extract_entry_name(self, line: str) -> str | None:
        """
        Extract entry name from a line if it's a valid entry.

        Returns:
            Entry name if valid entry, None otherwise
        """
        if not line.startswith(self.entry_indent) or line.strip().startswith("#"):
            return None

        stripped = line[len(self.entry_indent) :]
        # Check if it's an entry (not a child key like "children:" or "hosts:")
        if stripped and not stripped[0].isspace():
            return stripped.split(":", 1)[0]
        return None

    def _collect_properties(self) -> list[str]:
        """Collect all property lines for the current entry."""
        properties = []
        while self.index < len(self.lines):
            line = self.lines[self.index]
            if line.startswith(self.property_indent):
                properties.append(line)
                self.index += 1
            else:
                break
        return properties


def _sort_yaml_lines(lines: list[str], start_idx: int = 0, end_idx: int | None = None) -> list[str]:
    """
    Sort hosts and children in YAML lines while preserving formatting.

    This internal function works directly with line arrays to avoid join/split overhead.

    Args:
        lines: List of YAML lines (with line endings)
        start_idx: Starting index to process
        end_idx: Ending index (exclusive), None for end of list

    Returns:
        List of sorted lines
    """
    if end_idx is None:
        end_idx = len(lines)

    result: list[str] = []
    i = start_idx

    while i < end_idx:
        line = lines[i]
        result.append(line)

        # Check for "hosts:" line
        if hosts_match := HOSTS_PATTERN.match(line):
            indent = hosts_match.group(1)
            parser = EntriesParser(lines, i + 1, indent)
            hosts_block, i = parser.parse()

            # Sort and append hosts
            sorted_hosts = natural_sort(hosts_block, sort_key="name")
            for host in sorted_hosts:
                # Process nested blocks within host properties
                host_lines = host["lines"]
                sorted_lines = _sort_yaml_lines(host_lines, 0, len(host_lines))
                result.extend(sorted_lines)
            continue

        # Check for "children:" line
        if children_match := CHILDREN_PATTERN.match(line):
            indent = children_match.group(1)
            parser = EntriesParser(lines, i + 1, indent)
            children_block, i = parser.parse()

            # Sort and append children
            sorted_children = natural_sort(children_block, sort_key="name")
            for child in sorted_children:
                # Process nested blocks within child properties
                child_lines = child["lines"]
                sorted_lines = _sort_yaml_lines(child_lines, 0, len(child_lines))
                result.extend(sorted_lines)
            continue

        i += 1

    return result


def sort_hosts_in_yaml(content: str) -> str:
    """
    Sort hosts and children in YAML content while preserving formatting, comments, and blank lines.

    Both hosts and group names under children are sorted using case-insensitive natural (alphanumeric) ordering.
    Sorting is applied recursively to all nested children and hosts blocks.

    Args:
        content: YAML file content as a string

    Returns:
        Content with sorted hosts and children sections
    """
    lines = content.splitlines(keepends=True)
    sorted_lines = _sort_yaml_lines(lines)
    return "".join(sorted_lines)


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
    parser = argparse.ArgumentParser(description="Auto-sort host names and group names in Ansible inventory hosts.yml files.")
    parser.add_argument("files", nargs="*", type=Path, help="Files to sort (passed by pre-commit)")
    args = parser.parse_args()

    # Collect files to process
    if not args.files:
        return 0

    files_to_process = {f.resolve() for f in args.files}
    modified_files = process_files(files_to_process)

    if modified_files:
        print("\n--- Host and Group Sorting: Files Modified ---", file=sys.stderr)  # noqa: T201
        print("The following files had unsorted hosts/groups and have been automatically sorted:", file=sys.stderr)  # noqa: T201
        for file in modified_files:
            print(f"- {file}", file=sys.stderr)  # noqa: T201
        print("\nPlease review the changes and stage them.", file=sys.stderr)  # noqa: T201
        return 1

    # Silent success - no output when files are already sorted
    return 0


if __name__ == "__main__":
    sys.exit(main())
