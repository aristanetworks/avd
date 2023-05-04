from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.range_expand import FilterModule, AnsibleFilterError, range_expand
import pytest

RANGE_TO_EXPAND_INVALID_VALUES = ["1-3", {"key": "value"}, 33]
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
]

f = FilterModule()


class TestListCompressFilter():
    @pytest.mark.parametrize("RANGE_TO_EXPAND_INVALID", RANGE_TO_EXPAND_INVALID_VALUES)
    def test_range_expand(self, RANGE_TO_EXPAND_INVALID):
        with pytest.raises(AnsibleFilterError) as exc_info:
            range_expand(RANGE_TO_EXPAND_INVALID)
        assert str(
            exc_info.value) == f"value must be of type list or str, got {type(RANGE_TO_EXPAND_INVALID)}"

    @pytest.mark.parametrize("RANGE_TO_EXPAND_VALID", RANGE_TO_EXPAND_VALID_VALUES)
    def test_range_expand(self, RANGE_TO_EXPAND_VALID):
        resp = range_expand(RANGE_TO_EXPAND_VALID)
        assert resp in EXPECTED_RESULT_VALID_VALUES

    def test_range_expand_filter(self):
        resp = f.filters()
        assert isinstance(resp, dict)
        assert 'range_expand' in resp.keys()
