# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.vlan import VerifyVlanInternalPolicy, VerifyVlanStatus

from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyVlanStatusInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyVlanStatus` test.

    This factory generates test inputs for verifying the status of vlans.

    The expected status is 'suspended' when the interface is shutdown, 'active' otherwise.
    """

    def create(self) -> list[VerifyVlanStatus.Input] | None:
        """Create a list of inputs for the `VerifyVlanStatus` test."""
        vlans: list[dict[str, int | str]] = [
            {"vlan_id": vlan.id, "status": "suspended" if vlan.state == "suspend" else "active"} for vlan in self.structured_config.vlans
        ]

        return [VerifyVlanStatus.Input(vlans=natural_sort(vlans, sort_key="vlan_id"))] if vlans else None


class VerifyVlanInternalPolicyInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyVlanInternalPolicy` test."""

    def create(self) -> list[VerifyVlanInternalPolicy.Input] | None:
        """Create input for the `VerifyVlanInternalPolicy` test."""
        return [
            VerifyVlanInternalPolicy.Input(
                policy=self.structured_config.vlan_internal_order.allocation,
                start_vlan_id=self.structured_config.vlan_internal_order.range.beginning,
                end_vlan_id=self.structured_config.vlan_internal_order.range.ending,
            )
        ]
