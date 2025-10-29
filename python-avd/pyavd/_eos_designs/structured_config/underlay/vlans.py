# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd.j2filters import natural_sort, range_expand

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class VlansMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def vlans(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Set the structured config for vlans.

        The function creates uplink_native_vlan for this switch or downstream switches.
        """
        # Add configuration for uplink or peer's uplink_native_vlan if it is not defined as part of network services
        switch_vlans = set(map(int, range_expand(self.facts.vlans)))
        uplink_native_vlans = natural_sort(
            {link.native_vlan for link in self._underlay_links if link.native_vlan and link.native_vlan not in switch_vlans},
        )
        for peer_uplink_native_vlan in uplink_native_vlans:
            self.structured_config.vlans.append_new(id=int(peer_uplink_native_vlan), name="NATIVE", state="suspend")
