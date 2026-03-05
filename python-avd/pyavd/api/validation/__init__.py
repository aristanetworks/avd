# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING

from pyavd_utils.validation import ValidationResult

if TYPE_CHECKING:
    from pyavd_utils.validation import ValidatedDataResult as _ValidatedDataResult


@dataclass(frozen=True)
class ValidatedDataResult:
    validated_data: dict | None
    """Validated data as a dict. None if validation fails."""

    validation_result: ValidationResult
    """Result of data validation."""

    @classmethod
    def _from_pyavd_utils_validated_data_result(cls, pyavd_utils_validated_data_result: _ValidatedDataResult) -> ValidatedDataResult:
        validated_data = json.loads(pyavd_utils_validated_data_result.validated_data) if pyavd_utils_validated_data_result.validated_data is not None else None
        return ValidatedDataResult(
            validated_data=validated_data,
            validation_result=pyavd_utils_validated_data_result.validation_result,
        )


__all__ = ["ValidatedDataResult", "ValidationResult"]
