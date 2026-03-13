# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Benchmark tests for complete molecule scenarios.

These benchmarks test the full AVD workflow (validate → facts → structured_config → eos_config)
across various real-world molecule scenarios.
"""

import logging
import sys
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest
from pytest_codspeed import BenchmarkFixture

from pyavd import get_avd_facts, get_device_config, get_device_structured_config, validate_inputs

if TYPE_CHECKING:
    from tests.models import MoleculeScenario

logger = logging.getLogger(__name__)


@pytest.mark.molecule_scenarios(
    # EOS Designs scenarios (excluding negative tests and deprecated vars)
    "eos_designs_unit_tests",
    "eos_designs-l2ls",
    "eos_designs-mpls-isis-sr-ldp",
    "eos_designs-twodc-5stage-clos",
    # EVPN scenarios
    "evpn_underlay_ebgp_overlay_ebgp",
    "evpn_underlay_isis_overlay_ibgp",
    "evpn_underlay_ospf_overlay_ebgp",
    "evpn_underlay_rfc5549_overlay_ebgp",
    # Example scenarios
    "example-campus-fabric",
    "example-cv-pathfinder",
    "example-dual-dc-l3ls",
    "example-isis-ldp-ipvpn",
    "example-l2ls-fabric",
    "example-single-dc-l3ls",
    "example-single-dc-l3ls-ipv6",
)
def test_molecule_scenario_full_workflow_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
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
    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        # Disable logging during benchmark
        logging.disable(logging.CRITICAL)

        @benchmark
        def _() -> None:
            # Step 1: Validate inputs for all devices
            all_inputs = {}
            all_hostvars = {}
            for host in molecule_scenario.hosts:
                validated_result = validate_inputs(host.hostvars)
                if validated_result.validated_data:
                    all_inputs[host.name] = validated_result.validated_data
                    all_hostvars[host.name] = host.hostvars

            # Step 2: Generate AVD facts
            avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=molecule_scenario.pool_manager)

            # Step 3: Generate structured configs for all devices
            structured_configs = {}
            for hostname, inputs in all_inputs.items():
                structured_configs[hostname] = get_device_structured_config(
                    hostname=hostname,
                    inputs=inputs,
                    avd_facts=avd_facts,
                )

            # Step 4: Render EOS configs for all devices
            configs = {}
            for hostname, structured_config in structured_configs.items():
                configs[hostname] = get_device_config(structured_config)

            assert len(configs) == len(all_inputs)

        logging.disable(logging.NOTSET)

    logger.info(
        "Benchmarked full workflow for molecule scenario '%s' with %d devices",
        molecule_scenario.name,
        len(molecule_scenario.hosts),
    )
