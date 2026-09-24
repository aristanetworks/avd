# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Fixtures for benchmarking AVD."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

from pyavd.api.pool_manager import PoolManager
from pyavd.api.schemas import AVDDesign
from tools.e2e_test_avd import (
    AvdBuildContext,
    FabricConfig,
    FabricConfigOverrides,
    InlineExecutor,
    group_devices_per_fabric,
    load_config,
)

if TYPE_CHECKING:
    from collections.abc import Iterator

    from _pytest.terminal import TerminalReporter

logger = logging.getLogger(__name__)

E2E_PROJECT_DIR = Path(__file__).parents[1] / "ansible_collections/arista/avd/extensions/molecule/eos_designs_unit_tests"


@dataclass(frozen=True)
class BenchmarkFabric:
    """Prepared in-process representation of an end-to-end fabric."""

    config: FabricConfig
    inputs: dict[str, AVDDesign]
    hostvars: dict[str, dict[str, Any]]
    pool_manager: PoolManager

    @cached_property
    def avd_facts(self) -> dict[str, Any]:
        """Return cached fabric facts for per-device benchmarks."""
        from tools.e2e_test_avd import get_avd_facts_for_fabric

        return get_avd_facts_for_fabric(self.config, self.inputs, self.hostvars, self.pool_manager)


@dataclass(frozen=True)
class BenchmarkProject:
    """Prepared fabrics from an end-to-end project."""

    fabrics: tuple[BenchmarkFabric, ...]

    def fabric_for_device(self, device: str) -> BenchmarkFabric:
        """Return the fabric containing the requested device."""
        for fabric in self.fabrics:
            if device in fabric.inputs:
                return fabric

        msg = f"Device {device} was not found in the benchmark project"
        raise KeyError(msg)


@pytest.fixture(scope="session")
def benchmark_project() -> Iterator[BenchmarkProject]:
    """Load and validate the eos_designs_unit_tests project through the end-to-end framework."""
    project = load_config(E2E_PROJECT_DIR)
    scenario = next(scenario for scenario in project.scenarios if scenario.config.scenario_name == "main")
    context = AvdBuildContext(scenario.config, executor=InlineExecutor())
    try:
        benchmark_fabrics = []
        for fabric_name, devices in group_devices_per_fabric(context).items():
            fabric_config = FabricConfig.from_scenario(
                fabric_name,
                scenario.config,
                scenario.fabric_overrides.get(fabric_name, FabricConfigOverrides()),
            )
            all_inputs = {}
            all_hostvars = {}
            for device in devices:
                hostvars = context.inventory.get_vars(device)
                all_inputs[device] = AVDDesign._from_dict(hostvars)
                all_hostvars[device] = hostvars

            benchmark_fabrics.append(
                BenchmarkFabric(
                    config=fabric_config,
                    inputs=all_inputs,
                    hostvars=all_hostvars,
                    pool_manager=PoolManager(fabric_config.full_output_dir),
                )
            )

        yield BenchmarkProject(tuple(benchmark_fabrics))
    finally:
        context.close()


def pytest_terminal_summary(terminalreporter: TerminalReporter) -> None:
    """Display benchmark summary information."""
    terminalreporter.write_sep("=", "AVD Benchmark Summary")


def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest for benchmarking."""
    if config.getoption("--codspeed"):
        logging.disable(logging.CRITICAL)


def pytest_unconfigure(config: pytest.Config) -> None:
    """Re-enable logging after benchmarks."""
    if config.getoption("--codspeed"):
        logging.disable(logging.NOTSET)
