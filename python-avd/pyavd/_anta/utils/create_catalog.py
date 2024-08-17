# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._anta.lib import AntaCatalog, AntaTest, AntaTestDefinition

from .logging_utils import TestLoggerAdapter

if TYPE_CHECKING:
    from logging import Logger

    from pyavd.api.anta_test_spec import TestSpec

    from .config_manager import ConfigManager


def create_catalog(config_manager: ConfigManager, test_specs: list[TestSpec], logger: Logger) -> AntaCatalog:
    """Create an ANTA catalog for a device from the provided test specs.

    Parameters
    ----------
        config_manager: The ConfigManager object.
        test_specs: The list of TestSpec objects.
        logger: The logger object to use for logging messages.

    Returns:
    -------
        AntaCatalog: The ANTA catalog for the device.
    """
    test_definitions: list[AntaTestDefinition] = []
    for test in test_specs:
        test_logger = TestLoggerAdapter.create(device=config_manager.device_name, test=test.test_class.name, logger=logger)
        test_definition = test.create_test_definition(config_manager, test_logger)

        # Skip the test if we couldn't create the test definition. Logging is done in the service
        if test_definition is None:
            continue

        # Tag the test with the device name for the final catalog and add metadata
        test_definition.inputs.filters = AntaTest.Input.Filters(tags={config_manager.device_name})
        test_definition.inputs.result_overwrite = AntaTest.Input.ResultOverwrite(custom_field="Generated by PyAVD")
        test_definitions.append(test_definition)

    return AntaCatalog(tests=test_definitions)
