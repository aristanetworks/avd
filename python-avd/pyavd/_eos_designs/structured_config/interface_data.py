# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from ipaddress import IPv4Address, IPv6Address


@dataclass(frozen=True)
class InterfaceData:
    """Common data associated with a structured-config interface."""

    interface: str
    context: str
    interface_ip: IPv4Address | None = None
    interface_ipv6: IPv6Address | None = None
