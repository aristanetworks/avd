# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, get

from ..interface_descriptions import InterfaceDescriptionData
from .utils import UtilsMixin


class EthernetInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ethernet_interfaces(self) -> list | None:
        """
        Return structured config for ethernet_interfaces
        """
        ethernet_interfaces = []

        for link in self._underlay_links:
            # common values
            description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=link["interface"],
                    link_type=link["type"],
                    peer=link["peer"],
                    peer_interface=link["peer_interface"],
                )
            )
            ethernet_interface = {
                "name": link["interface"],
                "peer": link["peer"],
                "peer_interface": link["peer_interface"],
                "peer_type": link["peer_type"],
                "description": description,
                "speed": link.get("speed"),
                "shutdown": self.shared_utils.shutdown_interfaces_towards_undeployed_peers and not link["peer_is_deployed"],
            }

            # L3 interface
            # Used for p2p uplinks as well as main interface for p2p-vrfs.
            if link["type"] == "underlay_p2p":
                ethernet_interface.update(
                    {
                        "mtu": self.shared_utils.p2p_uplinks_mtu,
                        "service_profile": self.shared_utils.p2p_uplinks_qos_profile,
                        "mac_security": link.get("mac_security"),
                        "type": "routed",
                        "ipv6_enable": link.get("ipv6_enable"),
                        "link_tracking_groups": link.get("link_tracking_groups"),
                        "sflow": link.get("sflow"),
                    }
                )

                # PTP
                if get(link, "ptp.enable") is True:
                    ptp_config = {}

                    # Apply PTP profile config if using the new ptp config style
                    if self.shared_utils.ptp_enabled:
                        ptp_config.update(self.shared_utils.ptp_profile)

                    ptp_config["enable"] = True
                    ptp_config.pop("profile", None)

                    ethernet_interface["ptp"] = ptp_config

                # MPLS
                if self.shared_utils.underlay_mpls is True:
                    mpls_dict = {"ip": True}
                    if self.shared_utils.underlay_ldp is True:
                        mpls_dict["ldp"] = {
                            "interface": True,
                            "igp_sync": True,
                        }

                    ethernet_interface["mpls"] = mpls_dict

                # IP address
                if link.get("ip_address") is not None:
                    if "unnumbered" in link["ip_address"].lower():
                        ethernet_interface["ip_address"] = link["ip_address"]
                    else:
                        ethernet_interface["ip_address"] = f"{link['ip_address']}/{link['prefix_length']}"

                if self.shared_utils.underlay_ospf is True:
                    ethernet_interface["ospf_network_point_to_point"] = True
                    ethernet_interface["ospf_area"] = self.shared_utils.underlay_ospf_area

                if self.shared_utils.underlay_isis is True:
                    ethernet_interface.update(
                        {
                            "isis_enable": self.shared_utils.isis_instance_name,
                            "isis_metric": self.shared_utils.isis_default_metric,
                            "isis_network_point_to_point": True,
                            "isis_circuit_type": self.shared_utils.isis_default_circuit_type,
                        }
                    )

                if link.get("underlay_multicast") is True:
                    ethernet_interface["pim"] = {"ipv4": {"sparse_mode": True}}

                # Configuring flow tracking on LAN interfaces
                if self.shared_utils.wan_mode == "cv-pathfinder" and self.shared_utils.wan_role == "client":
                    ethernet_interface["flow_tracker"] = {"hardware": self.shared_utils.wan_ha_flow_tracker_name}

                # Structured Config
                ethernet_interface["struct_cfg"] = link.get("structured_config")

            # L2 interface
            elif link["type"] == "underlay_l2":
                if (channel_group_id := link.get("channel_group_id")) is not None:
                    ethernet_interface.update(
                        {
                            "type": "port-channel-member",
                            "channel_group": {
                                "id": int(channel_group_id),
                                "mode": "active",
                            },
                        }
                    )
                    if self.shared_utils.inband_ztp_parent and get(link, "child_mgmt_vlan"):
                        ethernet_interface.update({"mode": "access", "vlans": link["child_mgmt_vlan"]})
                else:
                    vlans = get(link, "vlans", default=[])
                    ethernet_interface.update(
                        {
                            "type": "switched",
                            "vlans": list_compress(vlans),
                            "native_vlan": link.get("native_vlan"),
                            "service_profile": self.shared_utils.p2p_uplinks_qos_profile,
                            "link_tracking_groups": link.get("link_tracking_groups"),
                        }
                    )

            # Remove None values
            ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}
            append_if_not_duplicate(
                list_of_dicts=ethernet_interfaces,
                primary_key="name",
                new_dict=ethernet_interface,
                context="Ethernet Interfaces defined for underlay",
                context_keys=["name", "peer", "peer_interface"],
            )

            # Adding subinterfaces for each VRF after the main interface.
            if link["type"] == "underlay_p2p" and "subinterfaces" in link:
                for subinterface in get(link, "subinterfaces", default=[]):
                    description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                        InterfaceDescriptionData(
                            shared_utils=self.shared_utils,
                            interface=subinterface["interface"],
                            link_type=link["type"],
                            peer=link["peer"],
                            peer_interface=subinterface["peer_interface"],
                            vrf=subinterface["vrf"],
                        )
                    )
                    ethernet_subinterface = {
                        "name": subinterface["interface"],
                        "peer": link["peer"],
                        "peer_interface": subinterface["peer_interface"],
                        "peer_type": link["peer_type"],
                        "vrf": subinterface["vrf"],
                        # TODO - for now reusing the encapsulation as it is hardcoded to the VRF ID which is used as
                        # subinterface name
                        "description": description,
                        "shutdown": self.shared_utils.shutdown_interfaces_towards_undeployed_peers and not link["peer_is_deployed"],
                        "type": "l3dot1q",
                        "encapsulation_dot1q_vlan": subinterface["encapsulation_dot1q_vlan"],
                        "ipv6_enable": subinterface.get("ipv6_enable"),
                        "sflow": link.get("sflow"),
                        "mtu": self.shared_utils.p2p_uplinks_mtu,
                    }
                    if subinterface.get("ip_address") is not None:
                        ethernet_subinterface.update({"ip_address": f"{subinterface['ip_address']}/{subinterface['prefix_length']}"}),

                    # Configuring flow tracking on LAN interfaces
                    if self.shared_utils.wan_mode == "cv-pathfinder" and self.shared_utils.wan_role == "client":
                        ethernet_interface["flow_tracker"] = {"hardware": self.shared_utils.wan_ha_flow_tracker_name}

                    ethernet_subinterface = {key: value for key, value in ethernet_subinterface.items() if value is not None}
                    append_if_not_duplicate(
                        list_of_dicts=ethernet_interfaces,
                        primary_key="name",
                        new_dict=ethernet_subinterface,
                        context="Ethernet sub-interfaces defined for underlay",
                        context_keys=["name", "peer", "peer_interface"],
                    )

        # Support l3_interface as sub interfaces
        subif_parent_interface_names = set()
        for l3_interface in self.shared_utils.l3_interfaces:
            interface_name = l3_interface["name"]
            if "." in interface_name:
                # This is a subinterface so we need to ensure that the parent is created
                parent_interface_name, subif_id = interface_name.split(".", maxsplit=1)
                subif_parent_interface_names.add(parent_interface_name)

            ethernet_interface = self._get_l3_interface_cfg(l3_interface)

            append_if_not_duplicate(
                list_of_dicts=ethernet_interfaces,
                primary_key="name",
                new_dict=ethernet_interface,
                context=f"L3 Interfaces defined under {self.shared_utils.node_type_key_data['key']} l3_interfaces",
                context_keys=["name", "peer", "peer_interface"],
            )

        subif_parent_interface_names = subif_parent_interface_names.difference(eth_int["name"] for eth_int in ethernet_interfaces)
        if subif_parent_interface_names:
            for interface_name in natural_sort(subif_parent_interface_names):
                parent_interface = {
                    "name": interface_name,
                    "type": "routed",
                    "peer_type": "l3_interface",
                    "shutdown": False,
                }

                # Configuring flow tracking on LAN interfaces
                if self.shared_utils.wan_mode == "cv-pathfinder" and self.shared_utils.wan_role == "client":
                    ethernet_interface["flow_tracker"] = {"hardware": self.shared_utils.wan_ha_flow_tracker_name}

                append_if_not_duplicate(
                    list_of_dicts=ethernet_interfaces,
                    primary_key="name",
                    new_dict=parent_interface,
                    context=f"L3 Interfaces defined under {self.shared_utils.node_type_key_data['key']} l3_interfaces",
                    context_keys=["name", "peer", "peer_interface"],
                )

        if ethernet_interfaces:
            return ethernet_interfaces

        return None
