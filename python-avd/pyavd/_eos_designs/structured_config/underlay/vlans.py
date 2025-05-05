# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
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

        This function goes through all the underlay trunk groups and returns an
        inverted dict where the key is the vlan ID and the value is the list of
        the unique trunk groups that should be configured under this vlan.

        The function also creates uplink_native_vlan for this switch or downstream switches.
        """
        # TODO: - can probably do this with sets but need list in the end so not sure it is worth it
        vlans = EosCliConfigGen.Vlans()
        self._update_underlay_vlan_trunk_groups(vlans)
        for vlan in vlans:
            vlan.trunk_groups = EosCliConfigGen.VlansItem.TrunkGroups(natural_sort(set(vlan.trunk_groups)))

        self.structured_config.vlans.extend(vlans)

        # Add configuration for uplink or peer's uplink_native_vlan if it is not defined as part of network services
        switch_vlans = set(map(int, range_expand(self.facts.vlans)))
        uplink_native_vlans = natural_sort(
            {link.native_vlan for link in self._underlay_links if link.native_vlan and link.native_vlan not in switch_vlans},
        )
        for peer_uplink_native_vlan in uplink_native_vlans:
            self.structured_config.vlans.append_new(id=int(peer_uplink_native_vlan), name="NATIVE", state="suspend")

    def _update_underlay_vlan_trunk_groups(self: AvdStructuredConfigUnderlayProtocol, vlans: EosCliConfigGen.Vlans) -> None:
        """Update trunk groups to configure on the underlay link."""
        if self.inputs.enable_trunk_groups is not True:
            return

        for peer in self.facts.downlink_switches:
            peer_facts = self.shared_utils.get_peer_facts(peer)
            for uplink in peer_facts.uplinks:
                if uplink.peer != self.shared_utils.hostname or not uplink.peer_trunk_groups or not uplink.vlans:
                    continue

                for vlan_id in map(int, range_expand(uplink.vlans)):
                    vlan_item_trunk_groups = vlans.obtain(vlan_id).trunk_groups
                    for trunk_group in uplink.peer_trunk_groups:
                        vlan_item_trunk_groups.append_unique(trunk_group)
