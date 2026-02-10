#!/usr/bin/env python3
# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Extract requirements from pyproject.toml and write to requirements.txt.

This script reads the pyproject.toml file, extracts all dependencies including
optional dependencies, and writes them to a requirements.txt file.
"""

import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore[import-not-found]


def extract_requirements(pyproject_path: Path, output_path: Path) -> None:
    """
    Extract requirements from pyproject.toml and write to requirements.txt.

    Args:
        pyproject_path: Path to the pyproject.toml file
        output_path: Path to the output requirements.txt file
    """
    # Read pyproject.toml
    with pyproject_path.open("rb") as f:
        data = tomllib.load(f)

    requirements = []

    # Extract main dependencies
    if "project" in data and "dependencies" in data["project"]:
        requirements.extend(data["project"]["dependencies"])

    # Extract optional dependencies (ansible and ansible-collection)
    if "project" in data and "optional-dependencies" in data["project"]:
        optional_deps = data["project"]["optional-dependencies"]

        # Add ansible dependencies (excluding self-references like pyavd[ansible-collection])
        if "ansible" in optional_deps:
            requirements.extend(dep for dep in optional_deps["ansible"] if dep != "pyavd[ansible-collection]")

        # Add ansible-collection dependencies
        if "ansible-collection" in optional_deps:
            requirements.extend(optional_deps["ansible-collection"])

    # Remove duplicates while preserving order
    seen = set()
    unique_requirements = []
    for req in requirements:
        if req not in seen:
            seen.add(req)
            unique_requirements.append(req)

    # Write to requirements.txt
    with output_path.open("w") as f:
        for req in unique_requirements:
            f.write(f"{req}\n")


if __name__ == "__main__":
    # Get pyproject.toml path from pre-commit (first argument)
    if len(sys.argv) > 1:
        pyproject_path = Path(sys.argv[1])
    else:
        # Fallback for manual execution
        script_dir = Path(__file__).parent
        pyproject_path = script_dir.parent / "python-avd" / "pyproject.toml"

    # Output path is always relative to script location
    script_dir = Path(__file__).parent
    output_path = script_dir / "requirements.txt"

    # Check if pyproject.toml exists
    if not pyproject_path.exists():
        msg = f"Error: {pyproject_path} not found"
        raise FileNotFoundError(msg)

    # Extract requirements
    extract_requirements(pyproject_path, output_path)
