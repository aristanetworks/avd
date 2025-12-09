# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansible.utils.display import Display

    from pyavd.load_inputs import ValidationResult


def parse_validation_result(validation_result: ValidationResult, hostname: str, ansible_display: Display) -> int:
    """Parser of pyavd.load_inputs.ValidationResult displaying warnings and errors and returning the number of validation errors."""
    for deprecation in validation_result.deprecations:
        ansible_display.deprecated(
            msg=f"{hostname}: {deprecation}",
            version=deprecation.version,
            date=deprecation.date,
            collection_name="arista.avd",
            removed=deprecation.removed,
        )

    if (error_count := len(validation_result.validation_errors)) > 0:
        for validation_error in validation_result.validation_errors:
            message = f"{hostname}: {validation_error}"
            ansible_display.error(message, wrap_text=False)

    return error_count


def build_result_message(validation_errors: int) -> str | None:
    if validation_errors:
        return f"{validation_errors} errors found during schema validation of input vars."

    return None
