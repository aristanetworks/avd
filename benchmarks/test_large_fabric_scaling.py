# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Benchmark tests for large fabric scaling."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import pytest

from benchmarks.generate_inventory import generate_hostvars
from pyavd import get_avd_facts, get_device_config, get_device_structured_config, validate_inputs

if TYPE_CHECKING:
    from pytest_codspeed import BenchmarkFixture

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "device_count",
    [
        pytest.param(15, id="15_devices"),
        pytest.param(150, marks=pytest.mark.benchmark_scale, id="150_devices"),
    ],
)
def test_large_fabric_full_workflow_benchmark(
    benchmark: BenchmarkFixture,
    device_count: int,
) -> None:
    """
    Benchmark COMPLETE AVD workflow with fabrics at different scales.

    Tests the full end-to-end workflow:
    1. Validate inputs
    2. Generate AVD facts
    3. Generate structured configs
    4. Render EOS configs

    Scale device count in multiples of 15 while preserving the 1:2:2 ratio of
    spines, L3 leaves, and L2 leaves. Each size uses 5 VRFs with 10 SVIs per VRF
    and two uplinks per leaf, so service density and uplink count stay fixed.
    Compare the results to assess scaling; linear runtime is not assumed.

    The 150-device test is marked for local full benchmark runs only.
    """
    # Generate synthetic inventory (outside benchmark).
    fabric_scale = device_count // 15
    hostvars = generate_hostvars(
        spine_count=3 * fabric_scale,
        l3leaf_count=6 * fabric_scale,
        l2leaf_count=6 * fabric_scale,
        vrf_count=5,
        per_vrf_svi_count=10,
    )

    def b() -> None:
        # Step 1: Validate inputs for all devices
        all_inputs = {}
        all_hostvars = {}
        for hostname, host_hostvars in hostvars.items():
            validated_result = validate_inputs(host_hostvars)
            if validated_result.validated_data:
                all_inputs[hostname] = validated_result.validated_data
                all_hostvars[hostname] = host_hostvars

        # Step 2: Generate AVD facts
        avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=all_hostvars)

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

        assert len(configs) == device_count

    previous_disable_level = logging.root.manager.disable
    logging.disable(logging.CRITICAL)
    try:
        benchmark(b)
    finally:
        logging.disable(previous_disable_level)

    logger.info("Benchmarked full workflow for %d devices", device_count)
