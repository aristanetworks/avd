# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class DpsInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def dps_interfaces(self) -> list | None:
        """
        Returns structured config for dps_interfaces

        Only used for WAN devices
        """
        if not self.shared_utils.wan_role:
            return None

        dps1 = {
            "name": "Dps1",
            "description": "DPS Interface",
            "tcp_mss_ceiling": {
                "ipv4": get(self.shared_utils.switch_data_combined, "dps_mss_ipv4", default=1000),
            },
        }

        # TODO do IPv6 when needed - for now no easy way in AVD to detect if this is needed
        # When needed - need a default value if different than IPv4

        if self.shared_utils.cv_pathfinder_role:
            dps1["flow_tracker"] = {"hardware": "WAN-FLOW-TRACKER"}

        return [dps1]
