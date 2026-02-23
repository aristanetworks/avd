# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# custom_modules/avd_overrides.py
from functools import cached_property

from pyavd.api.ip_addressing import AvdIpAddressing


class MyCustomIpAddressing(AvdIpAddressing):
    """Custom IP addressing that adds an offset to all loopback IPs."""

    @cached_property
    def _custom_offset(self) -> int:
        """Read a custom offset from hostvars."""
        return int(self._hostvars.get("custom_ip_offset", 0))

    def router_id(self) -> str:
        """Override router_id to add custom offset."""
        offset = self._id + self._loopback_ipv4_offset + self._custom_offset
        return self._ip(self._loopback_ipv4_pool, 32, offset, 0)

    def vtep_ip(self) -> str:
        """Override VTEP IP with custom offset."""
        offset = self._id + self._loopback_ipv4_offset + self._custom_offset
        return self._ip(self._vtep_loopback_ipv4_pool, 32, offset, 0)
