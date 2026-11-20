# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import cached_property
from ipaddress import IPv4Address, IPv6Address
from typing import TYPE_CHECKING, Protocol, cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.models import InterfaceData
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.get_ip_from_ip_prefix import get_ip_from_ip_prefix
from pyavd._utils.groupby import groupby_obj
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

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
            for session_config in session_configs_list[1:]:
                merged_settings._deepmerge(session_config.monitor_session)

            if session_settings := merged_settings.session_settings:
                access_group = session_settings._get("access_group")
                if access_group is not None:
                    missing_fields = [field for field in ("type", "name") if access_group._get(field) is None]
                    if missing_fields:
                        msg = (
                            f"Missing required field(s) '{', '.join(missing_fields)}' under `session_settings.access_group` "
                            f"for monitor session '{session_name}' after merging `session_settings` "
                            f"for host '{self.shared_utils.hostname}'."
                        )
                        raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

            if merged_settings.session_settings._get("access_group"):
                for session in session_configs_list:
                    if session.monitor_session.source_settings.access_group:
                        msg = (
                            f"Cannot set an ACL for both `session_settings` and `source_settings`"
                            f" under the monitor session '{session.name}' for {session.interface_data.context}."
                        )
                        raise AristaAvdInvalidInputsError(msg)

            monitor_session = EosCliConfigGen.MonitorSessionsItem(name=session_name)
            for session in session_configs_list:
                if session.monitor_session.role == "destination":
                    monitor_session.destinations.append(session.interface_data.interface)

            source_sessions = [session for session in session_configs_list if session.monitor_session.role == "source"]
            session_settings = merged_settings.session_settings
            session_access_group: EosCliConfigGen.MonitorSessionsItem.AccessGroup | None = None
            if session_settings and session_settings.access_group:
                session_access_group = session_settings.access_group._cast_as(EosCliConfigGen.MonitorSessionsItem.AccessGroup)

            use_interface_specific_source_acls = (
                session_access_group is not None
                and len(source_sessions) > 1
                and self.inputs.avd_design_future.configure_monitor_session_acls_from_catalog
                and self._monitor_session_acl_has_interface_substitution(session_access_group)
            )

            for session in source_sessions:
                source = EosCliConfigGen.MonitorSessionsItem.SourcesItem(
                    name=session.interface_data.interface,
                    direction=session.monitor_session.source_settings.direction,
                )
                if use_interface_specific_source_acls and session_access_group:
                    source.access_group = session_access_group._cast_as(EosCliConfigGen.MonitorSessionsItem.SourcesItem.AccessGroup)
                    self._configure_monitor_session_acl_from_catalog(
                        source.access_group,
                        session.interface_data,
                        session.interface_data.interface,
                    )
                elif access_group := session.monitor_session.source_settings.access_group:
                    source.access_group = access_group._cast_as(EosCliConfigGen.MonitorSessionsItem.SourcesItem.AccessGroup)
                    self._configure_monitor_session_acl_from_catalog(source.access_group, session.interface_data, session.interface_data.interface)
                monitor_session.sources.append(source)

            if session_settings:
                if session_access_group and not use_interface_specific_source_acls:
                    monitor_session.access_group = session_access_group
                    interface_data = source_sessions[0].interface_data if len(source_sessions) == 1 else None
                    interface_name = interface_data.interface if interface_data else session_name
                    self._configure_monitor_session_acl_from_catalog(monitor_session.access_group, interface_data, interface_name)
                monitor_session._update(
                    encapsulation_gre_metadata_tx=session_settings.encapsulation_gre_metadata_tx,
                    header_remove_size=session_settings.header_remove_size,
                    rate_limit_per_ingress_chip=session_settings.rate_limit_per_ingress_chip,
                    rate_limit_per_egress_chip=session_settings.rate_limit_per_egress_chip,
                    sample=session_settings.sample,
                    truncate=session_settings.truncate._cast_as(EosCliConfigGen.MonitorSessionsItem.Truncate),
                )

            self.structured_config.monitor_sessions.append(monitor_session)

    def _configure_monitor_session_acl_from_catalog(
        self: AvdStructuredConfigBaseProtocol,
        access_group: EosCliConfigGen.MonitorSessionsItem.AccessGroup | EosCliConfigGen.MonitorSessionsItem.SourcesItem.AccessGroup,
        interface_data: InterfaceData | None,
        interface_name: str,
    ) -> None:
        """Configure the ACL catalog entry referenced by a monitor-session access group when enabled."""
        if not self.inputs.avd_design_future.configure_monitor_session_acls_from_catalog or not access_group.name:
            return

        if access_group.type == "ip":
            acl = self.shared_utils.get_ipv4_acl_with_substitution(
                name=access_group.name,
                interface_name=interface_name,
                interface_ip=str(interface_data.interface_ip) if interface_data and interface_data.interface_ip else None,
            )
            self.structured_config_utils._set_ipv4_acl(acl)
            access_group.name = acl.name
        elif access_group.type == "ipv6":
            acl = self.shared_utils.get_ipv6_acl(
                name=access_group.name,
                interface_name=interface_name,
                interface_ipv6=str(interface_data.interface_ipv6) if interface_data and interface_data.interface_ipv6 else None,
            )
            self.structured_config_utils._set_ipv6_acl(acl)
            access_group.name = acl.name
        elif access_group.type == "mac":
            self.structured_config_utils._set_mac_acl(access_group.name)

    def _monitor_session_acl_has_interface_substitution(
        self: AvdStructuredConfigBaseProtocol,
        access_group: EosCliConfigGen.MonitorSessionsItem.AccessGroup | EosCliConfigGen.MonitorSessionsItem.SourcesItem.AccessGroup,
    ) -> bool:
        """Return whether a catalog ACL uses an interface or peer IP substitution."""
        # The access group is validated before this call, but the cast EOS CLI model marks the name as optional.
        name = cast("str", access_group.name)

        acl: EosDesigns.Ipv4AclsItem | EosDesigns.Ipv6AclsItem
        if access_group.type == "ip":
            if name not in self.inputs.ipv4_acls:
                return False
            acl = self.inputs.ipv4_acls[name]
            substitutions = {"interface_ip", "peer_ip"}
        elif access_group.type == "ipv6":
            if name not in self.inputs.ipv6_acls:
                return False
            acl = self.inputs.ipv6_acls[name]
            substitutions = {"interface_ipv6", "peer_ipv6", "interface_ip"}
        else:
            return False

        return any(not entry._get("remark") and (entry.source in substitutions or entry.destination in substitutions) for entry in acl.entries)

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

    @staticmethod
    def _get_monitor_session_interface_data(
        interface_data: InterfaceData,
        monitor_sessions: Iterable[EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem],
    ) -> Iterator[MonitorSessionInterfaceData]:
        """Return monitor session data for an interface, deep-copying each session."""
        return (
            MonitorSessionInterfaceData(
                interface_data=interface_data,
                monitor_session=monitor_session._deepcopy(),
            )
            for monitor_session in monitor_sessions
        )

    @cached_property
    def _monitor_session_configs(
        self: AvdStructuredConfigBaseProtocol,
    ) -> list[MonitorSessionInterfaceData]:
        """Return list of monitor session configs extracted from every interface."""
        monitor_session_configs = []
        adapter_monitor_sessions_type = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessions
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
                    monitor_session_configs.extend(self._get_monitor_session_interface_data(interface_data, adapter.monitor_sessions))
                    continue

                # Monitor session on Ethernet interface
                for node_index, node_name in enumerate(adapter.switches):
                    if node_name != self.shared_utils.hostname:
                        continue

                    ethernet_interface_name = adapter.switch_ports[node_index]
                    interface_data = InterfaceData(interface=ethernet_interface_name, context=adapter._internal_data.context)
                    monitor_session_configs.extend(self._get_monitor_session_interface_data(interface_data, adapter.monitor_sessions))

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
                        self._get_monitor_session_interface_data(
                            interface_data,
                            network_port.monitor_sessions._cast_as(adapter_monitor_sessions_type),
                        )
                    )
                    continue

                # Monitor session on Ethernet interface
                interface_data = InterfaceData(interface=ethernet_interface_name, context=network_port._internal_data.context)
                monitor_session_configs.extend(
                    self._get_monitor_session_interface_data(
                        interface_data,
                        network_port.monitor_sessions._cast_as(adapter_monitor_sessions_type),
                    )
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

                        monitor_session_configs.extend(
                            self._get_monitor_session_interface_data(
                                interface_data,
                                l3_interface.monitor_sessions._cast_as(adapter_monitor_sessions_type),
                            )
                        )

        return monitor_session_configs
