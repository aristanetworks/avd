# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd_utils.validation import Configuration

    from .api.validation import ValidatedDataResult


def validate_inputs(inputs: dict, *, configuration: Configuration | None = None) -> ValidatedDataResult:
    """
    Validate input variables according to the AVD Design schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        inputs: Dictionary with inputs for AVD Design.
        configuration: Optional Configuration object from pyavd_utils.validation.
            If not provided use a default configuration enabling warnings for EOS Config keys.

    Returns:
        ValidatedDataResult object with the ValidationResult containing validation errors, deprecation warnings
        and the validated_data as a dict. If the validation fails, the validated_data will be None.

    Raises:
        ValueError: If the inputs are not JSON serializable.
    """
    from pyavd_utils.validation import Configuration, get_validated_data  # noqa: PLC0415

    # Use default configuration if not provided
    configuration = configuration or Configuration(warn_eos_cli_config_gen_keys=True)

    from ._schema.store import init_store  # noqa: PLC0415
    from .api.validation import ValidatedDataResult  # noqa: PLC0415

    init_store()

    try:
        data_as_json = json.dumps(inputs, skipkeys=True, default=lambda _: "<not serializable>")
    except (TypeError, ValueError, RecursionError) as e:
        msg = f"Unable to serialize inputs: {e}"
        raise ValueError(msg) from e

    pyavd_utils_validated_data_result = get_validated_data(data_as_json=data_as_json, schema_name="eos_designs", configuration=configuration)
    return ValidatedDataResult._from_pyavd_utils_validated_data_result(pyavd_utils_validated_data_result)
