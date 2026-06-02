# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class StandardAccessListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def standard_access_lists(self: AvdStructuredConfigBaseProtocol) -> None:
        """Render every `standard_acls` entry from eos_designs as a `standard_access_lists` item."""
        for standard_acl in self.inputs.standard_acls:
            self.structured_config.standard_access_lists.append(standard_acl._cast_as(EosCliConfigGen.StandardAccessListsItem))
