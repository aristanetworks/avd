# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .template import template

if TYPE_CHECKING:
    from typing import Any

    from ansible.template import Templar


def template_var(template_file: str, template_vars: Any, templar: Templar | None) -> str:
    """
    Wrap "template" for single values like IP addresses.

    The result is forced into a string and leading/trailing newlines and whitespaces are removed.

    The templar will return None for an empty result or any other data type depending on the template result.
    This function returns "" for an empty result.

    Args:
        template_file: Path to Jinja2 template file
        template_vars: Variables to use when rendering template
        templar: Instance of Ansible Templar class
        searchpath: List of Paths

    Returns:
        The rendered template
    """
    result = template(template_file, template_vars, templar)
    return str(result).strip() if result is not None else ""
