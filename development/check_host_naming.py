#!/usr/bin/env python3

# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Pre-commit hook to ensure all hosts in hosts.yml files use hyphens instead of underscores."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml

if TYPE_CHECKING:
    from collections.abc import Generator

VALID_YAML_EXTENSIONS: set[str] = {".yml", ".yaml"}
Violation = tuple[str, int]  # (invalid_host_name, line_number)


def _has_underscore(name: str) -> bool:
    """Check if a name contains an underscore."""
    return "_" in name


def _suggest_fix(name: str) -> str:
    """Suggest a fixed name by replacing underscores with hyphens."""
    return name.replace("_", "-")


def _find_all_line_numbers(file_content: str, host_name: str) -> list[int]:
    """
    Find all line numbers where a host name appears in the file.

    Args:
        file_content: The file content as a string
        host_name: The host name to search for

    Returns:
        List of line numbers (1-indexed) where the host name appears
    """
    line_numbers = []
    for line_num, line in enumerate(file_content.splitlines(), start=1):
        # Look for the host name as a YAML key (with colon) or standalone
        stripped = line.strip()
        if stripped == f"{host_name}:" or stripped.startswith(f"{host_name}:") or stripped == host_name:
            line_numbers.append(line_num)
    return line_numbers


def _validate_hosts_section(value: Any) -> Generator[str, None, None]:
    """
    Validate a hosts section and yield invalid host names.

    Args:
        value: The hosts section value (dict or string)

    Yields:
        Invalid host names that contain underscores

    Examples:
        >>> list(_validate_hosts_section({"host_1": None, "host-2": None}))
        ['host_1']
        >>> list(_validate_hosts_section("test_host"))
        ['test_host']
    """
    if isinstance(value, dict):
        # Check each host name in this hosts section (dict keys are always strings)
        yield from (str(host_name) for host_name in value if _has_underscore(str(host_name)))
    elif isinstance(value, str) and _has_underscore(value):
        # Single host as string (like "l3_edge")
        yield value


def check_hosts_for_underscores(data: Any) -> Generator[str, None, None]:
    """
    Recursively check YAML data for 'hosts' sections and validate host names.

    Args:
        data: The YAML data structure to check (dict, list, str, or None)

    Yields:
        Invalid host names that contain underscores

    Examples:
        >>> data = {"all": {"hosts": {"host_1": None}}}
        >>> list(check_hosts_for_underscores(data))
        ['host_1']
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "hosts":
                # Validate hosts section
                yield from _validate_hosts_section(value)
            else:
                # Recursively check nested structures
                yield from check_hosts_for_underscores(value)

    elif isinstance(data, list):
        # Check list items
        for item in data:
            yield from check_hosts_for_underscores(item)


def process_file(file_path: Path) -> list[Violation]:
    """
    Process a single YAML file and return violations with line numbers.

    Args:
        file_path: Path to the YAML file

    Returns:
        List of tuples containing (invalid_host_name, line_number) for violations

    Raises:
        yaml.YAMLError: If the YAML file cannot be parsed
        OSError: If the file cannot be read
    """
    # Read file content for line number lookup
    file_content = file_path.read_text(encoding="utf-8")

    # Parse YAML data
    data = yaml.safe_load(file_content)

    if data is None:
        return []

    # Find all invalid host names
    invalid_hosts = list(check_hosts_for_underscores(data))

    # Map each invalid host to its line numbers (deduplicate by using a dict)
    host_line_map: dict[str, list[int]] = {}
    for host_name in invalid_hosts:
        if host_name not in host_line_map:
            host_line_map[host_name] = _find_all_line_numbers(file_content, host_name)

    # Create violations list with all unique (host, line) combinations
    violations: list[Violation] = [(host_name, line_num) for host_name, line_numbers in host_line_map.items() for line_num in line_numbers]

    return violations


def report_violations(all_violations: list[tuple[str, list[Violation]]]) -> None:
    """
    Print a formatted report of all violations.

    Args:
        all_violations: List of (file_path, violations) tuples
    """
    print("The following hosts use underscores instead of hyphens:")  # noqa: T201

    for file_path, violations in all_violations:
        print(f"File: {file_path}")  # noqa: T201
        for host_name, line_num in violations:
            suggested_name = _suggest_fix(host_name)
            if line_num > 0:
                print(f"  Line {line_num}: '{host_name}' → '{suggested_name}'")  # noqa: T201
            else:
                print(f"  '{host_name}' → '{suggested_name}'")  # noqa: T201


def main() -> int:
    """
    Main function to process files and check for host naming violations.

    Returns:
        Exit code: 0 if no violations found, 1 if violations found or errors occurred
    """
    parser = argparse.ArgumentParser(
        description="Check that all hosts in Ansible inventory YAML files use hyphens instead of underscores.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s hosts.yml
  %(prog)s inventory/*.yml
  pre-commit run check-host-naming --files inventory/hosts.yml
        """,
    )
    parser.add_argument(
        "files",
        nargs="+",
        type=Path,
        metavar="FILE",
        help="YAML file(s) to check",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Suppress output, only return exit code",
    )

    args = parser.parse_args()

    # Collect files to process
    files_to_check: set[Path] = set(args.files)

    all_violations: list[tuple[str, list[Violation]]] = []

    for file_path in sorted(files_to_check):
        # Only check YAML files
        if file_path.suffix not in VALID_YAML_EXTENSIONS:
            continue

        try:
            violations = process_file(file_path)

            if violations:
                all_violations.append((str(file_path), violations))

        except yaml.YAMLError as e:
            if not args.quiet:
                print(f"Error: Failed to parse YAML file '{file_path}': {e}", file=sys.stderr)  # noqa: T201
            return 1
        except OSError as e:
            if not args.quiet:
                print(f"Error: Failed to read file '{file_path}': {e}", file=sys.stderr)  # noqa: T201
            return 1

    # Report violations
    if all_violations:
        if not args.quiet:
            report_violations(all_violations)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
