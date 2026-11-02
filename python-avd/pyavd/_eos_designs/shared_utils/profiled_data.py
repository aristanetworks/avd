# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._utils.profiles import resolve_profile

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtilsProtocol


class ProfiledDataMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def dns_settings(self: SharedUtilsProtocol) -> EosDesigns.DnsSettings:
        """
        DNS settings with the node's `dns_settings_profile` resolved and merged in.

        If `dns_settings_profile` is not defined, the root-level `dns_settings` is returned.
        """
        if not self.node_config.dns_settings_profile:
            return self.inputs.dns_settings
        return resolve_profile(
            self.inputs.dns_settings,
            self.inputs.dns_settings_profiles,
            self.node_config.dns_settings_profile,
            target_name="dns_settings",
        )

    @cached_property
    def dns_settings_servers(self: SharedUtilsProtocol) -> EosDesigns.DnsSettings.Servers | None:
        """
        Return resolved DNS servers, or None if no servers are configured.

        Read without inserting a default empty list into the resolved DNS settings.
        """
        return self.dns_settings._get("servers") or None

    @cached_property
    def ntp_settings(self: SharedUtilsProtocol) -> EosDesigns.NtpSettings:
        """
        NTP settings with the node's `ntp_settings_profile` resolved and merged in.

        If `ntp_settings_profile` is not defined, the root-level `ntp_settings` is returned.
        """
        if not self.node_config.ntp_settings_profile:
            return self.inputs.ntp_settings

        return resolve_profile(
            self.inputs.ntp_settings,
            self.inputs.ntp_settings_profiles,
            self.node_config.ntp_settings_profile,
            target_name="ntp_settings",
        )
