from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item


class PtpMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to the SharedUtils class
    """

    hostvars: dict
    switch_data_combined: dict

    @cached_property
    def ptp_enabled(self) -> bool:
        default_ptp_enabled = get(self.hostvars, "ptp.enabled")
        return get(self.switch_data_combined, "ptp.enabled", default=default_ptp_enabled) is True

    @cached_property
    def ptp_profile_name(self) -> str:
        default_ptp_profile = get(self.hostvars, "ptp.profile", default="aes67-r16-2016")
        return get(self.switch_data_combined, "ptp.profile", default_ptp_profile)

    @cached_property
    def ptp_profile(self) -> dict:
        ptp_profiles = get(self.hostvars, "ptp_profiles", [])
        return get_item(ptp_profiles, "profile", self.ptp_profile_name, default={})
