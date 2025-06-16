# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.vxlan import VerifyVxlanVniBinding

from ._base_classes import AntaTestInputFactory


class VerifyVxlanVniBindingInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyVxlanVniBinding` test.

    This class extracts VNI-to-VLAN and VNI-to-VRF name bindings from the VXLAN interface
    configuration, and constructs a single input containing all bindings.
    """

    def create(self) -> list[VerifyVxlanVniBinding.Input] | None:
        """Create a list of bindings for the `VerifyVxlanVniBinding` test."""
        bindings = {}
        vxlan_config = self.structured_config.vxlan_interface.vxlan1.vxlan

        for vlan in vxlan_config.vlans:
            bindings[vlan.vni] = vlan.id

        for vrf in vxlan_config.vrfs:
            bindings[vrf.vni] = vrf.name

        return [VerifyVxlanVniBinding.Input(bindings=bindings)] if bindings else None
