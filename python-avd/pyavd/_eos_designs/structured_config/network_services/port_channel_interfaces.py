# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import default, get_ip_from_ip_prefix, short_esi_to_route_target

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class PortChannelInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def port_channel_interfaces(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set structured config for port_channel_interfaces.

        Only used with L1 network services or L3 network services
        """
        if not self.shared_utils.network_services_l1 and not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            self._set_l3_port_channels(tenant)

            if not tenant.point_to_point_services:
                continue

            self._set_point_to_point_port_channel_interfaces(tenant)

    def _set_l3_port_channels(
        self: AvdStructuredConfigNetworkServicesProtocol,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> None:
        """
        Set the port-channel interfaces for all network-services tenants in structured configuration.

        Raises:
            AristaAvdInvalidInputsError:
                if any subinterface is using a non supported key.
        """
        for vrf in tenant.vrfs:
            for l3_port_channel in vrf.l3_port_channels:
                if is_subinterface := "." in l3_port_channel.name:
                    # Validation for l3_port_channel subinterface
                    if l3_port_channel.member_interfaces:
                        msg = f"L3 Port-Channel sub-interface '{l3_port_channel.name}' has 'member_interfaces' set. This is not a valid setting."
                        raise AristaAvdInvalidInputsError(msg)
                    if l3_port_channel._get("mode"):
                        # implies 'mode' is set when not applicable for a sub-interface
                        msg = f"L3 Port-Channel sub-interface '{l3_port_channel.name}' has 'mode' set. This is not a valid setting."
                        raise AristaAvdInvalidInputsError(msg)
                    if l3_port_channel._get("mtu"):
                        # implies 'mtu' is set when not applicable for a sub-interface
                        msg = f"L3 Port-Channel sub-interface '{l3_port_channel.name}' has 'mtu' set. This is not a valid setting."
                        raise AristaAvdInvalidInputsError(msg)
                elif self.inputs.avd_design_future.raise_for_port_channels_without_members and not l3_port_channel.member_interfaces:
                    # Validation: Non-subinterface port-channels must have at least one member interface
                    msg = f"L3 Port-Channel '{l3_port_channel.name}' must have at least one member interface defined."
                    raise AristaAvdInvalidInputsError(msg)

                if not (interface_description := l3_port_channel.description):
                    interface_description = "_".join(filter(None, [l3_port_channel.peer, l3_port_channel.peer_port_channel]))

                # Generate their structured config for the l3_port_channels.
                port_channel_interface = EosCliConfigGen.PortChannelInterfacesItem(
                    name=l3_port_channel.name,
                    mtu=self.shared_utils.get_interface_mtu(l3_port_channel.name, l3_port_channel.mtu),
                    description=interface_description or None,
                    arp_gratuitous_accept=l3_port_channel.arp_gratuitous_accept,
                    shutdown=not l3_port_channel.enabled,
                    eos_cli=l3_port_channel.raw_eos_cli,
                    flow_tracker=self.shared_utils.get_flow_tracker(
                        l3_port_channel.flow_tracking, output_type=EosCliConfigGen.PortChannelInterfacesItem.FlowTracker
                    ),
                    vrf=vrf.name if vrf.name != "default" else None,
                    metadata=EosCliConfigGen.PortChannelInterfacesItem.Metadata(
                        peer_interface=l3_port_channel.peer_port_channel or None,
                        peer=l3_port_channel.peer,
                        peer_type="l3_port_channel",
                        validate_state=self.structured_config_utils.get_interface_validate_state(),
                    ),
                )
                self._update_port_channel_interface_ipv4(port_channel_interface, l3_port_channel=l3_port_channel, vrf=vrf, tenant=tenant)
                self._update_port_channel_interface_ipv6(port_channel_interface, l3_port_channel=l3_port_channel, vrf=vrf)

                if not is_subinterface:
                    port_channel_interface.switchport.enabled = False

                if is_subinterface:
                    self.structured_config_utils.parent_interfaces_tracker.register_port_channel_subinterface(l3_port_channel.name)

                    port_channel_interface.encapsulation_dot1q.vlan = default(
                        l3_port_channel.encapsulation_dot1q_vlan, int(l3_port_channel.name.split(".", maxsplit=1)[-1])
                    )
                    if not l3_port_channel.ip_address and not l3_port_channel.ipv6_addresses:
                        msg = (
                            f"{self.inputs._node_type_keys_item.key}.nodes[name={self.shared_utils.hostname}].l3_port_channels"
                            f"[name={l3_port_channel.name}].ip_address or ipv6_addresses"
                        )
                        raise AristaAvdMissingVariableError(msg)
                else:
                    self.structured_config_utils.parent_interfaces_tracker.register_port_channel_parent(l3_port_channel.name)

                if l3_port_channel.structured_config:
                    self.custom_structured_configs.nested.port_channel_interfaces.obtain(l3_port_channel.name)._deepmerge(
                        l3_port_channel.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                    )

                self.structured_config.port_channel_interfaces.append(port_channel_interface)

    def _update_port_channel_interface_ipv4(
        self: AvdStructuredConfigNetworkServicesProtocol,
        port_channel_interface: EosCliConfigGen.PortChannelInterfacesItem,
        *,
        l3_port_channel: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.L3PortChannelsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> None:
        """Set the IPv4-only configuration on a PortChannelInterface from its l3_port_channel."""
        # TODO: AVD 7.0.0 - early-return when `ip_address is None`, mirroring the IPv6 path. OSPFv2 requires a valid IPv4.
        port_channel_interface.ip_address = l3_port_channel.ip_address
        port_channel_interface.ip_address_secondaries = EosCliConfigGen.PortChannelInterfacesItem.IpAddressSecondaries(l3_port_channel.ip_address_secondaries)
        interface_ip = l3_port_channel.ip_address
        if interface_ip and "/" in interface_ip:
            interface_ip = get_ip_from_ip_prefix(interface_ip)
        if l3_port_channel.ipv4_acl_in:
            acl = self.shared_utils.get_ipv4_acl(name=l3_port_channel.ipv4_acl_in, interface_name=l3_port_channel.name, interface_ip=interface_ip)
            port_channel_interface.access_group_in = acl.name
            self.structured_config_utils._set_ipv4_acl(acl)
        if l3_port_channel.ipv4_acl_out:
            acl = self.shared_utils.get_ipv4_acl(name=l3_port_channel.ipv4_acl_out, interface_name=l3_port_channel.name, interface_ip=interface_ip)
            port_channel_interface.access_group_out = acl.name
            self.structured_config_utils._set_ipv4_acl(acl)
        self._update_port_channel_interface_ospf(port_channel_interface, l3_port_channel=l3_port_channel, vrf=vrf, tenant=tenant)

    def _update_port_channel_interface_ospf(
        self: AvdStructuredConfigNetworkServicesProtocol,
        port_channel_interface: EosCliConfigGen.PortChannelInterfacesItem,
        *,
        l3_port_channel: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.L3PortChannelsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> None:
        """Set the OSPF configuration on a PortChannelInterface from its l3_port_channel."""
        if l3_port_channel.ospf.enabled and vrf.ospf.enabled:
            port_channel_interface._update(
                ospf_area=l3_port_channel.ospf.area,
                ospf_network_point_to_point=l3_port_channel.ospf.point_to_point,
                ospf_cost=l3_port_channel.ospf.cost,
            )
            self.shared_utils.update_ospf_authentication(port_channel_interface, l3_port_channel, vrf, tenant)

    def _update_port_channel_interface_ipv6(
        self: AvdStructuredConfigNetworkServicesProtocol,
        port_channel_interface: EosCliConfigGen.PortChannelInterfacesItem,
        *,
        l3_port_channel: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.L3PortChannelsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None:
        """Set the IPv6-only configuration on a PortChannelInterface from its l3_port_channel."""
        if not l3_port_channel.ipv6_addresses:
            return
        port_channel_interface.ipv6_addresses.extend(l3_port_channel.ipv6_addresses)
        if vrf.name == "default":
            self.structured_config.ipv6_unicast_routing = True
        # Use the first IPv6 address for "interface_ip" substitution in ACLs, matching the IPv4 behavior.
        ipv6_interface_ip = next(iter(l3_port_channel.ipv6_addresses), None)
        if ipv6_interface_ip and "/" in ipv6_interface_ip:
            ipv6_interface_ip = get_ip_from_ip_prefix(ipv6_interface_ip)
        if l3_port_channel.ipv6_acl_in:
            acl = self.shared_utils.get_ipv6_acl(name=l3_port_channel.ipv6_acl_in, interface_name=l3_port_channel.name, interface_ipv6=ipv6_interface_ip)
            port_channel_interface.ipv6_access_group_in = acl.name
            self.structured_config_utils._set_ipv6_acl(acl)
        if l3_port_channel.ipv6_acl_out:
            acl = self.shared_utils.get_ipv6_acl(name=l3_port_channel.ipv6_acl_out, interface_name=l3_port_channel.name, interface_ipv6=ipv6_interface_ip)
            port_channel_interface.ipv6_access_group_out = acl.name
            self.structured_config_utils._set_ipv6_acl(acl)

    def _set_point_to_point_port_channel_interfaces(
        self: AvdStructuredConfigNetworkServicesProtocol,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> None:
        """Set the structured_config port_channel_interfaces with the point-to-point interfaces defined under network_services."""
        for point_to_point_service in tenant.point_to_point_services._natural_sorted():
            for endpoint in point_to_point_service.endpoints:
                if self.shared_utils.hostname not in endpoint.nodes:
                    continue

                node_index = endpoint.nodes.index(self.shared_utils.hostname)
                interface_name = endpoint.interfaces[node_index]
                if (port_channel_mode := endpoint.port_channel.mode) not in ["active", "on"]:
                    continue

                channel_group_id = "".join(re.findall(r"\d", interface_name))
                interface_name = f"Port-Channel{channel_group_id}"
                if point_to_point_service.subinterfaces:
                    # Create parent Port-Channel interface first
                    parent_interface = EosCliConfigGen.PortChannelInterfacesItem(
                        name=interface_name,
                        shutdown=False,
                    )
                    parent_interface.metadata.peer_type = "system"
                    parent_interface.switchport.enabled = False

                    if (short_esi := endpoint.port_channel.short_esi) is not None and len(short_esi.split(":")) == 3:
                        parent_interface.evpn_ethernet_segment._update(
                            identifier=f"{self.inputs.evpn_short_esi_prefix}{short_esi}",
                            route_target=short_esi_to_route_target(short_esi),
                        )
                        if port_channel_mode == "active":
                            parent_interface.lacp_id = short_esi.replace(":", ".")

                    self.structured_config_utils.parent_interfaces_tracker.register_port_channel_parent(interface_name)

                    self.structured_config.port_channel_interfaces.append(parent_interface)

                    # Now create subinterfaces
                    for subif in point_to_point_service.subinterfaces:
                        subif_name = f"{interface_name}.{subif.number}"

                        self.structured_config_utils.parent_interfaces_tracker.register_port_channel_subinterface(subif_name)

                        interface = EosCliConfigGen.PortChannelInterfacesItem(
                            name=subif_name,
                            shutdown=False,
                            encapsulation_vlan=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan(
                                client=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan.Client(encapsulation="dot1q", vlan=subif.number),
                                network=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan.Network(encapsulation="client"),
                            ),
                        )
                        interface.metadata.peer_type = "point_to_point_service"
                        if subif.port_channel.raw_eos_cli:
                            interface.eos_cli = subif.port_channel.raw_eos_cli

                        if subif.port_channel.structured_config:
                            self.custom_structured_configs.nested.port_channel_interfaces.obtain(subif_name)._deepmerge(
                                subif.port_channel.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                            )

                        self.structured_config.port_channel_interfaces.append(interface)

                else:
                    port_channel_interface = EosCliConfigGen.PortChannelInterfacesItem(
                        name=interface_name,
                        shutdown=False,
                    )
                    port_channel_interface.metadata.peer_type = "point_to_point_service"
                    port_channel_interface.switchport.enabled = False

                    if (short_esi := endpoint.port_channel.short_esi) is not None and len(short_esi.split(":")) == 3:
                        port_channel_interface.evpn_ethernet_segment._update(
                            identifier=f"{self.inputs.evpn_short_esi_prefix}{short_esi}",
                            route_target=short_esi_to_route_target(short_esi),
                        )
                        if port_channel_mode == "active":
                            port_channel_interface.lacp_id = short_esi.replace(":", ".")

                    self.structured_config_utils.parent_interfaces_tracker.register_port_channel_parent(interface_name)

                    self.structured_config.port_channel_interfaces.append(port_channel_interface)
