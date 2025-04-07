# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils import default

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class LinkTrackingGroupsMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def link_tracking_groups(self: SharedUtilsProtocol) -> EosCliConfigGen.LinkTrackingGroups | None:
        if not self.node_config.link_tracking.enabled:
            return None

        link_tracking_groups = EosCliConfigGen.LinkTrackingGroups()
        default_recovery_delay = default(self.platform_settings.reload_delay.mlag, 300)
        for lt_group in self.node_config.link_tracking.groups:
            link_tracking_groups.append_new(
                name=lt_group.name,
                links_minimum=lt_group.links_minimum,
                recovery_delay=default(lt_group.recovery_delay, default_recovery_delay),
            )

        return link_tracking_groups
