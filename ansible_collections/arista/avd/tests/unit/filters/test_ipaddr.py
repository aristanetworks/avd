from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.ipaddr import FilterModule
import pytest

f = FilterModule()

VALIDATE_LIST_INPUT_EXPECTED = [('', None), (3232235521, '192.168.0.1'), ('192.168.4.256/24', None), ('192.168', None),
                                ('10.10/24', None), ('192.168.0.1/', None), ('192.168.0.1', '192.168.0.1'), ('0.0.0.0', '0.0.0.0'),
                                ('255.255.255.255', '255.255.255.255'), ('0.0.0.1/24', '0.0.0.1/24'), ('192.168.1.0/24', '192.168.1.0/24'),
                                ('192.168.2.1/24', '192.168.2.1/24'), ('192.168.3.255/24', '192.168.3.255/24'), ('fe80::100/10', 'fe80::100/10'),
                                ('be1:123::abc/64', 'be1:123::abc/64')]

IP_ADDRESSES_INPUT = ['192.24.2.1', 'host.fqdn', '::1', '192.168.32.0/24', 'fe80::100/10', True, '', '192.168.32.1/24',
                      '42540766412265424405338506004571095040/64', '192.168.1.255/24', '192.168.1.34/28', '192.168.1.34/25']

IP_ADDRESSES_VALIDATE_EXPECTED = ['192.24.2.1', '::1', '192.168.32.0/24', 'fe80::100/10', '192.168.32.1/24', '192.168.1.255/24',
                                  '192.168.1.34/28', '192.168.1.34/25']
IP_ADDRESSES_NET_EXPECTED = ['192.168.32.0/24']
IP_ADDRESSES_SUBNETWORK_EXPECTED = ['192.24.2.1/32', '::1/128', '192.168.32.0/24', 'fe80::/10', '192.168.32.0/24', '192.168.1.0/24',
                                    '192.168.1.32/28', '192.168.1.0/25']
IP_ADDRESSES_NETMASK_EXPECTED = ['255.255.255.255', 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', '255.255.255.0', 'ffc0::', '255.255.255.0',
                                 '255.255.255.0', '255.255.255.240', '255.255.255.128']
IP_ADDRESSES_PREFIX_EXPECTED = [32, 128, 24, 10, 24, 24, 28, 25]
IP_ADDRESSES_SIZE_EXPECTED = [1, 1, 256, 332306998946228968225951765070086144, 256, 256, 16, 128]
IP_NETWORK_ADDRESSES_EXPECTED = ['192.24.2.1', '::1', '192.168.32.0', 'fe80::', '192.168.32.0', '192.168.1.0', '192.168.1.32', '192.168.1.0']
IP_ADDRESSES_EXPECTED = ['192.24.2.1', '::1', 'fe80::100', '192.168.32.1', '192.168.1.255', '192.168.1.34', '192.168.1.34']
DEFAULTATTR_INPUT = [5, '5', '192.168.0.0/16']
IP_ADDRESSES_DEFAULTATTR_EXPECTED = [['192.24.2.1', '::1', '192.168.32.5/24', 'fe80::5/10', '192.168.32.5/24', '192.168.1.5/24',
                                      '192.168.1.37/28', '192.168.1.5/25'],
                                     ['192.24.2.1', '::1', '192.168.32.5/24', 'fe80::5/10', '192.168.32.5/24', '192.168.1.5/24',
                                      '192.168.1.37/28', '192.168.1.5/25'],
                                     ['192.168.32.0/24', '192.168.32.1/24', '192.168.1.255/24', '192.168.1.34/28', '192.168.1.34/25']
                                     ]
INPUT_IPMATH_OFFSET = [1, '10', -1]
IPMATH_ADDRESSES_EXPECTED = [['192.24.2.2', '::2', '192.168.32.1', 'fe80::101', '192.168.32.2', '192.168.2.0', '192.168.1.35', '192.168.1.35'],
                             ['192.24.2.11', '::b', '192.168.32.10', 'fe80::10a', '192.168.32.11', '192.168.2.9', '192.168.1.44', '192.168.1.44'],
                             ['192.24.2.0', '::', '192.168.31.255', 'fe80::ff', '192.168.32.0', '192.168.1.254', '192.168.1.33', '192.168.1.33']
                             ]
