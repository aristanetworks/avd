# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdMissingVariableError

if TYPE_CHECKING:
    from . import AvdStructuredConfigConnectedEndpointsProtocol


class MacAccessListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_mac_acl(self: AvdStructuredConfigConnectedEndpointsProtocol, acl_name: str) -> None:
        if acl_name not in self.inputs.mac_acls:
            msg = f"mac_acls[name={acl_name}]"
            raise AristaAvdMissingVariableError(msg, host=self.shared_utils.hostname)

        acl = EosCliConfigGen.MacAccessListsItem(name=acl_name)
        for index, acl_entry in enumerate(self.inputs.mac_acls[acl_name].entries):
            if acl_entry.source != "any" and not acl_entry.source_wildcard:
                msg = f"mac_acls[name={acl_name}].entries[{index}].source_wildcard"
                raise AristaAvdMissingVariableError(msg, host=self.shared_utils.hostname)

            if acl_entry.destination != "any" and not acl_entry.destination_wildcard:
                msg = f"mac_acls[name={acl_name}].entries[{index}].destination_wildcard"
                raise AristaAvdMissingVariableError(msg, host=self.shared_utils.hostname)

            action = [acl_entry.action, acl_entry.source, acl_entry.source_wildcard, acl_entry.destination, acl_entry.destination_wildcard]
            action = [word for word in action if word is not None]
            action = " ".join(action)
            entry = EosCliConfigGen.MacAccessListsItem.EntriesItem(sequence=acl_entry.sequence, action=action)
            acl.entries.append(entry)

        self.structured_config.mac_access_lists.append(acl)
