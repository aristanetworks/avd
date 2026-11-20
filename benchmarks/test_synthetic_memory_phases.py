# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Isolate validation from generation when diagnosing synthetic memory profiles."""

from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING, Any

import pytest

from benchmarks.generate_inventory import generate_hostvars
from pyavd import get_avd_facts, get_device_config, get_device_structured_config, validate_inputs

if TYPE_CHECKING:
    from pytest_codspeed import BenchmarkFixture


@pytest.fixture
def synthetic_hostvars() -> dict[str, dict[str, Any]]:
    """Use the same topology and service density as the 15-device full workflow."""
    return generate_hostvars(spine_count=3, l3leaf_count=6, l2leaf_count=6, vrf_count=5, per_vrf_svi_count=10)


def _validate_hostvars(hostvars: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Validate every device with the same failure diagnostics as the full workflow."""
    all_inputs = {}
    for hostname, host_hostvars in hostvars.items():
        validated_result = validate_inputs(host_hostvars)
        validated_hostvars = validated_result.validated_data
        if validated_hostvars is None:
            violations = "; ".join(f"{violation.path}: {violation.message}" for violation in validated_result.validation_result.violations)
            pytest.fail(f"Invalid benchmark inputs for {hostname}: {violations}", pytrace=False)
        all_inputs[hostname] = validated_hostvars
    return all_inputs


@pytest.mark.benchmark_diagnostic
def test_synthetic_validation_memory_benchmark(benchmark: BenchmarkFixture, synthetic_hostvars: dict[str, dict[str, Any]]) -> None:
    """Measure input validation alone, including its Python and Rust work."""
    hostvars = synthetic_hostvars

    def setup() -> None:
        nonlocal hostvars
        hostvars = deepcopy(synthetic_hostvars)

    def run() -> None:
        assert len(_validate_hostvars(hostvars)) == 15

    benchmark.pedantic(run, setup=setup, iterations=1, rounds=1, warmup_rounds=1)


@pytest.mark.benchmark_diagnostic
def test_synthetic_generation_memory_benchmark(benchmark: BenchmarkFixture, synthetic_hostvars: dict[str, dict[str, Any]]) -> None:
    """Measure facts, structured configuration, and rendering after input validation."""
    source_hostvars = deepcopy(synthetic_hostvars)
    source_inputs = _validate_hostvars(source_hostvars)
    all_inputs, hostvars = source_inputs, source_hostvars

    def setup() -> None:
        nonlocal all_inputs, hostvars
        all_inputs, hostvars = deepcopy((source_inputs, source_hostvars))

    def run() -> None:
        avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=hostvars)
        structured_configs = {
            hostname: get_device_structured_config(hostname=hostname, inputs=inputs, avd_facts=avd_facts) for hostname, inputs in all_inputs.items()
        }
        configs = {hostname: get_device_config(structured_config) for hostname, structured_config in structured_configs.items()}
        assert len(configs) == 15
        assert all(configs.values())

    benchmark.pedantic(run, setup=setup, iterations=1, rounds=1, warmup_rounds=1)
