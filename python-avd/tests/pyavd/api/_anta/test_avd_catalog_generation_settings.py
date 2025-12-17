# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Iterator
from pathlib import Path

import pytest
from anta.tests.connectivity import VerifyReachability
from anta.tests.interfaces import VerifyInterfacesVoqAndEgressQueueDrops

from pyavd._anta.index import AVD_TEST_INDEX
from pyavd._anta.input_factories import VerifyReachabilityInputFactory
from pyavd._anta.input_factories._base_classes import AntaTestInputFactory
from pyavd.api._anta import AvdCatalogGenerationSettings, AvdTestSpec


def test_post_init_valid_output_dir(tmp_path: Path) -> None:
    """Test that a valid, existing directory is accepted."""
    settings = AvdCatalogGenerationSettings(output_dir=tmp_path)
    assert settings.output_dir == tmp_path


def test_post_init_none_output_dir() -> None:
    """Test that None is accepted (default behavior)."""
    settings = AvdCatalogGenerationSettings(output_dir=None)
    assert settings.output_dir is None


def test_post_init_non_existent_dir() -> None:
    """Test validation fails if the directory does not exist."""
    invalid_path = Path("/path/that/definitely/does/not/exist")
    with pytest.raises(ValueError, match="does not exist or is not a directory"):
        AvdCatalogGenerationSettings(output_dir=invalid_path)


def test_post_init_file_as_dir(tmp_path: Path) -> None:
    """Test validation fails if the path is a file, not a directory."""
    file_path = tmp_path / "test_file.txt"
    file_path.touch()
    with pytest.raises(ValueError, match="does not exist or is not a directory"):
        AvdCatalogGenerationSettings(output_dir=file_path)


def test_get_filtered_test_specs_no_filters() -> None:
    """No run_tests or skip_tests provided. Should return all."""
    settings = AvdCatalogGenerationSettings()
    result = settings.get_filtered_test_specs(AVD_TEST_INDEX)
    assert result == AVD_TEST_INDEX


def test_get_filtered_test_specs_invalid_test_names_in_run() -> None:
    """Invalid name in run_tests should raise ValueError."""
    settings = AvdCatalogGenerationSettings(run_tests=("VerifyReachability", "InvalidTest1", "InvalidTest2"))
    with pytest.raises(ValueError, match="Invalid test names in run_tests or skip_tests filters: InvalidTest1, InvalidTest2"):
        settings.get_filtered_test_specs(AVD_TEST_INDEX)


def test_get_filtered_test_specs_invalid_test_names_in_skip() -> None:
    """Invalid name in skip_tests should raise ValueError."""
    settings = AvdCatalogGenerationSettings(skip_tests=("VerifyReachability", "InvalidTest2", "InvalidTest1"))
    with pytest.raises(ValueError, match="Invalid test names in run_tests or skip_tests filters: InvalidTest1, InvalidTest2"):
        settings.get_filtered_test_specs(AVD_TEST_INDEX)


def test_get_filtered_test_specs_skip_tests_logic() -> None:
    """Specific tests should be removed."""
    skip_tests = ("VerifyNTP", "VerifyReachability")
    settings = AvdCatalogGenerationSettings(skip_tests=skip_tests)
    result = settings.get_filtered_test_specs(AVD_TEST_INDEX)
    result_names = [s.test_class.name for s in result]
    assert all(test not in result_names for test in skip_tests)
    assert len(result_names) == len(AVD_TEST_INDEX) - len(skip_tests)


def test_get_filtered_test_specs_run_tests_logic() -> None:
    """Only specific tests should remain."""
    run_tests = ("VerifyNTP", "VerifyReachability")
    settings = AvdCatalogGenerationSettings(run_tests=run_tests)
    result = settings.get_filtered_test_specs(AVD_TEST_INDEX)
    result_names = [s.test_class.name for s in result]
    assert result_names == list(run_tests)


