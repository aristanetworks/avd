# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from copy import deepcopy

import pytest

from pyavd import get_device_test_catalog, validate_inputs
from pyavd._anta.lib import AntaCatalog
from pyavd.api._anta import get_minimal_structured_configs
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "anta_runner",
    # "evpn_underlay_isis_overlay_ibgp",
    # "example-campus-fabric",
    # "example-single-dc-l3ls",
)
def test_get_device_test_catalog(molecule_host: MoleculeHost) -> None:
    """
    Test the get_device_test_catalog function.

    This test runs for various molecule scenarios and compares the generated ANTA
    test catalog with the expected catalog from the scenario's output files.
    """
    # The 'avd_structured_configs' fact contains the structured configuration for all devices
    # in the inventory. This is used to generate the minimal structured configs required by the catalog function.
    all_structured_configs = deepcopy(molecule_host.hostvars)

    # run validation on inputs to ensure it is converted
    validate_inputs(all_structured_configs)

    # Get the structured config for the specific device being tested in this run.
    structured_config = deepcopy(molecule_host.structured_config)
    minimal_structured_configs = get_minimal_structured_configs({molecule_host.name: structured_config})

    # Call the function under test.
    result_catalog = get_device_test_catalog(molecule_host.name, structured_config, minimal_structured_configs)

    # --- Assertions ---

    # 1. Verify the return type is an AntaCatalog.
    assert isinstance(result_catalog, AntaCatalog)

    # # 2. If the device is marked as not deployed, the catalog should be empty.
    # if not structured_config.get("is_deployed", False):
    #     assert not result_catalog, "Catalog should be empty for non-deployed devices"
    #     return

    # --- Data Comparison ---

    # 1. Get the expected catalog data from the molecule host.
    expected_catalog_data = deepcopy(molecule_host.test_catalog)

    # 2. Use the .dump() method to get the categorized catalog object.
    #    Then, convert it to a JSON string and parse it back into a Python dict.
    #    This ensures we are comparing the exact same structure and format.
    result_catalog_json = result_catalog.dump().to_json()
    result_catalog_data = json.loads(result_catalog_json)


    # 3. Assert that the generated catalog data matches the expected data.
    #    The structures should now be identical (dict grouped by category).

    assert result_catalog_data == expected_catalog_data
