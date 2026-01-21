# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import asdict
from logging import getLogger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._anta.lib import AntaCatalog
    from .api._anta import AvdCatalogGenerationSettings, AvdFabricData

LOGGER = getLogger(__name__)


def get_device_test_catalog(
    hostname: str,
    structured_config: dict,
    fabric_data: AvdFabricData,
    settings: AvdCatalogGenerationSettings | None = None,
) -> AntaCatalog:
    """
    Generate an ANTA test catalog for a single device.

    By default, the ANTA catalog will be generated from all tests specified in the AVD test index.

    An optional instance of `pyavd.api._anta.AvdCatalogGenerationSettings` can be provided
    to customize the catalog generation process, such as running only specific tests, or skipping certain tests.

    AVD needs fabric-wide data of all devices to generate the catalog. Make sure to create a single
    `pyavd.api._anta.AvdFabricData` instance for consistent data across catalog generations.

    Test definitions can be omitted from the catalog if the required data is not available for a specific device.
    You can configure logging and set the log level to DEBUG to see which test definitions are skipped and the reason why.

    Args:
        hostname: The hostname of the device for which the catalog is being generated.
        structured_config: The structured configuration of the device.
            Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.
        fabric_data: The `AvdFabricData` instance containing fabric-wide data for the catalog generation.
            Built from all device structured configurations using `AvdFabricData.from_structured_configs`.
        settings: An optional `AvdCatalogGenerationSettings` instance to customize the catalog generation process.

    Returns:
        The generated ANTA catalog for the device.
    """
    from ._anta.factories import create_catalog  # noqa: PLC0415
    from ._anta.models import InputFactoryDataSource  # noqa: PLC0415
    from ._anta.utils import dump_anta_catalog, get_filtered_test_specs  # noqa: PLC0415
    from ._eos_cli_config_gen.schema import EosCliConfigGen  # noqa: PLC0415
    from .api._anta import AvdCatalogGenerationSettings  # noqa: PLC0415

    settings = settings or AvdCatalogGenerationSettings()

    LOGGER.debug("<%s> Generating ANTA catalog with settings: %s", hostname, asdict(settings))

    data_source = InputFactoryDataSource(hostname, EosCliConfigGen._load(structured_config), fabric_data, settings)

    final_test_specs = get_filtered_test_specs(settings)

    catalog = create_catalog(data_source, final_test_specs)

    if settings.output_dir:
        dump_anta_catalog(hostname, catalog, settings.output_dir)

    return catalog
