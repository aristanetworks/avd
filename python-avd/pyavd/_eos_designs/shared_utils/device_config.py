# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.default import default

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class DeviceConfigMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def device_config(self: SharedUtilsProtocol) -> EosDesigns.DevicesItem | None:
        """
        Get device config and inherit from device profile.

        If there is no device config we still check for the global 'device_profile' and inherit from that.
        """
        if self.hostname not in self.inputs.devices and not self.inputs.device_profile:
            return None

        # Create a copy so we don't touch the original data.
        device_config = self.inputs.devices.get(self.hostname, EosDesigns.DevicesItem())._deepcopy()
        if not (device_profile_name:=default(device_config.profile, self.inputs.device_profile)):
            return device_config

        if not (device_profile := self.inputs.device_profiles.get(device_profile_name)):
            msg = f"The Device Profile '{device_profile_name}' applied for the device '{self.hostname}' does not exist under `device_profiles`."
            raise AristaAvdInvalidInputsError(msg)

        device_profiles_chain = EosDesigns.DeviceProfiles()
        device_profile = self.inputs.device_profiles[device_profile_name]._deepcopy()
        resolved_profile = self.inputs.device_profiles[device_profile_name]._deepcopy()
        if self.inputs.avd_design_future.allow_infinite_profile_inheritance:
            while device_profile.parent_profile is not None:
                if not (device_parent_profile := self.inputs.device_profiles.get(device_profile.parent_profile)):
                    msg = f"The Device Profile '{device_profile.parent_profile}' applied for the device '{self.hostname}' does not exist under `device_profiles`."
                    raise AristaAvdInvalidInputsError(msg)
                if device_profile.parent_profile in device_profiles_chain or device_profile.parent_profile == device_profile_name:
                    msg = (
                        f"Circular profile dependency detected: Profile '{device_profile.parent_profile}' "
                        f"cannot be assigned as the parent of '{device_profile.name}' because it would create a loop."
                    )
                    raise AristaAvdInvalidInputsError(msg)
                parent_profile = device_parent_profile._deepcopy()
                device_profiles_chain.append(parent_profile)
                device_profile = parent_profile

            for profile in device_profiles_chain:
                resolved_profile = resolved_profile._deepinherited(profile)
            device_config._deepinherit(resolved_profile._cast_as(EosDesigns.DevicesItem, ignore_extra_keys=True))
            return device_config

        if device_profile.parent_profile:
            if not (parent_profile := self.inputs.device_profiles.get(device_profile.parent_profile)):
                msg = (
                    f"Device Profile '{device_profile.parent_profile}' applied as 'parent_profile' on the profile '{device_profile.name}' "
                    "does not exist under 'device_profiles'."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)
            resolved_profile._deepinherit(parent_profile)

        device_config._deepinherit(resolved_profile._cast_as(EosDesigns.DevicesItem, ignore_extra_keys=True))
        return device_config
