# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from itertools import filterfalse
from pathlib import Path
from typing import TYPE_CHECKING

from pyavd._utils import AvdStringFormatter, default

from .base_classes import Pool, PoolAssignment, PoolCollection

if TYPE_CHECKING:
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


@dataclass()
class NodeIdPoolCollection(PoolCollection[int]):
    pools_key: str = "node_id_pools"
    pool_cls: type[Pool[int]] = Pool[int]
    assignment_cls: type[PoolAssignment[int]] = PoolAssignment[int]
    value_type: type = int

    @staticmethod
    def get_pool_key(shared_utils: SharedUtilsProtocol) -> str:
        """Returns the pool key to use for this device."""
        return AvdStringFormatter().format(
            shared_utils.inputs.fabric_numbering_node_id_pool,
            fabric_name=shared_utils.fabric_name,
            dc_name=shared_utils.inputs.dc_name,
            pod_name=shared_utils.inputs.pod_name,
            type=shared_utils.type,
            rack=shared_utils.node_config.rack,
        )

    @staticmethod
    def _pools_file_from_shared_utils(output_dir: Path, shared_utils: SharedUtilsProtocol) -> Path:
        """Returns the file to use for this device."""
        fabric_name = shared_utils.fabric_name
        default_id_file = output_dir.joinpath(f"data/{fabric_name}-ids.yml")
        return Path(default(shared_utils.inputs.fabric_numbering.node_id.pools_file, default_id_file))

    @staticmethod
    def get_assignment_key(shared_utils: SharedUtilsProtocol) -> str:
        """Returns the assignment key to use for this device."""
        return f"hostname={shared_utils.hostname}"

    @staticmethod
    def is_valid_value(value: int, pool: Pool[int]) -> bool:  # noqa: ARG004
        """Check if a value is valid according to the pool definition."""
        return bool(value)

    def add_pool(self, pool_key: str, assignments: dict[str, PoolAssignment[int]] | None = None) -> None:
        """Creates a new pool and add it to the collection with the given assignments or as an empty pool."""
        self._pools[pool_key] = self.pool_cls(
            collection=self,
            pool_key=pool_key,
            assignments=assignments or {},
        )

    def _next_available(self, pool: Pool[int]) -> int:
        """Finds next available value in the pool. This is not doing any assignment."""
        existing_ids = {assignment.value for assignment in pool.assignments.values()}
        # Create a filterfalse generator from a range starting 1, excluding the values that are already assigned.
        # Nothing will be iterated at this point, but the next(iter()) below will ask the generator for the first item.
        available_ids = filterfalse(existing_ids.__contains__, range(1, 1 + len(existing_ids) + 2))
        return next(iter(available_ids))
