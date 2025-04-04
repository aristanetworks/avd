# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import default, get_ip_from_ip_prefix, short_esi_to_route_target
from pyavd.j2filters import natural_sort

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

        # l3 port-channels tracking structures
        subif_parent_port_channel_names: set[str] = set()
        """Collect all L3 subinterface parent port-channel names across tenants."""
        regular_l3_port_channel_names: set[str] = set()
        """Collect all L3 subinterface parent port-channel names across tenants."""

        # point_to_point port-channels tracking structures.
        potential_parent_interfaces = EosCliConfigGen.PortChannelInterfaces()
        """
        Keeping separate list of auto-generated parent interfaces for point-to-point port-channel
        This is used to check for conflicts between auto-generated parents
        At the end of _set_point_to_point_port_channel_interfaces, parent interfaces are
        added to structured_config if they were not explicitly configured.
        """
        configured_physical_po: set[str] = set()
        """Set to collect all the physical port-channels explicitly configured by _set_point_to_point_port_channel_interfaces."""

        for tenant in self.shared_utils.filtered_tenants:
            self._set_l3_port_channels(tenant, subif_parent_port_channel_names, regular_l3_port_channel_names)

            if not tenant.point_to_point_services:
                continue

            self._set_point_to_point_port_channel_interfaces(tenant, potential_parent_interfaces, configured_physical_po)

            for potential_parent_interface in potential_parent_interfaces:
                if potential_parent_interface.name not in configured_physical_po:
                    self.structured_config.port_channel_interfaces.append(potential_parent_interface)

        # Sanity check if there are any L3 sub-interfaces for which parent Port-channel is not explicitly specified
        # This does not concerned point-to-point port channels.
        if missing_parent_port_channels := subif_parent_port_channel_names.difference(regular_l3_port_channel_names):
            msg = (
                f"One or more L3 Port-Channels '{', '.join(natural_sort(missing_parent_port_channels))}' "
                "need to be specified as they have sub-interfaces referencing them."
            )
            raise AristaAvdInvalidInputsError(msg)

    def _set_l3_port_channels(
        self: AvdStructuredConfigNetworkServicesProtocol,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        subif_parent_port_channel_names: set[str],
        regular_l3_port_channel_names: set[str],
    ) -> None:
        """
        Set the port-channel interfaces for all network-services tenants in structured configuration.

        Raises:
            AristaAvdInvalidInputsError:
                if any subinterface is using a non supported key
                Or
                if any subinterface is defined without a parent interface.
        """
        for vrf in tenant.vrfs:
            for l3_port_channel in vrf.l3_port_channels:
                if l3_port_channel.node != self.shared_utils.hostname:
                    continue

                if not (is_subinterface := "." in l3_port_channel.name):
                    # This is a regular Port-Channel (not sub-interface)
                    regular_l3_port_channel_names.add(l3_port_channel.name)
                    subif_parent_port_channel_names.add(l3_port_channel.name)
                else:
                    parent_port_channel_name = l3_port_channel.name.split(".", maxsplit=1)[0]
                    subif_parent_port_channel_names.add(parent_port_channel_name)

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

                if not (interface_description := l3_port_channel.description):
                    interface_description = "_".join(filter(None, [l3_port_channel.peer, l3_port_channel.peer_port_channel]))

                # Resolve interface IP
                interface_ip = l3_port_channel.ip_address
                if interface_ip and "/" in interface_ip:
                    interface_ip = get_ip_from_ip_prefix(interface_ip)

                # Generate their structured config for the l3_port_channels.
                port_channel_interface = EosCliConfigGen.PortChannelInterfacesItem(
                    name=l3_port_channel.name,
                    peer=l3_port_channel.peer,
                    mtu=l3_port_channel.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
                    description=interface_description or None,
                    ip_address=l3_port_channel.ip_address,
                    shutdown=not l3_port_channel.enabled,
                    eos_cli=l3_port_channel.raw_eos_cli,
                    flow_tracker=self.shared_utils.get_flow_tracker(
                        l3_port_channel.flow_tracking, output_type=EosCliConfigGen.EthernetInterfacesItem.FlowTracker
                    ),
                    vrf=vrf.name if vrf.name != "default" else None,
                    peer_type="l3_port_channel",
                    peer_interface=l3_port_channel.peer_port_channel if l3_port_channel.peer_port_channel else None,
                )
                if l3_port_channel.ipv4_acl_in:
                    acl = self.shared_utils.get_ipv4_acl(
                        name=l3_port_channel.ipv4_acl_in,
                        interface_name=l3_port_channel.name,
                        interface_ip=interface_ip,
                    )
                    port_channel_interface.access_group_in = acl.name
                    self._set_ipv4_acl(acl)

                if l3_port_channel.ipv4_acl_out:
                    acl = self.shared_utils.get_ipv4_acl(
                        name=l3_port_channel.ipv4_acl_out,
                        interface_name=l3_port_channel.name,
                        interface_ip=interface_ip,
                    )
                    port_channel_interface.access_group_out = acl.name
                    self._set_ipv4_acl(acl)

                if not is_subinterface:
                    port_channel_interface.switchport.enabled = False

                if l3_port_channel.ospf.enabled and vrf.ospf.enabled:
                    port_channel_interface._update(
                        ospf_area=l3_port_channel.ospf.area,
                        ospf_network_point_to_point=l3_port_channel.ospf.point_to_point,
                        ospf_cost=l3_port_channel.ospf.cost,
                    )
                    ospf_authentication = l3_port_channel.ospf.authentication
                    if ospf_authentication == "simple" and (ospf_simple_auth_key := l3_port_channel.ospf.simple_auth_key) is not None:
                        port_channel_interface._update(ospf_authentication=ospf_authentication, ospf_authentication_key=ospf_simple_auth_key)
                    elif ospf_authentication == "message-digest" and (ospf_message_digest_keys := l3_port_channel.ospf.message_digest_keys) is not None:
                        for ospf_key in ospf_message_digest_keys:
                            if not (ospf_key.id and ospf_key.key):
                                continue
                            port_channel_interface.ospf_message_digest_keys.append_new(
                                id=ospf_key.id,
                                hash_algorithm=ospf_key.hash_algorithm,
                                key=ospf_key.key,
                            )
                        if port_channel_interface.ospf_message_digest_keys:
                            port_channel_interface.ospf_authentication = ospf_authentication

                if is_subinterface:
                    port_channel_interface.encapsulation_dot1q.vlan = default(
                        l3_port_channel.encapsulation_dot1q_vlan, int(l3_port_channel.name.split(".", maxsplit=1)[-1])
                    )
                    if not l3_port_channel.ip_address:
                        msg = f"{self.shared_utils.node_type_key_data.key}.nodes[name={self.shared_utils.hostname}].l3_port_channels"
                        msg += f"[name={l3_port_channel.name}].ip_address"
                        raise AristaAvdMissingVariableError(msg)

                if l3_port_channel.structured_config:
                    self.custom_structured_configs.nested.port_channel_interfaces.obtain(l3_port_channel.name)._deepmerge(
                        l3_port_channel.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                    )

                self.structured_config.port_channel_interfaces.append(port_channel_interface)

    def _set_point_to_point_port_channel_interfaces(
        self: AvdStructuredConfigNetworkServicesProtocol,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        potential_parent_interfaces: EosCliConfigGen.PortChannelInterfaces,
        configured_physical_po_names: set[str],
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
                    # This is a subinterface so we need to ensure that the parent is created
                    parent_interface = EosCliConfigGen.PortChannelInterfacesItem(
                        name=interface_name,
                        peer_type="system",
                        shutdown=False,
                    )
                    parent_interface.switchport.enabled = False

                    if (short_esi := endpoint.port_channel.short_esi) is not None and len(short_esi.split(":")) == 3:
                        parent_interface.evpn_ethernet_segment._update(
                            identifier=f"{self.inputs.evpn_short_esi_prefix}{short_esi}", route_target=short_esi_to_route_target(short_esi)
                        )
                        if port_channel_mode == "active":
                            parent_interface.lacp_id = short_esi.replace(":", ".")

                    # Adding the auto-generated parent to the list of potential parents
                    potential_parent_interfaces.append(parent_interface)

                    for subif in point_to_point_service.subinterfaces:
                        subif_name = f"{interface_name}.{subif.number}"

                        self.structured_config.port_channel_interfaces.append_new(
                            name=subif_name,
                            peer_type="point_to_point_service",
                            shutdown=False,
                            encapsulation_vlan=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan(
                                client=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan.Client(encapsulation="dot1q", vlan=subif.number),
                                network=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan.Network(encapsulation="client"),
                            ),
                        )

                else:
                    port_channel_interface = EosCliConfigGen.PortChannelInterfacesItem(
                        name=interface_name,
                        peer_type="point_to_point_service",
                        shutdown=False,
                    )
                    port_channel_interface.switchport.enabled = False

                    if (short_esi := endpoint.port_channel.short_esi) is not None and len(short_esi.split(":")) == 3:
                        port_channel_interface.evpn_ethernet_segment._update(
                            identifier=f"{self.inputs.evpn_short_esi_prefix}{short_esi}",
                            route_target=short_esi_to_route_target(short_esi),
                        )
                        if port_channel_mode == "active":
                            port_channel_interface.lacp_id = short_esi.replace(":", ".")

                    self.structured_config.port_channel_interfaces.append(port_channel_interface)
                    # Tracking the physical interfaces to determine which auto-generated should be injected.
                    configured_physical_po_names.add(interface_name)
