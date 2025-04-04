# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils.password_utils.password import simple_7_encrypt
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class UtilsWanMixin(Protocol):
    """
    Mixin Class with internal functions for WAN.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _filtered_wan_vrfs(self: AvdStructuredConfigNetworkServicesProtocol) -> EosDesigns.WanVirtualTopologies.Vrfs:
        """Loop through all the VRFs defined under `wan_virtual_topologies.vrfs` and returns a list of mode."""
        wan_vrfs = EosDesigns.WanVirtualTopologies.Vrfs(
            vrf for vrf in self.inputs.wan_virtual_topologies.vrfs if vrf.name in self.shared_utils.vrfs or self.shared_utils.is_wan_server
        )

        # Check that default is in the list as it is required everywhere
        if "default" not in wan_vrfs:
            wan_vrfs.append(EosDesigns.WanVirtualTopologies.VrfsItem(name="default", wan_vni=1))

        return wan_vrfs

    @structured_config_contributor
    def set_wan_policies(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Top level structured config contributor for the WAN policies.

        It sets either the router-path selection policies (for autovpn mode) or the cv-pathfinder policies (for cv-pathfinder mode)
        including their dependencies (avt profiles, load-balancing policies, nat profiles, acls, internet-exit policy,
        router-service-insertion, relevant interfaces, ...).

        It also sets the relevant CV pathfinder metadata for the application traffic recognition.
        """
        if not self.shared_utils.is_wan_router:
            return

        added_policies: dict[str, EosCliConfigGen.RouterAdaptiveVirtualTopology.VrfsItem.Profiles] = {}
        """Dictionary to keep track of the policy names and the associated profiles already handled."""

        for vrf in self._filtered_wan_vrfs:
            if vrf.policy not in self.inputs.wan_virtual_topologies.policies:
                if vrf.policy == self._default_wan_policy_name and self._default_wan_policy_name not in self.inputs.wan_virtual_topologies.policies:
                    vrf_policy = self._default_wan_policy
                else:
                    msg = (
                        f"The policy {vrf.policy} applied to vrf {vrf.name} under `wan_virtual_topologies.vrfs` is not "
                        "defined under `wan_virtual_topologies.policies`."
                    )
                    raise AristaAvdInvalidInputsError(msg)
            else:
                vrf_policy = self.inputs.wan_virtual_topologies.policies[vrf.policy]

            if vrf.name == "default":
                # VRF default is always set and use an updated name so not tracked in added_policies
                if self.inputs.wan_mode == "autovpn":
                    self._set_autovpn_policy(vrf_policy, control_plane=True)
                    self._set_router_path_selection_vrf(vrf)
                else:  # cv-pathfinder
                    policy_profiles = self._set_cv_pathfinder_policy(vrf_policy, control_plane=True)
                    self._set_router_adaptive_virtual_topology_vrf(vrf, policy_profiles)
                continue

            if self.inputs.wan_mode == "autovpn":
                if vrf_policy.name not in added_policies:
                    self._set_autovpn_policy(vrf_policy)
                    added_policies[vrf_policy.name] = EosCliConfigGen.RouterAdaptiveVirtualTopology.VrfsItem.Profiles()
                self._set_router_path_selection_vrf(vrf)
            else:  # cv-pathfinder
                if vrf_policy.name not in added_policies:
                    policy_profiles = self._set_cv_pathfinder_policy(vrf_policy)
                    added_policies[vrf_policy.name] = policy_profiles
                self._set_router_adaptive_virtual_topology_vrf(vrf, added_policies[vrf_policy.name])

        # Add Application Traffic Recognition metadata after all policies have been taken care off.
        self.set_cv_pathfinder_metadata_applications()

    def _verify_policy_default_match(self: AvdStructuredConfigNetworkServicesProtocol, policy: EosDesigns.WanVirtualTopologies.PoliciesItem) -> None:
        """
        Verifies the policy has a proper default_match definition.

        Checks that:
            * the default_virtual_topology is defined.
            * either drop_unmatched must be set or some path_groups must be defined.

        Raises:
            AristaAvdInvalidInputsError: if any criteria is not met.
        """
        if not policy.default_virtual_topology:
            msg = f"wan_virtual_topologies.policies[{policy.name}].default_virtual_toplogy."
            raise AristaAvdInvalidInputsError(msg)

        if not policy.default_virtual_topology.drop_unmatched:
            context_path = f"wan_virtual_topologies.policies[{policy.name}].default_virtual_topology"
            # Verify that path_groups are set or raise
            # TODO: this functionality could be added to schema
            if not policy.default_virtual_topology.path_groups:
                msg = f"Either 'drop_unmatched' or 'path_groups' must be set under '{context_path}'."
                raise AristaAvdInvalidInputsError(msg)

    def _verify_internet_exit_policy(self: AvdStructuredConfigNetworkServicesProtocol, ie_policy_name: str, policy_name: str) -> None:
        """
        Check if the Internet Exit policy name is configured.

        If not raise an AristaAvdInvalidInputsError.

        TODO: This used to check that there is an interface to make it valid.
        """
        if ie_policy_name not in self.inputs.cv_pathfinder_internet_exit_policies:
            msg = (
                f"The internet exit policy {ie_policy_name} configured under "
                f"`wan_virtual_topologies.policies[name={policy_name}].internet_exit.policy` "
                "is not defined under `cv_pathfinder_internet_exit_policies`."
            )
            raise AristaAvdInvalidInputsError(msg)

    local_internet_exit_connections: dict[str, bool] | None = None
    """Poor-mans cache to only check local interfaces for an internet exit policy once."""

    def _internet_exit_policy_has_local_interfaces(self: AvdStructuredConfigNetworkServicesProtocol, ie_policy_name: str) -> bool:
        """Tests if an internet-exit policy is used locally."""
        if self.local_internet_exit_connections and ie_policy_name in self.local_internet_exit_connections:
            return self.local_internet_exit_connections[ie_policy_name]

        local_wan_l3_interfaces = EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces(
            [wan_interface for wan_interface in self.shared_utils.wan_interfaces if ie_policy_name in wan_interface.cv_pathfinder_internet_exit.policies]
        )
        # Update the cache so we don't resolve again next time.
        if self.local_internet_exit_connections is None:
            self.local_internet_exit_connections = {}
        self.local_internet_exit_connections[ie_policy_name] = bool(local_wan_l3_interfaces)

        return bool(local_wan_l3_interfaces)

    def _generate_wan_load_balance_policy(
        self: AvdStructuredConfigNetworkServicesProtocol,
        name: str,
        input_topology: EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology
        | EosDesigns.WanVirtualTopologies.PoliciesItem.DefaultVirtualTopology
        | EosDesigns.WanVirtualTopologies.PoliciesItem.ApplicationVirtualTopologiesItem,
        context_path: str,
    ) -> EosCliConfigGen.RouterPathSelection.LoadBalancePoliciesItem | None:
        """
        Generate and return a router path-selection load-balance policy.

        If HA is enabled:
        * the remote peer path-groups are considered.
        * inject the HA path-group with priority 1.

        Attrs:
            name (str): The name to use as prefix for the Load Balance policy
            input_dict (dict): The dictionary containing the list of path-groups and their preference.
            context_path (str): Key used for context for error messages.

        Returns:
            EosCliConfigGen.RouterPathSelection.LoadBalancePoliciesItem | None
        """
        lb_policy_name = self.shared_utils.generate_lb_policy_name(name)

        wan_load_balance_policy = EosCliConfigGen.RouterPathSelection.LoadBalancePoliciesItem(
            name=lb_policy_name,
            jitter=input_topology.constraints.jitter,
            latency=input_topology.constraints.latency,
            loss_rate=input_topology.constraints.loss_rate,
        )

        if self.shared_utils.is_cv_pathfinder_router:
            wan_load_balance_policy.lowest_hop_count = input_topology.lowest_hop_count

        # Using this flag while looping through all entries to keep track of any path group present on the remote host
        any_path_group_on_wan_ha_peer = self.shared_utils.wan_ha

        for policy_entry in input_topology.path_groups:
            policy_entry_priority = None
            if policy_entry.preference:
                policy_entry_priority = self._path_group_preference_to_eos_priority(policy_entry.preference, f"{context_path}[{policy_entry.names}]")

            for path_group_name in policy_entry.names:
                if (priority := policy_entry_priority) is None:
                    # No preference defined at the policy level, need to retrieve the default preference
                    if path_group_name not in self.inputs.wan_path_groups:
                        msg = (
                            f"Failed to retrieve path-group {path_group_name} from `wan_path_groups` when generating load balance policy {lb_policy_name}. "
                            f"Verify the path-groups defined under {context_path}."
                        )
                        raise AristaAvdInvalidInputsError(msg)
                    wan_path_group = self.inputs.wan_path_groups[path_group_name]
                    priority = self._path_group_preference_to_eos_priority(wan_path_group.default_preference, f"wan_path_groups[{wan_path_group.name}]")

                # Skip path-group on this device if not present on the router except for pathfinders
                if self.shared_utils.is_wan_client and path_group_name not in self.shared_utils.wan_local_path_group_names:
                    continue

                wan_load_balance_policy.path_groups.append_new(
                    name=path_group_name,
                    priority=priority if priority != 1 else None,
                )

            # Updating peer path-groups tracking
            any_path_group_on_wan_ha_peer = any_path_group_on_wan_ha_peer and set(self.shared_utils.wan_ha_peer_path_group_names).union(set(policy_entry.names))

        if len(wan_load_balance_policy.path_groups) == 0 and not any_path_group_on_wan_ha_peer:
            # The policy is empty, and either the site is not using HA or no path-group in the policy is present on the HA peer
            return None

        if self.shared_utils.wan_ha or self.shared_utils.is_cv_pathfinder_server:
            # Adding HA path-group with priority 1
            wan_load_balance_policy.path_groups.append_new(name=self.inputs.wan_ha.lan_ha_path_group_name)

        return wan_load_balance_policy

    def _path_group_preference_to_eos_priority(self: AvdStructuredConfigNetworkServicesProtocol, path_group_preference: int | str, context_path: str) -> int:
        """
        Convert "preferred" to 1 and "alternate" to 2. Everything else is returned as is.

        Arguments:
        ----------
        path_group_preference (str|int): The value of the preference key to be converted. It must be either "preferred", "alternate" or an integer.
        context_path (str): Input path context for the error message.
        """
        if path_group_preference == "preferred":
            return 1
        if path_group_preference == "alternate":
            return 2

        try:
            priority = int(path_group_preference)
        except ValueError:
            # Setting it too high
            priority = 65536

        if not 1 <= priority <= 65535:
            msg = (
                f"Invalid value '{path_group_preference}' for Path-Group preference - should be either 'preferred', "
                f"'alternate' or an integer[1-65535] for {context_path}."
            )
            raise AristaAvdError(msg)

        return priority

    @cached_property
    def _default_wan_policy_name(self: AvdStructuredConfigNetworkServicesProtocol) -> str:
        """TODO: make this configurable."""
        return "DEFAULT-POLICY"

    @cached_property
    def _default_policy_path_group_names(self: AvdStructuredConfigNetworkServicesProtocol) -> list[str]:
        """
        Return a list of path group names for the default policy.

        Return the list of path-groups to consider when generating a default policy with AVD
        whether for the default policy or the special Control-plane policy.
        """
        path_group_names = {path_group.name for path_group in self.inputs.wan_path_groups if not path_group.excluded_from_default_policy}
        if not path_group_names.intersection(self.shared_utils.wan_local_path_group_names):
            # No common path-group between this device local path-groups and the available path-group for the default policy
            msg = (
                f"Unable to generate the default WAN policy as none of the device local path-groups {self.shared_utils.wan_local_path_group_names} "
                "is eligible to be included. Make sure that at least one path-group for the device is not configured with "
                "`excluded_from_default_policy: true` under `wan_path_groups`."
            )
            raise AristaAvdError(msg)
        return natural_sort(path_group_names)

    @cached_property
    def _default_wan_policy(self: AvdStructuredConfigNetworkServicesProtocol) -> EosDesigns.WanVirtualTopologies.PoliciesItem:
        """
        Returning policy containing all path groups not excluded from default policy.

        If no policy is defined for a VRF under 'wan_virtual_topologies.vrfs', a default policy named DEFAULT-POLICY is used
        where all traffic is matched in the default category and distributed amongst all path-groups.
        """
        return EosDesigns.WanVirtualTopologies.PoliciesItem(
            name=self._default_wan_policy_name,
            default_virtual_topology=EosDesigns.WanVirtualTopologies.PoliciesItem.DefaultVirtualTopology(
                path_groups=EosDesigns.WanVirtualTopologies.PoliciesItem.DefaultVirtualTopology.PathGroups(
                    [
                        EosDesigns.WanVirtualTopologies.PoliciesItem.DefaultVirtualTopology.PathGroupsItem(
                            names=EosDesigns.WanVirtualTopologies.PoliciesItem.DefaultVirtualTopology.PathGroupsItem.Names(
                                self._default_policy_path_group_names
                            )
                        )
                    ]
                )
            ),
        )

    def _default_profile_name(self: AvdStructuredConfigNetworkServicesProtocol, profile_name: str, application_profile: str) -> str:
        """
        Helper function to consistently return the default name of a profile.

        Returns:
            str: {profile_name}-{application_profile}
        """
        return f"{profile_name}-{application_profile}"

    @cached_property
    def _wan_control_plane_virtual_topology(self: AvdStructuredConfigNetworkServicesProtocol) -> EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology:
        """
        Return the Control plane virtual topology or the default one.

        The default control_plane_virtual_topology, excluding path_groups with excluded_from_default_policy
        """
        if self.inputs.wan_virtual_topologies.control_plane_virtual_topology:
            return self.inputs.wan_virtual_topologies.control_plane_virtual_topology

        path_groups = self._default_policy_path_group_names
        if self.shared_utils.is_wan_client:
            # Filter only the path-groups connected to pathfinder
            local_path_groups_connected_to_pathfinder = [
                path_group.name
                for path_group in self.shared_utils.wan_local_path_groups
                if any(wan_interface["connected_to_pathfinder"] for wan_interface in path_group._internal_data.interfaces)
            ]
            path_groups = [path_group for path_group in path_groups if path_group in local_path_groups_connected_to_pathfinder]

        return EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology(
            path_groups=EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology.PathGroups(
                [
                    EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology.PathGroupsItem(
                        names=EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology.PathGroupsItem.Names(path_groups)
                    )
                ]
            )
        )

    @cached_property
    def _wan_control_plane_profile_name(self: AvdStructuredConfigNetworkServicesProtocol) -> str:
        """Control plane profile name."""
        vrf_default_policy_name = self._filtered_wan_vrfs["default"].policy
        return self._wan_control_plane_virtual_topology.name or f"{vrf_default_policy_name}-CONTROL-PLANE"

    def _get_ipsec_credentials(
        self: AvdStructuredConfigNetworkServicesProtocol, internet_exit_policy: EosDesigns.CvPathfinderInternetExitPoliciesItem
    ) -> tuple[str, str]:
        """Returns ufqdn, shared_key based on various details from the given internet_exit_policy."""
        if not internet_exit_policy.zscaler.domain_name:
            msg = "zscaler.domain_name"
            raise AristaAvdMissingVariableError(msg)

        if not internet_exit_policy.zscaler.ipsec_key_salt:
            msg = "zscaler.ipsec_key_salt"
            raise AristaAvdMissingVariableError(msg)

        ipsec_key = self._generate_ipsec_key(name=internet_exit_policy.name, salt=internet_exit_policy.zscaler.ipsec_key_salt)
        ufqdn = f"{self.shared_utils.hostname}_{internet_exit_policy.name}@{internet_exit_policy.zscaler.domain_name}"
        return ufqdn, ipsec_key

    def _generate_ipsec_key(self: AvdStructuredConfigNetworkServicesProtocol, name: str, salt: str) -> str:
        """
        Build a secret containing various components for this policy and device.

        Run type-7 obfuscation using a algorithmic salt so we ensure the same key every time.

        TODO: Maybe introduce some formatting with max length of each element, since the keys can become very very long.
        """
        secret = f"{self.shared_utils.hostname}_{name}_{salt}"
        type_7_salt = sum(salt.encode("utf-8")) % 16
        return simple_7_encrypt(secret, type_7_salt)
