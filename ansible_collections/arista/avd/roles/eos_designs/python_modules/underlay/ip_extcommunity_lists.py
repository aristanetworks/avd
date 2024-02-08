# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class IpExtCommunityListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ip_extcommunity_lists(self) -> list | None:
        """
        Return structured config for ip_extcommunity_lists
        """
        if self.shared_utils.underlay_routing_protocol != "ebgp":
            return None

        if self.shared_utils.is_cv_pathfinder_edge_or_transit:
            return [
                {
                    "name": "ECL-WAN-HA-SOO",
                    "entries": [
                        {
                            "type": "permit",
                            "extcommunities": f"soo {self.shared_utils.wan_bgp_soo}",
                        },
                    ],
                }
            ]

        return None
