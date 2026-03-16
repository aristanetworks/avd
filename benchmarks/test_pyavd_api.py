# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Benchmark tests for PyAVD API functions."""

import logging
import sys
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest
from pytest_codspeed import BenchmarkFixture

from pyavd import (
    get_avd_facts,
    get_device_config,
    get_device_doc,
    get_device_structured_config,
    get_device_test_catalog,
    get_fabric_documentation,
    validate_inputs,
    validate_structured_config,
)
from pyavd.api.anta import AVDFabricData

if TYPE_CHECKING:
    from tests.models import MoleculeHost, MoleculeScenario

logger = logging.getLogger(__name__)


def get_deterministic_sample_host(molecule_scenario: "MoleculeScenario") -> "MoleculeHost":
    """
    Get a deterministic sample host from a molecule scenario.

    Uses sorted host names to ensure the same host is always selected,
    preventing false performance regressions when host ordering changes.
    """
    sorted_hosts = sorted(molecule_scenario.hosts, key=lambda h: h.name)
    return sorted_hosts[0]


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_validate_inputs_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
) -> None:
    """Benchmark validate_inputs function for all hosts in the scenario."""
    # Disable logging during benchmark
    logging.disable(logging.CRITICAL)

    @benchmark
    def _() -> None:
        # Validate inputs for ALL hosts to get comprehensive coverage
        validated_count = 0
        for host in molecule_scenario.hosts:
            result = validate_inputs(host.hostvars)
            if result.validated_data is not None:
                validated_count += 1
        assert validated_count > 0

    logging.disable(logging.NOTSET)

    logger.info("Benchmarked validate_inputs for %d hosts", len(molecule_scenario.hosts))


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_get_avd_facts_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
) -> None:
    """Benchmark get_avd_facts function."""
    # Prepare inputs
    all_inputs = {}
    all_hostvars = {}

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        for host in molecule_scenario.hosts:
            validated_result = validate_inputs(host.hostvars)
            if validated_result.validated_data:
                all_inputs[host.name] = validated_result.validated_data
                all_hostvars[host.name] = host.hostvars

        # Disable logging during benchmark
        logging.disable(logging.CRITICAL)

        @benchmark
        def _() -> None:
            avd_facts = get_avd_facts(
                all_inputs=all_inputs,
                all_hostvars=all_hostvars,
                pool_manager=molecule_scenario.pool_manager,
            )
            assert len(avd_facts) == len(all_inputs)

        logging.disable(logging.NOTSET)

    logger.info("Benchmarked get_avd_facts for %d devices", len(all_inputs))


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_get_device_structured_config_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
) -> None:
    """Benchmark get_device_structured_config function for all devices."""
    # Prepare data for ALL devices
    all_inputs = {}
    all_hostvars = {}

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        for host in molecule_scenario.hosts:
            validated_result = validate_inputs(host.hostvars)
            if validated_result.validated_data:
                all_inputs[host.name] = validated_result.validated_data
                all_hostvars[host.name] = host.hostvars

        # Generate facts for the entire fabric (not part of the benchmark)
        avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=molecule_scenario.pool_manager)

        # Disable logging during benchmark
        logging.disable(logging.CRITICAL)

        @benchmark
        def _() -> None:
            # Generate structured configs for ALL devices
            structured_configs = {}
            for hostname, inputs in all_inputs.items():
                structured_configs[hostname] = get_device_structured_config(
                    hostname=hostname,
                    inputs=inputs,
                    avd_facts=avd_facts,
                )
            assert len(structured_configs) == len(all_inputs)

        logging.disable(logging.NOTSET)

    logger.info("Benchmarked get_device_structured_config for %d devices", len(all_inputs))


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_validate_structured_config_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
) -> None:
    """Benchmark validate_structured_config function for all devices."""
    # Prepare data for ALL devices
    all_inputs = {}
    all_hostvars = {}

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        for host in molecule_scenario.hosts:
            validated_result = validate_inputs(host.hostvars)
            if validated_result.validated_data:
                all_inputs[host.name] = validated_result.validated_data
                all_hostvars[host.name] = host.hostvars

        # Generate facts and structured configs for the entire fabric (not part of benchmark)
        avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=molecule_scenario.pool_manager)

        structured_configs_dicts = {}
        for hostname, inputs in all_inputs.items():
            structured_config = get_device_structured_config(
                hostname=hostname,
                inputs=inputs,
                avd_facts=avd_facts,
            )
            # TODO: validate_structured_config should accept EOSConfig models directly
            # Currently it only accepts dicts, so we need to convert using _as_dict()
            # This conversion adds overhead that shouldn't be necessary
            structured_configs_dicts[hostname] = structured_config._as_dict()

        # Disable logging during benchmark
        logging.disable(logging.CRITICAL)

        @benchmark
        def _() -> None:
            # Validate structured configs for ALL devices
            validated_count = 0
            for structured_config_dict in structured_configs_dicts.values():
                result = validate_structured_config(structured_config_dict)
                if result.validated_data is not None:
                    validated_count += 1
            assert validated_count == len(structured_configs_dicts)

        logging.disable(logging.NOTSET)

    logger.info("Benchmarked validate_structured_config for %d devices", len(all_inputs))


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_get_device_config_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
) -> None:
    """Benchmark get_device_config function (EOS CLI rendering) for all devices."""
    # Prepare data for ALL devices
    all_inputs = {}
    all_hostvars = {}

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        for host in molecule_scenario.hosts:
            validated_result = validate_inputs(host.hostvars)
            if validated_result.validated_data:
                all_inputs[host.name] = validated_result.validated_data
                all_hostvars[host.name] = host.hostvars

        # Generate facts and structured configs for the entire fabric (not part of benchmark)
        avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=molecule_scenario.pool_manager)

        structured_configs = {}
        for hostname, inputs in all_inputs.items():
            structured_configs[hostname] = get_device_structured_config(
                hostname=hostname,
                inputs=inputs,
                avd_facts=avd_facts,
            )

        # Disable logging during benchmark
        logging.disable(logging.CRITICAL)

        @benchmark
        def _() -> None:
            # Render EOS configs for ALL devices
            configs = {}
            for hostname, structured_config in structured_configs.items():
                configs[hostname] = get_device_config(structured_config)
            assert len(configs) == len(all_inputs)

        logging.disable(logging.NOTSET)

    logger.info("Benchmarked get_device_config for %d devices", len(all_inputs))


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_get_device_doc_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
) -> None:
    """Benchmark get_device_doc function (Markdown documentation rendering) for all devices."""
    # Prepare data for ALL devices
    all_inputs = {}
    all_hostvars = {}

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        for host in molecule_scenario.hosts:
            validated_result = validate_inputs(host.hostvars)
            if validated_result.validated_data:
                all_inputs[host.name] = validated_result.validated_data
                all_hostvars[host.name] = host.hostvars

        # Generate facts and structured configs for the entire fabric (not part of benchmark)
        avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=molecule_scenario.pool_manager)

        structured_configs_dicts = {}
        for hostname, inputs in all_inputs.items():
            structured_config = get_device_structured_config(
                hostname=hostname,
                inputs=inputs,
                avd_facts=avd_facts,
            )
            # Convert to dict - get_device_doc templates expect dict format
            structured_configs_dicts[hostname] = structured_config._as_dict()

        # Disable logging during benchmark
        logging.disable(logging.CRITICAL)

        @benchmark
        def _() -> None:
            # Generate documentation for ALL devices
            docs = {}
            for structured_config_dict in structured_configs_dicts.values():
                docs[len(docs)] = get_device_doc(structured_config_dict, add_md_toc=True)
            assert len(docs) == len(all_inputs)

        logging.disable(logging.NOTSET)

    logger.info("Benchmarked get_device_doc for %d devices", len(all_inputs))


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_get_fabric_documentation_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
) -> None:
    """Benchmark get_fabric_documentation function."""
    # Prepare data
    all_inputs = {}
    all_hostvars = {}

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        for host in molecule_scenario.hosts:
            validated_result = validate_inputs(host.hostvars)
            if validated_result.validated_data:
                all_inputs[host.name] = validated_result.validated_data
                all_hostvars[host.name] = host.hostvars

        avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=molecule_scenario.pool_manager)

        structured_configs = {}
        structured_configs_dicts = {}
        for hostname, inputs in all_inputs.items():
            structured_config = get_device_structured_config(
                hostname=hostname,
                inputs=inputs,
                avd_facts=avd_facts,
            )
            structured_configs[hostname] = structured_config
            # TODO: get_fabric_documentation should handle EOSConfig models directly
            # Currently passing EOSConfig models causes IPv6 parsing issues in fabric_documentation_facts
            # Converting to dict matches regular test behavior and avoids the bug
            # See: python-avd/pyavd/_eos_designs/fabric_documentation_facts/__init__.py line 200
            structured_configs_dicts[hostname] = structured_config._as_dict()

        # Get fabric_name from deterministic sample host
        sample_host = get_deterministic_sample_host(molecule_scenario)
        fabric_name = sample_host.hostvars.get("fabric_name", "AVD_FABRIC")

        # Disable logging during benchmark
        logging.disable(logging.CRITICAL)

        @benchmark
        def _() -> None:
            fabric_doc = get_fabric_documentation(
                avd_facts=avd_facts,
                structured_configs=structured_configs_dicts,
                fabric_name=fabric_name,
            )
            assert fabric_doc is not None

        logging.disable(logging.NOTSET)

    logger.info("Benchmarked get_fabric_documentation for %d devices", len(all_inputs))


