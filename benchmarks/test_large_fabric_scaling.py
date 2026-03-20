# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Benchmark tests for large fabric scaling."""

import logging

import pytest
from pytest_codspeed import BenchmarkFixture

from benchmarks.generate_inventory import generate_hostvars
from pyavd import get_avd_facts, get_device_config, get_device_structured_config, validate_inputs

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    ("device_count", "spine_count", "l3leaf_count", "l2leaf_count", "vrf_count", "per_vrf_svi_count"),
    [
        pytest.param(15, 3, 6, 6, 5, 10, id="15_devices"),
        pytest.param(150, 30, 75, 45, 10, 10, id="150_devices"),  # 20% spines, 50% l3leaf, 30% l2leaf
        pytest.param(1500, 300, 750, 450, 10, 10, id="1500_devices"),  # 20% spines, 50% l3leaf, 30% l2leaf
    ],
)
def test_large_fabric_full_workflow_benchmark(
    benchmark: BenchmarkFixture,
    device_count: int,
    spine_count: int,
    l3leaf_count: int,
    l2leaf_count: int,
    vrf_count: int,
    per_vrf_svi_count: int,
) -> None:
    """
    Benchmark COMPLETE AVD workflow with fabrics at different scales.

    Tests the full end-to-end workflow:
    1. Validate inputs
    2. Generate AVD facts
    3. Generate structured configs
    4. Render EOS configs

    Tests at 3 scales (15, 150, 1500 devices) to understand how performance scales:
    - 15 devices: Small fabric baseline
    - 150 devices: 10x scale (should be ~10x slower if linear)
    - 1500 devices: 100x scale (detects O(n²) issues if much slower than 100x)

    The 150 and 1500-device tests use a realistic topology: 20% spines, 50% l3leaf, 30% l2leaf.
    """
    # Generate synthetic inventory (outside benchmark)
    hostvars = generate_hostvars(
        spine_count=spine_count,
        l3leaf_count=l3leaf_count,
        l2leaf_count=l2leaf_count,
        vrf_count=vrf_count,
        per_vrf_svi_count=per_vrf_svi_count,
    )

    # Disable logging during benchmark
    logging.disable(logging.CRITICAL)

    @benchmark
    def _() -> None:
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

    logging.disable(logging.NOTSET)

    logger.info("Benchmarked full workflow for %d devices", device_count)
