# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils.shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def _avd_peers(self) -> list:
        """
        Returns a list of peers

        This cannot be loaded in shared_utils since it will not be calculated until EosDesignsFacts has been rendered
        and shared_utils are shared between EosDesignsFacts and AvdStructuredConfig classes like this one.
        """
        return natural_sort(get(self._hostvars, f"avd_topology_peers..{self.shared_utils.hostname}", separator="..", default=[]))

    @cached_property
    def _underlay_filter_peer_as_route_maps_asns(self) -> list:
        """
        Filtered ASNs
        """
        if self.shared_utils.underlay_filter_peer_as is False:
            return []

        # using set comprehension with `{}` to remove duplicates and then run natural_sort to convert to list.
        return natural_sort({link["peer_bgp_as"] for link in self._underlay_links if link["type"] == "underlay_p2p"})

    @cached_property
    def _underlay_links(self) -> list:
        """
        Returns the list of underlay links for this device
        """
        underlay_links = []
        underlay_links.extend(self._uplinks)
        if self.shared_utils.fabric_sflow_uplinks is not None:
            for uplink in underlay_links:
                uplink.update({"sflow": {"enable": self.shared_utils.fabric_sflow_uplinks}})

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self.shared_utils.hostname:
                    link = {
                        "interface": uplink["peer_interface"],
                        "peer": peer,
                        "peer_interface": uplink["interface"],
                        "peer_type": get(peer_facts, "type"),
                        "peer_is_deployed": peer_facts["is_deployed"],
                        "peer_bgp_as": get(peer_facts, "bgp_as"),
                        "type": get(uplink, "type", required=True),
                        "speed": get(uplink, "peer_speed", default=get(uplink, "speed")),
                        "ip_address": get(uplink, "peer_ip_address"),
                        "peer_ip_address": get(uplink, "ip_address"),
                        "channel_group_id": get(uplink, "peer_channel_group_id"),
                        "peer_channel_group_id": get(uplink, "channel_group_id"),
                        "channel_description": get(uplink, "peer_channel_description"),
                        "vlans": get(uplink, "vlans"),
                        "native_vlan": get(uplink, "native_vlan"),
                        "trunk_groups": get(uplink, "peer_trunk_groups"),
                        "bfd": get(uplink, "bfd"),
                        "ptp": get(uplink, "ptp"),
                        "mac_security": get(uplink, "mac_security"),
                        "short_esi": get(uplink, "peer_short_esi"),
                        "underlay_multicast": get(uplink, "underlay_multicast"),
                        "ipv6_enable": get(uplink, "ipv6_enable"),
                        "sflow": {"enable": self.shared_utils.fabric_sflow_downlinks},
                        "structured_config": get(uplink, "structured_config"),
                    }
                    underlay_links.append(strip_empties_from_dict(link))

        return natural_sort(underlay_links, "interface")

    @cached_property
    def _underlay_vlan_trunk_groups(self) -> list:
        """
        Returns a list of trunk groups to configure on the underlay link
        """
        if self.shared_utils.enable_trunk_groups is not True:
            return []

        trunk_groups = []

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self.shared_utils.hostname:
                    if (peer_trunk_groups := get(uplink, "peer_trunk_groups")) is None:
                        continue

                    trunk_groups.append(
                        {
                            "vlan_list": uplink["vlans"],
                            "trunk_groups": peer_trunk_groups,
                        }
                    )

        if trunk_groups:
            return trunk_groups

        return []

    @cached_property
    def _uplinks(self) -> list:
        return get(self._hostvars, "switch.uplinks")
