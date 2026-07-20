# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from types import SimpleNamespace

from pyavd._eos_designs.structured_config.network_services.utils import UtilsMixin


class UtilsMixinTester(UtilsMixin):
    def __init__(self, *, preserve_order: bool, svis: list[SimpleNamespace]) -> None:
        self.inputs = SimpleNamespace(avd_design_future=SimpleNamespace(preserve_svi_vrf_default_prefix_list_order=preserve_order))
        self.shared_utils = SimpleNamespace(filtered_tenants=[SimpleNamespace(vrfs={"default": SimpleNamespace(svis=svis)})])


def test_vrf_default_ipv4_subnets_legacy_order() -> None:
    """Test the legacy set-to-list behavior using a single prefix since the output order is not guaranteed."""
    utils = UtilsMixinTester(
        preserve_order=False,
        svis=[SimpleNamespace(ip_address="10.0.0.1/24", ip_address_virtual=None, ip_address_secondaries=[])],
    )

    assert utils._vrf_default_ipv4_subnets == ["10.0.0.0/24"]


def test_vrf_default_ipv4_subnets_preserve_order() -> None:
    utils = UtilsMixinTester(
        preserve_order=True,
        svis=[
            SimpleNamespace(ip_address="10.0.2.1/24", ip_address_virtual=None, ip_address_secondaries=["10.0.0.1/24"]),
            SimpleNamespace(ip_address="10.0.1.1/24", ip_address_virtual=None, ip_address_secondaries=["10.0.2.2/24"]),
        ],
    )

    assert utils._vrf_default_ipv4_subnets == ["10.0.2.0/24", "10.0.0.0/24", "10.0.1.0/24"]
