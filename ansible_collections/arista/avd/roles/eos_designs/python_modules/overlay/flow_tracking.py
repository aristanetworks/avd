# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

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
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        flow_tracking = get(self._hostvars, "flow_tracking_settings", default={})
        exporter_name = get(flow_tracking, "exporter.name", default="DPI-EXPORTER")
        template_interval = get(flow_tracking, "exporter.template_interval", default=3000000)
        on_inactive_timeout = get(flow_tracking, "record_export.on_inactive_timeout", default=70000)
        on_interval = get(flow_tracking, "record_export.on_interval", default=300000)
        return {
            "hardware": {
                "trackers": [
                    {
                        "name": self.shared_utils.wan_flow_tracker_name,
                        "record_export": {"on_inactive_timeout": on_inactive_timeout, "on_interval": on_interval},
                        "exporters": [
                            {"name": exporter_name, "collector": {"host": "127.0.0.1"}, "local_interface": "Loopback0", "template_interval": template_interval}
                        ],
                    }
                ],
                "shutdown": False,
            },
        }
