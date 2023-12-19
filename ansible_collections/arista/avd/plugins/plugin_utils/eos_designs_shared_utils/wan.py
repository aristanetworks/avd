# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class WanMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_mode(self: SharedUtils) -> str | None:
        return get(self.hostvars, "wan_mode", default="cv-pathfinder")

    @cached_property
    def wan_role(self: SharedUtils) -> str | None:
        if self.underlay_router is False or self.wan_mode is None:
            return None

        default_wan_role = get(self.node_type_key_data, "default_wan_role", default=None)
        wan_role = get(self.switch_data_combined, "wan_role", default=default_wan_role)
        if wan_role is not None and self.overlay_routing_protocol != "ibgp":
            raise AristaAvdError("Only 'ibgp' is supported as 'overlay_routing_protocol' for WAN nodes.")
        if wan_role == "server" and self.evpn_role != "server":
            raise AristaAvdError("'wan_role' server requires 'evpn_role' server.")
        if wan_role == "client" and self.evpn_role != "client":
            raise AristaAvdError("'wan_role' client requires 'evpn_role' client.")
        return wan_role

    @cached_property
    def cv_pathfinder_role(self: SharedUtils) -> str | None:
        if self.underlay_router is False or self.wan_mode != "cv-pathfinder":
            return None

        default_cv_pathfinder_role = get(self.node_type_key_data, "default_cv_pathfinder_role", default=None)
        cv_pathfinder_role = get(self.switch_data_combined, "cv_pathfinder_role", default=default_cv_pathfinder_role)
        if cv_pathfinder_role == "pathfinder" and self.wan_role != "server":
            raise AristaAvdError("'wan_role' must be 'server' when 'cv_pathfinder_role' is set to 'pathfinder'")
        if cv_pathfinder_role in ["transit", "edge"] and self.wan_role != "client":
            raise AristaAvdError("'wan_role' must be 'client' when 'cv_pathfinder_role' is set to 'transit' or 'edge'")
        return cv_pathfinder_role
