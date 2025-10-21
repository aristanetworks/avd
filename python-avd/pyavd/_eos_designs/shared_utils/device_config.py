# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class DeviceConfigMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def role(self: SharedUtilsProtocol) -> str | None:
        if self.device_config:
            return self.device_config.role

        return None

    @cached_property
    def device_config(self: SharedUtilsProtocol) -> EosDesigns.DevicesItem | None:
        """Get device config and inherit from device profile and role."""
        if not (device_config := self.inputs.devices.get(self.hostname) or self.get_match_devices_item()):
            if not self.type:
                msg = (
                    f"Device '{self.hostname} does not exist under `devices`. Either set `type` or `default_types` for legacy node config or "
                    "add the device under `devices` or `match_devices` with new devices config."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)
            return None

        # Create a copy so we don't touch the original data.
        device_config = device_config._deepcopy()

        if device_config.profile:
            if not (device_profile := self.inputs.device_profiles.get(device_config.profile)):
                msg = f"Device Profile '{device_config.profile}' applied for the device '{self.hostname}' does not exist in `device_profiles`."
                raise AristaAvdInvalidInputsError(msg)

            device_config._deepinherit(device_profile._cast_as(EosDesigns.DevicesItem, ignore_extra_keys=True))

            if device_profile.parent_profile:
                if not (parent_profile := self.inputs.device_profiles.get(device_profile.parent_profile)):
                    msg = (
                        f"Device Profile '{device_profile.parent_profile}' applied as 'parent_profile' on the profile '{device_profile.name}' "
                        "does not exist in `device_profiles`."
                    )
                    raise AristaAvdInvalidInputsError(msg, host=self.hostname)

                device_config._deepinherit(parent_profile._cast_as(EosDesigns.DevicesItem, ignore_extra_keys=True))

        if not (role := device_config.role):
            msg = "Device Role is not set. 'role' must be set under 'devices[]' or inherited from a Device Profile."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if not (device_role := self.inputs.device_roles.get(role)):
            msg = f"Device Role '{self.role}' applied under 'devices' does not exist in `device_roles`."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        device_config._deepinherit(self.get_device_role_as_devices_item(device_role))

        return device_config

    @staticmethod
    def get_device_role_as_devices_item(device_role: EosDesigns.DeviceRolesItem) -> EosDesigns.DevicesItem:
        """Manually recasting the device_role to DevicesItem since we have default values we need to honor and the _cast_as will not do it."""
        device_role_as_dict = device_role._as_dict(include_default_values=True)
        # Remove keys that are not supported as node config.
        invalid_keys = (
            "mpls_lsr",
            "connected_endpoints",
            "evpn_encapsulation",
            "mlag_support",
            "network_services",
            "underlay_router",
            "underlay_routing_protocol",
            "overlay_routing_protocol",
            "custom_ip_addressing",
            "custom_interface_descriptions",
        )
        [device_role_as_dict.pop(key, None) for key in invalid_keys]
        return EosDesigns.DevicesItem._load(device_role_as_dict)

    def get_match_devices_item(self: SharedUtilsProtocol) -> EosDesigns.DevicesItem | None:
        """Return a DevicesItem built from the first MatchDevicesItem that matches our hostname. Returns None if no matches are found."""
        for match_device in self.inputs.match_devices:
            if re.fullmatch(match_device.hostname_pattern, self.hostname):
                devices_item = match_device._cast_as(EosDesigns.DevicesItem, ignore_extra_keys=True)
                devices_item.name = self.hostname
                return devices_item

        return None
