# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from copy import deepcopy
from typing import Any, Literal

import pytest

from pyavd import get_device_test_catalog
from pyavd._anta.lib import AntaCatalog
from pyavd._utils import get
from pyavd.api.anta import AVDCatalogGenerationSettings, AVDFabricData
from tests.models import MoleculeHost, MoleculeScenario

SETTINGS_WITH_EXTRA_FABRIC_VALIDATION = AVDCatalogGenerationSettings(extra_fabric_validation=True)
SETTINGS_FILTERED_DEFAULT = AVDCatalogGenerationSettings(skip_tests=["VerifyNTP"])
SETTINGS_FILTERED_SVC_LEAF = AVDCatalogGenerationSettings(skip_tests=["VerifyNTP"], run_tests=["VerifyReachability"])
SETTINGS_FILTERED_SPINE = AVDCatalogGenerationSettings(run_tests=["VerifyLLDPNeighbors"], skip_tests=["VerifyLLDPNeighbors"])
TEST_SETTINGS_MAP: dict[str, Any] = {
    "default_run": {"default": None},
    "default_run_filtered_report": {"default": SETTINGS_WITH_EXTRA_FABRIC_VALIDATION},
    "filtered_run": {
        "default": SETTINGS_FILTERED_DEFAULT,
        # Host-specific overrides
        "dc1-svc-leaf1a": SETTINGS_FILTERED_SVC_LEAF,
        "dc1-svc-leaf1b": SETTINGS_FILTERED_SVC_LEAF,
        "dc2-spine1": SETTINGS_FILTERED_SPINE,
        "dc2-spine2": SETTINGS_FILTERED_SPINE,
    },
    "default_run_sorted_report": {"default": None},
}

RunName = Literal["default_run", "default_run_filtered_report", "filtered_run", "default_run_sorted_report"]


@pytest.mark.molecule_scenarios("anta_runner")
@pytest.mark.parametrize(
    "run_name",
    TEST_SETTINGS_MAP.keys(),
    ids=TEST_SETTINGS_MAP.keys(),
)
def test_get_device_test_catalog(molecule_host: MoleculeHost, molecule_scenario: MoleculeScenario, run_name: RunName) -> None:
    """Verify get_device_test_catalog generates the correct ANTA catalog."""
    all_configs = deepcopy(molecule_scenario.structured_configs)
    fabric_data = AVDFabricData.from_structured_configs(all_configs)
    host_config = deepcopy(molecule_host.structured_config)

    run_settings = TEST_SETTINGS_MAP[run_name]
    settings = get(run_settings, f"{molecule_host.name}", run_settings["default"])

    expected_data = deepcopy(molecule_host.get_test_catalog(run_name=run_name))

    if get(host_config, "metadata.is_deployed", default=True) is True:
        result_catalog = get_device_test_catalog(molecule_host.name, host_config, fabric_data, settings=settings)
    else:
        result_catalog = AntaCatalog()

    assert isinstance(result_catalog, AntaCatalog)
    result_data = json.loads(result_catalog.dump().to_json())
    assert result_data == expected_data
