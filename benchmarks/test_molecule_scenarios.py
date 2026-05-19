# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Benchmark tests for complete molecule scenarios.

These benchmarks test the full AVD workflow (validate → facts → structured_config → eos_config)
across various real-world molecule scenarios.
"""

from __future__ import annotations

import logging
import sys
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

from pyavd import get_device_config, get_device_structured_config, validate_inputs
from pyavd._schema.store import init_store
from pyavd.api.schemas import AVDDesign

if TYPE_CHECKING:
    from pytest_codspeed import BenchmarkFixture
    from tests.models import MoleculeHost

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


@pytest.mark.molecule_scenarios("eos_designs_unit_tests", hosts=REPRESENTATIVE_BENCHMARK_HOSTS)
def test_molecule_scenario_full_workflow_benchmark(
    benchmark: BenchmarkFixture,
    # molecule_scenario: "MoleculeScenario",
    molecule_host: MoleculeHost,
) -> None:
    """
    Benchmark complete AVD workflow for real molecule scenarios.

    Tests the full end-to-end workflow:
    1. Validate inputs for all devices
    2. Generate AVD facts
    3. Generate structured configs for all devices
    4. Render EOS configs for all devices

    This simulates the real-world usage of AVD across various deployment patterns.
    """
    logging.disable(logging.CRITICAL)
    init_store()

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

            # Step 4: Render EOS configs for all devices
            get_device_config(structured_config)

    benchmark.pedantic(b, iterations=5, warmup_rounds=1)  # type: ignore[reportAttributeAccessIssue]
    logging.disable(logging.NOTSET)
