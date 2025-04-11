# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdError

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterPathSelectionMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_router_path_selection_vrf(self: AvdStructuredConfigNetworkServicesProtocol, vrf: EosDesigns.WanVirtualTopologies.VrfsItem) -> None:
        """Set a VRF in the structured_config for router path-selection (DPS)."""
        self.structured_config.router_path_selection.vrfs.append_new(
            name=vrf.name,
            path_selection_policy=f"{vrf.policy}-WITH-CP" if vrf.name == "default" else vrf.policy,
        )

    def _set_autovpn_control_plane_virtual_topology(
        self: AvdStructuredConfigNetworkServicesProtocol,
        output_policy: EosCliConfigGen.RouterPathSelection.PoliciesItem,
    ) -> None:
        """
        Set structured_config data relevant to the input ControlPlaneVirtualTopology.

        This includes:
          * the load-balancing policy
          * update the input `output_policy` with the load-balancing entry
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

        output_policy.rules.append_new(
            id=10,
            application_profile=self.inputs.wan_virtual_topologies.control_plane_virtual_topology.application_profile,
            load_balance=load_balance_policy.name,
        )

        # Add load_balance_policy
        self.structured_config.router_path_selection.load_balance_policies.append(load_balance_policy)
        self._set_virtual_topology_application_classification(control_plane_virtual_topology, output_policy.name)

    def _set_autovpn_policy(
        self: AvdStructuredConfigNetworkServicesProtocol,
        policy: EosDesigns.WanVirtualTopologies.PoliciesItem,
        *,
        control_plane: bool = False,
    ) -> None:
        """
        Add a router path-selection policy and its dependencies to the structured_config.

        Router-path selection policies are used in autovpn mode.
        """
        index = 1
        output_policy = EosCliConfigGen.RouterPathSelection.PoliciesItem(name=policy.name)

        # For Control Plane override the policy name and add the control plane VT.
        if control_plane:
            output_policy.name = f"{output_policy.name}-WITH-CP"
            self._set_autovpn_control_plane_virtual_topology(output_policy)
            index = 2

        # Normal entries
        for application_virtual_topology in policy.application_virtual_topologies:
            name = application_virtual_topology.name or self._default_profile_name(policy.name, application_virtual_topology.application_profile)
            context_path = f"wan_virtual_topologies.policies[{policy.name}].application_virtual_topologies[{application_virtual_topology.application_profile}]"
            load_balance_policy = self._generate_wan_load_balance_policy(name, application_virtual_topology, context_path)
            if not load_balance_policy:
                # Empty load balance policy so skipping
                # TODO: Add "nodes" or similar under the profile and raise here if the node is set and there are no matching path groups.
                continue

            output_policy.rules.append_new(
                id=10 * index,
                application_profile=application_virtual_topology.application_profile,
                load_balance=load_balance_policy.name,
            )

            # Add load_balance_policy
            self.structured_config.router_path_selection.load_balance_policies.append(load_balance_policy)
            # Add application traffic recognition
            self._set_virtual_topology_application_classification(application_virtual_topology, policy.name)
            index += 1

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

            output_policy.default_match.load_balance = load_balance_policy.name
            # Add load_balance_policy
            self.structured_config.router_path_selection.load_balance_policies.append(load_balance_policy)

        if not output_policy.rules and not output_policy.default_match:
            # The policy is empty but should be assigned to a VRF
            msg = (
                f"The policy `wan_virtual_topologies.policies[{policy.name}]` cannot match any traffic but is assigned to a VRF. "
                "Make sure at least one path-group present on the device is used in the policy."
            )
            raise AristaAvdError(msg)

        self.structured_config.router_path_selection.policies.append(output_policy)
