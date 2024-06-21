# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import search
from typing import TYPE_CHECKING

from ..._utils import default, get

if TYPE_CHECKING:
    from . import SharedUtils

# Campus platforms are separated out by their ability to support "trident_forwarding_table_partition".
# This is required for EVPN multicast, currently only supported on all 720XP platforms.
# This command is not supported on 710P or 722XP platforms.  720D range has some devices that support this
# and others that don't, but I've grouped them all together as none of them support EVPN multicast.
DEFAULT_PLATFORM_SETTINGS = [
    {
        "platforms": ["default"],
        "reload_delay": {"mlag": 300, "non_mlag": 330},
        "feature_support": {
            "queue_monitor_length_notify": False,
        },
    },
    {
        "platforms": ["7050X3"],
        "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072",
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
        "feature_support": {
            "queue_monitor_length_notify": False,
        },
    },
    {
        "platforms": ["720XP"],
        "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072",
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
        "feature_support": {"queue_monitor_length_notify": False, "poe": True},
    },
    {
        "platforms": ["750", "755", "758"],
        "management_interface": "Management0",
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
        "feature_support": {"queue_monitor_length_notify": False, "poe": True},
    },
    {
        "platforms": ["720DP", "722XP", "710P"],
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
        "feature_support": {"queue_monitor_length_notify": False, "poe": True},
    },
    {
        "platforms": ["7010TX"],
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
        "feature_support": {"queue_monitor_length_notify": False, "per_interface_mtu": False},
    },
    {
        "platforms": ["7280R", "7280R2", "7020R"],
        "tcam_profile": "vxlan-routing",
        "lag_hardware_only": True,
        "reload_delay": {
            "mlag": 900,
            "non_mlag": 1020,
        },
    },
    {
        "platforms": ["7280R3"],
        "reload_delay": {
            "mlag": 900,
            "non_mlag": 1020,
        },
    },
    {
        "platforms": ["7500R", "7500R2"],
        "tcam_profile": "vxlan-routing",
        "lag_hardware_only": True,
        "management_interface": "Management0",
        "reload_delay": {
            "mlag": 900,
            "non_mlag": 1020,
        },
    },
    {
        "platforms": ["7500R3", "7800R3"],
        "management_interface": "Management0",
        "reload_delay": {
            "mlag": 900,
            "non_mlag": 1020,
        },
    },
    {
        "platforms": ["7358X4"],
        "management_interface": "Management1/1",
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
        "feature_support": {
            "queue_monitor_length_notify": False,
            "interface_storm_control": True,
            "bgp_update_wait_for_convergence": True,
            "bgp_update_wait_install": False,
        },
    },
    {
        "platforms": ["7368X4"],
        "management_interface": "Management0",
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
    },
    {
        "platforms": ["7300X3"],
        "management_interface": "Management0",
        "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072",
        "reload_delay": {
            "mlag": 1200,
            "non_mlag": 1320,
        },
    },
    {
        "platforms": ["VEOS", "VEOS-LAB", "vEOS", "vEOS-lab"],
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
        "feature_support": {
            "queue_monitor_length_notify": False,
            "interface_storm_control": False,
            "bgp_update_wait_for_convergence": False,
            "bgp_update_wait_install": False,
        },
    },
    {
        "platforms": ["CEOS", "cEOS", "ceos", "cEOSLab"],
        "management_interface": "Management0",
        "reload_delay": {
            "mlag": 300,
            "non_mlag": 330,
        },
        "feature_support": {
            "queue_monitor_length_notify": False,
            "interface_storm_control": False,
            "bgp_update_wait_for_convergence": False,
            "bgp_update_wait_install": False,
        },
    },
    {
        "platforms": ["AWE-5310", "AWE-5510", "AWE-7250R", "AWE-7230R"],
        "management_interface": "Management1/1",
        "feature_support": {
            "queue_monitor_length_notify": False,
            "interface_storm_control": False,
            "bgp_update_wait_for_convergence": True,
            "bgp_update_wait_install": False,
        },
    },
    {
        "platforms": ["AWE-7220R"],
        "management_interface": "Management1",
        "feature_support": {
            "queue_monitor_length_notify": False,
            "interface_storm_control": False,
            "bgp_update_wait_for_convergence": True,
            "bgp_update_wait_install": False,
            "poe": True,
        },
    },
]


class PlatformMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def platform(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "platform", default=self.cv_topology_platform)

    @cached_property
    def platform_settings(self: SharedUtils) -> dict:
        platform_settings = get(self.hostvars, "platform_settings", default=DEFAULT_PLATFORM_SETTINGS)

        # First look for a matching platform setting specifying our platform
        for platform_setting in platform_settings:
            if self.platform in platform_setting.get("platforms", []):
                return platform_setting

        # If not found, then look for a default platform setting
        for platform_setting in platform_settings:
            if "default" in platform_setting.get("platforms", []):
                return platform_setting

        return {}

    @cached_property
    def default_interfaces(self: SharedUtils) -> dict:
        """
        default_interfaces set based on default_interfaces
        """
        default_interfaces = get(self.hostvars, "default_interfaces", default=[])

        device_platform = default(self.platform, "default")

        # First look for a matching default interface set that matches our platform and type
        for default_interface in default_interfaces:
            for platform in default_interface.get("platforms", []):
                if search(f"^{platform}$", device_platform) and self.type in default_interface.get("types", []):
                    return default_interface

        # If not found, then look for a default default_interface that matches our type
        for default_interface in default_interfaces:
            for platform in default_interface.get("platforms", []):
                if search(f"^{platform}$", "default") and self.type in default_interface.get("types", []):
                    return default_interface

        return {}

    @cached_property
    def platform_settings_feature_support_interface_storm_control(self) -> bool:
        return get(self.platform_settings, "feature_support.interface_storm_control", default=True) is True

    @cached_property
    def platform_settings_feature_support_queue_monitor_length_notify(self) -> bool:
        return get(self.platform_settings, "feature_support.queue_monitor_length_notify", default=True) is True

    @cached_property
    def platform_settings_feature_support_poe(self) -> bool:
        return get(self.platform_settings, "feature_support.poe", default=False) is True

    @cached_property
    def platform_settings_feature_support_per_interface_mtu(self) -> bool:
        return get(self.platform_settings, "feature_support.per_interface_mtu", default=True) is True
