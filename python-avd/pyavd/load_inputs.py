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
class ValidationResult:
    validation_errors: Sequence[AvdValidationError]
    """Validation errors."""
    deprecations: Sequence[AvdDeprecationWarning]
    """Deprecation warnings."""


@dataclass(frozen=True)
class LoadInputsResult(ValidationResult):
    inputs: EosDesigns | None
    """Loaded inputs. None if we hit any schema violations."""


def load_inputs(data: Any) -> LoadInputsResult:
    """TODO docstring."""
    from pyavd_utils.validation import get_validated_data  # noqa: PLC0415

    from ._eos_designs.schema import EosDesigns  # noqa: PLC0415
    from ._errors import AvdDeprecationWarning, AvdValidationError  # noqa: PLC0415
    from ._schema.store import init_store  # noqa: PLC0415

    try:
        data_as_json = json.dumps(data)
    except (TypeError, ValueError, RecursionError) as e:
        msg = f"Unable to load inputs from the given data: {e}"
        raise ValueError(msg) from e

    init_store()
    validated_data_result = get_validated_data(data_as_json, "eos_designs")
    if validated_data_result.validated_data is not None:
        validated_data = json.loads(validated_data_result.validated_data)
        inputs = EosDesigns._load(validated_data)
    else:
        inputs = None

    validation_errors = tuple(AvdValidationError.from_violation(violation) for violation in validated_data_result.validation_result.violations)
    deprecations = tuple(AvdDeprecationWarning.from_deprecation(deprecation) for deprecation in validated_data_result.validation_result.deprecations)
    return LoadInputsResult(inputs=inputs, validation_errors=validation_errors, deprecations=deprecations)
