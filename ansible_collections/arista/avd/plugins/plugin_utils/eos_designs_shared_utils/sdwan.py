# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class SdwanMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_mode(self: SharedUtils) -> str | None:
        return get(self.hostvars, "wan_mode", default=None)

    @cached_property
    def wan_role(self: SharedUtils) -> str | None:
        if self.underlay_router is True and self.wan_mode is not None:
            default_wan_role = get(self.node_type_key_data, "default_wan_role", default=None)
            return get(self.switch_data_combined, "wan_role", default=default_wan_role)
        return None

    @cached_property
    def sdwan_role(self: SharedUtils) -> str | None:
        if self.underlay_router is True and self.wan_mode == "sdwan":
            default_sdwan_role = get(self.node_type_key_data, "default_sdwan_role", default=None)
            return get(self.switch_data_combined, "sdwan_role", default=default_sdwan_role)
        return None
