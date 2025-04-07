# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFactsProtocol
from pyavd._utils import remove_cached_property_type

if TYPE_CHECKING:
    from . import EosDesignsFactsGeneratorProtocol


class WanMixin(EosDesignsFactsProtocol, Protocol):
    """
    Mixin Class providing a subset of EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @remove_cached_property_type
    @cached_property
    def wan_path_groups(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.WanPathGroups:
        """
        Return the list of WAN path_groups directly connected to this router.

        Each with a list of dictionaries containing the (interface, ip_address) in the path_group.

        TODO: Also add the path_groups importing any of our connected path groups.
              Need to find out if we need to resolve recursive imports.
        """
        wan_path_groups = EosDesignsFactsProtocol.WanPathGroups()
        if not self.shared_utils.is_wan_router:
            return wan_path_groups

        for wan_local_path_group in self.shared_utils.wan_local_path_groups:
            wan_path_group = wan_local_path_group._cast_as(EosDesignsFactsProtocol.WanPathGroupsItem)
            for local_interface in wan_local_path_group._internal_data.interfaces:
                wan_path_group.interfaces.append_new(
                    name=local_interface["name"],
                    connected_to_pathfinder=local_interface["connected_to_pathfinder"],
                    public_ip=local_interface.get("public_ip"),
                    wan_circuit_id=local_interface.get("wan_circuit_id"),
                )
            wan_path_groups.append(wan_path_group)

        return wan_path_groups
