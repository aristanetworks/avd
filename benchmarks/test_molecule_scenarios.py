# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Benchmark tests using an end-to-end AVD project."""

from __future__ import annotations

import logging
from contextlib import contextmanager
from typing import TYPE_CHECKING, Protocol

import pytest

from pyavd import get_device_config
from tools.e2e_test_avd import get_avd_facts_for_fabric, get_structured_config_for_device

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator

    from benchmarks.conftest import BenchmarkProject

logger = logging.getLogger(__name__)


class BenchmarkFixture(Protocol):
    """Subset of the CodSpeed benchmark fixture used by these tests."""

    def pedantic(self, target: Callable[[], None], *, iterations: int, rounds: int = 1, warmup_rounds: int = 0) -> None: ...


REPRESENTATIVE_BENCHMARK_HOSTS = (
    # Baseline data center fabric roles.
    "dc1-spine1",
    "dc1-leaf1a",
    "dc1-l2leaf1a",
    # Network services and connected endpoints.
    "bgp-from-network-services-1",
    "connected-endpoints",
    # Custom Python modules and rendering-heavy feature coverage.
    "custom-python-modules-l3leaf1a",
    "overlay-routing-protocol-her-l3leaf3a",
    "ptp-tests-leaf1",
    "trunk-group-tests-l3leaf1a",
    "uplink-p2p-vrfs-tests-leaf1",
    # WAN/CV Pathfinder coverage.
    "cv-pathfinder-pathfinder1",
    "cv-pathfinder-edge1",
    "cv-pathfinder-transit1a",
)


@contextmanager
def disabled_logging() -> Iterator[None]:
    """Temporarily disable logging without discarding the runner's previous setting."""
    previous_disable_level = logging.root.manager.disable
    logging.disable(logging.CRITICAL)
    try:
        yield
    finally:
        logging.disable(previous_disable_level)


@pytest.mark.parametrize("_scenario", [None], ids=["eos_designs_unit_tests__eos_designs_unit_tests"])
def test_molecule_scenario_avd_facts_benchmark(
    benchmark: BenchmarkFixture,
    benchmark_project: BenchmarkProject,
    _scenario: None,
) -> None:
    """Benchmark fabric-wide AVD facts generation using the prepared end-to-end project."""

    def run() -> None:
        facts_count = 0
        input_count = 0
        for fabric in benchmark_project.fabrics:
            facts_count += len(get_avd_facts_for_fabric(fabric.config, fabric.inputs, fabric.hostvars, fabric.pool_manager))
            input_count += len(fabric.inputs)

        assert facts_count == input_count

    with disabled_logging():
        benchmark.pedantic(run, iterations=1, rounds=1, warmup_rounds=0)


@pytest.mark.parametrize(
    "hostname",
    REPRESENTATIVE_BENCHMARK_HOSTS,
    ids=[f"eos_designs_unit_tests__{hostname}" for hostname in REPRESENTATIVE_BENCHMARK_HOSTS],
)
def test_molecule_host_config_render_benchmark(
    benchmark: BenchmarkFixture,
    benchmark_project: BenchmarkProject,
    hostname: str,
) -> None:
    """Benchmark per-device structured configuration and EOS CLI generation through the end-to-end stages."""
    benchmark_fabric = benchmark_project.fabric_for_device(hostname)
    inputs = benchmark_fabric.inputs[hostname]
    hostvars = benchmark_fabric.hostvars[hostname]
    avd_facts = benchmark_fabric.avd_facts

    def run() -> None:
        structured_config = get_structured_config_for_device(
            hostname,
            inputs,
            hostvars,
            avd_facts,
            benchmark_fabric.config,
        )
        assert get_device_config(structured_config)

    with disabled_logging():
        benchmark.pedantic(run, iterations=5, warmup_rounds=1)
