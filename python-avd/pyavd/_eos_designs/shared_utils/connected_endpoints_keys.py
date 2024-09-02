# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get

if TYPE_CHECKING:
    from . import SharedUtils


class ConnectedEndpointsKeysMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def connected_endpoints_keys(self: SharedUtils) -> list:
        """
        Return connected_endpoints_keys filtered for invalid entries and unused keys.

        NOTE: This method is called _before_ any schema validation, since we need to resolve connected_endpoints_keys dynamically
        """
        connected_endpoints_keys = []
        # Reading default value from schema
        default_connected_endpoint_keys = self.schema.get_default_value(["connected_endpoints_keys"])
        connected_endpoints_keys = get(self.hostvars, "connected_endpoints_keys", default=default_connected_endpoint_keys)
        return [entry for entry in connected_endpoints_keys if entry.get("key") is not None and self.hostvars.get(entry["key"]) is not None]
