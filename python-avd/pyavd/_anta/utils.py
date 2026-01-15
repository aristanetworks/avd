# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Utility functions used by PyAVD for ANTA."""

from __future__ import annotations

from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING

from .index import AVD_TEST_INDEX

if TYPE_CHECKING:
    from anta.catalog import AntaCatalog

    from pyavd.api._anta import AvdCatalogGenerationSettings, AvdTestSpec


LOGGER = getLogger(__name__)


def dump_anta_catalog(hostname: str, catalog: AntaCatalog, catalog_dir: str | Path) -> None:
    """
    Dump the ANTA catalog for a device to the provided catalog directory.

    The catalog will be saved as a JSON file named after the device: `<device>.json`.
    """
    catalog_path = Path(catalog_dir) / f"{hostname}.json"
    catalog_dump = catalog.dump()

    LOGGER.debug("<%s> Dumping ANTA catalog at %s", hostname, catalog_path)
    with catalog_path.open(mode="w", encoding="UTF-8") as stream:
        stream.write(catalog_dump.to_json())


def get_filtered_test_specs(avd_catalog_generation_settings: AvdCatalogGenerationSettings) -> list[AvdTestSpec]:
    """Return a new list of AvdTestSpec based on the default AVD_TEST_INDEX list and the provided settings object."""
    run_tests_set = set(avd_catalog_generation_settings.run_tests)
    skip_tests_set = set(avd_catalog_generation_settings.skip_tests)

    # Check for invalid test names across all filters
    test_names = {test.test_class.name for test in AVD_TEST_INDEX}
    invalid_test_names = (run_tests_set | skip_tests_set) - test_names
    if invalid_test_names:
        msg = f"Invalid test name(s) in 'run_tests' or 'skip_tests' filters: {', '.join(sorted(invalid_test_names))}"
        raise ValueError(msg)

    # Remove any tests from run_tests that are in skip_tests
    remaining_run_tests = run_tests_set - skip_tests_set

    final_test_specs: list[AvdTestSpec] = []

    for test in AVD_TEST_INDEX:
        name = test.test_class.name

        # Skip tests explicitly mentioned in skip_tests
        if name in avd_catalog_generation_settings.skip_tests:
            continue

        # If run_tests is specified, only include tests in remaining_run_tests
        if avd_catalog_generation_settings.run_tests and name not in remaining_run_tests:
            continue

        final_test_specs.append(test)

    # Add custom test specs
    final_test_specs.extend(avd_catalog_generation_settings.custom_test_specs)

    return final_test_specs
