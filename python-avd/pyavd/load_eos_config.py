# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd.api.validation import LoadEOSConfigResult


def load_eos_config(inputs: dict) -> LoadEOSConfigResult:
    """
    Load and validate EOS Config data.

    Args:
        inputs: Dictionary with EOS Config data to be validated and loaded as an EOSConfig instance.

    Returns:
        LoadEOSConfigResult containing the loaded EOSConfig (or None if validation fails)
        and the validation result with any errors or warnings.
    """
    from . import validate_structured_config  # noqa: PLC0415
    from .api.schemas import EOSConfig  # noqa: PLC0415
    from .api.validation import LoadEOSConfigResult  # noqa: PLC0415

    validated_data_result = validate_structured_config(inputs)
    if validated_data_result.validated_data is not None:
        validated_data = json.loads(validated_data_result.validated_data)
        eos_config = EOSConfig._load(validated_data)
    else:
        eos_config = None

    return LoadEOSConfigResult(eos_config=eos_config, validation_result=validated_data_result.validation_result)
