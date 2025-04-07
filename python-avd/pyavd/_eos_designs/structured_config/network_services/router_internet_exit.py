# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterInternetExitMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_internet_exit_policy(
        self: AvdStructuredConfigNetworkServicesProtocol,
        input_topology: EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology
        | EosDesigns.WanVirtualTopologies.PoliciesItem.DefaultVirtualTopology
        | EosDesigns.WanVirtualTopologies.PoliciesItem.ApplicationVirtualTopologiesItem,
        policy_name: str,
    ) -> None:
        """
        Set the internet-exit policy for a given Virtual Topology if required.

        This will also call the relevant method to set the NAT, IP access list, monitor connections,
        router_service_insertion, static_route, ip_security and ethernet or tunnel interfaces in the structured config.
        """
        if not self.shared_utils.is_cv_pathfinder_client:
            return

        if not (internet_exit_policy_name := input_topology.internet_exit.policy):
            return

        if internet_exit_policy_name in self.structured_config.router_internet_exit.policies:
            # We have already added this policy
            return

        if internet_exit_policy_name not in self.inputs.cv_pathfinder_internet_exit_policies:
            msg = (
                f"The internet exit policy {internet_exit_policy_name} configured under "
                f"`wan_virtual_topologies.policies[name={policy_name}].internet_exit.policy` "
                "is not defined under `cv_pathfinder_internet_exit_policies`."
            )
            raise AristaAvdInvalidInputsError(msg)

        internet_exit_policy = self.inputs.cv_pathfinder_internet_exit_policies[internet_exit_policy_name]

        # duplicate with some function in utils_wan.
        # TODO: Add support for port_channels
        local_wan_l3_interfaces = EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces(
            [
                wan_interface
                for wan_interface in self.shared_utils.wan_interfaces
                if internet_exit_policy.name in wan_interface.cv_pathfinder_internet_exit.policies
            ]
        )
        if not local_wan_l3_interfaces:
            # No local interface for this policy
            # implies policy present in input yml, but not associated with any interface yet
            # TODO: Decide if we should raise here instead
            return

        # enabling monitor connectivity
        self.structured_config.monitor_connectivity.shutdown = False
        # enabling router_service_insertion once
        self.structured_config.router_service_insertion.enabled = True

        if internet_exit_policy.type == "direct":
            self._set_direct_internet_exit_policy(internet_exit_policy, local_wan_l3_interfaces)
        else:  # internet_exit_policy.type == "zscaler"
            self._set_zscaler_internet_exit_policy(internet_exit_policy, local_wan_l3_interfaces)
            # TODO: Technically we need this ONLY if there is ANY Zscaler policy
            if self.inputs.ipsec_settings.bind_connection_to_interface:
                self.structured_config.ip_security.connection_tx_interface_match_source_ip = True

    def _set_direct_internet_exit_policy(
        self: AvdStructuredConfigNetworkServicesProtocol,
        internet_exit_policy: EosDesigns.CvPathfinderInternetExitPoliciesItem,
        local_wan_l3_interfaces: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces,
    ) -> None:
        """
        Set the direct internet-exit policy in structured_config.

        This will also call the relevant method to set the NAT, IP access list, monitor connections,
        router_service_insertion, static_route and ethernet interfaces in the structured config.
        """
        policy_exit_groups = EosCliConfigGen.RouterInternetExit.PoliciesItem.ExitGroups()
        """Track the exit groups for the Internet Exit policy."""

        direct_ie_acl_interface_ips: set[str] = set()
        """Set of Interface IPs configure for the direct Internet Exit ACL if any."""

        for wan_interface in local_wan_l3_interfaces:
            if not wan_interface.peer_ip:
                msg = (
                    f"'l3_interfaces[name={wan_interface.name}].peer_ip' needs to be set. When using WAN interface "
                    "for direct type Internet exit, 'peer_ip' is used for nexthop, and connectivity monitoring."
                )
                raise AristaAvdInvalidInputsError(msg)

            # wan interface ip will be used for acl, hence raise error if ip is not available
            if (ip_address := wan_interface.ip_address) == "dhcp" and not (ip_address := wan_interface.dhcp_ip):
                msg = (
                    f"'l3_interfaces[name={wan_interface.name}].dhcp_ip' needs to be set. When using WAN interface for 'direct' type Internet exit, "
                    "'dhcp_ip' is used in the NAT ACL."
                )
                raise AristaAvdInvalidInputsError(msg)

            if not ip_address:  # pragma: no cover
                # This cannot raise in theory as it is currently caught in underlay so we can't test it with our scenarii.
                msg = (
                    f"'l3_interfaces[name={wan_interface.name}].ip_address' or 'dhcp_ip' needs to be set when using WAN interface for 'direct' "
                    "type Internet Exit."
                )
                raise AristaAvdInvalidInputsError(msg)

            connection_name = f"IE-{self.shared_utils.sanitize_interface_name(wan_interface.name)}"
            description = f"Internet Exit {internet_exit_policy.name}"

            self.set_direct_ie_monitor_connectivity(
                interface_name=wan_interface.name,
                monitor_name=connection_name,
                description=description,
                monitor_host=wan_interface.peer_ip,
            )
            self.set_direct_ie_router_service_insertion(monitor_name=connection_name, source_interface=wan_interface.name, next_hop=wan_interface.peer_ip)
            self.set_direct_ie_connection_ethernet_interfaces(source_interface=wan_interface.name)
            direct_ie_acl_interface_ips.add(ip_address)

            # Adding exit group
            policy_exit_groups.append_new(name=internet_exit_policy.name)
            self.structured_config.router_internet_exit.exit_groups.obtain(internet_exit_policy.name).local_connections.append_new(name=connection_name)

        if internet_exit_policy.fallback_to_system_default:
            policy_exit_groups.append_new(name="system-default-exit-group")

        self._set_direct_ie_policy_ip_nat(direct_ie_acl_interface_ips)

        self.structured_config.router_internet_exit.policies.append_new(name=internet_exit_policy.name, exit_groups=policy_exit_groups)

    def _set_zscaler_internet_exit_policy(
        self: AvdStructuredConfigNetworkServicesProtocol,
        internet_exit_policy: EosDesigns.CvPathfinderInternetExitPoliciesItem,
        local_wan_l3_interfaces: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces,
    ) -> None:
        """
        Set the Zscaler internet-exit policy in structured_config.

        This will also call the relevant method to set the NAT, IP access list, monitor connections,
        router_service_insertion, static_route, ip_security and tunnel interfaces in the structured config.
        """
        policy_exit_groups = EosCliConfigGen.RouterInternetExit.PoliciesItem.ExitGroups()
        """Track the exit groups for the Internet Exit policy."""
        metadata_tunnels = EosCliConfigGen.Metadata.CvPathfinder.InternetExitPoliciesItem.Tunnels()
        """Object to keep track of tunnel metadata for Zscaler Intermet Exit Policy."""

        for wan_interface in local_wan_l3_interfaces:
            if not wan_interface.peer_ip:
                msg = f"The configured internet-exit policy requires `peer_ip` configured under the WAN Interface {wan_interface.name}."
                raise AristaAvdInvalidInputsError(msg)

            interface_policy_config = wan_interface.cv_pathfinder_internet_exit.policies[internet_exit_policy.name]

            if interface_policy_config.tunnel_interface_numbers is None:
                msg = (
                    f"{wan_interface.name}.cv_pathfinder_internet_exit.policies[{internet_exit_policy.name}]."
                    "tunnel_interface_numbers needs to be set, when using wan interface for zscaler type internet exit."
                )
                raise AristaAvdInvalidInputsError(msg)

            tunnel_id_range: list[int] = range_expand(interface_policy_config.tunnel_interface_numbers)

            zscaler_endpoints = (self._zscaler_endpoints.primary, self._zscaler_endpoints.secondary, self._zscaler_endpoints.tertiary)
            for index, zscaler_endpoint in enumerate(zscaler_endpoints):
                if not zscaler_endpoint:
                    continue

                tunnel_id = tunnel_id_range[index]
                preference = ("primary", "secondary", "tertiary")[index]
                # PRI, SEC, TER used for groups
                # TODO: consider if we should use DC names as group suffix.
                suffix = preference[0:3].upper()

                connection_name = f"IE-Tunnel{tunnel_id}"
                description = f"Internet Exit {internet_exit_policy.name} {suffix}"

                self.set_zscaler_ie_tunnel_interface(
                    tunnel_id=tunnel_id,
                    description=description,
                    source_interface=wan_interface.name,
                    destination=zscaler_endpoint.ip_address,
                    ipsec_profile=f"IE-{internet_exit_policy.name}-PROFILE",
                )
                self.set_zscaler_ie_monitor_connectivity(
                    tunnel_id=tunnel_id, monitor_name=f"IE-Tunnel{tunnel_id}", description=description, monitor_host=zscaler_endpoint.ip_address
                )
                self.set_zscaler_ie_connection_static_route(
                    destination_ip=zscaler_endpoint.ip_address, name=f"IE-ZSCALER-{suffix}", next_hop=wan_interface.peer_ip
                )
                self.set_zscaler_ie_router_service_insertion(monitor_name=connection_name, tunnel_id=tunnel_id)

                # set metadata
                metadata_tunnels.append_new(
                    name=f"Tunnel{tunnel_id}",
                    preference="Preferred" if preference == "primary" else "Alternate",
                    endpoint=zscaler_endpoint._cast_as(EosCliConfigGen.Metadata.CvPathfinder.InternetExitPoliciesItem.TunnelsItem.Endpoint),
                )

                # Adding exit group
                exit_group_name = f"{internet_exit_policy.name}_{suffix}"
                policy_exit_groups.append_new(name=exit_group_name)
                self.structured_config.router_internet_exit.exit_groups.obtain(exit_group_name).local_connections.append_new(name=connection_name)

        if internet_exit_policy.fallback_to_system_default:
            policy_exit_groups.append_new(name="system-default-exit-group")

        self._set_zscaler_ie_policy_ip_nat()
        self._set_zscaler_internet_exit_policy_ip_security(internet_exit_policy)
        self.set_cv_pathfinder_metadata_zscaler_internet_exit_policy(internet_exit_policy, metadata_tunnels)

        self.structured_config.router_internet_exit.policies.append_new(name=internet_exit_policy.name, exit_groups=policy_exit_groups)
