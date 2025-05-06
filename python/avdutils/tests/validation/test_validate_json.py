# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
import sys
from pathlib import Path
from typing import Literal, cast

import pytest

from avdutils.validation import init_store_from_fragments, validate_json


@pytest.fixture
def init_store() -> None:
    org_path = sys.path
    # Insert /python-avd into the python path to be able to import constants from schema_tools.
    mocked_path = [str(Path(__file__).parents[4] / "python-avd"), *org_path]
    sys.path = mocked_path
    from schema_tools.constants import SCHEMAS

    init_store_from_fragments(
        eos_cli_config_gen=cast("Path", SCHEMAS["eos_cli_config_gen"].fragments_dir),
        eos_designs=cast("Path", SCHEMAS["eos_designs"].fragments_dir),
    )
    sys.path = org_path


@pytest.mark.usefixtures("init_store")
def test_validate_json() -> None:
    res = validate_json('{"ethernet_interfaces": [{"name": "Ethernet1"}, {"name": "Ethernet1"}, {}]}', "eos_cli_config_gen")
    result: dict[Literal["violations", "coercions"], list[dict]] = json.loads(res)
    assert result["coercions"] == [
        {"issue": "DefaultValueInserted", "path": ["avd_data_validation_mode"]},
        {"issue": "DefaultValueInserted", "path": ["config_end"]},
        {"issue": "DefaultValueInserted", "path": ["generate_default_config"]},
        {"issue": "DefaultValueInserted", "path": ["generate_device_documentation"]},
        {"issue": "DefaultValueInserted", "path": ["is_deployed"]},
        {"issue": "DefaultValueInserted", "path": ["transceiver_qsfp_default_mode_4x10"]},
    ]
    assert result["violations"] == [
        {
            "path": ["ethernet_interfaces", "2"],
            "issue": {"Validation": {"MissingRequiredKey": {"key": "name"}}},
        },
        {
            "path": ["ethernet_interfaces", "0", "name"],
            "issue": {"Validation": {"ValueNotUnique": {"other_path": ["ethernet_interfaces", "1", "name"]}}},
        },
        {
            "path": ["ethernet_interfaces", "1", "name"],
            "issue": {"Validation": {"ValueNotUnique": {"other_path": ["ethernet_interfaces", "0", "name"]}}},
        },
    ]
