from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, unique
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import load_interfacedescriptions


class AvdStructuredConfig(AvdFacts):
    def __init__(self, hostvars, templar):
        super().__init__(hostvars, templar)
        self._avd_interface_descriptions = load_interfacedescriptions(hostvars, templar)

    def render(self):
        """
        Wrap class render function with a check for switch.mlag is True
        """
        if self._mlag is True:
            return super().render()
        return {}

    @cached_property
    def _mlag(self):
        return get(self._hostvars, "switch.mlag")

    @cached_property
    def _mlag_l3(self):
        return get(self._hostvars, "switch.mlag_l3")

    @cached_property
    def _mlag_peer_l3_vlan(self):
        return get(self._hostvars, "switch.mlag_peer_l3_vlan")

    @cached_property
    def _mlag_peer_vlan(self):
        return get(self._hostvars, "switch.mlag_peer_vlan", required=True)

    @cached_property
    def _trunk_groups_mlag_name(self):
        return get(self._hostvars, "switch.trunk_groups.mlag.name", required=True)

    @cached_property
    def _trunk_groups_mlag_l3_name(self):
        return get(self._hostvars, "switch.trunk_groups.mlag_l3.name", required=True)

    @cached_property
    def _underlay_routing_protocol(self):
        return get(self._hostvars, "switch.underlay_routing_protocol", required=True)

    @cached_property
    def _p2p_uplinks_mtu(self):
        return get(self._hostvars, "p2p_uplinks_mtu", required=True)

    @cached_property
    def _mlag_port_channel_id(self) -> int:
        return int(get(self._hostvars, "switch.mlag_port_channel_id", required=True))

    @cached_property
    def _mlag_peer(self):
        return get(self._hostvars, "switch.mlag_peer", required=True)

    @cached_property
    def _mlag_ibgp_origin_incomplete(self):
        return get(self._hostvars, "switch.mlag_ibgp_origin_incomplete")

    @cached_property
    def _underlay_rfc5549(self):
        return get(self._hostvars, "underlay_rfc5549")

    @cached_property
    def _bgp_as(self):
        return get(self._hostvars, "switch.bgp_as", required=True)

    @cached_property
    def _mlag_peer_ip(self):
        return get(self._hostvars, "switch.mlag_peer_ip", required=True)

    @cached_property
    def spanning_tree(self):
        if self._mlag_peer_l3_vlan is not None:
            vlans = unique([self._mlag_peer_vlan, self._mlag_peer_l3_vlan])
            return {"no_spanning_tree_vlan": list_compress(vlans)}

        return {"no_spanning_tree_vlan": self._mlag_peer_vlan}

    @cached_property
    def vlans(self):
        vlans = {}
        if self._mlag_peer_l3_vlan is not None:
            vlans.update(
                {
                    self._mlag_peer_l3_vlan: {
                        "tenant": "system",
                        "name": "LEAF_PEER_L3",
                        "trunk_groups": [self._trunk_groups_mlag_l3_name],
                    }
                }
            )
        vlans.update(
            {
                self._mlag_peer_vlan: {
                    "tenant": "system",
                    "name": "MLAG_PEER",
                    "trunk_groups": [self._trunk_groups_mlag_name],
                }
            }
        )
        return vlans

    @cached_property
    def vlan_interfaces(self):
        """
        Return dict with VLAN Interfaces used for MLAG

        May return both the main MLAG VLAN as well as a dedicated L3 VLAN
        Can also combine L3 configuration on the main MLAG VLAN
        """

        # Create Main MLAG VLAN Interface
        main_vlan_interface_name = f"Vlan{self._mlag_peer_vlan}"
        main_vlan_interface = {}
        main_vlan_interface["description"] = "MLAG_PEER"
        main_vlan_interface["shutdown"] = False
        ip_address = get(self._hostvars, "switch.mlag_ip", required=True)
        main_vlan_interface["ip_address"] = f"{ip_address}/31"
        main_vlan_interface["no_autostate"] = True
        main_vlan_interface["mtu"] = self._p2p_uplinks_mtu
        if (struct_cfg := get(self._hostvars, "switch.mlag_peer_vlan_structured_config")) is not None:
            main_vlan_interface["struct_cfg"] = struct_cfg

        if not self._mlag_l3:
            return {main_vlan_interface_name: main_vlan_interface}

        # Create L3 data which will go on either a dedicated l3 vlan or the main mlag vlan
        l3_cfg = {}
        if self._underlay_routing_protocol == "ospf":
            l3_cfg["ospf_network_point_to_point"] = True
            l3_cfg["ospf_area"] = get(self._hostvars, "underlay_ospf_area", required=True)

        elif self._underlay_routing_protocol == "isis":
            l3_cfg["isis_enable"] = get(self._hostvars, "switch.isis_instance_name", required=True)
            l3_cfg["isis_metric"] = 50
            l3_cfg["isis_network_point_to_point"] = True

        if get(self._hostvars, "underlay_multicast") is True:
            l3_cfg["pim"] = {"ipv4": {"sparse_mode": True}}

        if self._underlay_rfc5549 is True:
            l3_cfg["ipv6_enable"] = True

        if (struct_cfg := get(self._hostvars, "switch.mlag_peer_l3_vlan_structured_config")) is not None:
            l3_cfg["struct_cfg"] = struct_cfg

        # Add L3 config if the main interface is also used for L3 peering
        if self._mlag_peer_l3_vlan is None:
            main_vlan_interface.update(l3_cfg)
            # Applying structured config again in the case it is set on both l3vlan and main vlan
            if (struct_cfg := get(self._hostvars, "switch.mlag_peer_vlan_structured_config")) is not None:
                main_vlan_interface["struct_cfg"] = struct_cfg

            return {main_vlan_interface_name: main_vlan_interface}

        # Next create l3 interface if not using the main vlan
        l3_vlan_interface_name = f"Vlan{self._mlag_peer_l3_vlan}"
        l3_vlan_interface = {}
        l3_vlan_interface["description"] = "MLAG_PEER_L3_PEERING"
        l3_vlan_interface["shutdown"] = False
        if self._underlay_rfc5549 is not True:
            ip_address = get(self._hostvars, "switch.mlag_l3_ip", required=True)
            l3_vlan_interface["ip_address"] = f"{ip_address}/31"

        l3_vlan_interface["mtu"] = self._p2p_uplinks_mtu
        l3_vlan_interface.update(l3_cfg)

        # Assembling the interface dict to retain legacy order from Jinja templates.
        return {
            l3_vlan_interface_name: l3_vlan_interface,
            main_vlan_interface_name: main_vlan_interface,
        }

    @cached_property
    def port_channel_interfaces(self):
        """
        Return dict with one Port Channel Interface used for MLAG Peer Link
        """

        port_channel_interface_name = f"Port-Channel{self._mlag_port_channel_id}"
        port_channel_interface = {}
        port_channel_interface["description"] = self._avd_interface_descriptions.mlag_port_channel_interfaces()
        port_channel_interface["type"] = "switched"
        port_channel_interface["shutdown"] = False
        port_channel_interface["vlans"] = get(self._hostvars, "switch.mlag_peer_link_allowed_vlans", required=True)
        port_channel_interface["mode"] = "trunk"
        if (p2p_uplinks_qos_profile := get(self._hostvars, "p2p_uplinks_qos_profile")) is not None:
            port_channel_interface["service_profile"] = p2p_uplinks_qos_profile

        port_channel_interface["trunk_groups"] = []
        if self._mlag_l3 is True:
            # Add LEAF_PEER_L3 even if we reuse the MLAG trunk group for underlay peering
            # since this trunk group is also used for overlay iBGP peerings
            port_channel_interface["trunk_groups"].append(self._trunk_groups_mlag_l3_name)

        port_channel_interface["trunk_groups"].append(self._trunk_groups_mlag_name)

        if (struct_cfg := get(self._hostvars, "switch.mlag_port_channel_structured_config")) is not None:
            port_channel_interface["struct_cfg"] = struct_cfg

        return {port_channel_interface_name: port_channel_interface}

    @cached_property
    def ethernet_interfaces(self):
        """
        Return dict with Ethernet Interfaces used for MLAG Peer Link
        """

        mlag_interfaces = get(self._hostvars, "switch.mlag_interfaces", [])
        if not mlag_interfaces:
            return None

        ethernet_interfaces = {}
        for mlag_interface in mlag_interfaces:
            ethernet_interface = {}
            ethernet_interface["peer"] = self._mlag_peer
            ethernet_interface["peer_interface"] = mlag_interface
            ethernet_interface["peer_type"] = "mlag_peer"
            ethernet_interface["description"] = self._avd_interface_descriptions.mlag_ethernet_interfaces(mlag_interface)
            ethernet_interface["type"] = "switched"
            ethernet_interface["shutdown"] = False
            ethernet_interface["channel_group"] = {
                "id": self._mlag_port_channel_id,
                "mode": "active",
            }
            if (mlag_interfaces_speed := get(self._hostvars, "switch.mlag_interfaces_speed")) is not None:
                ethernet_interface["speed"] = mlag_interfaces_speed

            ethernet_interfaces[mlag_interface] = ethernet_interface

        return ethernet_interfaces

    @cached_property
    def mlag_configuration(self):
        """
        Return Structured Config for MLAG Configuration
        """

        mlag_configuration = {}
        mlag_configuration["domain_id"] = get(self._hostvars, "switch.group", required=True)
        mlag_configuration["local_interface"] = f"Vlan{self._mlag_peer_vlan}"
        mlag_configuration["peer_address"] = self._mlag_peer_ip
        if (
            get(self._hostvars, "switch.mlag_dual_primary_detection") is True
            and (mlag_peer_mgmt_ip := get(self._hostvars, "switch.mlag_peer_mgmt_ip")) is not None
            and (mgmt_interface_vrf := get(self._hostvars, "mgmt_interface_vrf")) is not None
        ):
            mlag_configuration["peer_address_heartbeat"] = {
                "peer_ip": mlag_peer_mgmt_ip,
                "vrf": mgmt_interface_vrf,
            }
            mlag_configuration["dual_primary_detection_delay"] = 5

        mlag_configuration["peer_link"] = f"Port-Channel{self._mlag_port_channel_id}"
        if (reload_delay_mlag := get(self._hostvars, "switch.platform_settings.reload_delay.mlag")) is not None:
            mlag_configuration["reload_delay_mlag"] = reload_delay_mlag

        if (reload_delay_non_mlag := get(self._hostvars, "switch.platform_settings.reload_delay.non_mlag")) is not None:
            mlag_configuration["reload_delay_non_mlag"] = reload_delay_non_mlag

        return mlag_configuration

    @cached_property
    def route_maps(self):
        """
        Return dict with one route-map
        Origin Incomplete for MLAG iBGP learned routes
        """

        if not (self._mlag_l3 is True and self._mlag_ibgp_origin_incomplete is True and self._underlay_routing_protocol == "ebgp"):
            return None

        return {
            "RM-MLAG-PEER-IN": {
                "sequence_numbers": {
                    10: {
                        "type": "permit",
                        "set": ["origin incomplete"],
                        "description": "Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
                    }
                }
            }
        }

    @cached_property
    def router_bgp(self):
        """
        Return structured config for router bgp
        MLAG iBGP peering
        """

        if not (self._mlag_l3 is True and self._underlay_routing_protocol == "ebgp"):
            return None

        router_bgp = {}
        peer_group_name = get(
            self._hostvars,
            "switch.bgp_peer_groups.mlag_ipv4_underlay_peer.name",
            required=True,
        )
        peer_group = {}
        peer_group["type"] = "ipv4"
        peer_group["remote_as"] = self._bgp_as
        peer_group["next_hop_self"] = True
        peer_group["description"] = self._mlag_peer
        if (
            password := get(
                self._hostvars,
                "switch.bgp_peer_groups.mlag_ipv4_underlay_peer.password",
            )
        ) is not None:
            peer_group["password"] = password

        peer_group["maximum_routes"] = 12000
        peer_group["send_community"] = "all"
        if self._mlag_ibgp_origin_incomplete is True:
            peer_group["route_map_in"] = "RM-MLAG-PEER-IN"

        if (
            struct_cfg := get(
                self._hostvars,
                "switch.bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config",
            )
        ) is not None:
            peer_group["struct_cfg"] = struct_cfg

        router_bgp["peer_groups"] = {peer_group_name: peer_group}

        if get(self._hostvars, "switch.underlay_ipv6") is True:
            router_bgp["address_family_ipv6"] = {"peer_groups": {peer_group_name: {"activate": True}}}

        address_family_ipv4_peer_group = {"activate": True}
        if self._underlay_rfc5549 is True:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6_originate": True}

        router_bgp["address_family_ipv4"] = {"peer_groups": {peer_group_name: address_family_ipv4_peer_group}}

        if self._underlay_rfc5549 is True:
            vlan = default(self._mlag_peer_l3_vlan, self._mlag_peer_vlan)
            neighbor_interface_name = f"Vlan{vlan}"
            neighbor_interface = {}
            neighbor_interface["peer_group"] = peer_group_name
            neighbor_interface["remote_as"] = self._bgp_as
            neighbor_interface["description"] = self._mlag_peer
            router_bgp["neighbor_interfaces"] = {neighbor_interface_name: neighbor_interface}

        else:
            neighbor_name = get(self._hostvars, "switch.mlag_peer_l3_ip", default=self._mlag_peer_ip)
            neighbor = {}
            neighbor["peer_group"] = peer_group_name
            neighbor["description"] = self._mlag_peer
            router_bgp["neighbors"] = {neighbor_name: neighbor}

        return router_bgp
