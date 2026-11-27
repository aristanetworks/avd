# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.default import default
from pyavd._utils.format_string import AvdStringFormatter

from ._errors import InvalidPoolValueError, PoolAssignmentConflictError
from .base_classes import Pool, PoolAssignment, PoolCollection

if TYPE_CHECKING:
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


@dataclass()
class NodeIdPoolCollection(PoolCollection[int]):
    assignment_error_prefix: ClassVar[str] = (
        "When 'fabric_numbering.node_id.algorithm' is set to 'pool_manager', "
        "any explicitly configured 'id' is reserved in the pool to prevent duplicate allocations. "
    )
    pools_key: str = "node_id_pools"
    pool_cls: type[Pool[int]] = Pool[int]
    assignment_cls: type[PoolAssignment[int]] = PoolAssignment[int]
    value_type: type = int
    min_value: int = 1

    def _assignment_error(self, error: InvalidPoolValueError | PoolAssignmentConflictError) -> AristaAvdInvalidInputsError:
        if isinstance(error, InvalidPoolValueError):
            valid_range = f"at least {self.min_value}" if self.max_value is None else f"between {self.min_value} and {self.max_value}"
            message = f"The given 'id: {error.value}' is not a valid Node ID. The 'id' setting must be {valid_range}."
        else:
            assigned_hostname = error.assigned_key.removeprefix("hostname=")
            message = f"The given 'id: {error.value}' is already assigned to '{assigned_hostname}'. The 'id' setting must either be removed or changed."

        return AristaAvdInvalidInputsError(self.assignment_error_prefix + message, host=error.key.removeprefix("hostname="))

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
    def _pool_key_from_dict(pool_key_dict: dict) -> str:
        """
        Returns the formatted pool key generated from legacy pool key dict format.

        Caveat: This will always use the default template string to generate the pool names.

        Raises:
            KeyError: If any of the legacy fields are missing. Caught by the caller.
        """
        return AvdStringFormatter().format(
            "fabric_name={fabric_name}{dc_name?</dc_name=}{pod_name?</pod_name=}{type?</type=}",
            fabric_name=pool_key_dict["fabric_name"],
            dc_name=pool_key_dict["dc_name"],
            pod_name=pool_key_dict["pod_name"],
            type=pool_key_dict["type"],
            rack=None,
        )

    @staticmethod
    def _pools_file_from_shared_utils(output_dir: Path, shared_utils: SharedUtilsProtocol) -> Path:
        """Returns the file to use for this device."""
        fabric_name = shared_utils.fabric_name
        default_id_file = output_dir.joinpath(f"data/{fabric_name}-ids.yml")

        # Save the pool string on the class just in case
        return Path(default(shared_utils.inputs.fabric_numbering.node_id.pools_file, default_id_file))

    @staticmethod
    def _assignment_key_from_shared_utils(shared_utils: SharedUtilsProtocol) -> str:
        """Returns the assignment key to use for this device."""
        return f"hostname={shared_utils.hostname}"
