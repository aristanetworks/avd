# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

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

        if device_profile_name := default(device_config.profile, self.inputs.device_profile):
            if not (device_profile := self.inputs.device_profiles.get(device_profile_name)):
                msg = f"The Device Profile '{device_profile_name}' applied for the device '{self.hostname}' does not exist under `device_profiles`."
                raise AristaAvdInvalidInputsError(msg)

            device_config._deepinherit(device_profile._cast_as(EosDesigns.DevicesItem, ignore_extra_keys=True))

            if device_profile.parent_profile:
                if not (parent_profile := self.inputs.device_profiles.get(device_profile.parent_profile)):
                    msg = (
                        f"Device Profile '{device_profile.parent_profile}' applied as 'parent_profile' on the profile '{device_profile.name}' "
                        "does not exist under 'device_profiles'."
                    )
                    raise AristaAvdInvalidInputsError(msg, host=self.hostname)

                device_config._deepinherit(parent_profile._cast_as(EosDesigns.DevicesItem, ignore_extra_keys=True))

        return device_config
