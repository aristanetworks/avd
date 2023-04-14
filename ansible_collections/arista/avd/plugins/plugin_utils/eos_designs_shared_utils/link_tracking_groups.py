from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class LinkTrackingGroupsMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    """

    hostvars: dict
    switch_data_combined: dict

    @cached_property
    def link_tracking_groups(self) -> list | None:
        if get(self.switch_data_combined, "link_tracking.enabled") is True:
            link_tracking_groups = []
            default_recovery_delay = get(self.hostvars, "switch.reload_delay.mlag", 300)
            lt_groups = get(self.switch_data_combined, "link_tracking.groups", default=[])

            if len(lt_groups) > 0:
                for lt_group in lt_groups:
                    lt_group["recovery_delay"] = lt_group.get("recovery_delay", default_recovery_delay)
                    link_tracking_groups.append(lt_group)
            else:
                link_tracking_groups.append({"name": "LT_GROUP1", "recovery_delay": default_recovery_delay})

            return link_tracking_groups

        return None
