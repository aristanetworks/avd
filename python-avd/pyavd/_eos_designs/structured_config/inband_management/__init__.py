# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator, structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError


class AvdStructuredConfigInbandManagement(StructuredConfigGenerator):
    @structured_config_contributor
    def vlans(self) -> None:
        if not self.shared_utils.inband_management_parent_vlans and not (
            self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6
        ):
            return

        if self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6:
            self.structured_config.vlans.append_new(
                id=self.shared_utils.node_config.inband_mgmt_vlan, tenant="system", name=self.shared_utils.node_config.inband_mgmt_vlan_name
            )
            return
        for svi in self.shared_utils.inband_management_parent_vlans:
            self.structured_config.vlans.append_new(id=svi, tenant="system", name=self.shared_utils.node_config.inband_mgmt_vlan_name)

    @structured_config_contributor
    def vlan_interfaces(self) -> None:
        """VLAN interfaces can be our own management interface and/or SVIs created on behalf of child switches using us as uplink_switch."""
        if not self.shared_utils.inband_management_parent_vlans and not (
            self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6
        ):
            return

        if self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6:
            self.structured_config.vlan_interfaces.append_new(
                name=self.shared_utils.inband_mgmt_interface,
                description=self.shared_utils.node_config.inband_mgmt_description,
                shutdown=False,
                mtu=self.shared_utils.inband_mgmt_mtu,
                vrf=self.shared_utils.inband_mgmt_vrf,
                ip_address=self.shared_utils.inband_mgmt_ip,
                ipv6_enable=None if not self.shared_utils.configure_inband_mgmt_ipv6 else True,
                ipv6_address=self.shared_utils.inband_mgmt_ipv6_address,
                type="inband_mgmt",
            )
            return
        for vlan, subnet in self.shared_utils.inband_management_parent_vlans.items():
            self.structured_config.vlan_interfaces.append(self.get_parent_svi_cfg(vlan, subnet["ipv4"], subnet["ipv6"]))

    @cached_property
    def _inband_mgmt_ipv6_parent(self) -> bool:
        if self.shared_utils.inband_management_parent_vlans:
            for subnet in self.shared_utils.inband_management_parent_vlans.values():
                if subnet["ipv6"]:
                    return True
        return False

    @cached_property
    def _inband_mgmt_ipv4_parent(self) -> bool:
        if self.shared_utils.inband_management_parent_vlans:
            for subnet in self.shared_utils.inband_management_parent_vlans.values():
                if subnet["ipv4"]:
                    return True
        return False

    @structured_config_contributor
    def static_routes(self) -> None:
        if not self.shared_utils.configure_inband_mgmt or self.shared_utils.inband_mgmt_gateway is None:
            return

        self.structured_config.static_routes.append_new(
            destination_address_prefix="0.0.0.0/0", gateway=self.shared_utils.inband_mgmt_gateway, vrf=self.shared_utils.inband_mgmt_vrf
        )

    @structured_config_contributor
    def ipv6_static_routes(self) -> None:
        if not self.shared_utils.configure_inband_mgmt_ipv6 or self.shared_utils.inband_mgmt_ipv6_gateway is None:
            return

        self.structured_config.ipv6_static_routes.append_new(
            destination_address_prefix="::/0", gateway=self.shared_utils.inband_mgmt_ipv6_gateway, vrf=self.shared_utils.inband_mgmt_vrf
        )

    @structured_config_contributor
    def vrfs(self) -> None:
        if self.shared_utils.inband_mgmt_vrf is None:
            return

        if not self.shared_utils.inband_management_parent_vlans and not self.shared_utils.configure_inband_mgmt:
            return
        self.structured_config.vrfs.append_new(name=self.shared_utils.inband_mgmt_vrf)

    @structured_config_contributor
    def ip_virtual_router_mac_address(self) -> None:
        if not self.shared_utils.inband_management_parent_vlans:
            return

        if self.shared_utils.node_config.virtual_router_mac_address is None:
            msg = "'virtual_router_mac_address' must be set for inband management parent."
            raise AristaAvdInvalidInputsError(msg)
        self.structured_config.ip_virtual_router_mac_address = self.shared_utils.node_config.virtual_router_mac_address.lower()

    @structured_config_contributor
    def router_bgp(self) -> None:
        if self.shared_utils.inband_mgmt_vrf is not None:
            return

        if not self.shared_utils.inband_management_parent_vlans or not self.shared_utils.underlay_bgp:
            return

        self.structured_config.router_bgp.redistribute.attached_host.enabled = True

    @structured_config_contributor
    def prefix_lists(self) -> None:
        if (
            not self.shared_utils.inband_management_parent_vlans
            or not self.shared_utils.underlay_bgp
            or not self.inputs.underlay_filter_redistribute_connected
            or not self._inband_mgmt_ipv4_parent
        ):
            return

        if self.shared_utils.inband_mgmt_vrf is not None or self.shared_utils.overlay_routing_protocol == "none":
            return

        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, subnet in enumerate(self.shared_utils.inband_management_parent_vlans.values(), start=1):
            sequence_numbers.append_new(sequence=(index) * 10, action=f"permit {subnet['ipv4']}")

        self.structured_config.prefix_lists.append_new(name="PL-L2LEAF-INBAND-MGMT", sequence_numbers=sequence_numbers)

    @structured_config_contributor
    def ipv6_prefix_lists(self) -> None:
        if (
            not self.shared_utils.inband_management_parent_vlans
            or not self.shared_utils.underlay_bgp
            or not self.inputs.underlay_filter_redistribute_connected
            or not self._inband_mgmt_ipv6_parent
        ):
            return

        if self.shared_utils.inband_mgmt_vrf is not None:
            return

        sequence_numbers = EosCliConfigGen.Ipv6PrefixListsItem.SequenceNumbers()
        for index, subnet in enumerate(self.shared_utils.inband_management_parent_vlans.values(), start=1):
            sequence_numbers.append_new(sequence=(index) * 10, action=f"permit {subnet['ipv6']}")

        self.structured_config.ipv6_prefix_lists.append_new(name="IPv6-PL-L2LEAF-INBAND-MGMT", sequence_numbers=sequence_numbers)

    @structured_config_contributor
    def route_maps(self) -> None:
        if not self.shared_utils.inband_management_parent_vlans or not self.shared_utils.underlay_bgp or not self.inputs.underlay_filter_redistribute_connected:
            return

        if self.shared_utils.inband_mgmt_vrf is not None or self.shared_utils.overlay_routing_protocol == "none":
            return

        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        if self._inband_mgmt_ipv4_parent:
            sequence_numbers.append_new(
                sequence=20, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-L2LEAF-INBAND-MGMT"])
            )

        if self._inband_mgmt_ipv6_parent:
            sequence_numbers.append_new(
                sequence=60,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ipv6 address prefix-list IPv6-PL-L2LEAF-INBAND-MGMT"]),
            )

        self.structured_config.route_maps.append_new(name="RM-CONN-2-BGP", sequence_numbers=sequence_numbers)

    def get_parent_svi_cfg(self, vlan: int, subnet: str | None, ipv6_subnet: str | None) -> EosCliConfigGen.VlanInterfacesItem:
        svi = EosCliConfigGen.VlanInterfacesItem(
            name=f"Vlan{vlan}",
            description=self.shared_utils.node_config.inband_mgmt_description,
            shutdown=False,
            mtu=self.shared_utils.inband_mgmt_mtu,
            vrf=self.shared_utils.inband_mgmt_vrf,
        )

        if subnet is not None:
            network = ip_network(subnet, strict=False)
            ip = str(network[3]) if self.shared_utils.mlag_role == "secondary" else str(network[2])
            svi.ip_attached_host_route_export._update(enabled=True, distance=19)
            svi.ip_address = f"{ip}/{network.prefixlen}"
            svi.ip_virtual_router_addresses.append(str(network[1]))

        if ipv6_subnet is not None:
            v6_network = ip_network(ipv6_subnet, strict=False)
            ipv6 = str(v6_network[3]) if self.shared_utils.mlag_role == "secondary" else str(v6_network[2])
            svi.ipv6_address = f"{ipv6}/{v6_network.prefixlen}"
            svi.ipv6_enable = True
            svi.ipv6_attached_host_route_export._update(enabled=True, distance=19)
            svi.ipv6_virtual_router_addresses.append(str(v6_network[1]))

        return svi
