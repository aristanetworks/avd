# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.default import default
from pyavd._utils.format_string import AvdStringFormatter
from pyavd._utils.strip_empties import strip_null_from_data

if TYPE_CHECKING:
    from . import StructuredConfigUtilsProtocol


class SystemMixin(Protocol):
    """Utilities for resolving system MAC addresses during structured config generation."""

    @cached_property
    def custom_system_mac_address(self: StructuredConfigUtilsProtocol) -> str | None:
        """
        Return the rendered and validated custom system MAC address, or None if not set.

        The returned value preserves the original format (hhhh.hhhh.hhhh, hh:hh:hh:hh:hh:hh or hhhhhhhhhhhh).
        """
        custom_system_mac_address = default(self.shared_utils.node_config.custom_system_mac_address, self.inputs.custom_system_mac_address)
        if custom_system_mac_address is None:
            return None

        if default(self.shared_utils.node_config.system_mac_address, self.inputs.system_mac_address) is not None:
            msg = "'custom_system_mac_address' and 'system_mac_address' cannot both be set. Remove 'system_mac_address' when using 'custom_system_mac_address'."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        try:
            mac_address = AvdStringFormatter().format(
                custom_system_mac_address,
                **strip_null_from_data({"device_id": self.shared_utils.id, "hostname": self.shared_utils.hostname}),
            )
        except KeyError as error:
            field_name = error.args[0]
            if field_name == "device_id":
                msg = (
                    f"'custom_system_mac_address' uses formatter field 'device_id', but no AVD node ID could be resolved "
                    f"for host '{self.shared_utils.hostname}'. "
                    "Configure a node ID for this host or remove the field from the template."
                )
            else:
                msg = f"'custom_system_mac_address' uses unsupported formatter field '{field_name}'. Supported formatter fields are 'device_id' and 'hostname'."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname) from error

        pattern = (
            r"([0-9A-Fa-f][02468ACEace][0-9A-Fa-f]{2}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}"
            r"|[0-9A-Fa-f][02468ACEace](:[0-9A-Fa-f]{2}){5}"
            r"|[0-9A-Fa-f][02468ACEace][0-9A-Fa-f]{10})"
        )
        normalized = mac_address.replace(".", "").replace(":", "").lower()
        if not re.fullmatch(pattern, mac_address) or normalized == "0" * 12:
            msg = (
                f"'custom_system_mac_address' rendered '{mac_address}' which is not a valid unicast EOS system MAC address. "
                "The value must be a unicast MAC address in 'hhhh.hhhh.hhhh', 'hh:hh:hh:hh:hh:hh' or 'hhhhhhhhhhhh' format."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        return mac_address

    @cached_property
    def system_mac_address(self: StructuredConfigUtilsProtocol) -> str | None:
        """
        system_mac_address.

        system_mac_address is inherited from
        Host variable var custom_system_mac_address ->
            Fabric Topology data model system_mac_address ->
                Host variable var system_mac_address ->.

        When custom_system_mac_address is set the value is normalized to hh:hh:hh:hh:hh:hh format.
        """
        if (custom := self.custom_system_mac_address) is not None:
            raw = custom.replace(".", "").replace(":", "")
            return ":".join(raw[i : i + 2] for i in range(0, 12, 2))

        return default(self.shared_utils.node_config.system_mac_address, self.inputs.system_mac_address)
