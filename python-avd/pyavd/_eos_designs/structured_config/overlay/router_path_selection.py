# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import get, get_ip_from_ip_prefix

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class RouterPathSelectionMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_path_selection(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set structured config for router path-selection (DPS)."""
        if not self.shared_utils.is_wan_router:
            return

        self.structured_config.router_path_selection.tcp_mss_ceiling.ipv4_segment_size = self.shared_utils.node_config.dps_mss_ipv4
        self._set_path_groups()

        if self.shared_utils.is_wan_server:
            self.structured_config.router_path_selection.peer_dynamic_source = "stun"

    @cached_property
    def _dp_ipsec_profile_name(self: AvdStructuredConfigOverlayProtocol) -> str:
        """
        Returns the IPsec profile name to use for Data-Plane.

        If no data-plane config is present for IPsec, default to the control-plane profile-name.
        """
        if self.inputs.wan_ipsec_profiles.data_plane:
            return self.inputs.wan_ipsec_profiles.data_plane.profile_name
        return self.inputs.wan_ipsec_profiles.control_plane.profile_name

    def _set_path_groups(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the required path-groups locally."""
        # Configure all path-groups on Pathfinders and AutoVPN RRs. Otherwise only configure the local path-groups
        path_groups_to_configure = self.inputs.wan_path_groups if self.shared_utils.is_wan_server else self.shared_utils.wan_local_path_groups

        for path_group in path_groups_to_configure:
            is_local_pg = path_group.name in self.shared_utils.wan_local_path_group_names
            disable_dynamic_peer_ipsec = is_local_pg and not path_group.ipsec.dynamic_peers

            path_group_item = EosCliConfigGen.RouterPathSelection.PathGroupsItem(
                name=path_group.name,
                id=self._get_path_group_id(path_group.name, path_group.id),
            )
            self._update_local_interfaces_for_path_group(path_group_item)
            self._update_dynamic_peers(disable_ipsec=disable_dynamic_peer_ipsec, path_group=path_group_item)
            self._update_static_peers_for_path_group(path_group_item)

            if not is_local_pg:
                self.structured_config.router_path_selection.path_groups.append(path_group_item)
                continue

            # On pathfinder IPsec profile is not required for non local path_groups
            if path_group.ipsec.static_peers:
                path_group_item.ipsec_profile = self.inputs.wan_ipsec_profiles.control_plane.profile_name

            # KeepAlive config is not required for non local path_groups
            if interval := path_group.dps_keepalive.interval:
                if interval == "auto":
                    path_group_item.keepalive.auto = True
                else:
                    if not (interval.isdigit() and 50 <= int(interval) <= 60000):
                        msg = (
                            f"Invalid value '{interval}' for dps_keepalive.interval - "
                            f"should be either 'auto', or an integer[50-60000] for wan_path_groups[{path_group.name}]"
                        )
                        raise AristaAvdError(msg)
                    path_group_item.keepalive._update(interval=int(interval), failure_threshold=path_group.dps_keepalive.failure_threshold)

            self.structured_config.router_path_selection.path_groups.append(path_group_item)

        if self.shared_utils.wan_ha or self.shared_utils.is_cv_pathfinder_server:
            self._set_ha_path_group()

    def _set_ha_path_group(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Called only when self.shared_utils.wan_ha is True or on Pathfinders."""
        path_group = EosCliConfigGen.RouterPathSelection.PathGroupsItem(
            name=self.inputs.wan_ha.lan_ha_path_group_name,
            id=self._get_path_group_id(self.inputs.wan_ha.lan_ha_path_group_name),
            flow_assignment="lan",
        )

        if self.shared_utils.is_cv_pathfinder_server:
            self.structured_config.router_path_selection.path_groups.append(path_group)
            return

        if self.shared_utils.use_port_channel_for_direct_ha:
            path_group.local_interfaces.append_new(name=f"Port-Channel{self.shared_utils.wan_ha_port_channel_id}")
        else:
            # TODO: See if we can make the function returns directly the list of interfaces
            for interface in self.shared_utils.wan_ha_interfaces:
                path_group.local_interfaces.append_new(name=interface)
        # not a pathfinder device
        path_group.static_peers.append_new(
            router_ip=self._wan_ha_peer_vtep_ip(),
            name=self.shared_utils.wan_ha_peer,
            ipv4_addresses=EosCliConfigGen.RouterPathSelection.PathGroupsItem.StaticPeersItem.Ipv4Addresses(
                [get_ip_from_ip_prefix(ip_address) for ip_address in self.shared_utils.wan_ha_peer_ip_addresses]
            ),
        )

        if self.shared_utils.wan_ha_ipsec:
            path_group.ipsec_profile = self._dp_ipsec_profile_name

        self.structured_config.router_path_selection.path_groups.append(path_group)

    def _wan_ha_peer_vtep_ip(self: AvdStructuredConfigOverlayProtocol) -> str:
        peer_facts = self.shared_utils.get_peer_facts(self.shared_utils.wan_ha_peer)
        if not peer_facts.vtep_ip:
            msg = f"'vtep_ip' is required but was not found for host '{self.shared_utils.wan_ha_peer}'"
            raise AristaAvdInvalidInputsError(msg)
        return peer_facts.vtep_ip

    def _get_path_group_id(self: AvdStructuredConfigOverlayProtocol, path_group_name: str, config_id: int | None = None) -> int:
        """
        Get path group id.

        TODO: - implement algorithm to auto assign IDs - cf internal documentation
        TODO: - also implement algorithm for cross connects on public path_groups.
        """
        if path_group_name == self.inputs.wan_ha.lan_ha_path_group_name:
            return 65535
        if config_id is not None:
            return config_id
        return 500

    def _update_local_interfaces_for_path_group(
        self: AvdStructuredConfigOverlayProtocol, path_group: EosCliConfigGen.RouterPathSelection.PathGroupsItem
    ) -> None:
        """
        Update the local_interfaces list for the given path group.

        If the local_interface is configured with metric bandwidth, also set the metric bandwidth for router_path_selection.

        For AUTOVPN clients, configure the stun server profiles as appropriate
        """
        if path_group.name not in self.shared_utils.wan_local_path_groups:
            return

        for interface in self.shared_utils.wan_local_path_groups[path_group.name]._internal_data.interfaces:
            interface_name: str = get(interface, "name", required=True)
            local_interface = EosCliConfigGen.RouterPathSelection.PathGroupsItem.LocalInterfacesItem(name=interface_name)

            if self.shared_utils.is_wan_client and self.shared_utils.should_connect_to_wan_rs([path_group.name]):
                stun_server_profiles = self._stun_server_profiles.get(path_group.name, [])
                if stun_server_profiles:
                    for profile in stun_server_profiles:
                        local_interface.stun.server_profiles.append(profile.name)

            if interface_name.startswith("Port-Channel"):
                # metric bandwidth not supported on port-channel
                path_group.local_interfaces.append(local_interface)
                continue

            interface_input = self.shared_utils.wan_interfaces[interface_name]
            if interface_input.receive_bandwidth or interface_input.transmit_bandwidth:
                if "." in interface_name:
                    schema_key = f"{self.shared_utils.node_type_key_data.key}.nodes[name={self.shared_utils.hostname}].l3_interfaces[name={interface_name}]"
                    msg = f"Fields 'receive_bandwidth' and 'transmit_bandwidth' configured on {schema_key} are not supported for subinterfaces."
                    raise AristaAvdError(msg)
                self.structured_config.router_path_selection.interfaces.append_new(
                    name=interface_name,
                    metric_bandwidth=EosCliConfigGen.RouterPathSelection.InterfacesItem.MetricBandwidth(
                        receive=interface_input.receive_bandwidth, transmit=interface_input.transmit_bandwidth
                    ),
                )

            path_group.local_interfaces.append(local_interface)

    def _update_dynamic_peers(
        self: AvdStructuredConfigOverlayProtocol, disable_ipsec: bool, path_group: EosCliConfigGen.RouterPathSelection.PathGroupsItem
    ) -> None:
        """TODO: support ip_local ?"""
        if not self.shared_utils.is_wan_client:
            return

        path_group.dynamic_peers.enabled = True

        if disable_ipsec:
            path_group.dynamic_peers.ipsec = False

    def _update_static_peers_for_path_group(self: AvdStructuredConfigOverlayProtocol, path_group: EosCliConfigGen.RouterPathSelection.PathGroupsItem) -> None:
        """Update the static peers for the given path-group based on the connected nodes."""
        if not self.shared_utils.is_wan_router:
            return

        for wan_route_server in self.shared_utils.filtered_wan_route_servers:
            if path_group.name not in wan_route_server.path_groups:
                continue

            ipv4_addresses = [
                get_ip_from_ip_prefix(interface.public_ip) for interface in wan_route_server.path_groups[path_group.name].interfaces if interface.public_ip
            ]

            path_group.static_peers.append_new(
                router_ip=wan_route_server.vtep_ip,
                name=wan_route_server.hostname,
                ipv4_addresses=EosCliConfigGen.RouterPathSelection.PathGroupsItem.StaticPeersItem.Ipv4Addresses(ipv4_addresses),
            )
