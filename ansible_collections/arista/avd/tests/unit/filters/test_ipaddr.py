from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.ipaddr import FilterModule
import pytest

f = FilterModule()

VALIDATE_LIST_INPUT_EXPECTED = [('', None), (3232235521, '192.168.0.1'), ('192.168.4.256/24', None), ('192.168', None),
                              ('10.10/24', None), ('192.168.0.1/', None), ('192.168.0.1', '192.168.0.1'), ('0.0.0.0','0.0.0.0'),
                              ('255.255.255.255','255.255.255.255'), ('0.0.0.1/24', '0.0.0.1/24'), ('192.168.1.0/24', '192.168.1.0/24'),
                              ('192.168.2.1/24', '192.168.2.1/24'), ('192.168.3.255/24', '192.168.3.255/24')]

IP_ADDRESSES = ['192.24.2.1', 'host.fqdn', '::1', '192.168.32.0/24', 'fe80::100/10', True, '', '192.168.32.1/24', '42540766412265424405338506004571095040/64']
IP_ADDRESSES_VALIDATE_EXPECTED = ['192.24.2.1', None, '::1', '192.168.32.0/24', 'fe80::100/10', None, None, '192.168.32.1/24', None]

IP_ADDRESSES_NETWORK = ['192.24.2.1', 'host.fqdn', '::1', '192.168.32.0/24', 'fe80::100/10', True, '', '192.168.32.1/24',
                        '42540766412265424405338506004571095040/64', '192.168.1.255/24', '192.168.1.34/28', '192.168.1.34/25']
IP_ADDRESSES_NETWORK_EXPECTED = ['192.24.2.1/32', None, '::1/128', '192.168.32.0/24', 'fe80::/10', None, None, '192.168.32.0/24', None,
                                 '192.168.1.0/24', '192.168.1.32/28', '192.168.1.0/25']

class TestIpAddrFilter():
    @pytest.mark.parametrize("VALIDATE_INPUT,VALIDATE_EXPECTED", VALIDATE_LIST_INPUT_EXPECTED)
    def test_validate_function(self, VALIDATE_INPUT, VALIDATE_EXPECTED):
        resp = f.validate(VALIDATE_INPUT)
        if resp:
            resp = str(resp)
        assert resp == VALIDATE_EXPECTED

    @pytest.mark.parametrize("IP_ADDRESS", IP_ADDRESSES)
    def test_ipaddr_validate_item(self, IP_ADDRESS):
        resp = f.ipaddr(IP_ADDRESS)
        expected_ip = f.validate(IP_ADDRESS)
        if type(IP_ADDRESS) in (str,int) and expected_ip:
            assert resp == str(expected_ip)
        else:
            assert resp is None

    @pytest.mark.parametrize("IP_ADDRESS_LIST_INPUT,IP_ADDRESS_LIST_EXPECTED", [(IP_ADDRESSES, IP_ADDRESSES_VALIDATE_EXPECTED)])
    def test_ipaddr_validate_list(self, IP_ADDRESS_LIST_INPUT, IP_ADDRESS_LIST_EXPECTED):
        resp_list = f.ipaddr(IP_ADDRESS_LIST_INPUT)
        for index, resp_ip in enumerate(resp_list):
            if resp_ip:
                assert resp_ip == IP_ADDRESS_LIST_EXPECTED[index]
            else:
                assert resp_ip is None

    @pytest.mark.parametrize("IP_ADDRESS_LIST_INPUT,IP_ADDRESS_LIST_EXPECTED", [(IP_ADDRESSES_NETWORK, IP_ADDRESSES_NETWORK_EXPECTED)])
    def test_ipaddr_network_list(self, IP_ADDRESS_LIST_INPUT, IP_ADDRESS_LIST_EXPECTED):
        resp_list = f.ipaddr(IP_ADDRESS_LIST_INPUT, method = 'net')
        assert resp_list == IP_ADDRESS_LIST_EXPECTED
