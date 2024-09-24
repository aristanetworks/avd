# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get, get_item

if TYPE_CHECKING:
    from . import SharedUtils

DEFAULT_PTP_PROFILES = [
    {
        "profile": "aes67-r16-2016",
        "announce": {
            "interval": 0,
            "timeout": 3,
        },
        "delay_req": -3,
        "sync_message": {"interval": -3},
        "transport": "ipv4",
    },
    {
        "profile": "smpte2059-2",
        "announce": {
            "interval": -2,
            "timeout": 3,
        },
        "delay_req": -4,
        "sync_message": {"interval": -4},
        "transport": "ipv4",
    },
    {
        "profile": "aes67",
        "announce": {
            "interval": 2,
            "timeout": 3,
        },
        "delay_req": 0,
        "sync_message": {"interval": 0},
        "transport": "ipv4",
    },
]


class PtpMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def ptp_enabled(self: SharedUtils) -> bool:
        default_ptp_enabled = get(self.hostvars, "ptp_settings.enabled")
        return get(self.switch_data_combined, "ptp.enabled", default=default_ptp_enabled) is True

    @cached_property
    def ptp_mlag(self: SharedUtils) -> bool:
        return get(self.switch_data_combined, "ptp.mlag") is True

    @cached_property
    def ptp_profile_name(self: SharedUtils) -> str:
        default_ptp_profile = get(self.hostvars, "ptp_settings.profile", default="aes67-r16-2016")
        return get(self.switch_data_combined, "ptp.profile", default_ptp_profile)

    @cached_property
    def ptp_profile(self: SharedUtils) -> dict:
        return get_item(self.ptp_profiles, "profile", self.ptp_profile_name, default={})

    @cached_property
    def ptp_profiles(self: SharedUtils) -> list:
        """Return ptp_profiles."""
        return get(self.hostvars, "ptp_profiles", default=DEFAULT_PTP_PROFILES)
