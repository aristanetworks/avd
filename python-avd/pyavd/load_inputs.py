# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Sequence

    from ._eos_designs.schema import EosDesigns
    from ._errors import AvdDeprecationWarning, AvdValidationError


@dataclass(frozen=True)
class LoadInputsResult:
    inputs: EosDesigns | None
    """Loaded inputs. None if we hit any schema violations."""
    validation_errors: Sequence[AvdValidationError]
    """Validation errors."""
    deprecations: Sequence[AvdDeprecationWarning]
    """Deprecation warnings."""


def load_inputs(data: Any) -> LoadInputsResult:
    """TODO docstring."""
    from pyavd_utils.validation import get_validated_data  # noqa: PLC0415

    from ._eos_designs.schema import EosDesigns  # noqa: PLC0415
    from ._errors import AvdDeprecationWarning, AvdValidationError  # noqa: PLC0415

    try:
        data_as_json = json.dumps(data)
    except (TypeError, ValueError, RecursionError) as e:
        msg = f"Unable to load inputs from the given data: {e}"
        raise ValueError(msg) from e

    get_validated_data_result = get_validated_data(data_as_json, "eos_designs")
    if get_validated_data_result.validated_data is not None:
        validated_data = json.loads(get_validated_data_result.validated_data)
        inputs = EosDesigns._load(validated_data)
    else:
        inputs = None
    errors = tuple(AvdValidationError.from_violation(violation) for violation in get_validated_data_result.validation_result.violations)
    warnings = tuple(AvdDeprecationWarning.from_deprecation(deprecation) for deprecation in get_validated_data_result.validation_result.deprecations)
    return LoadInputsResult(inputs, errors, warnings)
