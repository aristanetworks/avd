# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Benchmark tests for complete molecule scenarios.

These benchmarks test per-host config generation and rendering with cached fabric facts
across representative real-world molecule hosts.
"""

from __future__ import annotations

import logging
import sys
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any
from unittest.mock import patch

import pytest

from pyavd import get_avd_facts, get_device_config, get_device_structured_config, validate_inputs
from pyavd.api.schemas import AVDDesign

if TYPE_CHECKING:
    from collections.abc import Iterator

    from pytest_codspeed import BenchmarkFixture
    from tests.models import MoleculeHost, MoleculeScenario

logger = logging.getLogger(__name__)

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


def get_molecule_scenario_inputs(molecule_scenario: MoleculeScenario) -> tuple[dict[str, AVDDesign], dict[str, dict[str, Any]]]:
    """Return loaded inputs and hostvars for all hosts in a molecule scenario."""
    all_inputs = {}
    all_hostvars = {}

    for host in molecule_scenario.hosts:
        hostvars = host.hostvars
        validated_data_result = validate_inputs(hostvars)
        assert validated_data_result.validated_data is not None
        all_inputs[host.name] = AVDDesign._from_dict(validated_data_result.validated_data)
        all_hostvars[host.name] = hostvars

    return all_inputs, all_hostvars


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_molecule_scenario_avd_facts_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: MoleculeScenario,
) -> None:
    """
    Benchmark fabric-wide AVD facts generation for the full eos_designs_unit_tests scenario.

    Input validation and model loading are prepared outside the timed path, so
    this benchmark tracks the facts generation pass itself.
    """
    with disabled_logging():
        all_inputs, all_hostvars = get_molecule_scenario_inputs(molecule_scenario)

        def _() -> None:
            with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
                avd_facts = get_avd_facts(
                    all_inputs=all_inputs,
                    all_hostvars=all_hostvars,
                    pool_manager=molecule_scenario.pool_manager,
                    digital_twin=molecule_scenario.digital_twin,
                )

            assert len(avd_facts) == len(molecule_scenario.hosts)

        benchmark(_)


@pytest.mark.molecule_scenarios("eos_designs_unit_tests", hosts=REPRESENTATIVE_BENCHMARK_HOSTS)
def test_molecule_host_config_render_benchmark(
    benchmark: BenchmarkFixture,
    molecule_host: MoleculeHost,
) -> None:
    """
    Benchmark per-host AVD config generation for real molecule scenario hosts.

    Fabric facts are prepared by the molecule scenario fixture outside the timed
    path, so this benchmark tracks per-host validation, structured config
    generation, and EOS config rendering.
    """

    def b() -> None:
        hostvars = molecule_host.hostvars

        # Validate inputs
        validated_data_result = validate_inputs(hostvars)

        assert validated_data_result.validated_data is not None

        design = AVDDesign._from_dict(validated_data_result.validated_data)

        with patch("sys.path", [*sys.path, *molecule_host.scenario.extra_python_paths]):
            avd_facts = molecule_host.scenario.avd_facts
            structured_config = get_device_structured_config(
                molecule_host.name, design, avd_facts, hostvars=hostvars, digital_twin=molecule_host.scenario.digital_twin
            )

            get_device_config(structured_config)

    with disabled_logging():
        benchmark.pedantic(b, iterations=5, warmup_rounds=1)  # type: ignore[reportAttributeAccessIssue]
