# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class ManagementSecurityMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def management_security(self) -> dict | None:
        if not self.shared_utils.stun_ssl_profiles():
            return None

        management_security = {}
        ssl_profiles = []
        ssl_profiles.extend(self._get_stun_ssl_profiles())

        if ssl_profiles:
            management_security["ssl_profiles"] = ssl_profiles

        return management_security

    def _get_stun_ssl_profiles(self) -> list:
        ssl_profiles = self.shared_utils.stun_ssl_profiles()
        stun_ssl_profiles = []
        for ssl_profile in ssl_profiles:
            stun_ssl_profiles.append(
                {
                    "name": ssl_profile,
                    "certificate": {
                        "file": ssl_profile + ".crt",
                        "key": ssl_profile + ".key",
                    },
                    "trust_certificate": {"certificates": ["aristaDeviceCertProvisionerDefaultRootCA.crt"]},
                }
            )
        return stun_ssl_profiles
