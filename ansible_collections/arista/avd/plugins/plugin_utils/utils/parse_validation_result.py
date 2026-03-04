# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansible.utils.display import Display
    from pyavd_utils.validation import ValidationResult

    from pyavd._utils.json_path_to_string import json_path_to_string

try:
    from pyavd._utils.json_path_to_string import json_path_to_string

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


def parse_validation_result(validation_result: ValidationResult, hostname: str, ansible_display: Display) -> int:
    """Parser of ValidationResult displaying warnings and errors and returning the number of validation errors."""
    if not HAS_PYAVD:
        msg = "The 'arista.avd' collection requires the 'pyavd' Python library. Got import error."
        raise ImportError(msg)

    for deprecation in validation_result.deprecations:
        path = json_path_to_string(deprecation.path)

        message = f"[{hostname}]: The input data model '{path}' is deprecated."
        if deprecation.replacement:
            message += f" Use '{deprecation.replacement}' instead."
        if deprecation.url:
            message += f" See {deprecation.url} for details."

        # Assign this to a variable to work around a bug in ansible-test's pylint check (https://github.com/ansible/ansible/issues/85614)
        collection_name = "arista.avd"

        ansible_display.deprecated(
            msg=message,
            version=deprecation.version,
            collection_name=collection_name,
        )

    for ignored_key in validation_result.ignored_eos_config_keys:
        path = json_path_to_string(ignored_key.path)

        message = (
            f"[{hostname}]: The EOS Config input key '{path}' is present in the input to 'eos_designs' and will be ignored. "
            f"To address this, use the equivalent AVD Design input model if available or use custom_structured_configuration. "
            f"See https://avd.arista.com/6.x/docs/porting-guides/6.x.x.html#using-eos-config-eos_cli_config_gen-data-models-when-running-eos_designs "
            "for details."
        )
        ansible_display.warning(message, formatted=True)

    if (error_count := len(validation_result.violations)) > 0:
        for violation in validation_result.violations:
            path_message = f" for the input data model '{json_path_to_string(violation.path)}'" if violation.path else ""
            message = f"[{hostname}] Validation error{path_message}: {violation.message}"
            ansible_display.error(message, wrap_text=False)

    return error_count


def build_result_message(validation_errors: int) -> str | None:
    if validation_errors:
        plural = "s" if validation_errors > 1 else ""
        return f"{validation_errors} error{plural} found during schema validation of input variables."

    return None
