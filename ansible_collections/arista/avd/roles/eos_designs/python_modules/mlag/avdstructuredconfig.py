# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get


class AvdStructuredConfigMlag(AvdFacts):
    def render(self):
        """
        Wrap class render function with a check for mlag is True
        """
        if self.shared_utils.mlag is True:
            return super().render()
        return {}

    @cached_property
    def _trunk_groups_mlag_name(self):
        return get(self.shared_utils.trunk_groups, "mlag.name", required=True)

    @cached_property
    def _trunk_groups_mlag_l3_name(self):
        return get(self.shared_utils.trunk_groups, "mlag_l3.name", required=True)

    @cached_property
    def spanning_tree(self):
        if self.shared_utils.mlag_peer_l3_vlan is not None:
            vlans = [self.shared_utils.mlag_peer_vlan, self.shared_utils.mlag_peer_l3_vlan]
            return {"no_spanning_tree_vlan": list_compress(vlans)}

        return {"no_spanning_tree_vlan": self.shared_utils.mlag_peer_vlan}

    @cached_property
    def vlans(self) -> list:
        vlans = []
        if self.shared_utils.mlag_peer_l3_vlan is not None:
            vlans.append(
                {
                    "id": self.shared_utils.mlag_peer_l3_vlan,
                    "tenant": "system",
                    "name": "LEAF_PEER_L3",
                    "trunk_groups": [self._trunk_groups_mlag_l3_name],
                }
            )

        vlans.append(
            {
                "id": self.shared_utils.mlag_peer_vlan,
                "tenant": "system",
                "name": "MLAG_PEER",
                "trunk_groups": [self._trunk_groups_mlag_name],
            }
        )
        return vlans

    @cached_property
    def vlan_interfaces(self) -> list | None:
        """
        Return list with VLAN Interfaces used for MLAG

        May return both the main MLAG VLAN as well as a dedicated L3 VLAN
        Can also combine L3 configuration on the main MLAG VLAN
        """

        # Create Main MLAG VLAN Interface
        main_vlan_interface_name = f"Vlan{self.shared_utils.mlag_peer_vlan}"
        main_vlan_interface = {
            "name": main_vlan_interface_name,
            "description": "MLAG_PEER",
            "shutdown": False,
            "ip_address": f"{self.shared_utils.mlag_ip}/31",
            "no_autostate": True,
            "struct_cfg": self.shared_utils.mlag_peer_vlan_structured_config,
            "mtu": self.shared_utils.p2p_uplinks_mtu,
        }
        if not self.shared_utils.mlag_l3:
            return [strip_empties_from_dict(main_vlan_interface)]

        # Create L3 data which will go on either a dedicated l3 vlan or the main mlag vlan
        l3_cfg = {
            "struct_cfg": get(self.shared_utils.switch_data_combined, "mlag_peer_l3_vlan_structured_config"),
        }
        if self.shared_utils.underlay_routing_protocol == "ospf":
            l3_cfg.update(
                {
                    "ospf_network_point_to_point": True,
                    "ospf_area": self.shared_utils.underlay_ospf_area,
                }
            )

        elif self.shared_utils.underlay_routing_protocol == "isis":
            l3_cfg.update(
                {
                    "isis_enable": self.shared_utils.isis_instance_name,
                    "isis_metric": 50,
                    "isis_network_point_to_point": True,
                }
            )

        if self.shared_utils.underlay_multicast:
            l3_cfg["pim"] = {"ipv4": {"sparse_mode": True}}

        if self.shared_utils.underlay_rfc5549:
            l3_cfg["ipv6_enable"] = True

        # Add L3 config if the main interface is also used for L3 peering
        if self.shared_utils.mlag_peer_l3_vlan is None:
            main_vlan_interface.update(l3_cfg)
            # Applying structured config again in the case it is set on both l3vlan and main vlan
            if self.shared_utils.mlag_peer_vlan_structured_config is not None:
                main_vlan_interface["struct_cfg"] = self.shared_utils.mlag_peer_vlan_structured_config

            return [strip_empties_from_dict(main_vlan_interface)]

        # Next create l3 interface if not using the main vlan
        l3_vlan_interface_name = f"Vlan{self.shared_utils.mlag_peer_l3_vlan}"
        l3_vlan_interface = {
            "name": l3_vlan_interface_name,
            "description": "MLAG_PEER_L3_PEERING",
            "shutdown": False,
            "mtu": self.shared_utils.p2p_uplinks_mtu,
        }
        if not self.shared_utils.underlay_rfc5549:
            l3_vlan_interface["ip_address"] = f"{self.shared_utils.mlag_l3_ip}/31"

        l3_vlan_interface.update(l3_cfg)

        return [
            strip_empties_from_dict(l3_vlan_interface),
            strip_empties_from_dict(main_vlan_interface),
        ]

    @cached_property
    def port_channel_interfaces(self):
        """
        Return dict with one Port Channel Interface used for MLAG Peer Link
        """

        port_channel_interface_name = f"Port-Channel{self.shared_utils.mlag_port_channel_id}"
        port_channel_interface = {
            "name": port_channel_interface_name,
            "description": self.shared_utils.interface_descriptions.mlag_port_channel_interfaces(),
            "type": "switched",
            "shutdown": False,
            "vlans": get(self.shared_utils.switch_data_combined, "mlag_peer_link_allowed_vlans"),
            "mode": "trunk",
            "service_profile": self.shared_utils.p2p_uplinks_qos_profile,
            "trunk_groups": [self._trunk_groups_mlag_name],
            "struct_cfg": get(self.shared_utils.switch_data_combined, "mlag_port_channel_structured_config"),
        }

        if self.shared_utils.mlag_l3 is True and self._trunk_groups_mlag_l3_name != self._trunk_groups_mlag_name:
            # Add LEAF_PEER_L3 even if we reuse the MLAG trunk group for underlay peering
            # since this trunk group is also used for overlay iBGP peerings
            # except in the case where the same trunk group name is defined.
            port_channel_interface["trunk_groups"].append(self._trunk_groups_mlag_l3_name)
            # Retain legacy order
            port_channel_interface["trunk_groups"].reverse()

        if (self.shared_utils.fabric_sflow_mlag_interfaces) is not None:
            port_channel_interface["sflow"] = {"enable": self.shared_utils.fabric_sflow_mlag_interfaces}

        if self.shared_utils.ptp_enabled and self.shared_utils.ptp_mlag:
            ptp_config = {}
            ptp_config.update(self.shared_utils.ptp_profile)
            ptp_config["enable"] = True
            ptp_config.pop("profile", None)
            # Apply ptp config to port-channel
            port_channel_interface["ptp"] = ptp_config

        return [strip_empties_from_dict(port_channel_interface)]

    @cached_property
    def ethernet_interfaces(self):
        """
        Return dict with Ethernet Interfaces used for MLAG Peer Link
        """

        if not (mlag_interfaces := self.shared_utils.mlag_interfaces):
            return None

        ethernet_interfaces = []
        for mlag_interface in mlag_interfaces:
            ethernet_interface = {
                "name": mlag_interface,
                "peer": self.shared_utils.mlag_peer,
                "peer_interface": mlag_interface,
                "peer_type": "mlag_peer",
                "description": self.shared_utils.interface_descriptions.mlag_ethernet_interfaces(mlag_interface),
                "type": "port-channel-member",
                "shutdown": False,
                "channel_group": {
                    "id": self.shared_utils.mlag_port_channel_id,
                    "mode": "active",
                },
                "speed": self.shared_utils.mlag_interfaces_speed,
            }
            ethernet_interfaces.append(strip_empties_from_dict(ethernet_interface))

        return ethernet_interfaces

    @cached_property
    def mlag_configuration(self):
        """
        Return Structured Config for MLAG Configuration
        """

        mlag_configuration = {
            "domain_id": get(self.shared_utils.switch_data_combined, "mlag_domain_id", default=self.shared_utils.group),
            "local_interface": f"Vlan{self.shared_utils.mlag_peer_vlan}",
            "peer_address": self.shared_utils.mlag_peer_ip,
            "peer_link": f"Port-Channel{self.shared_utils.mlag_port_channel_id}",
            "reload_delay_mlag": get(self.shared_utils.platform_settings, "reload_delay.mlag"),
            "reload_delay_non_mlag": get(self.shared_utils.platform_settings, "reload_delay.non_mlag"),
        }
        if (
            get(self.shared_utils.switch_data_combined, "mlag_dual_primary_detection", default=False) is True
            and self.shared_utils.mlag_peer_mgmt_ip is not None
            and (self.shared_utils.mgmt_interface_vrf) is not None
        ):
            mlag_configuration.update(
                {
                    "peer_address_heartbeat": {
                        "peer_ip": self.shared_utils.mlag_peer_mgmt_ip,
                        "vrf": self.shared_utils.mgmt_interface_vrf,
                    },
                    "dual_primary_detection_delay": 5,
                }
            )

        return strip_empties_from_dict(mlag_configuration)

    @cached_property
    def route_maps(self):
        """
        Return dict with one route-map
        Origin Incomplete for MLAG iBGP learned routes

        TODO: Partially duplicated in network_services. Should be moved to a common class
        """

        if not (self.shared_utils.mlag_l3 is True and self.shared_utils.mlag_ibgp_origin_incomplete is True and self.shared_utils.underlay_bgp):
            return None

        return [
            {
                "name": "RM-MLAG-PEER-IN",
                "sequence_numbers": [
                    {
                        "sequence": 10,
                        "type": "permit",
                        "set": ["origin incomplete"],
                        "description": "Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
                    }
                ],
            }
        ]

    @cached_property
    def router_bgp(self):
        """
        Return structured config for router bgp

        Peer group and underlay MLAG iBGP peering is created only for BGP underlay.
        For other underlay protocols the MLAG peer-group may be created as part of the network services logic.
        """

        if not (self.shared_utils.mlag_l3 is True and self.shared_utils.underlay_bgp):
            return None

        # MLAG Peer group
        peer_group_name = self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]
        router_bgp = self._router_bgp_mlag_peer_group()

        # Underlay MLAG peering
        if self.shared_utils.underlay_rfc5549:
            vlan = default(self.shared_utils.mlag_peer_l3_vlan, self.shared_utils.mlag_peer_vlan)
            neighbor_interface_name = f"Vlan{vlan}"
            router_bgp["neighbor_interfaces"] = [
                {
                    "name": neighbor_interface_name,
                    "peer_group": peer_group_name,
                    "peer": self.shared_utils.mlag_peer,
                    "remote_as": self.shared_utils.bgp_as,
                    "description": self.shared_utils.mlag_peer,
                }
            ]

        else:
            neighbor_ip = default(self.shared_utils.mlag_peer_l3_ip, self.shared_utils.mlag_peer_ip)
            router_bgp["neighbors"] = [
                {
                    "ip_address": neighbor_ip,
                    "peer_group": peer_group_name,
                    "peer": self.shared_utils.mlag_peer,
                    "description": self.shared_utils.mlag_peer,
                }
            ]

        return strip_empties_from_dict(router_bgp)

    def _router_bgp_mlag_peer_group(self) -> dict:
        """
        Return a partial router_bgp structured_config covering the MLAG peer_group
        and associated address_family activations

        TODO: Duplicated in network_services. Should be moved to a common class
        """
        peer_group_name = self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]
        router_bgp = {}
        peer_group = {
            "name": peer_group_name,
            "type": "ipv4",
            "remote_as": self.shared_utils.bgp_as,
            "next_hop_self": True,
            "description": self.shared_utils.mlag_peer,
            "password": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["password"],
            "bfd": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["bfd"],
            "maximum_routes": 12000,
            "send_community": "all",
            "struct_cfg": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["structured_config"],
        }
        if self.shared_utils.mlag_ibgp_origin_incomplete is True:
            peer_group["route_map_in"] = "RM-MLAG-PEER-IN"

        router_bgp["peer_groups"] = [strip_empties_from_dict(peer_group)]

        if self.shared_utils.underlay_ipv6:
            router_bgp["address_family_ipv6"] = {
                "peer_groups": [
                    {
                        "name": peer_group_name,
                        "activate": True,
                    }
                ]
            }

        address_family_ipv4_peer_group = {"name": peer_group_name, "activate": True}
        if self.shared_utils.underlay_rfc5549:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6": {"enabled": True, "originate": True}}

        router_bgp["address_family_ipv4"] = {"peer_groups": [address_family_ipv4_peer_group]}

        return router_bgp
