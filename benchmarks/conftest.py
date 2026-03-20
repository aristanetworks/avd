# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Fixtures for benchmarking AVD."""

from __future__ import annotations

import logging
import sys
from itertools import chain
from pathlib import Path

import pytest
from _pytest.terminal import TerminalReporter

# Add python-avd to path so we can import from tests.models
sys.path.insert(0, str(Path(__file__).parent.parent / "python-avd"))

from tests.models import MoleculeHost, MoleculeScenario

logger = logging.getLogger(__name__)

# Cache for MoleculeScenario instances (shared with main tests)
MOLECULE_SCENARIOS: dict[str, MoleculeScenario] = {}


@pytest.fixture(scope="session")
def benchmark_cache() -> dict:
    """Cache for expensive operations across benchmark tests."""
    return {
        "molecule_scenarios": {},
        "validated_inputs": {},
        "avd_facts": {},
    }


@pytest.fixture(scope="session")
def molecule_scenario_cache() -> dict[str, MoleculeScenario]:
    """Cache MoleculeScenario instances to avoid re-parsing."""
    return {}


@pytest.fixture(scope="session")
def benchmark_data_dir() -> Path:
    """Return the path to benchmark data directory."""
    return Path(__file__).parent / "data"


def pytest_terminal_summary(terminalreporter: TerminalReporter) -> None:
    """Display benchmark summary information."""
    terminalreporter.write_sep("=", "AVD Benchmark Summary")


def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest for benchmarking."""
    # Disable logging during benchmarks to avoid timing overhead
    if config.getoption("--codspeed"):
        logging.disable(logging.CRITICAL)


def pytest_unconfigure(config: pytest.Config) -> None:
    """Re-enable logging after benchmarks."""
    if config.getoption("--codspeed"):
        logging.disable(logging.NOTSET)


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
