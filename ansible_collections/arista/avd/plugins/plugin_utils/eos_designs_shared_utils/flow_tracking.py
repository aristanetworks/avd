# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class FlowTrackingMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def flow_tracker_settings(self: SharedUtils) -> str:
        return get(self.hostvars, "flow_tracking_settings", default={})

    @cached_property
    def default_flow_tracker_name(self: SharedUtils) -> str:
        return "FLOW-TRACKER"

    @cached_property
    def fabric_flow_tracking(self: SharedUtils):
        return get(self.hostvars, "fabric_flow_tracking", default={})

    def resolve_flow_tracker_name(self: SharedUtils, settings: dict | None,
        context_path: str) -> tuple[bool | None, str | None, str | None]:
        """
        Take flow_tracking object of a link, and perform validations.
        Return flow_tracker enabled, flow_tracker type, flow_tracker name
        """
        if settings is None:
            return None, None, None

        trackerEnabled = settings.get("enabled")
        trackerType = settings.get("type")
        trackerName = settings.get("name")

        raiseError = None
        if trackerType and not trackerName:
            raiseError = "type"
        if trackerName and not trackerType:
            raiseError = "name"
        if raiseError:
            raise AristaAvdError(f"Both type and name need to be configured for flow tracker but only '{raiseError}'" f" is configured for {context_path}.")
        return trackerEnabled, trackerType, trackerName

    def fabric_flow_tracking_data_model(self: SharedUtils, data_model: str) -> dict | None:
        """
        Return fabric level flow tracking settings for a data model
        """
        # By default, flow tracking is enabled only on DPS interfaces
        default = (data_model == "dps_interfaces")

        flow_tracking = self.fabric_flow_tracking.get(data_model)

        trackerEnabled, trackerType, trackerName = self.resolve_flow_tracker_name(flow_tracking, "")

        return {
            "enabled": trackerEnabled or default,
            "type": trackerType,
            "name": trackerName,
        }

    def get_flow_tracker(self: SharedUtils, link_settings: dict | None, data_model: str) -> dict:
        """
        Return flow_tracking settings for a link, falling back to the fabric flow_tracking_settings if not defined.
        """
        link_flow = {}
        if link_settings is not None:
            link_flow = get(link_settings, "flow_tracking", default={})

        link_tracker_enabled, link_tracker_type, link_tracker_name = self.resolve_flow_tracker_name(link_flow, "")

        fabric_flow = {}
        if (link_tracker_enabled is None) or (link_tracker_enabled and not link_tracker_type):
            fabric_flow = self.fabric_flow_tracking_data_model(data_model)

        trackingEnabled = link_tracker_enabled if link_tracker_enabled is not None else fabric_flow["enabled"]
        if not trackingEnabled:
            return None

        if link_tracker_type:
            return {link_tracker_type: link_tracker_name}
        elif fabric_flow.get("type"):
            return {fabric_flow.get("type"): fabric_flow.get("name")}
        else:
            return {"hardware": self.default_flow_tracker_name}
