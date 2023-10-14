# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import ipaddress

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError


def get_ip_from_pool(pool: str, prefixlen: int, subnet_offset: int, ip_offset: int) -> str:
    """
    get_ip_from_pool returns one IP address from given pool.

    Parameters
    ----------
    pool : IP pool in string format, example: "1.2.3.4/24"
    prefixlen : Integer
    subnet_offset : Integer
    ip_offset : Integer

    Returns
    -------
    IP address
    """

    pool_network = ipaddress.ip_network(pool, strict=False)
    prefixlen_diff = prefixlen - pool_network.prefixlen

    try:
        subnet_size = (int(pool_network.hostmask) + 1) >> prefixlen_diff
    except ValueError as e:
        raise AristaAvdError(f"Prefix length {prefixlen} is smaller than pool network prefix length {pool_network.prefixlen}") from e

    if (subnet_offset + 1) * subnet_size > pool_network.num_addresses:
        raise AristaAvdError(f"Unable to get {subnet_offset + 1} /{prefixlen} subnets from pool {pool}")

    subnet = ipaddress.ip_network((int(pool_network.network_address) + subnet_offset * subnet_size, prefixlen))

    try:
        ip = subnet[ip_offset]
    except IndexError as e:
        raise AristaAvdError(f"Unable to get {ip_offset+1} hosts in subnet {subnet} taken from pool {pool}") from e

    return str(ip)
