# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from typing import Literal

from avdutils._validation import validate_json


def test_validate_json() -> None:
    res = validate_json('{"ethernet_interfaces": [{"name": "Ethernet1"}, {"name": "Ethernet1"}, {}]}', "eos_cli_config_gen")
    result: dict[Literal["violations", "coercions"], list[dict]] = json.loads(res)
    assert result["coercions"] == []
    assert result["violations"] == [
        {"path": ["ethernet_interfaces", "2"], "item": {"Validation": {"List": "PrimaryKey"}}},
        {"item": {"Validation": {"List": "Unique"}}, "path": ["ethernet_interfaces", "0", "name"]},
        {"item": {"Validation": {"List": "Unique"}}, "path": ["ethernet_interfaces", "1", "name"]},
    ]
