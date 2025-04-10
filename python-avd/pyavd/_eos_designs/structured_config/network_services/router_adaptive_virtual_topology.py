# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterAdaptiveVirtualTopologyMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_router_adaptive_virtual_topology_vrf(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vrf: EosDesigns.WanVirtualTopologies.VrfsItem,
        profiles: EosCliConfigGen.RouterAdaptiveVirtualTopology.VrfsItem.Profiles,
    ) -> None:
        """Set a VRF in the structured_config for router adaptive-virtual-topology."""
        self.structured_config.router_adaptive_virtual_topology.vrfs.append_new(
            name=vrf.name,
            policy=f"{vrf.policy}-WITH-CP" if vrf.name == "default" else vrf.policy,
            profiles=profiles,
        )

    def _set_cv_pathfinder_control_plane_virtual_topology(
        self: AvdStructuredConfigNetworkServicesProtocol,
        output_policy: EosCliConfigGen.RouterAdaptiveVirtualTopology.PoliciesItem | EosCliConfigGen.RouterPathSelection.PoliciesItem,
        cv_pathfinder_policy_profiles: EosCliConfigGen.RouterAdaptiveVirtualTopology.VrfsItem.Profiles,
    ) -> None:
        """
        Set structured_config data relevant to the input ControlPlaneVirtualTopology.

        This includes:
          * the load-balancing policy
          * the potential internet-exit policy
          * the router-adaptive-virtual-topology profile referencing the load-balancing policy and the internet-exit policy if any
          * update the input `output_policy` targeting the profile
          * setting the profile in the cv_pathfinder_policy_profiles
          * the relevant application traffic recognition settings
        """
        control_plane_virtual_topology = self._wan_control_plane_virtual_topology

        if (
            load_balance_policy := self._generate_wan_load_balance_policy(
                self._wan_control_plane_profile_name,
                control_plane_virtual_topology,
                output_policy.name,
            )
        ) is None:
            msg = "The WAN control-plane load-balance policy is empty. Make sure at least one path-group can be used in the policy"
            raise AristaAvdError(msg)

        if self.inputs.wan_mode == "autovpn":
            output_policy.rules.append_new(
                id=10,
                application_profile=self.inputs.wan_virtual_topologies.control_plane_virtual_topology.application_profile,
                load_balance=load_balance_policy.name,
            )
        else:  # cv-pathfinder
            output_policy.matches.append_new(
                application_profile=self.inputs.wan_virtual_topologies.control_plane_virtual_topology.application_profile,
                avt_profile=self._wan_control_plane_profile_name,
                traffic_class=control_plane_virtual_topology.traffic_class,
                dscp=control_plane_virtual_topology.dscp,
            )

            # Add profile
            profile = EosCliConfigGen.RouterAdaptiveVirtualTopology.ProfilesItem(
                name=self._wan_control_plane_profile_name,
                load_balance_policy=load_balance_policy.name,
            )

            # Handling Internet Exit
            if control_plane_virtual_topology.internet_exit.policy:
                self._verify_internet_exit_policy(control_plane_virtual_topology.internet_exit.policy, output_policy.name)
                if self._internet_exit_policy_has_local_interfaces(control_plane_virtual_topology.internet_exit.policy):
                    profile.internet_exit_policy = control_plane_virtual_topology.internet_exit.policy
                self._set_internet_exit_policy(control_plane_virtual_topology, output_policy.name)

            self.structured_config.router_adaptive_virtual_topology.profiles.append(profile)
            cv_pathfinder_policy_profiles.append_new(name=self._wan_control_plane_profile_name, id=254)

        # Add load_balance_policy
        self.structured_config.router_path_selection.load_balance_policies.append(load_balance_policy)
        self._set_virtual_topology_application_classification(control_plane_virtual_topology, output_policy.name)

    def _set_cv_pathfinder_policy(
        self: AvdStructuredConfigNetworkServicesProtocol,
        policy: EosDesigns.WanVirtualTopologies.PoliciesItem,
        *,
        control_plane: bool = False,
    ) -> EosCliConfigGen.RouterAdaptiveVirtualTopology.VrfsItem.Profiles:
        """
        Add a router adaptive-virtual-topology policy to the structured_config.

        TODO: Split this up in smaller methods.

        Returns:
            EosCliConfigGen.RouterAdaptiveVirtualTopology.VrfsItem.Profiles: the list of profiles to configure in the VRFs using this policy.
        """
        output_policy = EosCliConfigGen.RouterAdaptiveVirtualTopology.PoliciesItem(name=policy.name)
        policy_profiles = EosCliConfigGen.RouterAdaptiveVirtualTopology.VrfsItem.Profiles()
        """List of profiles to add to VRFs using this policy."""

        # For Control Plane override the policy name and add the control plane VT.
        if control_plane:
            output_policy.name = f"{output_policy.name}-WITH-CP"
            self._set_cv_pathfinder_control_plane_virtual_topology(output_policy, policy_profiles)

        # Normal entries
        for application_virtual_topology in policy.application_virtual_topologies:
            name = application_virtual_topology.name or self._default_profile_name(policy.name, application_virtual_topology.application_profile)
            context_path = f"wan_virtual_topologies.policies[{policy.name}].application_virtual_topologies[{application_virtual_topology.application_profile}]"
            load_balance_policy = self._generate_wan_load_balance_policy(name, application_virtual_topology, context_path)

            if not load_balance_policy:
                # Empty load balance policy so skipping
                # TODO: Add "nodes" or similar under the profile and raise here
                # if the node is set and there are no matching path groups.
                continue

            if not application_virtual_topology.id:
                msg = (
                    f"Missing mandatory `id` in "
                    f"`wan_virtual_topologies.policies[{policy.name}].application_virtual_topologies[{application_virtual_topology.application_profile}]` "
                    "when `wan_mode` is 'cv-pathfinder."
                )
                raise AristaAvdInvalidInputsError(msg)

            output_policy.matches.append_new(
                application_profile=application_virtual_topology.application_profile,
                avt_profile=name,
                traffic_class=application_virtual_topology.traffic_class,
                dscp=application_virtual_topology.dscp,
            )
            policy_profiles.append_new(id=application_virtual_topology.id, name=name)

            # Add load_balance_policy
            self.structured_config.router_path_selection.load_balance_policies.append(load_balance_policy)
            # Add application traffic recognition
            self._set_virtual_topology_application_classification(application_virtual_topology, policy.name)

            # Need to create the object and not use append_new otherwise it conflicts
            # with other profiles as we are not adding the internet_exit_policy immediately
            profile = EosCliConfigGen.RouterAdaptiveVirtualTopology.ProfilesItem(
                name=name,
                load_balance_policy=load_balance_policy.name,
            )
            if application_virtual_topology.internet_exit.policy:
                self._verify_internet_exit_policy(application_virtual_topology.internet_exit.policy, policy.name)
                if self._internet_exit_policy_has_local_interfaces(application_virtual_topology.internet_exit.policy):
                    profile.internet_exit_policy = application_virtual_topology.internet_exit.policy

                # Handling Internet Exit
                self._set_internet_exit_policy(application_virtual_topology, output_policy.name)

            self.structured_config.router_adaptive_virtual_topology.profiles.append(profile)

        # default match
        self._verify_policy_default_match(policy)
        if not policy.default_virtual_topology.drop_unmatched:
            name = policy.default_virtual_topology.name or self._default_profile_name(policy.name, "DEFAULT")
            context_path = f"wan_virtual_topologies.policies[{policy.name}].default_virtual_topology"
            load_balance_policy = self._generate_wan_load_balance_policy(name, policy.default_virtual_topology, context_path)

            if not load_balance_policy:
                msg = (
                    f"The `default_virtual_topology` path-groups configuration for `wan_virtual_topologies.policies[{policy.name}]` produces "
                    "an empty load-balancing policy. Make sure at least one path-group present on the device is allowed in the "
                    "`default_virtual_topology` path-groups."
                )
                raise AristaAvdError(msg)

            output_policy.matches.append_new(
                application_profile="default",
                avt_profile=name,
                traffic_class=policy.default_virtual_topology.traffic_class,
                dscp=policy.default_virtual_topology.dscp,
            )
            # Add load_balance_policy
            self.structured_config.router_path_selection.load_balance_policies.append(load_balance_policy)

            profile = EosCliConfigGen.RouterAdaptiveVirtualTopology.ProfilesItem(
                name=name,
                load_balance_policy=load_balance_policy.name,
            )
            if policy.default_virtual_topology.internet_exit.policy:
                self._verify_internet_exit_policy(policy.default_virtual_topology.internet_exit.policy, policy.name)
                if self._internet_exit_policy_has_local_interfaces(policy.default_virtual_topology.internet_exit.policy):
                    profile.internet_exit_policy = policy.default_virtual_topology.internet_exit.policy
                # Handling Internet Exit
                self._set_internet_exit_policy(policy.default_virtual_topology, output_policy.name)
            self.structured_config.router_adaptive_virtual_topology.profiles.append(profile)

            policy_profiles.append_new(id=1, name=name)

        if not output_policy.matches:
            # The policy is empty but should be assigned to a VRF
            msg = (
                f"The policy `wan_virtual_topologies.policies[{policy.name}]` cannot match any traffic but is assigned to a VRF. "
                "Make sure at least one path-group present on the device is used in the policy."
            )
            raise AristaAvdError(msg)

        self.structured_config.router_adaptive_virtual_topology.policies.append(output_policy)

        return policy_profiles
