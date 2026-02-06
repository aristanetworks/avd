# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api.validation import ValidatedDataResult


def validate_structured_config(structured_config: dict) -> ValidatedDataResult:
    """
    Validate structured config according the `eos_cli_config_gen` schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        structured_config: Dictionary with structured configuration.

    Returns:
        ValidatedDataResult object with the ValidationResult containing validation errors, deprecation warnings
        and the validated_data as a dict. If the validation fails, the validated_data will be None.

    Raises:
        ValueError: If the structured_config is not JSON serializable.
    """
    from pyavd_utils.validation import get_validated_data  # noqa: PLC0415

    from ._schema.store import init_store  # noqa: PLC0415
    from .api.validation import ValidatedDataResult  # noqa: PLC0415

    init_store()

    try:
        data_as_json = json.dumps(structured_config, skipkeys=True, default=lambda _: "<not serializable>")
    except (TypeError, ValueError, RecursionError) as e:
        msg = f"Unable to serialize structured_config: {e}"
        raise ValueError(msg) from e

    pyavd_utils_validated_data_result = get_validated_data(data_as_json=data_as_json, schema_name="eos_cli_config_gen")
    return ValidatedDataResult._from_pyavd_utils_validated_data_result(pyavd_utils_validated_data_result)
