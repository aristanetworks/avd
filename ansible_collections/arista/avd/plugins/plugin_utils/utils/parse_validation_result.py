# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansible.utils.display import Display
    from pyavd_utils.validation import ValidationResult

    from pyavd._utils import json_path_to_string

try:
    from pyavd._utils import json_path_to_string

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


def parse_validation_result(validation_result: ValidationResult, hostname: str, ansible_display: Display) -> int:
    """Parser of pyavd.load_design.ValidationResult displaying warnings and errors and returning the number of validation errors."""
    if not HAS_PYAVD:
        msg = "The 'arista.avd' collection requires the 'pyavd' Python library. Got import error."
        raise ImportError(msg)

    for deprecation in validation_result.deprecations:
        path = json_path_to_string(deprecation.path)

        message = f"[{hostname}]: The input data model '{path}' is deprecated"
        if deprecation.replacement:
            message += f" Use '{deprecation.replacement}' instead."
        if deprecation.url:
            message += f" See {deprecation.url} for details."

        ansible_display.deprecated(
            msg=message,
            version=str(deprecation.version) if deprecation.version else None,
            collection_name="arista.avd",
            removed=deprecation.removed,
        )

    if (error_count := len(validation_result.violations)) > 0:
        for violation in validation_result.violations:
            path = json_path_to_string(violation.path)
            message = f"[{hostname}] Validation Error: '{path}' {violation.message}"
            ansible_display.error(message, wrap_text=False)

    return error_count


def build_result_message(validation_errors: int) -> str | None:
    if validation_errors:
        return f"{validation_errors} errors found during schema validation of input vars."

    return None