IPV4_ADDRESSES_VALIDATE_EXPECTED = ['192.24.2.1', '192.168.32.0/24', '192.168.32.1/24', '192.168.1.255/24', '192.168.1.34/28',
                                    '192.168.1.34/25']


def get_by_method(IP_ADDRESS_INPUT_LIST=None, method='validate'):
    if IP_ADDRESS_INPUT_LIST is None:
        return []
    resp_list = []
    for IP_ADDRESS in IP_ADDRESS_INPUT_LIST:
        if isinstance(IP_ADDRESS, bool) or IP_ADDRESS in ['', [], None]:
            continue
        if res := getattr(f, method)(IP_ADDRESS):
            if not isinstance(res, int):
                res = str(res)
            resp_list.append(res)
    return resp_list


def ipv4_ipv6_assert(INPUT_RESP, EXPECTED_OUTPUT):
    # f.ipv4(output) --> filters IPv4 output by leveraging validate method
    assert f.ipv4(INPUT_RESP) == f.ipv4(EXPECTED_OUTPUT)
    assert f.ipv6(INPUT_RESP) == f.ipv6(EXPECTED_OUTPUT)


class TestIpAddrFilter():
    @pytest.mark.parametrize("VALIDATE_INPUT,VALIDATE_EXPECTED", VALIDATE_LIST_INPUT_EXPECTED)
    def test_validate_function(self, VALIDATE_INPUT, VALIDATE_EXPECTED):
        '''
        Test the validate function with manual test cases
        Input: str, int, bool
        Output: Filter all valid IP
        bool input (0/1) is not considered a valid IP
        '''
        resp = f.validate(VALIDATE_INPUT)
        if resp:
            resp = str(resp)
        assert resp == VALIDATE_EXPECTED

    @pytest.mark.parametrize("IP_ADDRESS", IP_ADDRESSES_INPUT)
    def test_ipaddr_validate_item(self, IP_ADDRESS):
        '''
        Test single input to ipaddr('validate')
        '''
        resp = f.ipaddr(IP_ADDRESS)
        expected_ip = f.validate(IP_ADDRESS)
        if type(IP_ADDRESS) in (str, int) and expected_ip:
            assert resp == str(expected_ip)
        else:
            assert resp is None

    def test_ipaddr_validate_list(self):
        '''
        Test list input to ipaddr('validate')
        '''
        resp_list = f.ipaddr(IP_ADDRESSES_INPUT)
        assert f.ipaddr(IP_ADDRESSES_INPUT) == IP_ADDRESSES_VALIDATE_EXPECTED
        assert get_by_method(IP_ADDRESSES_INPUT, 'validate') == IP_ADDRESSES_VALIDATE_EXPECTED
        ipv4_ipv6_assert(resp_list, IP_ADDRESSES_VALIDATE_EXPECTED)

    def test_ipaddr_network_list(self):
        '''
        Test list input to ipaddr('net')
        network -> Filter only valid network IP (with their prefix)
        '''
        resp_list = f.ipaddr(IP_ADDRESSES_INPUT, method='net')
        assert resp_list == IP_ADDRESSES_NET_EXPECTED
        assert get_by_method(IP_ADDRESSES_INPUT, 'net') == IP_ADDRESSES_NET_EXPECTED
        ipv4_ipv6_assert(resp_list, IP_ADDRESSES_NET_EXPECTED)

    def test_ipaddr_subnetwork_list(self):
        '''
        Test list input to ipaddr('subnet')
        subnet -> Filter a valid IP and return their Network IP
        default prefix is /32 if it's just an IP
        '''
        resp_list = f.ipaddr(IP_ADDRESSES_INPUT, method='subnet')
        assert resp_list == IP_ADDRESSES_SUBNETWORK_EXPECTED
        assert get_by_method(IP_ADDRESSES_INPUT, 'subnet') == IP_ADDRESSES_SUBNETWORK_EXPECTED
        ipv4_ipv6_assert(resp_list, IP_ADDRESSES_SUBNETWORK_EXPECTED)

    def test_ipaddr_netmask_list(self):
        '''
        Test list input to ipaddr('netmask')
        netmask -> Filter a valid IP and return their subnet Mask
        default subnet mask is 255.255.255.255 if it's just an IP
        '''
        resp_list = f.ipaddr(IP_ADDRESSES_INPUT, method='netmask')
        assert resp_list == IP_ADDRESSES_NETMASK_EXPECTED
        assert get_by_method(IP_ADDRESSES_INPUT, 'netmask') == IP_ADDRESSES_NETMASK_EXPECTED
        ipv4_ipv6_assert(resp_list, IP_ADDRESSES_NETMASK_EXPECTED)

    def test_ipaddr_prefixes_list(self):
        '''
        Test list input to ipaddr('prefix')
        prefix -> Filter a valid IP and return their network prefix
        default prefix is /32 if it's just an IP
        '''
        assert f.ipaddr(IP_ADDRESSES_INPUT, method='prefix') == IP_ADDRESSES_PREFIX_EXPECTED
        assert get_by_method(IP_ADDRESSES_INPUT, 'prefix') == IP_ADDRESSES_PREFIX_EXPECTED

    def test_ipaddr_size_list(self):
        '''
        Test list input to ipaddr('size')
        size -> Filter a valid IP/pool and return the maximum # possible IPs
        default size is 1 IP (for a valid IP)
        '''
        assert f.ipaddr(IP_ADDRESSES_INPUT, method='size') == IP_ADDRESSES_SIZE_EXPECTED
        assert get_by_method(IP_ADDRESSES_INPUT, 'size') == IP_ADDRESSES_SIZE_EXPECTED

    def test_ipaddr_network_address_list(self):
        '''
        Test list input to ipaddr('network')
        network -> Filter a valid IP/pool and return only network IP
        If its only an IP address then the same is returned
        '''
        resp_list = f.ipaddr(IP_ADDRESSES_INPUT, method='network')
        assert resp_list == IP_NETWORK_ADDRESSES_EXPECTED
        assert get_by_method(IP_ADDRESSES_INPUT, 'network') == IP_NETWORK_ADDRESSES_EXPECTED
        ipv4_ipv6_assert(resp_list, IP_NETWORK_ADDRESSES_EXPECTED)

    def test_ipaddr_address_list(self):
        '''
        Test list input to ipaddr('address')
        address -> Filter a valid IP/pool and return the IP address with out prefix
        If its only an IP address then the same is returned
        '''
        resp_list = f.ipaddr(IP_ADDRESSES_INPUT, method='address')
        assert resp_list == IP_ADDRESSES_EXPECTED
        assert get_by_method(IP_ADDRESSES_INPUT, 'address') == IP_ADDRESSES_EXPECTED
        ipv4_ipv6_assert(resp_list, IP_ADDRESSES_EXPECTED)

    def test_ipaddr_defaultattr_offset_list(self):
        '''
        1) Test list input to ipaddr(<some_other_subnet>)
            <some_other_subnet> -> Filter a valid IP/pool which is subset of <some_other_subnet>
        2) Test list input to ipaddr(<integer>)
            <integer> -> Calculate the network IP and then returns the Network IP + <integer>
            If its only an IP address then the same is returned
        '''
        for indx, INPUT_VAL in enumerate(DEFAULTATTR_INPUT):
            EXPECTED_OUTPUT = IP_ADDRESSES_DEFAULTATTR_EXPECTED[indx]
            resp_list = f.ipaddr(IP_ADDRESSES_INPUT, method=INPUT_VAL)
            assert resp_list == EXPECTED_OUTPUT

    def test_ipmath_address_list(self):
        '''
        Test list input to ipmath(<integer>)
        Return the IP Address + <integer>
        '''
        for index, OFFSET in enumerate(INPUT_IPMATH_OFFSET):
            resp_list = f.ipmath(IP_ADDRESSES_INPUT, OFFSET)
            IP_ADDRESS_LIST_EXPECTED = IPMATH_ADDRESSES_EXPECTED[index]
            assert resp_list == IP_ADDRESS_LIST_EXPECTED
