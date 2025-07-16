# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from copy import deepcopy

import pytest

from pyavd import get_device_test_catalog
from pyavd._anta.lib import AntaCatalog
from pyavd.api._anta import get_minimal_structured_configs
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "anta_runner",
)
def test_get_device_test_catalog(molecule_host: MoleculeHost) -> None:
    """
    Verify that get_device_test_catalog generates the correct ANTA catalog.

    This test compares the generated catalog against the expected output file
    from the molecule scenario to ensure correctness and prevent regressions.
    """
    all_configs = deepcopy(molecule_host.structured_configs)
    minimal_configs = get_minimal_structured_configs(all_configs)

    # Get the configuration for the specific host under test.
    host_config = deepcopy(molecule_host.structured_config)

    # Generate the ANTA catalog for the device.
    result_catalog = get_device_test_catalog(molecule_host.name, host_config, minimal_configs)

    # 1. Verify the function returns the correct object type.
    assert isinstance(result_catalog, AntaCatalog)

    # 2. Compare the generated catalog with the expected data.
    expected_data = deepcopy(molecule_host.test_catalog)

    # Use the .dump() method to serialize the result into the same categorized
    # dictionary format as the expected data file.
    result_data = json.loads(result_catalog.dump().to_json())

    # The final assertion ensures the generated content is identical to the expected output.
    assert result_data == expected_data
