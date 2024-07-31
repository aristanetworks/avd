# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get

if TYPE_CHECKING:
    from . import SharedUtils


class LinkTrackingGroupsMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def link_tracking_groups(self: SharedUtils) -> list | None:
        if get(self.switch_data_combined, "link_tracking.enabled") is True:
            link_tracking_groups = []
            default_recovery_delay = get(self.platform_settings, "reload_delay.mlag", 300)
            lt_groups = get(self.switch_data_combined, "link_tracking.groups", default=[])

            if len(lt_groups) > 0:
                for lt_group in lt_groups:
                    lt_group["recovery_delay"] = lt_group.get("recovery_delay", default_recovery_delay)
                    link_tracking_groups.append(lt_group)
            else:
                link_tracking_groups.append({"name": "LT_GROUP1", "recovery_delay": default_recovery_delay})

            return link_tracking_groups

        return None
