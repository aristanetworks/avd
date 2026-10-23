# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils.groupby import groupby_obj
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


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
            merged_settings = session_configs_list[0]._deepcopy()
            for session_config in session_configs_list[1:]:
                merged_settings._deepmerge(session_config)

            if merged_settings.session_settings._get("access_group"):
                for session in session_configs_list:
                    if session.source_settings.access_group:
                        msg = (
                            f"Cannot set an ACL for both `session_settings` and `source_settings`"
                            f" under the monitor session '{session.name}' for {session._internal_data.context}."
                        )
                        raise AristaAvdInvalidInputsError(msg)

            monitor_session = EosCliConfigGen.MonitorSessionsItem(name=session_name)
            for session in session_configs_list:
                if session.role == "destination":
                    monitor_session.destinations.append(session._internal_data.interface)

            source_sessions = [session for session in session_configs_list if session.role == "source"]

            for session in source_sessions:
                source = EosCliConfigGen.MonitorSessionsItem.SourcesItem(
                    name=session._internal_data.interface,
                    direction=session.source_settings.direction,
                )
                acl = session.source_settings.access_group
                if acl:
                    self._set_monitor_session_access_group(acl.type, acl.name)
                    source.access_group = EosCliConfigGen.MonitorSessionsItem.SourcesItem.AccessGroup(
                        type=self._get_monitor_session_access_group_type(acl.type),
                        name=acl.name,
                        priority=acl.priority,
                    )
                monitor_session.sources.append(source)

            if session_settings := merged_settings.session_settings:
                acl = session_settings.access_group
                if acl:
                    self._set_monitor_session_access_group(acl.type, acl.name)
                monitor_session._update(
                    encapsulation_gre_metadata_tx=session_settings.encapsulation_gre_metadata_tx,
                    header_remove_size=session_settings.header_remove_size,
                    access_group=EosCliConfigGen.MonitorSessionsItem.AccessGroup(
                        type=self._get_monitor_session_access_group_type(acl.type),
                        name=acl.name,
                    ),
                    rate_limit_per_ingress_chip=session_settings.rate_limit_per_ingress_chip,
                    rate_limit_per_egress_chip=session_settings.rate_limit_per_egress_chip,
                    sample=session_settings.sample,
                    truncate=session_settings.truncate._cast_as(EosCliConfigGen.MonitorSessionsItem.Truncate),
                )

            self.structured_config.monitor_sessions.append(monitor_session)

    def _set_monitor_session_access_group(self: AvdStructuredConfigBaseProtocol, acl_type: str, acl_name: str) -> None:
        """Validate and configure ACLs referenced by monitor sessions."""
        if acl_type in ("ip", "ipv6", "mac") and not self.inputs.avd_design_future.validate_monitor_session_acls:
            return
        self._validate_monitor_session_access_group(acl_type, acl_name)
        match acl_type:
            case "ip":
                self.structured_config_utils._set_ipv4_acl(self.inputs.ipv4_acls[acl_name])
            case "ipv4_standard":
                self.structured_config_utils._set_ipv4_standard_acl(acl_name)
            case "ipv6":
                self.structured_config_utils._set_ipv6_acl(self.inputs.ipv6_acls[acl_name])
            case "mac":
                self.structured_config_utils._set_mac_acl(acl_name)

    def _validate_monitor_session_access_group(self: AvdStructuredConfigBaseProtocol, acl_type: str, acl_name: str) -> None:
        """Validate that the referenced ACL exists in the corresponding catalog without generating its definition."""
        catalog_name = {
            "ip": "ipv4_acls",
            "ipv4_standard": "ipv4_standard_acls",
            "ipv6": "ipv6_acls",
            "mac": "mac_acls",
        }.get(acl_type)
        if catalog_name is not None and acl_name not in getattr(self.inputs, catalog_name):
            msg = f"{catalog_name}[name={acl_name}]"
            raise AristaAvdMissingVariableError(msg, host=self.shared_utils.hostname)

    @staticmethod
    def _get_monitor_session_access_group_type(
        acl_type: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem.SourceSettings.AccessGroup.Type
        | None,
    ) -> EosCliConfigGen.MonitorSessionsItem.SourcesItem.AccessGroup.Type | None:
        """Return the EOS ACL type for a monitor-session access group."""
        if acl_type == "ipv4_standard":
            return "ip"
        return acl_type

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
    ) -> list[EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem]:
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
                    for monitor_session in adapter.monitor_sessions:
                        per_interface_monitor_session = monitor_session._deepcopy()
                        per_interface_monitor_session._internal_data.interface = port_channel_interface_name
                        per_interface_monitor_session._internal_data.context = adapter._internal_data.context
                        monitor_session_configs.append(per_interface_monitor_session)
                    continue

                # Monitor session on Ethernet interface
                for node_index, node_name in enumerate(adapter.switches):
                    if node_name != self.shared_utils.hostname:
                        continue

                    ethernet_interface_name = adapter.switch_ports[node_index]
                    for monitor_session in adapter.monitor_sessions:
                        per_interface_monitor_session = monitor_session._deepcopy()
                        per_interface_monitor_session._internal_data.interface = ethernet_interface_name
                        per_interface_monitor_session._internal_data.context = adapter._internal_data.context
                        monitor_session_configs.append(per_interface_monitor_session)

        for network_port in self.shared_utils.filtered_network_ports:
            if not network_port.monitor_sessions:
                continue

            for ethernet_interface_name in range_expand(network_port.switch_ports):
                # Monitor session on Port-channel interface
                if network_port.port_channel and network_port.port_channel.mode is not None:
                    default_channel_group_id = int("".join(re.findall(r"\d", ethernet_interface_name)))
                    channel_group_id = network_port.port_channel.channel_id or default_channel_group_id

                    port_channel_interface_name = f"Port-Channel{channel_group_id}"
                    for monitor_session in network_port.monitor_sessions:
                        per_interface_monitor_session = monitor_session._deepcopy()
                        per_interface_monitor_session._internal_data.interface = port_channel_interface_name
                        per_interface_monitor_session._internal_data.context = network_port._internal_data.context
                        monitor_session_configs.append(per_interface_monitor_session)
                    continue

                # Monitor session on Ethernet interface
                for monitor_session in network_port.monitor_sessions:
                    per_interface_monitor_session = monitor_session._deepcopy()
                    per_interface_monitor_session._internal_data.interface = ethernet_interface_name
                    per_interface_monitor_session._internal_data.context = network_port._internal_data.context
                    monitor_session_configs.append(per_interface_monitor_session)

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for l3_interface_index, l3_interface in enumerate(vrf.l3_interfaces):
                    for node_index, node_name in enumerate(l3_interface.nodes):
                        if node_name != self.shared_utils.hostname:
                            continue
                        interface_name = l3_interface.interfaces[node_index]
                        context = f"{tenant._internal_data.context}[name={tenant.name}].vrfs[name={vrf.name}].l3_interfaces[{l3_interface_index}]"
                        # TODO: DO not raise the error for digital twin
                        if (
                            l3_interface.monitor_sessions
                            and "." in interface_name
                            and not self.shared_utils.platform_settings.feature_support.subinterface_monitor_session
                        ):
                            msg = (
                                "Monitor session on sub-interfaces is not supported on this platform. "
                                f"Got monitor session on interface '{interface_name}' under {context}."
                            )
                            raise AristaAvdInvalidInputsError(msg)
                        for monitor_session in l3_interface.monitor_sessions:
                            self._validate_monitor_session_on_subinterface(interface_name, monitor_session, context)

                            # We merge using the adapter datamodel to catch conflicts in direction.
                            per_interface_monitor_session = monitor_session._deepcopy()._cast_as(
                                EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem
                            )
                            per_interface_monitor_session._internal_data.interface = interface_name
                            per_interface_monitor_session._internal_data.context = context

                            monitor_session_configs.append(per_interface_monitor_session)

        return monitor_session_configs
