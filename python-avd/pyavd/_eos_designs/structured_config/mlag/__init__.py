# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator, structured_config_contributor
from pyavd._utils import AvdStringFormatter, default
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.j2filters import list_compress


class AvdStructuredConfigMlag(StructuredConfigGenerator):
    def render(self) -> None:
        """Wrap class render function with a check for mlag is True."""
        if self.shared_utils.mlag is True:
            return super().render()
        return None

    @structured_config_contributor
    def spanning_tree(self) -> None:
        vlans = [self.shared_utils.node_config.mlag_peer_vlan]
        if self.shared_utils.mlag_peer_l3_vlan is not None:
            vlans.append(self.shared_utils.mlag_peer_l3_vlan)

        self.structured_config.spanning_tree.no_spanning_tree_vlan = list_compress(vlans)

    @structured_config_contributor
    def vlans(self) -> None:
        if self.shared_utils.mlag_peer_l3_vlan is not None and self.shared_utils.underlay_routing_protocol != "none":
            self.structured_config.vlans.append_new(
                id=self.shared_utils.mlag_peer_l3_vlan,
                tenant="system",
                name=AvdStringFormatter().format(
                    self.inputs.mlag_peer_l3_vlan_name, mlag_peer=self.shared_utils.mlag_peer, mlag_peer_l3_vlan=self.shared_utils.mlag_peer_l3_vlan
                ),
                trunk_groups=EosCliConfigGen.VlansItem.TrunkGroups([self.inputs.trunk_groups.mlag_l3.name]),
            )

        self.structured_config.vlans.append_new(
            id=self.shared_utils.node_config.mlag_peer_vlan,
            tenant="system",
            name=AvdStringFormatter().format(
                self.inputs.mlag_peer_vlan_name, mlag_peer=self.shared_utils.mlag_peer, mlag_peer_vlan=self.shared_utils.node_config.mlag_peer_vlan
            ),
            trunk_groups=EosCliConfigGen.VlansItem.TrunkGroups([self.inputs.trunk_groups.mlag.name]),
        )

    @structured_config_contributor
    def vlan_interfaces(self) -> None:
        """
        Set list with VLAN Interfaces used for MLAG.

        May set both the main MLAG VLAN as well as a dedicated L3 VLAN if we have an underlay routing protocol.
        Can also combine L3 configuration on the main MLAG VLAN
        """
        # Create Main MLAG VLAN Interface
        main_vlan_interface_name = f"Vlan{self.shared_utils.node_config.mlag_peer_vlan}"
        main_vlan_interface = EosCliConfigGen.VlanInterfacesItem(
            name=main_vlan_interface_name,
            description=self.shared_utils.interface_descriptions.mlag_peer_svi(
                InterfaceDescriptionData(shared_utils=self.shared_utils, interface=main_vlan_interface_name)
            ),
            shutdown=False,
            no_autostate=True,
            mtu=self.shared_utils.p2p_uplinks_mtu,
        )

        if self.shared_utils.node_config.mlag_peer_vlan_structured_config:
            self.custom_structured_configs.nested.vlan_interfaces.obtain(main_vlan_interface_name)._deepmerge(
                self.shared_utils.node_config.mlag_peer_vlan_structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.node_config.mlag_peer_address_family == "ipv6":
            main_vlan_interface.ipv6_address = f"{self.shared_utils.mlag_ip}/{self.inputs.fabric_ip_addressing.mlag.ipv6_prefix_length}"
        else:
            main_vlan_interface.ip_address = f"{self.shared_utils.mlag_ip}/{self.inputs.fabric_ip_addressing.mlag.ipv4_prefix_length}"
        if not self.shared_utils.mlag_l3 or self.shared_utils.underlay_routing_protocol == "none":
            self.structured_config.vlan_interfaces.append(main_vlan_interface)
            return

        # Add L3 config if the main interface is also used for L3 peering
        if self.shared_utils.mlag_peer_l3_vlan is None:
            self._set_mlag_l3_vlan_interface(main_vlan_interface)
            # Applying structured config from l3_vlan only when not set on the main vlan
            if self.shared_utils.node_config.mlag_peer_l3_vlan_structured_config and not self.shared_utils.node_config.mlag_peer_vlan_structured_config:
                self.custom_structured_configs.nested.vlan_interfaces.obtain(main_vlan_interface_name)._deepmerge(
                    self.shared_utils.node_config.mlag_peer_l3_vlan_structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                )

            return

        # Next create l3 interface if not using the main vlan
        l3_vlan_interface_name = f"Vlan{self.shared_utils.mlag_peer_l3_vlan}"
        l3_vlan_interface = EosCliConfigGen.VlanInterfacesItem(
            name=l3_vlan_interface_name,
            description=self.shared_utils.interface_descriptions.mlag_peer_l3_svi(
                InterfaceDescriptionData(shared_utils=self.shared_utils, interface=l3_vlan_interface_name)
            ),
            shutdown=False,
            mtu=self.shared_utils.p2p_uplinks_mtu,
        )
        if not self.inputs.underlay_rfc5549:
            l3_vlan_interface.ip_address = f"{self.shared_utils.mlag_l3_ip}/{self.inputs.fabric_ip_addressing.mlag.ipv4_prefix_length}"

        self._set_mlag_l3_vlan_interface(l3_vlan_interface)

        if self.shared_utils.node_config.mlag_peer_l3_vlan_structured_config:
            self.custom_structured_configs.nested.vlan_interfaces.obtain(l3_vlan_interface_name)._deepmerge(
                self.shared_utils.node_config.mlag_peer_l3_vlan_structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )
        self.structured_config.vlan_interfaces.append(main_vlan_interface)

    def _set_mlag_l3_vlan_interface(self, vlan_interface: EosCliConfigGen.VlanInterfacesItem) -> None:
        if self.shared_utils.underlay_routing_protocol == "ospf":
            vlan_interface._update(
                ospf_network_point_to_point=True,
                ospf_area=self.inputs.underlay_ospf_area,
            )

        elif self.shared_utils.underlay_routing_protocol == "isis":
            vlan_interface._update(
                isis_enable=self.shared_utils.isis_instance_name,
                isis_bfd=self.inputs.underlay_isis_bfd or None,
                isis_metric=50,
                isis_network_point_to_point=True,
            )
            if self.inputs.underlay_isis_authentication_mode:
                vlan_interface.isis_authentication.both.mode = self.inputs.underlay_isis_authentication_mode

            if self.inputs.underlay_isis_authentication_key is not None:
                vlan_interface.isis_authentication.both._update(
                    key=self.inputs.underlay_isis_authentication_key,
                    key_type="7",
                )
        if self.shared_utils.underlay_multicast:
            vlan_interface.pim.ipv4.sparse_mode = True

        if self.inputs.underlay_rfc5549:
            vlan_interface.ipv6_enable = True
        self.structured_config.vlan_interfaces.append(vlan_interface)

    @structured_config_contributor
    def port_channel_interfaces(self) -> None:
        """Set one Port Channel Interface used for MLAG Peer Link."""
        port_channel_interface_name = f"Port-Channel{self.shared_utils.mlag_port_channel_id}"

        port_channel_interface = EosCliConfigGen.PortChannelInterfacesItem(
            name=port_channel_interface_name,
            description=self.shared_utils.interface_descriptions.mlag_port_channel_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=port_channel_interface_name,
                    peer_interface=f"Port-Channel{self.shared_utils.mlag_peer_port_channel_id}",
                    # The description class has @property methods for other mlag related facts.
                ),
            ),
            shutdown=False,
            service_profile=self.inputs.p2p_uplinks_qos_profile,
            flow_tracker=self.shared_utils.get_flow_tracker(
                self.inputs.fabric_flow_tracking.mlag_interfaces, EosCliConfigGen.PortChannelInterfacesItem.FlowTracker
            ),
        )

        port_channel_interface.switchport._update(enabled=True, mode="trunk")
        port_channel_interface.switchport.trunk.allowed_vlan = self.shared_utils.node_config.mlag_peer_link_allowed_vlans
        port_channel_interface.switchport.trunk.groups.append(self.inputs.trunk_groups.mlag.name)

        if self.shared_utils.node_config.mlag_port_channel_structured_config:
            self.custom_structured_configs.nested.port_channel_interfaces.obtain(port_channel_interface_name)._deepmerge(
                self.shared_utils.node_config.mlag_port_channel_structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.mlag_l3 is True and self.inputs.trunk_groups.mlag_l3.name != self.inputs.trunk_groups.mlag.name:
            # Add mlag_l3 trunk group even if we reuse the MLAG trunk group for underlay peering
            # since this trunk group is also used for overlay iBGP peerings
            # except in the case where the same trunk group name is defined.
            port_channel_interface.switchport.trunk.groups.append(self.inputs.trunk_groups.mlag_l3.name)

        if (self.inputs.fabric_sflow.mlag_interfaces) is not None:
            port_channel_interface.sflow.enable = self.inputs.fabric_sflow.mlag_interfaces

        if self.shared_utils.ptp_enabled and self.shared_utils.node_config.ptp.mlag:
            ptp_profile_config = self.shared_utils.ptp_profile._deepcopy()
            delattr(ptp_profile_config, "profile")
            port_channel_interface.ptp = ptp_profile_config._cast_as(EosCliConfigGen.PortChannelInterfacesItem.Ptp, ignore_extra_keys=True)
            port_channel_interface.ptp.enable = True

        if self.shared_utils.mlag and self.shared_utils.mlag_peer_facts.inband_ztp is True:
            port_channel_interface._update(
                lacp_fallback_mode="individual", lacp_fallback_timeout=self.shared_utils.mlag_peer_facts.inband_ztp_lacp_fallback_delay
            )

        self.structured_config.port_channel_interfaces.append(port_channel_interface)

    @structured_config_contributor
    def ethernet_interfaces(self) -> None:
        """Set list of Ethernet Interfaces used for MLAG Peer Link."""
        for index, mlag_interface in enumerate(self.shared_utils.mlag_interfaces):
            ethernet_interface = EosCliConfigGen.EthernetInterfacesItem(
                name=mlag_interface,
                peer=self.shared_utils.mlag_peer,
                peer_interface=mlag_interface,
                peer_type="mlag_peer",
                description=self.shared_utils.interface_descriptions.mlag_ethernet_interface(
                    InterfaceDescriptionData(
                        shared_utils=self.shared_utils,
                        interface=mlag_interface,
                        peer_interface=self.shared_utils.mlag_peer_interfaces[index],
                        # The description class has @property methods for other mlag related facts.
                    ),
                ),
                shutdown=False,
                speed=self.shared_utils.node_config.mlag_interfaces_speed,
            )
            ethernet_interface.channel_group._update(id=self.shared_utils.mlag_port_channel_id, mode="active")
            if self.shared_utils.mlag and self.shared_utils.mlag_peer_facts.inband_ztp is True:
                ethernet_interface.switchport._update(enabled=True, mode="access", access_vlan=self.shared_utils.mlag_peer_facts.inband_ztp_vlan)
            self.structured_config.ethernet_interfaces.append(ethernet_interface)

    @structured_config_contributor
    def mlag_configuration(self) -> None:
        """Set the Structured Config for MLAG Configuration."""
        mlag_configuration = EosCliConfigGen.MlagConfiguration(
            domain_id=default(self.shared_utils.node_config.mlag_domain_id, self.shared_utils.group),
            local_interface=f"Vlan{self.shared_utils.node_config.mlag_peer_vlan}",
            peer_address=self.shared_utils.mlag_peer_ip,
            peer_link=f"Port-Channel{self.shared_utils.mlag_port_channel_id}",
            reload_delay_mlag=str(default(self.shared_utils.platform_settings.reload_delay.mlag, "")) or None,
            reload_delay_non_mlag=str(default(self.shared_utils.platform_settings.reload_delay.non_mlag, "")) or None,
        )
        if self.shared_utils.node_config.mlag_dual_primary_detection and self.shared_utils.mlag_peer_mgmt_ip and self.inputs.mgmt_interface_vrf:
            mlag_configuration.peer_address_heartbeat._update(
                peer_ip=self.shared_utils.mlag_peer_mgmt_ip,
                vrf=self.inputs.mgmt_interface_vrf,
            )
            mlag_configuration.dual_primary_detection_delay = 5
        self.structured_config.mlag_configuration = mlag_configuration

    @structured_config_contributor
    def route_maps(self) -> None:
        """
        Set list of route-maps.

        Origin Incomplete for MLAG iBGP learned routes.

        TODO: Partially duplicated in network_services. Should be moved to a common class
        """
        if not (self.shared_utils.mlag_l3 and self.shared_utils.node_config.mlag_ibgp_origin_incomplete and self.shared_utils.underlay_bgp):
            return

        route_map = EosCliConfigGen.RouteMapsItem(name="RM-MLAG-PEER-IN")
        route_map.sequence_numbers.append_new(
            sequence=10,
            type="permit",
            description="Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["origin incomplete"]),
        )
        self.structured_config.route_maps.append(route_map)

    @structured_config_contributor
    def router_bgp(self) -> None:
        """
        Set the structured config for router bgp.

        Peer group and underlay MLAG iBGP peering is created only for BGP underlay.
        For other underlay protocols the MLAG peer-group may be created as part of the network services logic.
        """
        if not (self.shared_utils.mlag_l3 is True and self.shared_utils.underlay_bgp):
            return

        # MLAG Peer group
        peer_group_name = self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name
        self.shared_utils.update_router_bgp_with_mlag_peer_group(self.structured_config.router_bgp, self.custom_structured_configs)

        vlan = default(self.shared_utils.mlag_peer_l3_vlan, self.shared_utils.node_config.mlag_peer_vlan)
        interface_name = f"Vlan{vlan}"

        # Underlay MLAG peering
        if self.inputs.underlay_rfc5549:
            self.structured_config.router_bgp.neighbor_interfaces.append_new(
                name=interface_name,
                peer_group=peer_group_name,
                peer=self.shared_utils.mlag_peer,
                remote_as=self.shared_utils.bgp_as,
                description=AvdStringFormatter().format(
                    self.inputs.mlag_bgp_peer_description,
                    mlag_peer=self.shared_utils.mlag_peer,
                    interface=interface_name,
                    peer_interface=interface_name,
                ),
            )

        else:
            neighbor_ip = default(self.shared_utils.mlag_peer_l3_ip, self.shared_utils.mlag_peer_ip)
            self.structured_config.router_bgp.neighbors.append_new(
                ip_address=neighbor_ip,
                peer_group=peer_group_name,
                peer=self.shared_utils.mlag_peer,
                description=AvdStringFormatter().format(
                    self.inputs.mlag_bgp_peer_description,
                    mlag_peer=self.shared_utils.mlag_peer,
                    interface=interface_name,
                    peer_interface=interface_name,
                ),
            )
