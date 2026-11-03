# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import cached_property
from ipaddress import IPv4Address, IPv6Address
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.interface_data import InterfaceData
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.get_ip_from_ip_prefix import get_ip_from_ip_prefix
from pyavd._utils.groupby import groupby_obj
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


@dataclass(frozen=True)
class MonitorSessionInterfaceData:
    """Monitor session configuration associated with one interface."""

    interface_data: InterfaceData
    monitor_session: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem

    @property
    def name(self) -> str:
        """Return the monitor session name for grouping."""
        return self.monitor_session.name


class MonitorSessionsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def monitor_sessions(self: AvdStructuredConfigBaseProtocol) -> None:
        """Set the structured_config for monitor_sessions."""
        if not self._monitor_session_configs:
            return

        for session_name, session_configs in groupby_obj(self._monitor_session_configs, "name"):
            # Convert iterator to list since we can only access it once.
            session_configs_list = list(session_configs)
            merged_settings = session_configs_list[0].monitor_session._deepcopy()
            for session_data in session_configs_list[1:]:
                merged_settings._deepmerge(session_data.monitor_session)

            if merged_settings.session_settings._get("access_group"):
                for session_data in session_configs_list:
                    if session_data.monitor_session.source_settings.access_group:
                        msg = (
                            f"Cannot set an ACL for both `session_settings` and `source_settings`"
                            f" under the monitor session '{session_data.name}' for {session_data.interface_data.context}."
                        )
                        raise AristaAvdInvalidInputsError(msg)

            monitor_session = EosCliConfigGen.MonitorSessionsItem(name=session_name)
            for session_data in session_configs_list:
                if session_data.monitor_session.role == "destination":
                    monitor_session.destinations.append(session_data.interface_data.interface)

            source_sessions = [session_data for session_data in session_configs_list if session_data.monitor_session.role == "source"]

            for session_data in source_sessions:
                session = session_data.monitor_session
                source = EosCliConfigGen.MonitorSessionsItem.SourcesItem(
                    name=session_data.interface_data.interface,
                    direction=session.source_settings.direction,
                )
                if session.source_settings.access_group.name:
                    source.access_group = session.source_settings.access_group._cast_as(EosCliConfigGen.MonitorSessionsItem.SourcesItem.AccessGroup)
                monitor_session.sources.append(source)

            if session_settings := merged_settings.session_settings:
                monitor_session._update(
                    encapsulation_gre_metadata_tx=session_settings.encapsulation_gre_metadata_tx,
                    header_remove_size=session_settings.header_remove_size,
                    access_group=session_settings.access_group._cast_as(EosCliConfigGen.MonitorSessionsItem.AccessGroup),
                    rate_limit_per_ingress_chip=session_settings.rate_limit_per_ingress_chip,
                    rate_limit_per_egress_chip=session_settings.rate_limit_per_egress_chip,
                    sample=session_settings.sample,
                    truncate=session_settings.truncate._cast_as(EosCliConfigGen.MonitorSessionsItem.Truncate),
                )

            self.structured_config.monitor_sessions.append(monitor_session)

    @staticmethod
    def _validate_monitor_session_on_subinterface(
        interface_name: str,
        monitor_session: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.L3InterfacesItem.MonitorSessionsItem,
        context: str,
    ) -> None:
        """Raise on per-session sub-interface constraints."""
        if "." not in interface_name:
            return
        if monitor_session.role == "destination":
            msg = (
                "Port mirroring destination on sub-interface is not supported. "
                f"Got 'role: {monitor_session.role}' for monitor session '{monitor_session.name}' "
                f"on interface '{interface_name}' under {context}."
            )
            raise AristaAvdInvalidInputsError(msg)
        if monitor_session.source_settings.direction != "rx":
            msg = (
                "Only 'direction: rx' supported on sub-interfaces for monitor session. "
                f"Got 'direction: {monitor_session.source_settings.direction}' for monitor session '{monitor_session.name}' "
                f"on interface '{interface_name}' under {context}."
            )
            raise AristaAvdInvalidInputsError(msg)

    @cached_property
    def _monitor_session_configs(
        self: AvdStructuredConfigBaseProtocol,
    ) -> list[MonitorSessionInterfaceData]:
        """Return list of monitor session configs extracted from every interface."""
        monitor_session_configs = []
        for connected_endpoint in self.shared_utils.filtered_connected_endpoints:
            for adapter in connected_endpoint.adapters:
                if not adapter.monitor_sessions:
                    continue

                # Monitor session on Port-channel interface
                if adapter.port_channel.mode:
                    default_channel_group_id = int("".join(re.findall(r"\d", adapter.switch_ports[0])))
                    channel_group_id = adapter.port_channel.channel_id or default_channel_group_id

                    port_channel_interface_name = f"Port-Channel{channel_group_id}"
                    interface_data = InterfaceData(interface=port_channel_interface_name, context=adapter._internal_data.context)
                    monitor_session_configs.extend(
                        MonitorSessionInterfaceData(
                            interface_data=interface_data,
                            monitor_session=monitor_session._deepcopy(),
                        )
                        for monitor_session in adapter.monitor_sessions
                    )
                    continue

                # Monitor session on Ethernet interface
                for node_index, node_name in enumerate(adapter.switches):
                    if node_name != self.shared_utils.hostname:
                        continue

                    ethernet_interface_name = adapter.switch_ports[node_index]
                    interface_data = InterfaceData(interface=ethernet_interface_name, context=adapter._internal_data.context)
                    monitor_session_configs.extend(
                        MonitorSessionInterfaceData(
                            interface_data=interface_data,
                            monitor_session=monitor_session._deepcopy(),
                        )
                        for monitor_session in adapter.monitor_sessions
                    )

        for network_port in self.shared_utils.filtered_network_ports:
            if not network_port.monitor_sessions:
                continue

            for ethernet_interface_name in range_expand(network_port.switch_ports):
                # Monitor session on Port-channel interface
                if network_port.port_channel and network_port.port_channel.mode is not None:
                    default_channel_group_id = int("".join(re.findall(r"\d", ethernet_interface_name)))
                    channel_group_id = network_port.port_channel.channel_id or default_channel_group_id

                    port_channel_interface_name = f"Port-Channel{channel_group_id}"
                    interface_data = InterfaceData(interface=port_channel_interface_name, context=network_port._internal_data.context)
                    monitor_session_configs.extend(
                        MonitorSessionInterfaceData(
                            interface_data=interface_data,
                            monitor_session=monitor_session._deepcopy()._cast_as(
                                EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem
                            ),
                        )
                        for monitor_session in network_port.monitor_sessions
                    )
                    continue

                # Monitor session on Ethernet interface
                interface_data = InterfaceData(interface=ethernet_interface_name, context=network_port._internal_data.context)
                monitor_session_configs.extend(
                    MonitorSessionInterfaceData(
                        interface_data=interface_data,
                        monitor_session=monitor_session._deepcopy()._cast_as(
                            EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem
                        ),
                    )
                    for monitor_session in network_port.monitor_sessions
                )

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for l3_interface_index, l3_interface in enumerate(vrf.l3_interfaces):
                    for node_index, node_name in enumerate(l3_interface.nodes):
                        if node_name != self.shared_utils.hostname:
                            continue
                        if not l3_interface.monitor_sessions:
                            continue

                        interface_name = l3_interface.interfaces[node_index]
                        ip_address = l3_interface.ip_addresses[node_index] if l3_interface.ip_addresses else None
                        interface_ip = IPv4Address(get_ip_from_ip_prefix(ip_address)) if ip_address else None
                        ipv6_address = l3_interface.ipv6_addresses[node_index] if l3_interface.ipv6_addresses else None
                        interface_ipv6 = IPv6Address(get_ip_from_ip_prefix(ipv6_address)) if ipv6_address else None
                        context = f"{tenant._internal_data.context}[name={tenant.name}].vrfs[name={vrf.name}].l3_interfaces[{l3_interface_index}]"
                        # TODO: DO not raise the error for digital twin
                        if "." in interface_name and not self.shared_utils.platform_settings.feature_support.subinterface_monitor_session:
                            msg = (
                                "Monitor session on sub-interfaces is not supported on this platform. "
                                f"Got monitor session on interface '{interface_name}' under {context}."
                            )
                            raise AristaAvdInvalidInputsError(msg)
                        interface_data = InterfaceData(
                            interface=interface_name,
                            context=context,
                            interface_ip=interface_ip,
                            interface_ipv6=interface_ipv6,
                        )
                        for monitor_session in l3_interface.monitor_sessions:
                            self._validate_monitor_session_on_subinterface(interface_name, monitor_session, context)

                            # We merge using the adapter datamodel to catch conflicts in direction.
                            monitor_session_configs.append(
                                MonitorSessionInterfaceData(
                                    interface_data=interface_data,
                                    monitor_session=monitor_session._deepcopy()._cast_as(
                                        EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem
                                    ),
                                )
                            )

        return monitor_session_configs
