# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re
from collections.abc import Iterator

import pytest
from anta.tests.connectivity import VerifyReachability
from anta.tests.interfaces import VerifyInterfacesVoqAndEgressQueueDrops

from pyavd._anta.index import AVD_TEST_INDEX
from pyavd._anta.input_factories.base_classes import AntaTestInputFactory
from pyavd._anta.input_factories.connectivity import VerifyReachabilityInputFactory
from pyavd._anta.utils import get_filtered_test_specs
from pyavd.api.anta import AVDCatalogGenerationSettings, AVDTestSpec


def test_get_filtered_test_specs_no_filters() -> None:
    """No run_tests or skip_tests provided. Should return all."""
    settings = AVDCatalogGenerationSettings()
    result = get_filtered_test_specs(settings)
    assert result == AVD_TEST_INDEX


def test_get_filtered_test_specs_invalid_test_names_in_run() -> None:
    """Invalid name in run_tests should raise ValueError."""
    settings = AVDCatalogGenerationSettings(run_tests=("VerifyReachability", "InvalidTest1", "InvalidTest2"))
    with pytest.raises(ValueError, match=re.escape("Invalid test name(s) in 'run_tests' or 'skip_tests' filters: InvalidTest1, InvalidTest2")):
        get_filtered_test_specs(settings)


def test_get_filtered_test_specs_invalid_test_names_in_skip() -> None:
    """Invalid name in skip_tests should raise ValueError."""
    settings = AVDCatalogGenerationSettings(skip_tests=("VerifyReachability", "InvalidTest2", "InvalidTest1"))
    with pytest.raises(ValueError, match=re.escape("Invalid test name(s) in 'run_tests' or 'skip_tests' filters: InvalidTest1, InvalidTest2")):
        get_filtered_test_specs(settings)


def test_get_filtered_test_specs_skip_tests_logic() -> None:
    """Specific tests should be removed."""
    skip_tests = ("VerifyNTP", "VerifyReachability")
    settings = AVDCatalogGenerationSettings(skip_tests=skip_tests)
    result = get_filtered_test_specs(settings)
    result_names = [s.test_class.name for s in result]
    assert all(test not in result_names for test in skip_tests)
    assert len(result_names) == len(AVD_TEST_INDEX) - len(skip_tests)


def test_get_filtered_test_specs_run_tests_logic() -> None:
    """Only specific tests should remain."""
    run_tests = ("VerifyNTP", "VerifyReachability")
    settings = AVDCatalogGenerationSettings(run_tests=run_tests)
    result = get_filtered_test_specs(settings)
    result_names = [s.test_class.name for s in result]
    assert result_names == list(run_tests)


def test_get_filtered_test_specs_both_filters_overlap_remaining_run_tests() -> None:
    """Both filters provided with overlap, with remaining run_tests."""
    # User asks to run A and B, but explicitly skips B. Result should be A only.
    run_tests = ("VerifyNTP", "VerifyReachability")
    skip_tests = ("VerifyReachability",)
    settings = AVDCatalogGenerationSettings(run_tests=run_tests, skip_tests=skip_tests)
    result = get_filtered_test_specs(settings)
    result_names = [s.test_class.name for s in result]
    assert result_names == ["VerifyNTP"]


def test_get_filtered_test_specs_both_filters_overlap_no_remaining_run_tests() -> None:
    """Both filters provided with overlap, no remaining run_tests."""
    # User asks to run A only, but explicitly skips A. Result should be nothing.
    run_tests = ("VerifyNTP",)
    skip_tests = ("VerifyNTP",)
    settings = AVDCatalogGenerationSettings(run_tests=run_tests, skip_tests=skip_tests)
    result = get_filtered_test_specs(settings)
    assert len(result) == 0


def test_get_filtered_test_specs_custom_test_specs_addition() -> None:
    """Custom test is added to the final list."""

    class VerifyInterfacesVoqAndEgressQueueDropsInputFactory(AntaTestInputFactory[VerifyInterfacesVoqAndEgressQueueDrops.Input]):
        """Input factory class for the `VerifyInterfacesVoqAndEgressQueueDrops` test."""

        def create(self) -> Iterator[VerifyInterfacesVoqAndEgressQueueDrops.Input]:
            """Generate the inputs for the `VerifyInterfacesVoqAndEgressQueueDrops` test."""
            return

    test_spec = AVDTestSpec(test_class=VerifyInterfacesVoqAndEgressQueueDrops, input_factory=VerifyInterfacesVoqAndEgressQueueDropsInputFactory)
    custom_test_specs = (test_spec,)
    settings = AVDCatalogGenerationSettings(custom_test_specs=custom_test_specs)
    result = get_filtered_test_specs(settings)
    assert test_spec in result
    assert len(result) == len(AVD_TEST_INDEX) + len(custom_test_specs)


def test_get_filtered_test_specs_custom_test_specs_deduplication() -> None:
    """Custom test is added to the final list even if duplicated (honor user intent)."""
    test_spec = AVDTestSpec(test_class=VerifyReachability, input_factory=VerifyReachabilityInputFactory)
    custom_test_specs = (test_spec,)
    settings = AVDCatalogGenerationSettings(custom_test_specs=custom_test_specs)
    result = get_filtered_test_specs(settings)
    verify_reachability_count = sum(1 for s in result if s.test_class.name == test_spec.test_class.name)
    assert verify_reachability_count == 2
    assert len(result) == len(AVD_TEST_INDEX) + len(custom_test_specs)


def test_get_filtered_test_specs_custom_test_specs_with_filters() -> None:
    """Filters apply to default list, not custom test specs which are appended afterwards."""

    class VerifyInterfacesVoqAndEgressQueueDropsInputFactory(AntaTestInputFactory[VerifyInterfacesVoqAndEgressQueueDrops.Input]):
        """Input factory class for the `VerifyInterfacesVoqAndEgressQueueDrops` test."""

        def create(self) -> Iterator[VerifyInterfacesVoqAndEgressQueueDrops.Input]:
            """Generate the inputs for the `VerifyInterfacesVoqAndEgressQueueDrops` test."""
            return

    test_spec = AVDTestSpec(test_class=VerifyInterfacesVoqAndEgressQueueDrops, input_factory=VerifyInterfacesVoqAndEgressQueueDropsInputFactory)
    custom_test_specs = (test_spec,)
    run_tests = ("VerifyNTP",)
    settings = AVDCatalogGenerationSettings(run_tests=run_tests, custom_test_specs=custom_test_specs)
    result = get_filtered_test_specs(settings)
    result_names = [s.test_class.name for s in result]
    assert result_names == ["VerifyNTP", test_spec.test_class.name]


def test_get_filtered_test_specs_replace_default_with_custom() -> None:
    """Test skipping a default test but adding it back via custom_test_specs."""
    test_spec = AVDTestSpec(test_class=VerifyReachability, input_factory=VerifyReachabilityInputFactory)
    custom_test_specs = (test_spec,)
    skip_tests = ("VerifyReachability",)
    settings = AVDCatalogGenerationSettings(skip_tests=skip_tests, custom_test_specs=custom_test_specs)
    result = get_filtered_test_specs(settings)
    matching_verify_reachability = [s for s in result if s.test_class.name == "VerifyReachability"]
    assert len(matching_verify_reachability) == 1
    assert matching_verify_reachability[0] is test_spec
