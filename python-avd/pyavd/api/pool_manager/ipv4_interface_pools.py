# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from ipaddress import IPv4Interface, IPv4Network
from itertools import filterfalse
from pathlib import Path
from typing import TYPE_CHECKING

from pyavd._utils import default

from .base_classes import Pool, PoolAssignment, PoolCollection

if TYPE_CHECKING:
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


@dataclass()
class IPv4InterfacePoolCollection(PoolCollection[IPv4Interface]):
    """The expected key for each pool is <network>/<mask>/<assignment_mask>."""

    pools_key: str = "ipv4_interface_pools"
    pools: dict[str, Pool[IPv4Interface]] = field(default_factory=dict)
    pool_cls: type[Pool[IPv4Interface]] = Pool[IPv4Interface]
    assignment_cls: type[PoolAssignment[IPv4Interface]] = PoolAssignment[IPv4Interface]
    value_type: type = IPv4Interface

    @staticmethod
    def get_pool_key(subnet: IPv4Network, prefix_size: int) -> str:
        """Returns the pool key to use for this device."""
        return f"{subnet}/{prefix_size}"

    @staticmethod
    def _pools_file_from_shared_utils(output_dir: Path, shared_utils: SharedUtilsProtocol) -> Path:
        """Returns the file to use for this device."""
        fabric_name = shared_utils.fabric_name
        default_id_file = output_dir.joinpath(f"data/{fabric_name}-ids.yml")
        return Path(default(shared_utils.inputs.fabric_numbering.node_id.pools_file, default_id_file))

    @staticmethod
    def get_assignment_key(shared_utils: SharedUtilsProtocol, interface: str) -> str:
        """Returns the assignment key to use for this device."""
        return f"hostname={shared_utils.hostname}/interface={interface}"

    @staticmethod
    def is_valid_value(value: IPv4Interface, pool: Pool[IPv4Interface]) -> bool:
        """Check if a value is valid according to the pool definition."""
        pool_cidr, prefix_size = pool.pool_key.rsplit("/", maxsplit=1)
        prefix_size = int(prefix_size)
        if value.network.prefixlen != prefix_size:
            return False

        return value.network.subnet_of(IPv4Network(pool_cidr))

    def add_pool(self, pool_key: str, assignments: dict[str, PoolAssignment[IPv4Interface]] | None = None) -> None:
        """Creates a new pool and add it to the collection with the given assignments or as an empty pool."""
        self._pools[pool_key] = self.pool_cls(
            collection=self,
            pool_key=pool_key,
            assignments=assignments or {},
        )

    def _next_available(self, pool: Pool[IPv4Interface]) -> IPv4Interface:
        """
        Finds next available value in the pool. This is not doing any assignment.

        Raises:
            StopIteration: If no available values are found for this pool.
        """
        existing_networks = {assignment.value.network for assignment in pool.assignments.values()}
        pool_cidr, prefix_size = pool.pool_key.rsplit("/", maxsplit=1)
        prefix_size = int(prefix_size)

        # Create a filterfalse generator for all subnets in the pool with the given prefix length that are not assigned.
        # Nothing will be iterated at this point, but the next(iter()) below will ask the generator for the first item.
        all_networks = IPv4Network(pool_cidr).subnets(new_prefix=prefix_size)
        available_networks = filterfalse(existing_networks.__contains__, all_networks)

        next_available_network = next(iter(available_networks))
        first_host = next(iter(next_available_network.hosts()))
        return IPv4Interface(f"{first_host}/{prefix_size}")