@pytest.mark.molecule_scenarios("eos_designs_unit_tests")
def test_get_device_test_catalog_benchmark(
    benchmark: BenchmarkFixture,
    molecule_scenario: "MoleculeScenario",
) -> None:
    """Benchmark get_device_test_catalog function (ANTA catalog generation) for all devices."""
    # Prepare data for all devices
    all_inputs = {}
    all_hostvars = {}

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        for host in molecule_scenario.hosts:
            validated_result = validate_inputs(host.hostvars)
            if validated_result.validated_data:
                all_inputs[host.name] = validated_result.validated_data
                all_hostvars[host.name] = host.hostvars

        avd_facts = get_avd_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=molecule_scenario.pool_manager)

        # Generate all structured configs for fabric_data (not part of benchmark)
        all_structured_configs_dicts = {}
        for hostname, inputs in all_inputs.items():
            structured_config = get_device_structured_config(
                hostname=hostname,
                inputs=inputs,
                avd_facts=avd_facts,
            )
            # TODO: AVDFabricData.from_structured_configs should accept EOSConfig models
            # Currently it expects dict[str, dict], so we need to convert
            # This conversion adds overhead that shouldn't be necessary
            all_structured_configs_dicts[hostname] = structured_config._as_dict()

        # Create fabric_data from all structured configs (as dicts)
        fabric_data = AVDFabricData.from_structured_configs(all_structured_configs_dicts)

        # Disable logging during benchmark
        logging.disable(logging.CRITICAL)

        @benchmark
        def _() -> None:
            # Generate ANTA test catalogs for ALL devices
            # TODO: get_device_test_catalog should accept EOSConfig models directly
            # Currently it expects structured_config: dict, so we use the dict version
            # This conversion adds overhead that shouldn't be necessary
            test_catalogs = {}
            for hostname, structured_config_dict in all_structured_configs_dicts.items():
                test_catalogs[hostname] = get_device_test_catalog(
                    hostname=hostname,
                    structured_config=structured_config_dict,
                    fabric_data=fabric_data,
                )
            assert len(test_catalogs) == len(all_inputs)

        logging.disable(logging.NOTSET)

    logger.info("Benchmarked get_device_test_catalog for %d devices", len(all_inputs))
