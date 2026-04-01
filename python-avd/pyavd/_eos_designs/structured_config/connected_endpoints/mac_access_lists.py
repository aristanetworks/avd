# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError

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

        if acl_name in self.structured_config.mac_access_lists:
            return

        acl = EosCliConfigGen.MacAccessListsItem(name=acl_name)
        mac_acl = self.inputs.mac_acls[acl_name]
        acl.counters_per_entry = mac_acl.counters_per_entry
        for index, acl_entry in enumerate(mac_acl.entries):
            action = ""
            if acl_entry.remark:
                action += f"remark {acl_entry.remark}"
            elif acl_entry.action and acl_entry.source:
                if acl_entry.source != "any" and not acl_entry.source_wildcard:
                    msg = f"mac_acls[name={acl_name}].entries[{index}].source_wildcard"
                    raise AristaAvdMissingVariableError(msg, host=self.shared_utils.hostname)

                if not acl_entry.destination:
                    msg = f"mac_acls[name={acl_name}].entries[{index}].destination"
                    raise AristaAvdMissingVariableError(msg, host=self.shared_utils.hostname)

                if acl_entry.destination != "any" and not acl_entry.destination_wildcard:
                    msg = f"mac_acls[name={acl_name}].entries[{index}].destination_wildcard"
                    raise AristaAvdMissingVariableError(msg, host=self.shared_utils.hostname)

                if acl_entry.source == "any" and acl_entry.source_wildcard:
                    msg = (
                        f"Can not set 'mac_acls[name={acl_name}].entries[{index}].source_wildcard' when source is 'any' for host {self.shared_utils.hostname}."
                    )
                    raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

                if acl_entry.destination == "any" and acl_entry.destination_wildcard:
                    msg = (
                        f"Can not set 'mac_acls[name={acl_name}].entries[{index}].destination_wildcard' when destination is 'any'"
                        f" for host {self.shared_utils.hostname}."
                    )
                    raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

                action += acl_entry.action
                action = action + " " + acl_entry.source
                if acl_entry.source_wildcard:
                    action = action + " " + acl_entry.source_wildcard

                action = action + " " + acl_entry.destination
                if acl_entry.destination_wildcard:
                    action = action + " " + acl_entry.destination_wildcard

            entry = EosCliConfigGen.MacAccessListsItem.EntriesItem(sequence=acl_entry.sequence, action=action)
            acl.entries.append(entry)

        self.structured_config.mac_access_lists.append(acl)
