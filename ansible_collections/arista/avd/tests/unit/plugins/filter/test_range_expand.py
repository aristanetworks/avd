# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible_collections.arista.avd.plugins.filter.range_expand import AnsibleFilterError, FilterModule, range_expand

RANGE_TO_EXPAND_INVALID_VALUES = [
    pytest.param(
        True,
        AnsibleFilterError,
        "Error during expansion of range 'True': range_expand only accepts a string or a list. Got <class 'bool'>.",
        id="Wrong input type - bool",
    ),
    pytest.param(
        {"key": "value"},
        AnsibleFilterError,
        "Error during expansion of range '{'key': 'value'}': range_expand only accepts a string or a list. Got <class 'dict'>.",
        id="Wrong input type - dict",
    ),
    pytest.param(33, AnsibleFilterError, "", id="Wrong input type - int"),
    pytest.param(
        "Ethernet4-2",
        AnsibleFilterError,
        "Error during expansion of range 'Ethernet4-2': Invalid range. Start value '4' is larger than end value '2'.",
        id="Wrong interface range",
    ),
    pytest.param(
        "Ethernet1,51-3/2",
        AnsibleFilterError,
        "Error during expansion of range 'Ethernet1,51-3/2': Invalid range. Start value '51' is larger than end value '3'.",
        id="Wrong module range",
    ),
    pytest.param(
        "Ethernet1.42-21",
        AnsibleFilterError,
        "Error during expansion of range 'Ethernet1.42-21': Invalid range. Start value '42' is larger than end value '21'.",
        id="Wrong subinterface range",
    ),
    pytest.param(
        "Ethernet4/2-1/4",
        AnsibleFilterError,
        "Error during expansion of range 'Ethernet4/2-1/4': Invalid range. Start value '2' is larger than end value '1'.",
        id="Wrong parent interface range",
    ),
]

RANGE_TO_EXPAND_VALID_VALUES = [
    "Ethernet1",
    "Ethernet1-2",
    "Eth 3-5,7-8",
    "et2-6,po1-2",
    ["Ethernet1"],
    ["Ethernet 1-2", "Eth3-5", "7-8"],
    ["Ethernet2-6", "Port-channel1-2"],
    ["Ethernet1/1-2", "Eth1-2/3-5,5/1-2"],
    ["Eth1.1,9-10.1", "Eth2.2-3", "Eth3/1-2.3-4"],
    "1-3",
    ["1", "2", "3"],
    "vlan1-3",
    "Et1-2/3-4/5-6",
    "65100.0",
    "65100.0-4",
    "65100.0-2,65200.1-2",
    "1-2.0-1",
    "eth{7,9,11-13}/1,21/1,26/1",
]

EXPECTED_RESULT_VALID_VALUES = [
    ["Ethernet1"],
    ["Ethernet1", "Ethernet2"],
    ["Eth 3", "Eth 4", "Eth 5", "Eth 7", "Eth 8"],
    ["et2", "et3", "et4", "et5", "et6", "po1", "po2"],
    ["Ethernet1"],
    ["Ethernet 1", "Ethernet 2", "Eth3", "Eth4", "Eth5", "7", "8"],
    ["Ethernet2", "Ethernet3", "Ethernet4", "Ethernet5", "Ethernet6", "Port-channel1", "Port-channel2"],
    ["Ethernet1/1", "Ethernet1/2", "Eth1/3", "Eth1/4", "Eth1/5", "Eth2/3", "Eth2/4", "Eth2/5", "Eth5/1", "Eth5/2"],
    ["Eth1.1", "Eth9.1", "Eth10.1", "Eth2.2", "Eth2.3", "Eth3/1.3", "Eth3/1.4", "Eth3/2.3", "Eth3/2.4"],
    ["1", "2", "3"],
    ["1", "2", "3"],
    ["vlan1", "vlan2", "vlan3"],
    ["Et1/3/5", "Et1/3/6", "Et1/4/5", "Et1/4/6", "Et2/3/5", "Et2/3/6", "Et2/4/5", "Et2/4/6"],
    ["65100.0"],
    ["65100.0", "65100.1", "65100.2", "65100.3", "65100.4"],
    ["65100.0", "65100.1", "65100.2", "65200.1", "65200.2"],
    ["1.0", "1.1", "2.0", "2.1"],
    ["eth7/1", "eth9/1", "eth11/1", "eth12/1", "eth13/1", "eth21/1", "eth26/1"],
]

f = FilterModule()


class TestRangeExpandFilter:
    @pytest.mark.parametrize("input_value, expected_raise, expected_raise_message", RANGE_TO_EXPAND_INVALID_VALUES)
    def test_range_expand_invalid(self, input_value, expected_raise, expected_raise_message):
        with pytest.raises(expected_raise, match=expected_raise_message):
            range_expand(input_value)

    @pytest.mark.parametrize(["index", "RANGE_TO_EXPAND_VALID"], enumerate(RANGE_TO_EXPAND_VALID_VALUES))
    def test_range_expand_valid(self, index, RANGE_TO_EXPAND_VALID):
        resp = range_expand(RANGE_TO_EXPAND_VALID)
        assert resp == EXPECTED_RESULT_VALID_VALUES[index]

    def test_range_expand_filter(self):
        resp = f.filters()
        assert isinstance(resp, dict)
        assert "range_expand" in resp.keys()
