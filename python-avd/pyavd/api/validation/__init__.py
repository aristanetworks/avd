# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from pyavd_utils.validation import ValidatedDataResult, ValidationResult

if TYPE_CHECKING:
    from pyavd.api.schemas import Design, EOSConfig


@dataclass(frozen=True)
class LoadDesignResult:
    design: Design | None
    """Loaded design. None if we hit any schema violations."""

    validation_result: ValidationResult
    """Result of data validation."""


@dataclass(frozen=True)
class LoadEOSConfigResult:
    eos_config: EOSConfig | None
    """Loaded EOS Config data. None if we hit any schema violations."""

    validation_result: ValidationResult
    """Result of data validation."""


__all__ = ["LoadDesignResult", "LoadEOSConfigResult", "ValidatedDataResult", "ValidationResult"]
