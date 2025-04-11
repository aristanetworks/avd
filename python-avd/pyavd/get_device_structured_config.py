# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import ChainMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts


def get_device_structured_config(hostname: str, inputs: dict, avd_facts: dict[str, EosDesignsFacts]) -> dict:
    """
    Build and return the AVD structured configuration for one device.

    Args:
        hostname: Hostname of device.
        inputs: Dictionary with inputs for "eos_designs".
            Variables should be converted and validated according to AVD `eos_designs` schema first using `pyavd.validate_inputs`.
        avd_facts: Dictionary of avd_facts as returned from `pyavd.get_avd_facts`.

    Returns:
        Device Structured Configuration as a dictionary
    """
    # pylint: disable=import-outside-toplevel
    from ._eos_designs.structured_config import get_structured_config
    from ._errors import AristaAvdError
    from .avd_schema_tools import AvdSchemaTools
    from .constants import EOS_DESIGNS_SCHEMA_ID

    # pylint: enable=import-outside-toplevel
    #
    # Map in avd_facts without touching the hostvars
    mapped_hostvars = ChainMap(
        {
            "switch": avd_facts[hostname]._as_dict(),
        },
        inputs,
    )

    input_schema_tools = AvdSchemaTools(schema_id=EOS_DESIGNS_SCHEMA_ID)
    result = {}

    # We do not validate input variables in this stage (done in "validate_inputs")
    structured_config = get_structured_config(
        hostname=hostname,
        hostvars=mapped_hostvars,
        input_schema_tools=input_schema_tools,
        all_facts=avd_facts,
        result=result,
        templar=None,
        validate=False,
    )
    if result.get("failed") or structured_config is None:
        msg = f"{[str(error) for error in result['errors']]}"
        raise AristaAvdError(msg)

    return structured_config._as_dict()
