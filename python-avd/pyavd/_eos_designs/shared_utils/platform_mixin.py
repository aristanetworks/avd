# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import search
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._utils import default

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class PlatformMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def platform(self: SharedUtilsProtocol) -> str | None:
        if self.digital_twin:
            return self.digital_twin_platform
        return self.original_platform

    @cached_property
    def original_platform(self: SharedUtilsProtocol) -> str | None:
        return default(self.node_config.platform, self.cv_topology_platform)

    @cached_property
    def digital_twin_platform(self: SharedUtilsProtocol) -> str | None:
        return default(self.get_platform_settings(self.original_platform).digital_twin.platform, self.original_platform)

    @cached_property
    def platform_settings(self: SharedUtilsProtocol) -> EosDesigns.PlatformSettingsItem | EosDesigns.CustomPlatformSettingsItem:
        return self.get_platform_settings(self.platform)

    def get_platform_settings(self: SharedUtilsProtocol, platform: str | None) -> EosDesigns.PlatformSettingsItem | EosDesigns.CustomPlatformSettingsItem:
        # First look for a matching platform setting specifying our platform
        if platform is not None:
            for platform_setting in self.inputs.custom_platform_settings:
                if platform in platform_setting.platforms:
                    return platform_setting
            for platform_setting in self.inputs.platform_settings:
                if platform in platform_setting.platforms:
                    return platform_setting

        # If not found, then look for a default platform setting
        for platform_setting in self.inputs.custom_platform_settings:
            if "default" in platform_setting.platforms:
                return platform_setting
        for platform_setting in self.inputs.platform_settings:
            if "default" in platform_setting.platforms:
                return platform_setting

        return EosDesigns.PlatformSettingsItem()

    @cached_property
    def default_interfaces(self: SharedUtilsProtocol) -> EosDesigns.DefaultInterfacesItem:
        """default_interfaces set based on default_interfaces."""
        if self.digital_twin and self.inputs.digital_twin.use_default_interfaces_of_digital_twin_platform:
            device_platform = self.platform or "default"
        else:
            device_platform = self.original_platform or "default"

        # First look for a matching default interface set that matches our platform and type
        for default_interface in self.inputs.default_interfaces:
            for platform in default_interface.platforms:
                if search(f"^{platform}$", device_platform) and self.type in default_interface.types:
                    return default_interface

        # If not found, then look for a default default_interface that matches our type
        for default_interface in self.inputs.default_interfaces:
            for platform in default_interface.platforms:
                if search(f"^{platform}$", "default") and self.type in default_interface.types:
                    return default_interface

        return EosDesigns.DefaultInterfacesItem()
