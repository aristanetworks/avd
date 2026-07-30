# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Test that all hosts in molecule scenarios use hyphens instead of underscores and are naturally sorted."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "eos_cli_config_gen",
    "eos_cli_config_gen_negative_unit_tests",
    "eos_cli_config_gen_deprecated_vars",
)
def test_host_naming_convention(molecule_host: MoleculeHost) -> None:
    """
    Test that all host names use hyphens instead of underscores and are lowercase.

    This ensures consistency in naming conventions across all molecule scenarios.
    Host names with underscores can cause issues in certain contexts and reduce readability.
    Host names must be lowercase to maintain consistency.
    """
    issues: list[str] = []
    suggested_name = molecule_host.name

    if "_" in molecule_host.name:
        issues.append("contains underscore")
        suggested_name = suggested_name.replace("_", "-")

    if molecule_host.name != molecule_host.name.lower():
        issues.append("contains uppercase letters")
        suggested_name = suggested_name.lower()

    assert not issues, (
        f"Host '{molecule_host.name}' in scenario '{molecule_host.scenario.name}' has naming issues: {', '.join(issues)}\n"
        f"Suggested name: {suggested_name}\n"
        "\nPlease rename this host to use hyphens (-) instead of underscores (_) and ensure it is lowercase."
    )
