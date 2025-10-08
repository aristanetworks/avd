# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from time import perf_counter
from typing import TYPE_CHECKING

from pyavd._utils import default, get

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
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen  # noqa: PLC0415

    from ._anta.factories import create_catalog  # noqa: PLC0415
    from ._anta.index import AVD_TEST_INDEX, AVD_TEST_NAMES  # noqa: PLC0415
    from ._anta.lib import AntaCatalog  # noqa: PLC0415
    from ._anta.models import DeviceContext, TestContext  # noqa: PLC0415
    from ._anta.utils import dump_anta_catalog, parse_tests  # noqa: PLC0415
    from .api._anta import AvdCatalogGenerationSettings  # noqa: PLC0415

    settings = settings or AvdCatalogGenerationSettings()

    start_time = perf_counter()
    LOGGER.debug("<%s> Generating ANTA catalog with settings: %s", hostname, settings.model_dump(mode="json"))

    if settings.ignore_is_deployed is False and not default(get(structured_config, "metadata.is_deployed", get(structured_config, "is_deployed", False))):
        LOGGER.info("<%s> Device is not deployed, returning an empty catalog", hostname)
        return AntaCatalog()

    run_map = parse_tests(settings.run_tests)
    skip_map = parse_tests(settings.skip_tests)
    if run_map:
        LOGGER.debug("<%s> Parsed run_tests filter: %s", hostname, run_map)
    if skip_map:
        LOGGER.debug("<%s> Parsed skip_tests filter: %s", hostname, skip_map)

    # Validate that all specified peer devices in filters exist.
    all_filtered_peers = {peer for peer_list in list(run_map.values()) + list(skip_map.values()) for peer in peer_list}
    if unknown_peers := all_filtered_peers - set(minimal_structured_configs.keys()):
        msg = f"Unknown peer devices found in 'run_tests' or 'skip_tests' filters: {', '.join(sorted(unknown_peers))}"
        raise ValueError(msg)

    # Validate that all specified test names exist.
    all_filtered_tests = set(run_map.keys()) | set(skip_map.keys())
    if invalid_tests := all_filtered_tests - set(AVD_TEST_NAMES):
        msg = f"Invalid test names found in 'run_tests' or 'skip_tests' filters: {', '.join(sorted(invalid_tests))}"
        raise ValueError(msg)

    test_contexts: list[TestContext] = []

    # If run_tests is specified, it forms the basis of which tests to consider. Otherwise, consider all AVD tests.
    test_specs_to_consider = [spec for spec in AVD_TEST_INDEX if spec.test_class.name in run_map] if run_map else AVD_TEST_INDEX

    for test_spec in test_specs_to_consider:
        test_name = test_spec.test_class.name

        peers_to_run = run_map.get(test_name, set())
        peers_to_skip = skip_map.get(test_name, set())

        # Raise if a test is globally specified in both lists.
        if not peers_to_run and test_name in run_map and not peers_to_skip and test_name in skip_map:
            msg = f"Test '{test_name}' is specified in both run_tests and skip_tests filters, which is a contradiction."
            raise ValueError(msg)

        # Raise if peers are specified in both run and skip lists for the same test.
        if conflicting_peers := peers_to_run & peers_to_skip:
            msg = f"Test '{test_name}' has conflicting peer filters: peers {sorted(conflicting_peers)} are in both run_tests and skip_tests filters."
            raise ValueError(msg)

        # Skip tests that are present in skip_map with an empty peer set.
        if test_name in skip_map and not peers_to_skip:
            continue

        test_contexts.append(TestContext(test_spec=test_spec, peers_to_run=peers_to_run, peers_to_skip=peers_to_skip))

    # Add custom test specs, which are not subject to DSL filtering.
    test_contexts.extend([TestContext(test_spec=test_spec) for test_spec in settings.custom_test_specs])

    device_context = DeviceContext(
        hostname=hostname,
        structured_config=EosCliConfigGen._load(structured_config),
        minimal_structured_configs=minimal_structured_configs,
        input_factory_settings=settings.input_factory_settings,
    )
    catalog = create_catalog(device_context, test_contexts)

    if settings.output_dir:
        dump_anta_catalog(hostname, catalog, settings.output_dir)

    stop_time = perf_counter()
    LOGGER.debug("<%s> Generated ANTA catalog in %.4f seconds", hostname, stop_time - start_time)

    return catalog
