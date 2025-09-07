# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import sleep as asyncio_sleep
from asyncio.exceptions import TimeoutError as AsyncioTimeoutError
from functools import wraps
from inspect import signature
from logging import getLogger
from re import compile as re_compile
from re import fullmatch
from types import UnionType
from typing import TYPE_CHECKING, Any, ClassVar, ParamSpec, TypeVar, get_args, get_origin

from grpclib import Status
from grpclib.exceptions import GRPCError

from pyavd._cv.client.exceptions import CVClientException, CVResourceNotFound, CVTimeoutError
from pyavd._utils import batch

from .constants import CVAAS_VERSION_STRING
from .exceptions import CVGRPCStatusUnavailable, CVMessageSizeExceeded
from .versioning import CvVersion

if TYPE_CHECKING:
    from collections.abc import Callable
    from inspect import BoundArguments, Signature

LOGGER = getLogger(__name__)

P = ParamSpec("P")
T = TypeVar("T")


MSG_SIZE_EXCEEDED_REGEX = re_compile(r"grpc: received message larger than max \((?P<size>\d+) vs\. (?P<max>\d+)\)")


class LimitCvVersion:
    """
    Decorator used to limit the supported CloudVision versions for a certain method.

    The decorator will maintain a map of decorated function variants and their supported versions.

    The decorator will only work in CvClient class methods since it expects the _cv_client attribute on 'self'.
    """

    versioned_funcs: ClassVar[dict[str, dict[tuple[CvVersion, CvVersion], Callable]]] = {}
    """
    Map of versioned functions keyed by function name.

    {
        <function_name>: {
            (<min_cv_version>, <max_cv_version>): <method>,
            (<min_cv_version>, <max_cv_version>): <method>,
        }
    }
    """

    def __init__(self, min_ver: str = "2024.1.0", max_ver: str = CVAAS_VERSION_STRING) -> None:
        """__init__ is called with the arguments of the decorator."""
        # Storing these on the instance so it can be read in the __call__ method.
        self.min_version = CvVersion(min_ver)
        self.max_version = CvVersion(max_ver)

        if self.max_version < self.min_version:
            msg = (
                "Invalid min and max versions passed to 'cv_version' decorator. Min version must be larger than max version. "
                f"Got min_ver '{self.min_version}', max_var '{self.max_version}'."
            )
            raise ValueError(msg)

    def __call__(self, func: Callable[P, T]) -> Callable[P, T]:
        """
        Store the method in the map of versioned functions after checking for overlapping decorators for the same method.

        __call__ is called with the method being decorated.
        """
        for existing_min_version, existing_max_version in LimitCvVersion.versioned_funcs.get(func.__name__, []):
            if existing_min_version <= self.max_version and existing_max_version >= self.min_version:
                msg = (
                    "Overlapping min and max versions passed to 'cv_version' decorator."
                    f"{self.min_version}-{self.max_version} overlaps with {existing_min_version}-{existing_max_version}."
                )
                raise ValueError(msg)

        LimitCvVersion.versioned_funcs.setdefault(func.__name__, {})[(self.min_version, self.max_version)] = func

        @wraps(func)
        async def wrapper_cv_version(*args: P.args, **kwargs: P.kwargs) -> T:
            """
            Call the appropriate original method depending on the _cv_version attribute of 'self'.

            The wrapper is being called by regular method calls with the args and kwargs given by the calling code (including 'self').
            """
            # Extract the version of the connected CloudVision server from the 'self' object passed to the method.
            # Defaulting to 'CVaaS' which means newest versions.
            cv_version: CvVersion = getattr(args[0], "_cv_version", CvVersion("CVaaS"))
            LOGGER.info("wrapper_cv_version: Called '%s' with version '%s'", func.__name__, cv_version)

            for min_max_versions, versioned_func in LimitCvVersion.versioned_funcs[func.__name__].items():
                min_version, max_version = min_max_versions
                if min_version <= cv_version <= max_version:
                    return await versioned_func(*args, **kwargs)

            msg = f"Unsupported version of CloudVision: '{cv_version}'."
            raise LookupError(msg)

        return wrapper_cv_version


