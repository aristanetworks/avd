from __future__ import annotations

from functools import cached_property
from re import search
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class PlatformMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def platform(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "platform")

    @cached_property
    def platform_settings(self: SharedUtils) -> dict:
        platform_settings = get(self.hostvars, "platform_settings", default=[])

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
