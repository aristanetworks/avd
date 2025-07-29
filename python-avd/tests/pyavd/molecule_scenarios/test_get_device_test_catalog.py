# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from copy import deepcopy
from typing import Literal

import pytest

from pyavd import get_device_test_catalog
from pyavd._anta.lib import AntaCatalog
from pyavd.api._anta import AvdCatalogGenerationSettings, InputFactorySettings, get_minimal_structured_configs
from pyavd.api._anta.generate_anta_settings import generate_anta_settings
from tests.models import MoleculeHost, MoleculeScenario

RunName = Literal["default_run", "allow_bgp_vrfs_run", "filtered_run"]

AVD_CATALOG_FILTER: list[dict[str, list[str]]] = [
    {"skip_tests": ["VerifyNTP"]},
    {"device_list": ["dc1-svc-leaf1a", "dc1-svc-leaf1b"], "run_tests": ["VerifyReachability"]},
    {"device_list": ["dc2-spine1", "dc2-spine2"], "run_tests": ["VerifyLLDPNeighbors"], "skip_tests": ["VerifyLLDPNeighbors"]},
]


def _get_avd_catalog_generation_settings(molecule_host: MoleculeHost, run_name: RunName) -> AvdCatalogGenerationSettings | None:
    """Create the AvdCatalogGenerationSettings object based on the test run name."""
    if run_name == "allow_bgp_vrfs_run":
        return AvdCatalogGenerationSettings(input_factory_settings=InputFactorySettings(allow_bgp_vrfs=True))

    if run_name == "filtered_run":
        input_settings = InputFactorySettings()
        output_directory = None

        return generate_anta_settings(
            input_factory_settings=input_settings,
            output_dir=output_directory,
            device=molecule_host.name,
            avd_catalogs_filters=AVD_CATALOG_FILTER,
        )

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
def test_get_device_test_catalog(molecule_host: MoleculeHost, molecule_scenario: MoleculeScenario, run_name: RunName) -> None:
    """Verify get_device_test_catalog generates the correct ANTA catalog."""
    all_configs = deepcopy(molecule_scenario.structured_configs)
    minimal_configs = get_minimal_structured_configs(all_configs)
    host_config = deepcopy(molecule_host.structured_config)
    settings = _get_avd_catalog_generation_settings(molecule_host, run_name)

    expected_data = deepcopy(molecule_host.get_test_catalog(run_name=run_name))
    result_catalog = get_device_test_catalog(molecule_host.name, host_config, minimal_configs, settings=settings)

    assert isinstance(result_catalog, AntaCatalog)
    result_data = json.loads(result_catalog.dump().to_json())
    assert result_data == expected_data
