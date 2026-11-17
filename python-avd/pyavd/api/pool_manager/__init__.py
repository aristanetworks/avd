# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Literal, overload

from yaml import CSafeDumper

from .ipv4_allocations import Ipv4AllocationCollection
from .ipv4_pools import Ipv4PoolCollection
from .node_id_pools import NodeIdPoolCollection

if TYPE_CHECKING:
    from pathlib import Path

    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol

    from .base_classes import Pool, PoolCollection

PoolType = Literal["node_id_pools"]
PoolCollectionType = Literal["node_id_pools", "ipv4_pools"]


class PoolManager:
    """
    Class used to handle pooled resources.

    This class is imported and initialized once in eos_designs_facts
    and given to shared_utils for each device.
    """

    _pool_collection_types: ClassVar = {"node_id_pools": NodeIdPoolCollection, "ipv4_pools": Ipv4PoolCollection}
    _output_dir: Path
    _pool_collections: dict[PoolCollectionType, dict[Path, PoolCollection]]
    """PoolCollection collections keys by file path."""

    def __init__(self, output_dir: Path) -> None:
        self._output_dir = output_dir
        self._pool_collections = {}
        self._changed_pool_files = {}
        self._ipv4_allocation_collections: dict[str, Ipv4AllocationCollection] = {}

    def get_ipv4_allocation_collection(self, fabric_name: str) -> Ipv4AllocationCollection:
        """Return fabric-scoped persistent IPv4 reservations without node-ID pruning semantics."""
        if fabric_name not in self._ipv4_allocation_collections:
            path = self._output_dir / "data" / f"{fabric_name}-ipv4-allocations.yml"
            self._ipv4_allocation_collections[fabric_name] = Ipv4AllocationCollection(path)
        return self._ipv4_allocation_collections[fabric_name]

    def save_updated_pools(self, dumper_cls: type = CSafeDumper) -> bool:
        """
        Save data if anything changed. Returns a boolean telling if anything was changed.

        Node-ID pools prune unaccessed assignments and empty pools. IPv4 reservations retain absent owners.
        """
        any_changes = False
        for pools_files_map in self._pool_collections.values():
            changes_for_this_pool_type = [pool_collection.save_updates(dumper_cls) for pool_collection in pools_files_map.values()]
            any_changes = any_changes or any(changes_for_this_pool_type)
        for collection in self._ipv4_allocation_collections.values():
            changed = collection.save_updates(dumper_cls)
            any_changes = any_changes or changed
        return any_changes

    def get_pool(self, pool_type: PoolType, shared_utils: SharedUtilsProtocol) -> Pool:
        """Returns the pool of the given type for this device. Pool will be autocreated if missing."""
        if pool_type != "node_id_pools":
            msg = f"Invalid pool type '{pool_type}'. Expected node_id_pools."
            raise ValueError(msg)

        pools_cls = NodeIdPoolCollection
        pools_file = pools_cls._pools_file_from_shared_utils(self._output_dir, shared_utils)
        pool_collection = self.get_pool_collection(pool_type, pools_file)

        pool_key = pools_cls._pool_key_from_shared_utils(shared_utils)
        return pool_collection.get_pool(pool_key)

    @overload
    def get_pool_collection(self, pool_type: Literal["node_id_pools"], pools_file: Path) -> NodeIdPoolCollection: ...

    @overload
    def get_pool_collection(self, pool_type: Literal["ipv4_pools"], pools_file: Path) -> Ipv4PoolCollection: ...

    def get_pool_collection(self, pool_type: PoolCollectionType, pools_file: Path) -> PoolCollection:
        """Return a registered collection without requiring a device-specific allocation context."""
        if pool_type not in self._pool_collection_types:
            msg = f"Invalid pool type '{pool_type}'. Expected one of {', '.join(self._pool_collection_types)}"
            raise ValueError(msg)
        pools_files_map = self._pool_collections.setdefault(pool_type, {})
        if pools_file not in pools_files_map:
            pools_files_map[pools_file] = self._pool_collection_types[pool_type](pools_file=pools_file)
        return pools_files_map[pools_file]

    def get_assignment(self, pool_type: PoolType, shared_utils: SharedUtilsProtocol, requested_value: int | str | None = None) -> int:
        """
        Returns the assignment value for this device for the given pool type. Assignment and pool will be autocreated if missing.

        Args:
            pool_type: Currently only supports "node_id_pools".
            shared_utils: Instance of SharedUtils for the device.
            requested_value: A requested value to assign to the device if available. Existing assignment will be changed if possible.
                There are no guarantees that this value will be assigned, so the caller should check and handle accordingly.
        """
        pool = self.get_pool(pool_type, shared_utils)
        key = NodeIdPoolCollection._assignment_key_from_shared_utils(shared_utils)
        return pool.get_assignment(key, requested_value).value
