# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class RouterPathSelectionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_path_selection(self) -> dict | None:
        """
        Return structured config for router path-selection (DPS)
        """

        if not self.shared_utils.wan_role:
            return None

        path_groups = self._get_path_groups()

        router_path_selection = {
            "path_groups": path_groups,
            "load_balance_policies": self._get_load_balance_policies(path_groups),
            "policies": self._get_policies(),
            "vrfs": self._get_vrfs(),
        }

        if self.shared_utils.wan_role == "server":
            router_path_selection["peer_dynamic_source"] = "stun"

        return strip_empties_from_dict(router_path_selection)

    def _get_path_groups(self) -> list:
        """
        Generate the required path-groups locally
        """
        # TODO - get this once WAN interface are available
        # TODO - this function will need to handle Crossconnection of public carriers
        #
        local_carriers = []
        # The value will be set based on the WAN interfaces configuration
        # local_carriers = self.shared_utils.carriers

        if not local_carriers:
            return []

        path_groups = []

        # TODO - need to have default value in one place only -> maybe facts / shared_utils ?
        ipsec_profile_name = get(self._hostvars, "wan_ipsec_profiles.control_plane.profile_name", required=True)

        for carrier in local_carriers:
            path_groups.append(
                {
                    "name": carrier.get("name"),
                    "id": self._get_carrier_id(carrier),
                    "ipsec_profile": ipsec_profile_name,  # TODO - disable on a per carrier basis
                    "local_interfaces": self._get_local_interfaces(carrier),
                    "dynamic_peers": self._get_dynamic_peers(),
                    "static_peers": self._get_static_peers(carrier),
                }
            )

        if self.shared_utils.cv_pathfinder_role:
            pass
            # implement LAN_HA here

        return path_groups

    def _get_load_balance_policies(self, path_groups: dict) -> dict | None:
        """ """
        # TODO for now a default load balance policy with all path-groups.
        load_balance_policies = []
        load_balance_policies.append({"name": "LBPOLICY", "path_groups": [pg.get("name") for pg in path_groups]})
        return load_balance_policies

    def _get_policies(self) -> list | None:
        """
        Only configure a default DPS policy for the default VRF if wan_mode is autovpn
        for cv-pathfinder, the VRFs are confgured under adaptive_virtual_topology.
        """
        policies = []
        if self.shared_utils.wan_mode == "autovpn":
            # TODO DPS policies - for now adding one default one - MAYBE NEED TO REMOVED
            policies = [{"name": "dps-policy-default", "default_match": {"load_balance": "LBPOLICY"}}]
            return policies
        return None

    def _get_vrfs(self) -> list | None:
        """
        Only configure a default VRF if wan_mode is autovpn
        for cv-pathfinder, the VRFs are confgured under adaptive_virtual_topology.
        """
        vrfs = []
        if self.shared_utils.wan_mode == "autovpn":
            # TODO - Adding default VRF here - check if it makes sense later
            vrfs = [{"name": "default", "path_selection_policy": "dps-policy-default"}]
            return vrfs
        return None

    def _get_carrier_id(self, carrier: dict) -> int:
        """
        TODO - implement algorithm to auto assign IDs - cf internal documenation
        TODO - also implement algorithm for cross connects on public carriers
        """
        if carrier["name"] == "LAN_HA":
            return 65535
        return 500

    def _get_local_interfaces(self, carrier: dict) -> list | None:
        """
        Generate the router_path_selection.local_interfaces list

        For AUTOVPN clients, configure the stun server profiles as appropriate
        """
        local_interfaces = []
        return local_interfaces

    def _get_dynamic_peers(self) -> dict | None:
        """ """
        if self.shared_utils.wan_role != "client":
            return None
        return {"enabled": True}

    def _get_static_peers(self, transport: dict) -> list | None:
        """
        TODO
        """
        if self.shared_utils.wan_role != "client":
            return None
        static_peers = []
        return static_peers
