# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations
from typing import TYPE_CHECKING, Protocol
from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from . import AvdStructuredConfigConnectedEndpointsProtocol


class MacAccessListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """
    def _set_mac_acls(self: AvdStructuredConfigConnectedEndpointsProtocol, mac_acl:str) -> None:
        acl = self.inputs.mac_acls[mac_acl]
        self.structured_config.mac_access_lists.append(acl._cast_as(EosCliConfigGen.MacAccessListsItem))
