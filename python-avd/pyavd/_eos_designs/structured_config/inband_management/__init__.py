# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_network
from typing import cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator, structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.run_once import run_once_method


class AvdStructuredConfigInbandManagement(StructuredConfigGenerator):
    @structured_config_contributor
    def inband_management(self) -> None:
        if self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6:
            self._set_vlan()
            self._set_vlan_interface()
            if self.shared_utils.configure_inband_mgmt:
                self.set_inband_mgmt_vrf()
                if self.shared_utils.inband_mgmt_gateway is not None:
                    self._set_ipv4_default_route()
            if self.shared_utils.configure_inband_mgmt_ipv6:
                if self.inputs.avd_design_future.configure_inband_mgmt_ipv6_vrf:
                    self.set_inband_mgmt_vrf()
                if self.shared_utils.inband_mgmt_ipv6_gateway is not None:
                    self._set_ipv6_default_route()
            return

        if self.shared_utils.inband_management_parent_vlans:
            self._set_ip_virtual_router_mac_address()
            self.set_inband_mgmt_vrf()
            for index, (vlan_id, vlan) in enumerate(self.shared_utils.inband_management_parent_vlans.items(), start=1):
                self._set_parent_vlan(vlan_id)
                self._set_parent_vlan_interface(vlan, vlan_id)
                if self.shared_utils.inband_mgmt_vrf is None and self.shared_utils.underlay_bgp:
                    self._set_once_enable_router_bgp_redistribute_attached_host()
                    if self.inputs.underlay_filter_redistribute_connected:
                        if self.shared_utils.overlay_routing_protocol != "none" and vlan["ipv4"]:
                            self._set_once_route_map_conn_2_bgp_sequence_20()
                            self._set_l2leaf_inband_mgmt_prefix_lists(vlan, index)
                        if vlan["ipv6"]:
                            if not self.inputs.avd_design_future.only_configure_ipv6_inband_mgmt_prefix_list_when_used:
                                self._set_l2leaf_inband_mgmt_ipv6_prefix_lists(vlan, index)
                            if self.shared_utils.overlay_routing_protocol != "none":
                                self._set_once_route_map_conn_2_bgp_sequence_60()
                                if self.inputs.avd_design_future.only_configure_ipv6_inband_mgmt_prefix_list_when_used:
                                    self._set_l2leaf_inband_mgmt_ipv6_prefix_lists(vlan, index)

    @run_once_method
    def set_inband_mgmt_vrf(self: AvdStructuredConfigInbandManagement) -> None:
        """Set inband management VRF if not present in the structured config."""
        if self.shared_utils.inband_mgmt_vrf and self.shared_utils.inband_mgmt_vrf not in self.structured_config.vrfs:
            self.structured_config.vrfs.append_new(name=self.shared_utils.inband_mgmt_vrf)

    def _set_vlan(self) -> None:
        # TODO: Refactor this later to inject from filtered tenants
        # Note that an attempt was made for this in #6073 but it has been postponed
        # To keep current behavior we need to overwrite the existing values if the vlan was introduced via network_services
        # otherwise it is created via obtain and updated accordingly.
        inband_mgmt_vlan = self.structured_config.vlans.obtain(self.shared_utils.node_config.inband_mgmt_vlan)
        inband_mgmt_vlan.name = self.shared_utils.node_config.inband_mgmt_vlan_name
        inband_mgmt_vlan.metadata.tenants.append_unique("system")

    def _set_parent_vlan(self, vlan_id: int) -> None:
        # TODO: explore combine here
        self.structured_config.vlans.append_new(
            id=vlan_id,
            metadata=EosCliConfigGen.VlansItem.Metadata(tenants=EosCliConfigGen.VlansItem.Metadata.Tenants(["system"])),
            name=self.shared_utils.node_config.inband_mgmt_vlan_name,
        )

    def _set_vlan_interface(self) -> None:
        """VLAN interfaces can be our own management interface and/or SVIs created on behalf of child switches using us as uplink_switch."""
        vlan_interface = EosCliConfigGen.VlanInterfacesItem(
            name=cast("str", self.shared_utils.inband_mgmt_interface),
            description=self.shared_utils.node_config.inband_mgmt_description,
            shutdown=False,
            mtu=self.shared_utils.inband_mgmt_mtu,
            vrf=self.shared_utils.inband_mgmt_vrf,
            ip_address=self.shared_utils.inband_mgmt_ip,
            ipv6_enable=None if not self.shared_utils.configure_inband_mgmt_ipv6 else True,
            metadata=EosCliConfigGen.VlanInterfacesItem.Metadata(type="inband_mgmt"),
        )
        if ipv6_address := self.shared_utils.inband_mgmt_ipv6_address:
            vlan_interface.ipv6_addresses.append(ipv6_address)
        self.structured_config.vlan_interfaces.append(vlan_interface)

    def _set_ipv4_default_route(self) -> None:
        """Set default route with inband management gateway in inband management VRF."""
        self.structured_config.static_routes.append_new(
            prefix="0.0.0.0/0", next_hop=self.shared_utils.inband_mgmt_gateway, vrf=self.shared_utils.inband_mgmt_vrf
        )

    def _set_ipv6_default_route(self) -> None:
        """Set default route with IPv6 inband management gateway in inband management VRF."""
        self.structured_config.ipv6_static_routes.append_new(
            prefix="::/0", next_hop=self.shared_utils.inband_mgmt_ipv6_gateway, vrf=self.shared_utils.inband_mgmt_vrf
        )

    def _set_ip_virtual_router_mac_address(self) -> None:
        if self.shared_utils.node_config.virtual_router_mac_address is None:
            msg = "'virtual_router_mac_address' must be set for inband management parent."
            raise AristaAvdInvalidInputsError(msg)
        self.structured_config.ip_virtual_router_mac_address = self.shared_utils.node_config.virtual_router_mac_address.lower()

    @run_once_method
    def _set_once_enable_router_bgp_redistribute_attached_host(self) -> None:
        self.structured_config.router_bgp.redistribute.attached_host.enabled = True

    def _set_l2leaf_inband_mgmt_prefix_lists(self, vlan: dict, index: int) -> None:
        prefix_list = self.structured_config.prefix_lists.obtain("PL-L2LEAF-INBAND-MGMT")
        prefix_list.sequence_numbers.append_new(sequence=(index) * 10, action=f"permit {vlan['ipv4']}")

    def _set_l2leaf_inband_mgmt_ipv6_prefix_lists(self, vlan: dict, index: int) -> None:
        prefix_list = self.structured_config.ipv6_prefix_lists.obtain("IPv6-PL-L2LEAF-INBAND-MGMT")
        prefix_list.sequence_numbers.append_new(sequence=(index) * 10, action=f"permit {vlan['ipv6']}")

    @run_once_method
    def _set_once_route_map_conn_2_bgp_sequence_20(self) -> None:
        route_map = self.structured_config.route_maps.obtain("RM-CONN-2-BGP")
        route_map.sequence_numbers.append_new(
            sequence=20, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-L2LEAF-INBAND-MGMT"])
        )

    @run_once_method
    def _set_once_route_map_conn_2_bgp_sequence_60(self) -> None:
        route_map = self.structured_config.route_maps.obtain("RM-CONN-2-BGP")
        route_map.sequence_numbers.append_new(
            sequence=60,
            type="permit",
            match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ipv6 address prefix-list IPv6-PL-L2LEAF-INBAND-MGMT"]),
        )

    def _set_parent_vlan_interface(self, vlan: dict, vlan_id: int) -> None:
        svi = EosCliConfigGen.VlanInterfacesItem(
            name=f"Vlan{vlan_id}",
            description=self.shared_utils.node_config.inband_mgmt_description,
            shutdown=False,
            mtu=self.shared_utils.inband_mgmt_mtu,
            vrf=self.shared_utils.inband_mgmt_vrf,
        )

        if vlan["ipv4"] is not None:
            network = ip_network(vlan["ipv4"], strict=False)
            ip = str(network[3]) if self.shared_utils.mlag_role == "secondary" else str(network[2])
            svi.ip_address = f"{ip}/{network.prefixlen}"
            svi.ip_virtual_router_addresses.append(str(network[1]))
            if self.shared_utils.underlay_routing_protocol == "ebgp":
                svi.ip_attached_host_route_export._update(enabled=True, distance=19)

        if vlan["ipv6"] is not None:
            v6_network = ip_network(vlan["ipv6"], strict=False)
            ipv6 = str(v6_network[3]) if self.shared_utils.mlag_role == "secondary" else str(v6_network[2])
            svi.ipv6_addresses.append(f"{ipv6}/{v6_network.prefixlen}")
            svi.ipv6_enable = True
            svi.ipv6_virtual_router_addresses.append(str(v6_network[1]))
            if self.shared_utils.underlay_routing_protocol == "ebgp":
                svi.ipv6_attached_host_route_export._update(enabled=True, distance=19)

        self.structured_config.vlan_interfaces.append(svi)