def test_get_filtered_test_specs_both_filters_overlap_remaining_run_tests() -> None:
    """Both filters provided with overlap, with remaining run_tests."""
    # User asks to run A and B, but explicitly skips B. Result should be A only.
    run_tests = ("VerifyNTP", "VerifyReachability")
    skip_tests = ("VerifyReachability",)
    settings = AvdCatalogGenerationSettings(run_tests=run_tests, skip_tests=skip_tests)
    result = settings.get_filtered_test_specs(AVD_TEST_INDEX)
    result_names = [s.test_class.name for s in result]
    assert result_names == ["VerifyNTP"]


def test_get_filtered_test_specs_both_filters_overlap_no_remaining_run_tests() -> None:
    """Both filters provided with overlap, no remaining run_tests."""
    # User asks to run A only, but explicitly skips A. Result should be all except A.
    run_tests = ("VerifyNTP",)
    skip_tests = ("VerifyNTP",)
    settings = AvdCatalogGenerationSettings(run_tests=run_tests, skip_tests=skip_tests)
    result = settings.get_filtered_test_specs(AVD_TEST_INDEX)
    result_names = [s.test_class.name for s in result]
    assert "VerifyNTP" not in result_names
    assert len(result_names) == len(AVD_TEST_INDEX) - len(skip_tests)


def test_get_filtered_test_specs_custom_test_specs_addition() -> None:
    """Custom test is added to the final list."""

    class VerifyInterfacesVoqAndEgressQueueDropsInputFactory(AntaTestInputFactory[VerifyInterfacesVoqAndEgressQueueDrops.Input]):
        """Input factory class for the `VerifyInterfacesVoqAndEgressQueueDrops` test."""

        def create(self) -> Iterator[VerifyInterfacesVoqAndEgressQueueDrops.Input]:
            """Generate the inputs for the `VerifyInterfacesVoqAndEgressQueueDrops` test."""
            return

    test_spec = AvdTestSpec(test_class=VerifyInterfacesVoqAndEgressQueueDrops, input_factory=VerifyInterfacesVoqAndEgressQueueDropsInputFactory)
    custom_test_specs = (test_spec,)
    settings = AvdCatalogGenerationSettings(custom_test_specs=custom_test_specs)
    result = settings.get_filtered_test_specs(AVD_TEST_INDEX)
    assert test_spec in result
    assert len(result) == len(AVD_TEST_INDEX) + len(custom_test_specs)


def test_get_filtered_test_specs_custom_test_specs_deduplication() -> None:
    """If a custom test is already in the list (value equality), it is not added twice."""
    test_spec = AvdTestSpec(test_class=VerifyReachability, input_factory=VerifyReachabilityInputFactory)
    custom_test_specs = (test_spec,)
    settings = AvdCatalogGenerationSettings(custom_test_specs=custom_test_specs)
    result = settings.get_filtered_test_specs(AVD_TEST_INDEX)
    verify_reachability_count = sum(1 for s in result if s.test_class.name == test_spec.test_class.name)
    assert verify_reachability_count == 1
    assert result == AVD_TEST_INDEX


def test_get_filtered_test_specs_custom_test_specs_with_filters() -> None:
    """Filters apply to default list, not custom test specs which are appended afterwards."""

    class VerifyInterfacesVoqAndEgressQueueDropsInputFactory(AntaTestInputFactory[VerifyInterfacesVoqAndEgressQueueDrops.Input]):
        """Input factory class for the `VerifyInterfacesVoqAndEgressQueueDrops` test."""

        def create(self) -> Iterator[VerifyInterfacesVoqAndEgressQueueDrops.Input]:
            """Generate the inputs for the `VerifyInterfacesVoqAndEgressQueueDrops` test."""
            return

    test_spec = AvdTestSpec(test_class=VerifyInterfacesVoqAndEgressQueueDrops, input_factory=VerifyInterfacesVoqAndEgressQueueDropsInputFactory)
    custom_test_specs = (test_spec,)
    run_tests = ("VerifyNTP",)
    settings = AvdCatalogGenerationSettings(run_tests=run_tests, custom_test_specs=custom_test_specs)
    result = settings.get_filtered_test_specs(AVD_TEST_INDEX)
    result_names = [s.test_class.name for s in result]
    assert result_names == ["VerifyNTP", test_spec.test_class.name]
