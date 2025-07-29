# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from pathlib import Path
from typing import Any

from pyavd.api._anta import AvdCatalogGenerationSettings, InputFactorySettings

LOGGER = logging.getLogger("ansible_collections.arista.avd")


def generate_anta_settings(
    input_factory_settings: InputFactorySettings,
    output_dir: Path | str | None,
    device: str,
    avd_catalogs_filters: list[dict[str, Any]],
) -> AvdCatalogGenerationSettings:
    """Creates the AvdCatalogGenerationSettings object by processing device filters."""
    return AvdCatalogGenerationSettings(
        input_factory_settings=input_factory_settings,
        output_dir=output_dir,
        **get_device_catalog_filters(device, avd_catalogs_filters),
    )


def get_device_catalog_filters(
    device: str,
    avd_catalogs_filters: list[dict[str, Any]],
) -> dict[str, list[str]]:
    """
    Get the test filters for a device from the provided AVD catalogs filters.

    A filter is applied to the device unless `device_list` is provided in the filter and the device is *not* part of it.

    Filters are not cumulative for the device. If the device matches multiple filters, the last filter (appearing later in the list) wins.

    Args:
        device: The device name to get the filters for.
        avd_catalogs_filters: The AVD catalogs filters from the plugin argument `avd_catalogs.filters`.

    Returns:
        dict: A dictionary with the list of tests to run and/or skip: `{"run_tests: [<test1>, ...], "skip_tests" [<test2>, ...]}`.
    """
    final_filters: dict[str, list[str]] = {"run_tests": [], "skip_tests": []}

    for filter_config in avd_catalogs_filters:
        # Skip this filter for the device if it's not part of device_list if provided
        device_list = filter_config.get("device_list")
        if device_list is not None and device not in device_list:
            continue

        # Refactored to handle both 'run_tests' and 'skip_tests' with the same logic.
        for key in ["run_tests", "skip_tests"]:
            if (new_tests := filter_config.get(key)) is not None:
                if final_filters[key]:
                    LOGGER.debug("<%s> %s overridden from %s to %s", device, key, final_filters[key], new_tests)
                final_filters[key] = list(set(new_tests))

    return final_filters
