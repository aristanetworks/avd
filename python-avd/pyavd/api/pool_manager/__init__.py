# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from yaml import CSafeDumper

from .ipv4_interface_pools import IPv4InterfacePoolCollection
from .node_id_pools import NodeIdPoolCollection

if TYPE_CHECKING:
    from ipaddress import IPv4Interface, IPv4Network
    from pathlib import Path

    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol

    from .base_classes import Pool, PoolCollection

NODE_ID_POOLS = "node_id_pools"
IPV4_INTERFACE_POOLS = "ipv4_interface_pools"

PoolType = Literal["node_id_pools", "ipv4_interface_pools"]


class PoolManager:
    """
    Class used to handle pooled resources.

    This class is imported and initialized once in eos_designs_facts
    and given to shared_utils for each device.
    """

    _output_dir: Path
    _pool_collections: dict[PoolType, dict[Path, PoolCollection]]
    """PoolCollection collections keys by file path."""

    def __init__(self, output_dir: Path) -> None:
        self._output_dir = output_dir
        self._pool_collections = {}
        self._changed_pool_files = {}

    def save_updated_pools(self, dumper_cls: type = CSafeDumper) -> bool:
        """
        Save data if anything changed. Returns a boolean telling if anything was changed.

        Note that this will also prune any unused/stale allocations (not requested for since initialization) and remove empty pools.
        """
        any_changes = False
        for pools_files_map in self._pool_collections.values():
            changes_for_this_pool_type = [pool_collection.save_updates(dumper_cls) for pool_collection in pools_files_map.values()]
            any_changes = any_changes or any(changes_for_this_pool_type)
        return any_changes

    def get_node_id_pool(self, shared_utils: SharedUtilsProtocol) -> Pool[int]:
        """Returns the node id pool for this device. Pool will be autocreated if missing."""
        pools_files_map = self._pool_collections.setdefault(NODE_ID_POOLS, {})
        pools_file = NodeIdPoolCollection._pools_file_from_shared_utils(self._output_dir, shared_utils)

        if pools_file not in pools_files_map:
            # Not using setdefault since initializing the pool will read from file.
            pools_files_map[pools_file] = NodeIdPoolCollection(pools_file=pools_file)
        pool_collection = pools_files_map[pools_file]

        pool_key = NodeIdPoolCollection.get_pool_key(shared_utils)
        return pool_collection.get_pool(pool_key)

    def get_node_id_assignment(self, shared_utils: SharedUtilsProtocol, requested_value: int | None = None) -> int:
        """
        Returns the assigned node id for this device. Assignment and pool will be autocreated if missing.

        Args:
            shared_utils: Instance of SharedUtils for the device.
            requested_value: A requested value to assign to the device if available. Existing assignment will be changed if possible.
                There are no guarantees that this value will be assigned, so the caller should check and handle accordingly.
        """
        pool = self.get_node_id_pool(shared_utils)
        key = NodeIdPoolCollection.get_assignment_key(shared_utils)
        return pool.get_assignment(key, requested_value).value

    def get_ipv4_interface_pool(self, subnet: IPv4Network, prefix_size: int, shared_utils: SharedUtilsProtocol) -> Pool[IPv4Interface]:
        """Returns the node id pool for this device. Pool will be autocreated if missing."""
        pools_files_map = self._pool_collections.setdefault(IPV4_INTERFACE_POOLS, {})
        pools_file = IPv4InterfacePoolCollection._pools_file_from_shared_utils(self._output_dir, shared_utils)

        if pools_file not in pools_files_map:
            # Not using setdefault since initializing the pool will read from file.
            pools_files_map[pools_file] = IPv4InterfacePoolCollection(pools_file=pools_file)
        pool_collection = pools_files_map[pools_file]

        pool_key = IPv4InterfacePoolCollection.get_pool_key(subnet, prefix_size)
        return pool_collection.get_pool(pool_key)

    def get_ipv4_interface_assignment(
        self, shared_utils: SharedUtilsProtocol, interface: str, subnet: IPv4Network, prefix_size: int, requested_value: IPv4Interface | None = None
    ) -> IPv4Interface:
        """
        Returns the assigned IPv4 address for this interface on this device. Assignment and pool will be autocreated if missing.

        Args:
            shared_utils: Instance of SharedUtils for the device.
            interface: Interface name
            subnet: Subnet from which to assign a prefix.
            prefix_size: Size of prefix to assign.
            requested_value: A requested value to assign to the device if available. Existing assignment will be changed if possible.
                There are no guarantees that this value will be assigned, so the caller should check and handle accordingly.
        """
        pool = self.get_ipv4_interface_pool(subnet, prefix_size, shared_utils)
        key = IPv4InterfacePoolCollection.get_assignment_key(shared_utils, interface)
        return pool.get_assignment(key, requested_value).value
