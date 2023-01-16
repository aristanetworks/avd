from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.ip_addressing_utils import get_ip_from_pool

# default values for testcases
(pool, prefixlen, subnet_offset, ip_offset) = ("1.2.3.4/24", 32, 1, 0)


@pytest.mark.parametrize("pool, prefixlen, subnet_offset, ip_offset, expected", [(pool, prefixlen, subnet_offset, ip_offset, "1.2.3.1")])
def test_ip_with_default_values(pool, prefixlen, subnet_offset, ip_offset, expected):
    """
    Valid cases for get_ip_from_pool with default values.
    """

    resp = get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert resp == expected


@pytest.mark.parametrize("pool, prefixlen, subnet_offset, ip_offset", [("1.2.3.0/32", prefixlen, subnet_offset, ip_offset)])
def test_ip_with_low_subnet_size(pool, prefixlen, subnet_offset, ip_offset):
    """
    Invalid cases for get_ip_from_pool with change in pool value as "1.2.3.0/32" to make low subnet_size.
    """

    with pytest.raises(AristaAvdError) as exc_info:
        get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert str(exc_info.value) == f"Unable to get {subnet_offset + 1} /{prefixlen} subnets from pool {pool}"


@pytest.mark.parametrize("pool, prefixlen, subnet_offset, ip_offset, expected", [(pool, 8, subnet_offset, ip_offset, "negative shift count")])
def test_ip_with_lower_prefixlen(pool, prefixlen, subnet_offset, ip_offset, expected):
    """
    Invalid cases for get_ip_from_pool with change in prefixlen value as 8 to capture invalid prefixlen wrt pool.
    """

    with pytest.raises(ValueError) as exc_info:
        get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert str(exc_info.value) == expected


@pytest.mark.parametrize("pool, prefixlen, subnet_offset, ip_offset", [(pool, prefixlen, 256, ip_offset)])
def test_ip_with_high_subnet_offset(pool, prefixlen, subnet_offset, ip_offset):
    """
    Invalid cases for get_ip_from_pool with change in subnet_offset value as 256.
    """

    with pytest.raises(AristaAvdError) as exc_info:
        get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert str(exc_info.value) == f"Unable to get {subnet_offset + 1} /{prefixlen} subnets from pool {pool}"


@pytest.mark.parametrize("pool, prefixlen, subnet_offset, ip_offset", [(pool, prefixlen, subnet_offset, 1)])
def test_ip_with_more_ip_offset(pool, prefixlen, subnet_offset, ip_offset):
    """
    Invalid cases for get_ip_from_pool with change in ip_offset value as 1.
    """

    with pytest.raises(AristaAvdError) as exc_info:
        get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert f"Unable to get {ip_offset+1} hosts in subnet" in str(exc_info.value)
