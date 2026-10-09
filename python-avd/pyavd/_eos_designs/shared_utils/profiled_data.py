# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._utils.profiles import resolve_profile

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class ProfiledDataMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def dns_settings(self: SharedUtilsProtocol) -> EosDesigns.DnsSettings:
        """DNS settings with the node's dns_settings_profile resolved and merged in."""
        return resolve_profile(
            self.inputs.dns_settings or EosDesigns.DnsSettings(),
            self.inputs.dns_settings_profiles,
            self.node_config.dns_settings_profile,
        )
