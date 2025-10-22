# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from copy import deepcopy
from typing import Any, Literal

import pytest

from pyavd import get_device_test_catalog
from pyavd._anta.lib import AntaCatalog
from pyavd._utils import get
from pyavd.api._anta import AvdCatalogGenerationSettings, InputFactorySettings, get_minimal_structured_configs
from tests.models import MoleculeHost, MoleculeScenario

SETTINGS_WITH_BGP_VRFS = AvdCatalogGenerationSettings(input_factory_settings=InputFactorySettings(allow_bgp_vrfs=True))
SETTINGS_FILTERED_DEFAULT = AvdCatalogGenerationSettings(skip_tests=["VerifyNTP"])
SETTINGS_FILTERED_SVC_LEAF = AvdCatalogGenerationSettings(skip_tests=["VerifyNTP"], run_tests=["VerifyReachability"])
SETTINGS_FILTERED_SPINE = AvdCatalogGenerationSettings(run_tests=["VerifyLLDPNeighbors"], skip_tests=["VerifyLLDPNeighbors"])
TEST_SETTINGS_MAP: dict[str, Any] = {
    "default_run": {"default": None},
    "allow_bgp_vrfs_run": {"default": SETTINGS_WITH_BGP_VRFS},
    "filtered_run": {
        "default": SETTINGS_FILTERED_DEFAULT,
        # Host-specific overrides
        "dc1-svc-leaf1a": SETTINGS_FILTERED_SVC_LEAF,
        "dc1-svc-leaf1b": SETTINGS_FILTERED_SVC_LEAF,
        "dc2-spine1": SETTINGS_FILTERED_SPINE,
        "dc2-spine2": SETTINGS_FILTERED_SPINE,
    },
}

RunName = Literal["default_run", "allow_bgp_vrfs_run", "filtered_run"]


@pytest.mark.molecule_scenarios("anta_runner")
@pytest.mark.parametrize(
    "run_name",
    TEST_SETTINGS_MAP.keys(),
    ids=TEST_SETTINGS_MAP.keys(),
)
def test_get_device_test_catalog(molecule_host: MoleculeHost, molecule_scenario: MoleculeScenario, run_name: RunName) -> None:
    """Verify get_device_test_catalog generates the correct ANTA catalog."""
    all_configs = deepcopy(molecule_scenario.structured_configs)
    minimal_configs = get_minimal_structured_configs(all_configs)
    host_config = deepcopy(molecule_host.structured_config)

    run_settings = TEST_SETTINGS_MAP[run_name]
    settings = get(run_settings, f"{molecule_host.name}", run_settings["default"])

    expected_data = deepcopy(molecule_host.get_test_catalog(run_name=run_name))
    result_catalog = get_device_test_catalog(molecule_host.name, host_config, minimal_configs, settings=settings)

    assert isinstance(result_catalog, AntaCatalog)
    result_data = json.loads(result_catalog.dump().to_json())
    assert result_data == expected_data
