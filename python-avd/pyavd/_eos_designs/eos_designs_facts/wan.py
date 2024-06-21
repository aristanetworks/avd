# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ...j2filters import natural_sort

if TYPE_CHECKING:
    from . import EosDesignsFacts


class WanMixin:
    """
    Mixin Class providing a subset of EosDesignsFacts
    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_path_groups(self: EosDesignsFacts) -> list | None:
        """
        TODO: Also add the path_groups importing any of our connected path groups.
                      Need to find out if we need to resolve recursive imports.

        Return the list of WAN path_groups directly connected to this router, with a list of dictionaries
        containing the (interface, ip_address) in the path_group.
        """
        if not self.shared_utils.is_wan_server:
            return None

        return self.shared_utils.wan_local_path_groups

    @cached_property
    def wan_router_uplink_vrfs(self: EosDesignsFacts) -> list[str] | None:
        """
        Exposed in avd_switch_facts

        Return the list of VRF names present on uplink switches.
        These VRFs will be attracted (configured) on WAN "clients" (edge/transit) unless filtered.

        Note that if the attracted VRFs do not have 'wan_vni' set, the code for interface Vxlan1 will raise an error.
        """
        if not self.shared_utils.is_wan_client or self.shared_utils.uplink_type != "p2p-vrfs":
            return None

        # Partially recreating logic from 'uplinks', but since this fact is used to build 'filtered_tenants',
        # which in turn is used to build 'uplinks', we cannot reuse 'uplinks' (recursion)

        # Since uplinks logic silently skips extra entries in uplink vars, we only need to parse shortest list.
        min_length = min(len(self.shared_utils.uplink_switch_interfaces), len(self.shared_utils.uplink_interfaces), len(self.shared_utils.uplink_switches))
        # Using set to only get unique uplink switches
        unique_uplink_switches = set(self.shared_utils.uplink_switches[:min_length])

        vrfs = set()
        for uplink_switch in unique_uplink_switches:
            uplink_switch_facts = self.shared_utils.get_peer_facts(uplink_switch)
            vrfs.update(uplink_switch_facts.shared_utils.vrfs)

        return natural_sort(vrfs) or None
