from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class PtpMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def ptp_enabled(self: SharedUtils) -> bool:
        default_ptp_enabled = get(self.hostvars, "ptp.enabled")
        return get(self.switch_data_combined, "ptp.enabled", default=default_ptp_enabled) is True

    @cached_property
    def ptp_profile_name(self: SharedUtils) -> str:
        default_ptp_profile = get(self.hostvars, "ptp.profile", default="aes67-r16-2016")
        return get(self.switch_data_combined, "ptp.profile", default_ptp_profile)

    @cached_property
    def ptp_profile(self: SharedUtils) -> dict:
        return get_item(self.ptp_profiles, "profile", self.ptp_profile_name, default={})

    @cached_property
    def ptp_profiles(self: SharedUtils) -> list:
        """
        Return ptp_profiles or []
        """
        return get(self.hostvars, "ptp_profiles", default=[])
