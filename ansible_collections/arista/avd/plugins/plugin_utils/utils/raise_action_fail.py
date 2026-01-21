# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Utility function for raising AnsibleActionFail with proper exception chaining."""

from ansible.errors import AnsibleActionFail


def raise_action_fail(message: str, exception: Exception | None = None) -> None:
    """
    Raise AnsibleActionFail with exception chaining but without message duplication.

    In Ansible 2.19+, using `raise AnsibleActionFail(msg) from exception` causes the
    error message to be duplicated/concatenated. To avoid this while preserving the
    full traceback chain, we recursively clear all exception messages in the chain
    as we tend to add the deeper error message in our top level Exception.

    TODO: Reevaluate this as Ansible way of handling nested exceptions evolves. Cf References.

    Args:
        message: The error message to display
        exception: The original exception (optional). If provided, the full traceback
                  chain will be preserved.

    Raises:
        AnsibleActionFail: Always raises with the provided message.

    References:
        https://docs.ansible.com/projects/ansible/latest/porting_guides/porting_guide_core_2.19.html#contextual-warnings-and-errors
    """
    if exception is None:
        raise AnsibleActionFail(message) from None

    _clear_exception_chain(exception)
    raise AnsibleActionFail(message) from exception


def _clear_exception_chain(exc: BaseException) -> None:
    """Recursively clear all exception messages in the chain to avoid duplication while preserving the full traceback chain."""
    if exc is not None:
        exc.args = ()
        if exc.__cause__ is not None:
            _clear_exception_chain(exc.__cause__)
        if exc.__context__ is not None and not exc.__suppress_context__:
            _clear_exception_chain(exc.__context__)
