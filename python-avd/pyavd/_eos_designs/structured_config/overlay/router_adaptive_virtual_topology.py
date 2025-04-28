# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class RouterAdaptiveVirtualTopologyMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_adaptive_virtual_topology(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for router adaptive-virtual-topology (AVT)."""
        if not self.shared_utils.is_cv_pathfinder_router:
            return

        # A Pathfinder has no region, zone, site info.
        if self.shared_utils.is_cv_pathfinder_server:
            self.structured_config.router_adaptive_virtual_topology.topology_role = "pathfinder"
            return

        if (wan_region := self.shared_utils.wan_region) is None:
            # Should never happen but just in case.
            msg = "Could not find 'cv_pathfinder_region' so it is not possible to generate config for router_adaptive_virtual_topology."
            raise AristaAvdInvalidInputsError(msg)

        if (wan_site := self.shared_utils.wan_site) is None:
            # Should never happen but just in case.
            msg = "Could not find 'cv_pathfinder_site' so it is not possible to generate config for router_adaptive_virtual_topology."
            raise AristaAvdInvalidInputsError(msg)

        # Edge or Transit
        self.structured_config.router_adaptive_virtual_topology._update(topology_role=self.shared_utils.cv_pathfinder_role, zone=self.shared_utils.wan_zone)
        self.structured_config.router_adaptive_virtual_topology.region._update(name=wan_region.name, id=wan_region.id)
        self.structured_config.router_adaptive_virtual_topology.site._update(name=wan_site.name, id=wan_site.id)
