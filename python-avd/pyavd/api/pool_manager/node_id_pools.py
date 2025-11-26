# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
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
    min_value: int = 1

    @staticmethod
    def _pool_key_from_shared_utils(shared_utils: SharedUtilsProtocol) -> str:
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
    def _assignment_key_from_shared_utils(shared_utils: SharedUtilsProtocol) -> str:
        """Returns the assignment key to use for this device."""
        return f"hostname={shared_utils.hostname}"
