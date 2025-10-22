# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class NodeTypeKeysMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def node_type_key_data(self: SharedUtilsProtocol) -> EosDesigns.NodeTypeKeysItem:
        """node_type_key_data containing settings for this node_type."""
        for node_type_key in self.inputs.custom_node_type_keys:
            if node_type_key.type == self.type:
                return node_type_key._cast_as(EosDesigns.NodeTypeKeysItem)

        node_type_keys = self.inputs.node_type_keys
        for node_type_key in node_type_keys:
            if node_type_key.type == self.type:
                return node_type_key

        # This should never happen, as it should be caught during validation
        msg = f"Could not find the given type '{self.type}' in node_type_keys or custom_node_type_keys."
        raise AristaAvdInvalidInputsError(msg)
