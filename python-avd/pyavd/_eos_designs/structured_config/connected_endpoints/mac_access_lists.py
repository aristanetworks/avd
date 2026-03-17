# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigConnectedEndpointsProtocol


class MacAccessListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_mac_acls(self: AvdStructuredConfigConnectedEndpointsProtocol, mac_acl: EosDesigns.MacAclsItem) -> None:
        acl = self.structured_config.mac_access_lists.obtain(mac_acl.name)
        for acl_entry in mac_acl.entries:
            action = [acl_entry.action, acl_entry.source, acl_entry.source_wildcard, acl_entry.destination, acl_entry.destination_wildcard]
            action = [act for act in action if act is not None]
            action = (" ").join(action)
            entry = EosCliConfigGen.MacAccessListsItem.EntriesItem(sequence=acl_entry.sequence, action=action)
            if entry not in acl.entries:
                acl.entries.append(entry)
