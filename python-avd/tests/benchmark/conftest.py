# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Fixtures for benchmarking AVD."""

import logging
from pathlib import Path

import pytest
from _pytest.terminal import TerminalReporter

from tests.models import MoleculeScenario

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


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """Handle molecule_scenario fixture for benchmark tests (same as main tests)."""
    if "molecule_scenario" in metafunc.fixturenames:
        molecule_scenarios: list[MoleculeScenario] = []
        for marker in metafunc.definition.iter_markers(name="molecule_scenarios"):
            for molecule_scenario_name in marker.args:
                if molecule_scenario_name not in MOLECULE_SCENARIOS:
                    MOLECULE_SCENARIOS[molecule_scenario_name] = MoleculeScenario(molecule_scenario_name)
                molecule_scenarios.append(MOLECULE_SCENARIOS[molecule_scenario_name])

        if molecule_scenarios:
            metafunc.parametrize("molecule_scenario", molecule_scenarios)
