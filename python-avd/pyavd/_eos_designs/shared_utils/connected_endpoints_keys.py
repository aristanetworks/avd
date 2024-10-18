# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtils


class ConnectedEndpointsKeysMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def connected_endpoints_keys(self: SharedUtils) -> list[EosDesigns.ConnectedEndpointsKeysItem]:
        """Return connected_endpoints_keys filtered for invalid entries and unused keys."""
        used_connected_endpoints_keys = [entry.key for entry in self.inputs._dynamic_keys.connected_endpoints_keys]
        return [entry for entry in self.inputs.connected_endpoints_keys if entry.key in used_connected_endpoints_keys]
