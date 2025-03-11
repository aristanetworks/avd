# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd.j2filters import list_compress

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class SpanningTreeMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def spanning_tree(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """spanning_tree priorities set per VLAN if spanning_tree mode is "rapid-pvst"."""
        if not self.shared_utils.network_services_l2:
            return

        spanning_tree_mode = self.shared_utils.node_config.spanning_tree_mode
        if spanning_tree_mode != "rapid-pvst":
            return

        default_priority = self.shared_utils.node_config.spanning_tree_priority

        vlan_stp_priorities = {}
        non_default_vlans = set()
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    if (priority := svi.spanning_tree_priority) is None:
                        continue
                    vlan_stp_priorities.setdefault(priority, set()).add(svi.id)
                    non_default_vlans.add(svi.id)
            for l2vlan in tenant.l2vlans:
                if (priority := l2vlan.spanning_tree_priority) is None:
                    continue
                vlan_stp_priorities.setdefault(priority, set()).add(l2vlan.id)
                non_default_vlans.add(l2vlan.id)

        if not non_default_vlans:
            # Quick return with only default
            self.structured_config.spanning_tree.rapid_pvst_instances.append_new(id="1-4094", priority=default_priority)
            return

        default_vlans = non_default_vlans.symmetric_difference(range(1, 4094))
        vlan_stp_priorities.setdefault(default_priority, set()).update(default_vlans)
        for priority, vlans in vlan_stp_priorities.items():
            self.structured_config.spanning_tree.rapid_pvst_instances.append_new(id=list_compress(list(vlans)), priority=priority)
