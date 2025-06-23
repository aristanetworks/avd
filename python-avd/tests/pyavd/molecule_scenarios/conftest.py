# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from itertools import chain

import pytest

from tests.models import MoleculeHost, MoleculeScenario

MOLECULE_SCENARIOS: dict[str, MoleculeScenario] = {}


def get_test_id(host: MoleculeHost) -> str:
    return f"{host.scenario.name}__{host.name}"


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """
    Generate MoleculeHost or MoleculeScenario instances for the scenarios given with pytest.mark.molecule_scenarios(<scenario>, <scenario>).

    The generated objects are inserted with parametrize to generate a test case for each.

    Reads/updates MOLECULE_SCENARIOS for caching.
    """
    molecule_scenarios: list[MoleculeScenario] = []

    for marker in metafunc.definition.iter_markers(name="molecule_scenarios"):
        for arg in marker.args:
            artifacts_path_offset = ""
            if isinstance(arg, str):
                molecule_scenario_name = arg
            elif isinstance(arg, tuple):
                if len(arg) != 2:
                    msg = f"molecule_scenarios marker error: Length of the tuple must be 2. Provided tuple: '{arg}'"
                    raise ValueError(msg)
                molecule_scenario_name = arg[0]
                if not isinstance(molecule_scenario_name, str):
                    msg = (
                        "molecule_scenarios marker error: Scenario's name must be provided as a 'str'. "
                        f"Actual input ('{molecule_scenario_name}') has type '{type(molecule_scenario_name)}'"
                    )
                    raise TypeError(msg)
                artifacts_path_offset = arg[1]
                if not isinstance(artifacts_path_offset, str):
                    msg = (
                        "molecule_scenarios marker error: Scenario's path offset must be provided as a 'str'. "
                        f"Actual input ('{artifacts_path_offset}') has type '{type(artifacts_path_offset)}'"
                    )
                    raise TypeError(msg)
            else:
                msg = (
                    "molecule_scenarios marker error: Accepted formats: <str> (molecule scenario name) OR "
                    "<tuple[str, str]> (molecule scenario name followed by the path offset)."
                )
                raise TypeError(msg)

            molecule_scenario_extended_name = molecule_scenario_name + artifacts_path_offset
            if molecule_scenario_extended_name not in MOLECULE_SCENARIOS:
                # Using this method since setdefault triggers init of the class which is expensive.
                MOLECULE_SCENARIOS[molecule_scenario_extended_name] = MoleculeScenario(molecule_scenario_name, artifacts_path_offset)
            molecule_scenarios.append(MOLECULE_SCENARIOS[molecule_scenario_extended_name])

    if "molecule_host" in metafunc.fixturenames:
        metafunc.parametrize("molecule_host", chain.from_iterable(scenario.hosts for scenario in molecule_scenarios), ids=get_test_id)

    if "molecule_scenario" in metafunc.fixturenames:
        metafunc.parametrize("molecule_scenario", molecule_scenarios, ids=lambda scenario: scenario.name)
