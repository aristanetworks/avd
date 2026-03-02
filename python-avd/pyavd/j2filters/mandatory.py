# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from jinja2 import TemplateRuntimeError
from jinja2.runtime import Undefined


def mandatory(value: object, msg: str | None = None) -> object:
    """
    Mandatory will test if value is defined and not none, otherwise raise an error.

    This filter is used to enforce that a variable is defined and has a value.
    If the variable is undefined or None, it will raise a TemplateRuntimeError
    with the provided error message (or a default message).

    Example when used as a jinja filter
    -------
    {{ required_var | mandatory('This variable is required!') }}

    Args:
        value: The value to test.
        msg: Optional error message to display if value is undefined or None.

    Returns:
        The value if it is defined and not None.

    Raises:
        TemplateRuntimeError: If value is undefined or None.
    """
    if value is None or isinstance(value, Undefined):
        error_msg = msg or "Variable is required but not defined"
        raise TemplateRuntimeError(error_msg)

    return value
