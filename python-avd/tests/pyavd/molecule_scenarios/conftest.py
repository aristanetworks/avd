# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from itertools import chain

import pytest

from tests.models import MoleculeHost, MoleculeScenario

MOLECULE_SCENARIOS: dict[str, MoleculeScenario] = {}


def get_test_id(fixture: MoleculeHost | MoleculeScenario) -> str:
    match fixture:
        case MoleculeScenario():
            return f"{fixture.name}{'_digital_twin' if fixture.digital_twin else ''}__{fixture.name}"
        case MoleculeHost():
            return f"{fixture.scenario.name}{'_digital_twin' if fixture.scenario.digital_twin else ''}__{fixture.name}"


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """
    Generate MoleculeHost or MoleculeScenario instances for scenarios given with pytest.mark.molecule_scenarios(<scenario>, <scenario>, digital_twin=<bool>).

    The generated objects are inserted with parametrize to generate a test case for each.

    Reads/updates MOLECULE_SCENARIOS for caching.
    """
    molecule_scenarios: list[MoleculeScenario] = []
    for marker in metafunc.definition.iter_markers(name="molecule_scenarios"):
        for molecule_scenario_name in marker.args:
            if molecule_scenario_name not in MOLECULE_SCENARIOS:
                # Using this method since setdefault triggers init of the class which is expensive.
                MOLECULE_SCENARIOS[molecule_scenario_name] = MoleculeScenario(molecule_scenario_name)
            molecule_scenarios.append(MOLECULE_SCENARIOS[molecule_scenario_name])

    for marker in metafunc.definition.iter_markers(name="digital_twin_molecule_scenarios"):
        for molecule_scenario_name in marker.args:
            molecule_scenario_extended_name = f"{molecule_scenario_name}_digital_twin"
            if molecule_scenario_extended_name not in MOLECULE_SCENARIOS:
                # Using this method since setdefault triggers init of the class which is expensive.
                MOLECULE_SCENARIOS[molecule_scenario_extended_name] = MoleculeScenario(molecule_scenario_name, digital_twin=True)
            molecule_scenarios.append(MOLECULE_SCENARIOS[molecule_scenario_extended_name])

    if "molecule_host" in metafunc.fixturenames:
        metafunc.parametrize("molecule_host", chain.from_iterable(scenario.hosts for scenario in molecule_scenarios), ids=get_test_id)

    if "molecule_scenario" in metafunc.fixturenames:
        metafunc.parametrize("molecule_scenario", molecule_scenarios, ids=get_test_id)
