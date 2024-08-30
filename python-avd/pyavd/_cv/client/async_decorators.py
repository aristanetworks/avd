# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Callable
from functools import wraps
from inspect import signature
from logging import getLogger
from typing import Any

from pyavd._utils import batch

from .exceptions import CVMessageSizeExceeded

LOGGER = getLogger(__name__)


def grpc_msg_size_handler(list_field: str) -> Callable:
    def decorator_grpc_msg_size_handler(func: Callable) -> Callable:
        func_signature = signature(func)
        if isinstance(func_signature.return_annotation, list):
            msg = (
                f"grpc_msg_size_handler decorator is unable to bind to the function '{func.__name__}'. "
                f"Expected a return type of list. Got '{func_signature.return_annotation}'."
            )
            raise TypeError(msg)

        @wraps(func)
        async def wrapper_grpc_msg_size_handler(*args: Any, **kwargs: Any) -> list:
            bound_arguments = func_signature.bind(*args, **kwargs)
            arguments = bound_arguments.arguments
            if list_field not in arguments:
                msg = f"grpc_msg_size_handler decorator is unable to find the list_field '{list_field}' in the given arguments to '{func.__name__}'."
                raise KeyError(msg)

            list_value: list = arguments[list_field]
            if not isinstance(list_value, list):
                msg = f"grpc_msg_size_handler decorator expected the value of the list_field '{list_field}' to be a list. Got '{type(list_value)}'"
                raise TypeError(msg)

            LOGGER.info("wrapper_grpc_msg_size_handler: Called '%s' with '%s' items", func.__name__, len(list_value))

            if len(list_value) < 2:
                # No need to try/except if we cannot split the list.
                return await func(*args, **kwargs)

            try:
                return await func(*args, **kwargs)
            except CVMessageSizeExceeded as e:
                # At minimum try to split in two.
                # The double negatives make // round up instead of down.
                ratio = max(2, -(-e.size // e.max_size))
                chunk_size = len(list_value) // ratio
                LOGGER.info(
                    "wrapper_grpc_msg_size_handler: Message size %s exceeded the max of %s. Splitting into %s smaller calls with up to %s items each.",
                    e.size,
                    e.max_size,
                    ratio,
                    chunk_size,
                )
                # For every chunk we call ourselves recursively, so we can catch any further needs of splitting.
                result = []
                for chunk in batch(list_value, chunk_size):
                    arguments[list_field] = chunk
                    result.extend(await wrapper_grpc_msg_size_handler(*bound_arguments.args, **bound_arguments.kwargs))
                return result

        return wrapper_grpc_msg_size_handler

    return decorator_grpc_msg_size_handler
