# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigMetadataProtocol


class UtilsMixin(Protocol):
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class or other Mixins.
    """

    def get_resolved_validation_profile(self: AvdStructuredConfigMetadataProtocol, profile_name: str) -> EosDesigns.ValidationProfilesItem:
        """
        Return a fully resolved validation profile.

        The validation profile is resolved as follows:
        * Verify that the requested validation profile exists.
        * If a parent profile is defined, verify that the parent profile exists.
        * Deep-inherit the profile from its parent profile.
        * Remove the `parent_profile` attribute from the resolved profile to
        prevent further inheritance processing.

        Args:
            profile_name: Name of the validation profile applied under the node
                configuration.

        Returns:
            The resolved validation profile with inheritance applied.

        Raises:
            AristaAvdInvalidInputsError: If the validation profile or its parent
                profile is not defined under `inputs.validation_profiles`.
        """
        validation_profiles = self.inputs.validation_profiles

        if profile_name not in validation_profiles:
            msg = f"Validation profile '{profile_name}' referenced in node configuration is not defined under 'validation_profiles'."
            raise AristaAvdInvalidInputsError(msg)

        validation_profile = validation_profiles[profile_name]

        if (parent_name := validation_profile.parent_profile) is not None:
            if parent_name not in validation_profiles:
                msg = f"Parent validation profile '{parent_name}' referenced by validation profile '{profile_name}' is not defined under 'validation_profiles'."
                raise AristaAvdInvalidInputsError(msg)

            parent_profile = validation_profiles[parent_name]
            validation_profile = validation_profile._deepinherited(parent_profile)

        # Remove parent_profile after resolution to avoid re-processing inheritance
        delattr(validation_profile, "parent_profile")

        return validation_profile
