# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Benchmark tests using an end-to-end AVD project."""

from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING

import pytest

from pyavd import get_device_config
from tools.e2e_test_avd import get_avd_facts_for_fabric, get_structured_config_for_device

if TYPE_CHECKING:
    from pytest_codspeed import BenchmarkFixture

    from benchmarks.conftest import BenchmarkProject

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
    "cv-pathfinder-transit1a",
    "cv-pathfinder-pathfinder1",
    "cv-pathfinder-edge1",
)


def test_molecule_scenario_avd_facts_benchmark(
    benchmark: BenchmarkFixture,
    benchmark_project: BenchmarkProject,
) -> None:
    """Benchmark fabric-wide AVD facts generation using the prepared end-to-end project."""
    source_data = [(fabric.inputs, fabric.hostvars, fabric.pool_manager) for fabric in benchmark_project.fabrics]
    fabric_data = source_data

    def setup() -> None:
        nonlocal fabric_data
        fabric_data = deepcopy(source_data)

    def run() -> None:
        facts_count = 0
        input_count = 0
        for fabric, (inputs, hostvars, pool_manager) in zip(benchmark_project.fabrics, fabric_data, strict=True):
            facts_count += len(get_avd_facts_for_fabric(fabric.config, inputs, hostvars, pool_manager))
            input_count += len(inputs)

        assert facts_count == input_count

    benchmark.pedantic(run, setup=setup, iterations=1, rounds=1, warmup_rounds=1)


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
    source_data = (inputs, hostvars, avd_facts)

    def setup() -> None:
        nonlocal inputs, hostvars, avd_facts
        inputs, hostvars, avd_facts = deepcopy(source_data)

    def run() -> None:
        structured_config = get_structured_config_for_device(
            hostname,
            inputs,
            hostvars,
            avd_facts,
            benchmark_fabric.config,
        )
        assert get_device_config(structured_config)

    benchmark.pedantic(run, setup=setup, iterations=1, warmup_rounds=1)
