# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Test that all hosts in molecule scenarios use hyphens instead of underscores and are naturally sorted."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tests.models import MoleculeScenario


@pytest.mark.molecule_scenarios(
    # "eos_designs_unit_tests",
    "eos_designs_negative_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_cli_config_gen",
    "eos_cli_config_gen_negative_unit_tests",
    "eos_cli_config_gen_deprecated_vars",
)
def test_host_naming_convention(molecule_scenario: MoleculeScenario) -> None:
    """
    Test that all host names use hyphens instead of underscores and are lowercase.

    This ensures consistency in naming conventions across all molecule scenarios.
    Host names with underscores can cause issues in certain contexts and reduce readability.
    Host names must be lowercase to maintain consistency.
    """
    invalid_hosts: list[str] = []

    for host in molecule_scenario.hosts:
        issues = []
        suggested_name = host.name

        if "_" in host.name:
            issues.append("contains underscore")
            suggested_name = suggested_name.replace("_", "-")

        if host.name != host.name.lower():
            issues.append("contains uppercase letters")
            suggested_name = suggested_name.lower()

        if issues:
            invalid_hosts.append(f"  - {host.name} → {suggested_name} ({', '.join(issues)})")

    assert not invalid_hosts, (
        f"The following hosts in scenario '{molecule_scenario.name}' have naming issues:\n"
        + "\n".join(invalid_hosts)
        + "\n\nPlease rename these hosts to use hyphens (-) instead of underscores (_) and ensure they are lowercase."
    )