class GRPCRequestHandler:
    """
    Decorator used to handle execution of the async gRPC calls towards CloudVision.

    Retries an async method upon getting gRPC Status.UNAVAILABLE (14) using exponential backoff mechanism and max retry limit.
    Converts GRPCError or AsyncioTimeoutError instances to an instance of the relevant subclass of CVClientException.
    Splits gRPC messages into smaller chunks (based on reported maximum supported size) if Status.RESOURCE_EXHAUSTED is received.

    Args:
        max_retries (int): Maximum number of retry attempts for Status.UNAVAILABLE. Total attempts = 1 + max_retries.
        initial_delay (int): Initial delay in seconds before the first retry.
        factor (int): Multiplier for the delay in subsequent retries.
        list_field (str): Name of the parameter to be split if Status.RESOURCE_EXHAUSTED is received.
        min_items_for_splitting_attempt (int): Minimum length of the item that we'll still try to split.
    """

    max_retries: int
    initial_delay: int
    factor: int
    list_field: str | None
    min_items_for_splitting_attempt: int
    func: Callable
    func_signature: Signature
    bound_arguments: BoundArguments
    current_arguments_dict: dict

    def __init__(
        self,
        max_retries: int = 5,
        initial_delay: int = 1,
        factor: int = 2,
        list_field: str | None = None,
        min_items_for_splitting_attempt: int = 2,
    ) -> None:
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.factor = factor
        self.list_field = list_field
        self.min_items_for_splitting_attempt = max(2, min_items_for_splitting_attempt)

    def __call__(self, func: Callable[P, T]) -> Callable[P, T]:
        self.func = func
        self.func_signature = signature(func)

        if self.list_field:
            if not (return_annotation := self._is_list_annotation(self.func_signature.return_annotation, strict=True))[0]:
                msg = (
                    f"GRPCRequestHandler decorator is unable to bind to the function '{func.__name__}' with the 'list_field' argument. "
                    f"Expected a return type of 'list'. Got '{return_annotation[1]}'."
                )
                raise TypeError(msg)

            # Verify that `self.list_field` is listed in parameters of the decorated function
            if self.list_field not in (func_parameters := self.func_signature.parameters.keys()):
                msg = (
                    f"{self.__class__.__name__} decorator is unable to find the list_field '{self.list_field}' "
                    f"in the given arguments to '{self.func.__name__}'. Found: '{list(func_parameters)}'."
                )
                raise KeyError(msg)

            # Verify that annotation of `self.list_field` is a `list` (or a `UnionType` with `list` being one of the arguments)
            if not (list_field_annotation := self._is_list_annotation(self.func_signature.parameters[self.list_field].annotation))[0]:
                msg = (
                    f"{self.__class__.__name__} decorator expected the type of the list_field '{self.list_field}' in function '{self.func.__name__}' "
                    f"to be defined as a list. Got '{list_field_annotation[1]}' (type '{type(list_field_annotation[1])}')."
                )
                raise TypeError(msg)

        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            return await self._execute_with_splitting(args, kwargs)

        return wrapper

    @staticmethod
    def _is_list_annotation(annotation: Any, strict: bool = False) -> tuple[bool, Any]:
        """
        Check if provided annotation is a `list`.

        Default `strict: False` will also match 'types.UnionType' with included `list`.
        """
        _string_based_annotation = (
            list
            if (
                (isinstance(annotation, str) and annotation.startswith("list"))
                or (not strict and get_origin(annotation) is UnionType and any(get_origin(arg) is list for arg in get_args(annotation)))
            )
            else annotation
        )

        return _string_based_annotation is list or get_origin(annotation) is list, _string_based_annotation

    async def _execute_single_call_with_retries(self, call_args: tuple, call_kwargs: dict) -> None:
        """Executes a single call to self.func with retry logic for gRPC UNAVAILABLE."""
        func_name = self.func.__name__

        for attempt in range(1, self.max_retries + 2):
            try:
                return await self.func(*call_args, **call_kwargs)
            except Exception as e:  # noqa: PERF203
                match e:
                    case CVClientException():
                        raise

                    case AsyncioTimeoutError():
                        raise CVTimeoutError(*e.args, call_args, call_kwargs)

                    case GRPCError():
                        match e.status:
                            case Status.NOT_FOUND:
                                raise CVResourceNotFound(*e.args, call_args, call_kwargs)

                            case Status.CANCELLED:
                                raise CVTimeoutError(*e.args, call_args, call_kwargs)

                            case Status.UNAVAILABLE:
                                if attempt <= self.max_retries:
                                    delay = self.initial_delay * (self.factor ** (attempt - 1))
                                    LOGGER.warning(
                                        "%s: Attempt %s/%s to execute call '%s' returned '%s'. Retrying in %ss...",
                                        self.__class__.__name__,
                                        attempt,
                                        self.max_retries + 1,
                                        func_name,
                                        e,
                                        delay,
                                    )
                                    await asyncio_sleep(delay)
                                # Use case where all retries for this specific call failed
                                else:
                                    msg = f"{self.__class__.__name__}: Attempt {attempt}/{self.max_retries + 1} to execute call '{func_name}' failed."
                                    raise CVGRPCStatusUnavailable(msg, *e.args, call_args, call_kwargs)

                            case Status.RESOURCE_EXHAUSTED:
                                if matches := fullmatch(MSG_SIZE_EXCEEDED_REGEX, e.message):
                                    new_exception = CVMessageSizeExceeded(*e.args)
                                    new_exception.max_size = int(matches.group("max"))
                                    new_exception.size = int(matches.group("size"))
                                    raise new_exception

                            case _:
                                raise CVClientException(*e.args, call_args, call_kwargs)

                    case _:
                        raise CVClientException(*e.args, call_args, call_kwargs)
        # Required by ruff
        return None

    async def _execute_with_splitting(self, original_call_args: tuple, original_call_kwargs: dict) -> Any:
        func_name = self.func.__name__

        if not (self.list_field and self.func_signature):
            # No list_field configured for splitting, execute the call directly (with retries)
            return await self._execute_single_call_with_retries(original_call_args, original_call_kwargs)

        bound_arguments = self.func_signature.bind(*original_call_args, **original_call_kwargs)
        current_arguments_dict = bound_arguments.arguments

        list_value: list = current_arguments_dict.get(self.list_field, [])
        if not isinstance(list_value, list):
            msg = (
                f"{self.__class__.__name__} decorator expected the value of the list_field '{self.list_field}' for function '{func_name}' "
                f"to be a list. Got '{type(list_value)}'."
            )
            raise TypeError(msg)

        LOGGER.debug("%s: Preparing call for '%s' for list_field '%s' with %s item(s).", self.__class__.__name__, func_name, self.list_field, len(list_value))

        if len(list_value) < self.min_items_for_splitting_attempt:
            # No need to try/except if we cannot split the list.
            return await self._execute_single_call_with_retries(original_call_args, original_call_kwargs)

        try:
            # Initial attempt with the full list
            return await self._execute_single_call_with_retries(original_call_args, original_call_kwargs)
        except CVMessageSizeExceeded as e:
            # At minimum try to split in two.
            # The double negatives make // round up instead of down.
            ratio = max(2, -(-e.size // e.max_size))
            chunk_size = len(list_value) // ratio
            LOGGER.info(
                "%s: Message size %s exceeded the max of %s for '%s' on list_field '%s'. Attempting to split %s items.",
                self.__class__.__name__,
                e.size,
                e.max_size,
                func_name,
                self.list_field,
                len(list_value),
            )
            # Use case where ratio is too high leading to the chuck_size being calculated as zero
            if chunk_size == 0 and len(list_value) > 0:
                chunk_size = 1

            planned_attempts_qty = int((len(list_value) / chunk_size) + (1 if len(list_value) % chunk_size else 0))

            LOGGER.info(
                "%s: Splitting list_field '%s' for '%s' into %s calls with up to %s items each.",
                self.__class__.__name__,
                self.list_field,
                func_name,
                planned_attempts_qty,
                chunk_size,
            )

            # For every chunk we call ourselves recursively, so we can catch any further needs of splitting.
            aggregated_results = []
            for chunk_id, chunk in enumerate(batch(list_value, chunk_size)):
                LOGGER.info(
                    "%s: Processing chunk %s/%s for '%s' with %s item(s) from list_field '%s'.",
                    self.__class__.__name__,
                    chunk_id + 1,
                    planned_attempts_qty,
                    func_name,
                    len(chunk),
                    self.list_field,
                )
                current_arguments_dict[self.list_field] = chunk

                aggregated_results.extend(await self._execute_with_splitting(bound_arguments.args, bound_arguments.kwargs))

        return aggregated_results
