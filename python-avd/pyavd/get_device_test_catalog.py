# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from time import perf_counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._anta.lib import AntaCatalog
    from .api._anta import AvdCatalogGenerationSettings, MinimalStructuredConfig

LOGGER = getLogger(__name__)


def get_device_test_catalog(
    hostname: str,
    structured_config: dict,
    minimal_structured_configs: dict[str, MinimalStructuredConfig],
    settings: AvdCatalogGenerationSettings | None = None,
) -> AntaCatalog:
    """
    Generate an ANTA test catalog for a single device.

    By default, the ANTA catalog will be generated from all tests specified in the AVD test index.

    An optional instance of `pyavd.api._anta.AvdCatalogGenerationSettings` can be provided
    to customize the catalog generation process, such as running only specific tests, or skipping certain tests.

    AVD uses minimal structured configurations of all devices containing only the required data.
    Make sure to create a single `minimal_structured_configs` dictionary using `pyavd.api._anta.get_minimal_structured_configs`
    for consistent data across catalog generations.

    Test definitions can be omitted from the catalog if the required data is not available for a specific device.
    You can configure logging and set the log level to DEBUG to see which test definitions are skipped and the reason why.

    Parameters
    ----------
    hostname : str
        The hostname of the device for which the catalog is being generated.
    structured_config : dict
        The structured configuration of the device.
        Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.
    minimal_structured_configs : dict[str, MinimalStructuredConfig]
        Dictionary keyed by hostname containing minimal structured configurations for all devices.
        Must be generated using `pyavd.api._anta.get_minimal_structured_configs`.
    settings : AvdCatalogGenerationSettings, optional
        The settings object to customize the catalog generation process.
        Must be an instance of `pyavd.api._anta.AvdCatalogGenerationSettings`, by default `None`.

    Returns:
    -------
    AntaCatalog
        The generated ANTA catalog for the device.
    """
    from ._anta.factories import create_catalog
    from ._anta.index import AVD_TEST_INDEX, AVD_TEST_NAMES
    from ._anta.lib import AntaCatalog
    from ._anta.utils import dump_anta_catalog
    from .api._anta import AvdCatalogGenerationSettings

    settings = settings or AvdCatalogGenerationSettings()

    start_time = perf_counter()
    LOGGER.info("<%s>: generating catalog with settings: %s", hostname, settings.model_dump(mode="json"))

    if settings.ignore_is_deployed is False and not structured_config.get("is_deployed", False):
        LOGGER.debug("<%s>: device is not deployed, returning an empty catalog", hostname)
        return AntaCatalog()

    # Check for invalid test names across all filters
    invalid_tests = {
        "run_tests": set(settings.run_tests) - set(AVD_TEST_NAMES),
        "skip_tests": set(settings.skip_tests) - set(AVD_TEST_NAMES),
    }

    for filter_type, invalid_names in invalid_tests.items():
        if invalid_names:
            msg = f"Invalid test names in {filter_type}: {', '.join(invalid_names)}"
            raise ValueError(msg)

    # Remove any tests from run_tests that are in skip_tests
    if settings.run_tests and settings.skip_tests:
        settings.run_tests = [test for test in settings.run_tests if test not in settings.skip_tests]
        LOGGER.debug("<%s>: cleaned up run_tests after removing skipped tests: %s", hostname, settings.run_tests)

    # Filter test specs based on skip_tests and run_tests
    filtered_test_specs = []

    for test in AVD_TEST_INDEX:
        # Skip tests explicitly mentioned in skip_tests
        if test.test_class.name in settings.skip_tests:
            continue
        # If run_tests is specified, only include tests in that set
        if settings.run_tests and test.test_class.name not in settings.run_tests:
            continue

        filtered_test_specs.append(test)

    # Add custom test specs, avoiding duplicates
    filtered_test_specs.extend([test for test in settings.custom_test_specs if test not in filtered_test_specs])

    catalog = create_catalog(hostname, structured_config, minimal_structured_configs, settings.input_factory_settings, filtered_test_specs)

    if settings.output_dir:
        dump_anta_catalog(hostname, catalog, settings.output_dir)

    stop_time = perf_counter()
    LOGGER.debug("<%s>: generated catalog in %.4f seconds", hostname, stop_time - start_time)

    return catalog
