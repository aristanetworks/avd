# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from copy import deepcopy
from typing import Any

import pytest

from pyavd import get_device_test_catalog
from pyavd._anta.lib import AntaCatalog
from pyavd.api._anta import AvdCatalogGenerationSettings, InputFactorySettings, get_minimal_structured_configs
from tests.models import MoleculeHost, MoleculeScenario


# Helper Function for Filter Logic
def _get_avd_catalog_generation_settings(molecule_host: MoleculeHost, run_name: str) -> AvdCatalogGenerationSettings | None:
    """Create the AvdCatalogGenerationSettings object based on the test run name."""
    if run_name == "allow_bgp_vrfs":
        return AvdCatalogGenerationSettings(input_factory_settings=InputFactorySettings(allow_bgp_vrfs=True))

    if run_name == "filtered":
        # Filter rules defined here, mirroring the playbook.
        avd_catalogs_filters: list[dict[str, Any]] = [
            {"skip_tests": ["VerifyNTP"]},
            {"device_list_group": "DC1_SVC_LEAVES", "run_tests": ["VerifyReachability"]},
            {"device_list_group": "DC2_SPINES", "run_tests": ["VerifyLLDPNeighbors"], "skip_tests": ["VerifyLLDPNeighbors"]},
        ]

        host_groups = molecule_host.hostvars.get("group_names", [])
        final_filters: dict[str, Any] = {}

        for filter_config in avd_catalogs_filters:
            device_list_group = filter_config.get("device_list_group")
            if device_list_group and device_list_group not in host_groups:
                continue

            # "Last filter wins" logic
            if "run_tests" in filter_config:
                final_filters["run_tests"] = filter_config["run_tests"]
            if "skip_tests" in filter_config:
                final_filters["skip_tests"] = filter_config["skip_tests"]

        return AvdCatalogGenerationSettings(**final_filters)

    # For the "default" run or any other case, return no settings.
    return None


@pytest.mark.molecule_scenarios("anta_runner")
@pytest.mark.parametrize(
    ("run_name"),
    [
        ("default_run"),
        ("allow_bgp_vrfs_run"),
        ("filtered_run"),
    ],
    ids=["default_run", "allow_bgp_vrfs_run", "filtered_run"],
)
def test_get_device_test_catalog(molecule_host: MoleculeHost, molecule_scenario: MoleculeScenario, run_name: str, expected_catalog_property_name: str) -> None:
    """Verify get_device_test_catalog generates the correct ANTA catalog."""
    all_configs = deepcopy(molecule_scenario.structured_configs)
    minimal_configs = get_minimal_structured_configs(all_configs)
    host_config = deepcopy(molecule_host.structured_config)
    settings = _get_avd_catalog_generation_settings(molecule_host, run_name)

    expected_data_property = getattr(molecule_host, expected_catalog_property_name)
    expected_data = deepcopy(expected_data_property)
    if not expected_data:
        pytest.skip(f"Expected catalog not found for test case: {expected_catalog_property_name}")

    result_catalog = get_device_test_catalog(molecule_host.name, host_config, minimal_configs, settings=settings)

    assert isinstance(result_catalog, AntaCatalog)
    result_data = json.loads(result_catalog.dump().to_json())
    assert result_data == expected_data
