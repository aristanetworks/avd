# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class FlowTrackingMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def flow_tracking(self) -> dict | None:
        """
        Return structured config for flow_tracking

        TODO: Make this configurable.
        """
        if not self.shared_utils.cv_pathfinder_role:
            return None

        return {
            "hardware": {
                "trackers": [
                    {
                        "name": "WAN-FLOW-TRACKER",
                        "record_export": {"on_inactive_timeout": 70000, "on_interval": 5000},
                        "exporters": [{"name": "DPI-EXPORTER", "collector": {"host": "127.0.0.1"}, "local_interface": "Loopback0", "template_interval": 5000}],
                    }
                ],
                "shutdown": False,
            },
        }
