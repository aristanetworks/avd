# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api.validation import LoadEOSConfigResult


def load_eos_config(inputs: dict) -> LoadEOSConfigResult:
    """
    Load and validate EOS Config data.

    Args:
        inputs: Dictionary with EOS Config data to be validated and loaded as an EOSConfig instance.

    Returns:
        LoadEOSConfigResult containing the loaded EOSConfig (or None if validation fails)
        and the validation result with any errors or warnings.

    Notes:
        Currently the `get_device_config` and `get_device_doc` functions need the validated data as a dict,
        so they will dump the loaded class if given.
        For now it is more efficient to use the `validate_structured_config` function and give the returned dict
        to those functions instead of using the EOSConfig class.
        If you already have the EOSConfig instance loaded as returned from `get_device_structured_config`,
        you can just use that instance directly.
    """
    from . import validate_structured_config  # noqa: PLC0415
    from .api.schemas import EOSConfig  # noqa: PLC0415
    from .api.validation import LoadEOSConfigResult  # noqa: PLC0415

    validated_data_result = validate_structured_config(inputs)
    eos_config = EOSConfig._load(validated_data_result.validated_data) if validated_data_result.validated_data is not None else None

    return LoadEOSConfigResult(eos_config=eos_config, validation_result=validated_data_result.validation_result)
