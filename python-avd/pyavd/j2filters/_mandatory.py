# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Any

from jinja2.runtime import Undefined

from pyavd._errors import AristaAvdInvalidInputsError


def _mandatory(value: Any, msg: str | None = None) -> Any:
    """
    Hidden compatibility shim for legacy eos_cli_config_gen templates.

    This only restores the small part of Ansible's mandatory filter behavior
    needed by templates that moved from Ansible templating to PyAVD templating.
    Do not use this for new validation; prefer schema or Python validation.
    """
    if isinstance(value, Undefined) or value is None:
        raise AristaAvdInvalidInputsError(msg or "Mandatory variable is not defined.")

    return value
