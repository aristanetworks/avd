# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from pyavd._lazy_import import LazyImports, get_lazy_attr, get_lazy_dir

if TYPE_CHECKING:
    from pyavd_utils.validation import ValidatedDataResult as _ValidatedDataResult
    from pyavd_utils.validation import ValidationResult


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

_LAZY_IMPORTS: LazyImports = {"ValidationResult": ("pyavd_utils.validation", "ValidationResult")}


def __getattr__(name: str) -> Any:
    return get_lazy_attr(name, _LAZY_IMPORTS, globals())


def __dir__() -> list[str]:
    return get_lazy_dir(_LAZY_IMPORTS, globals())
