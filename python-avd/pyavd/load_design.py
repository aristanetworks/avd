# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api.validation import LoadDesignResult


def load_design(inputs: dict) -> LoadDesignResult:
    """
    Load and validate Design data.

    Args:
        inputs: Dictionary with  data to be validated and loaded as a Design instance.

    Returns:
        LoadDesignResult containing the loaded design (or None if validation fails)
        and the validation result with any errors or warnings.
    """
    from . import validate_inputs  # noqa: PLC0415
    from .api.schemas import Design  # noqa: PLC0415
    from .api.validation import LoadDesignResult  # noqa: PLC0415

    validated_data_result = validate_inputs(inputs)
    if validated_data_result.validated_data is not None:
        validated_data = json.loads(validated_data_result.validated_data)
        design = Design._load(validated_data)
    else:
        design = None

    return LoadDesignResult(design=design, validation_result=validated_data_result.validation_result)
