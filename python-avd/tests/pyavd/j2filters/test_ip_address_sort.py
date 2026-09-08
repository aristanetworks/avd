# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest

from pyavd.j2filters.ip_address_sort import ip_address_sort


def test_ip_address_sort() -> None:
    """Test numeric sorting of IPv4 and IPv6 addresses."""
    addresses = ["11:22:33:44:55:66:77:77", "1::1/64", "::ffff:192.1.56.10", "192.0.2.10/24", "192.0.2.2/24"]

    assert ip_address_sort(addresses) == [
        "192.0.2.2/24",
        "192.0.2.10/24",
        "::ffff:192.1.56.10",
        "1::1/64",
        "11:22:33:44:55:66:77:77",
    ]

    entries = [{"address": address} for address in addresses]
    assert ip_address_sort(entries, sort_key="address") == [{"address": address} for address in ip_address_sort(addresses)]


def test_ip_address_sort_invalid_address() -> None:
    """Test that invalid IP addresses raise ValueError."""
    with pytest.raises(ValueError, match="does not appear to be an IPv4 or IPv6 interface"):
        ip_address_sort(["invalid"])
