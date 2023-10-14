# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_ip_from_pool

# default values for testcases
(pool, prefixlen, subnet_offset, ip_offset) = ("1.2.3.4/24", 32, 1, 0)


@pytest.mark.parametrize(
    "pool, prefixlen, subnet_offset, ip_offset, expected",
    [
        ("1.2.3.0/32", prefixlen, subnet_offset, ip_offset, f"Unable to get {subnet_offset + 1} /{prefixlen} subnets from pool 1.2.3.0/32"),
        (pool, 8, subnet_offset, ip_offset, "Prefix length 8 is smaller than pool network prefix length"),
        (pool, prefixlen, 256, ip_offset, f"Unable to get 257 /{prefixlen} subnets from pool {pool}"),
        (pool, prefixlen, subnet_offset, 1, "Unable to get 2 hosts in subnet"),
    ],
)
def test_get_ip_from_pool_invalid(pool, prefixlen, subnet_offset, ip_offset, expected):
    """
    Invalid cases for get_ip_from_pool.
    """
    with pytest.raises(AristaAvdError) as exc_info:
        get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert expected in str(exc_info.value)


def test_get_ip_from_pool_valid():
    """
    Valid cases for get_ip_from_pool with default values.
    """

    resp = get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert resp == "1.2.3.1"
