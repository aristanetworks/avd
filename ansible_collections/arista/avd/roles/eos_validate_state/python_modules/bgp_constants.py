# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

BGP_ADDRESS_FAMILIES = [
    {"afi": "evpn", "safi": None, "description": "EVPN"},
    {"afi": "path-selection", "safi": None, "description": "Path-Selection"},
    {"afi": "link-state", "safi": None, "description": "Link-State"},
    {"afi": "ipv4", "safi": "unicast", "description": "IPv4 Unicast"},
    {"afi": "ipv6", "safi": "unicast", "description": "IPv6 Unicast"},
    {"afi": "ipv4", "safi": "sr-te", "description": "IPv4 SR-TE"},
    {"afi": "ipv6", "safi": "sr-te", "description": "IPv6 SR-TE"},
]
"""
List of dictionaries that map the BGP address family identifier (AFI) and the subsequent address family identifier (SAFI) for validation
and description as formatted input messages in the report.
"""
