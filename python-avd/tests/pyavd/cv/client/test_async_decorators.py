# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import re
from asyncio.exceptions import InvalidStateError as AsyncioInvalidStateError
from asyncio.exceptions import TimeoutError as AsyncioTimeoutError
from collections import defaultdict
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from hashlib import sha256
from itertools import pairwise
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest
from grpclib import Status
from grpclib.exceptions import GRPCError

from pyavd._cv.client.async_decorators import GRPCRequestHandler, LimitCvVersion
from pyavd._cv.client.exceptions import CVClientException, CVGRPCStatusUnavailable, CVMessageSizeExceeded, CVResourceNotFound, CVTimeoutError
from pyavd._cv.client.versioning import CVAAS_VERSION_STRING, CvVersion

LOGGER = logging.getLogger(__name__)

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]

INVALID_VERSION_TESTS = [
    # version , expected_exception
    pytest.param("2023.1.0", LookupError("Unsupported version of CloudVision: '2023.1.0'."), id="invalid_version"),
    pytest.param("223.1.0", ValueError("Invalid CV Version '223.1.0'. The version must conform to the pattern '.+'"), id="invalid_version_syntax_1"),
    pytest.param("cvaas", ValueError("Invalid CV Version 'cvaas'. The version must conform to the pattern '.+'"), id="invalid_version_syntax_2"),
]

VALID_VERSION_TESTS = [
    # Format: version , expected_response (matched_min_ver, matched_max_ver)
    pytest.param("2024.1.0", ("2024.1.0", "2024.1.99"), id="valid_version_1"),
    pytest.param("2024.1.5", ("2024.1.0", "2024.1.99"), id="valid_version_2"),
    pytest.param("2025.42.25", ("2025.1.0", "2025.99.99"), id="valid_version_3"),
    pytest.param(CVAAS_VERSION_STRING, (CVAAS_VERSION_STRING, CVAAS_VERSION_STRING), id="valid_version_4"),
]

MSG_SIZE_HANDLER_TESTS = [
    # Format: data, max_len, expected_response (list of ints where each entry is one execution and the int is the number of entries covered)
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [5, 5], id="equal_sized_chunks_1"),
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [3, 3, 3], id="equal_sized_chunks_2"),
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 1, 1, 1, 1, 1, 1, 1, 1], id="equal_sized_chunks_3"),
    # The items are chunked by calculating a ratio. This ratio rounds up, so the number of items per message is rounded down. So numbers below can look funny.
    # This is on purpose since this is actually variable sized items in bytes fitting into messages of 10MB.
    # We wish to pack many but also avoid many attempts stepping over the boundary.
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [3, 3, 3], id="variable_sized_chunks_1"),
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [4, 4, 1], id="variable_sized_chunks_2"),
]


class CvClass:
    _cv_version: CvVersion

    def __init__(self, version: CvVersion) -> None:
        self._cv_version = version
        self._grpc_call_count = defaultdict(int)
        self._grpc_msgsize_unlimited_call_count = defaultdict(int)
        self._grpc_msgsize_limited_call_count = defaultdict(lambda: defaultdict(int))

    @LimitCvVersion(min_ver="2024.1.0", max_ver="2024.1.99")
    async def version_limited_method(self) -> tuple[str, str]:
        return ("2024.1.0", "2024.1.99")

    @LimitCvVersion(min_ver="2024.2.0", max_ver="2024.99.99")
    async def version_limited_method(self) -> tuple[str, str]:  # noqa: F811
        return ("2024.2.0", "2024.99.99")

    @LimitCvVersion(min_ver="2025.1.0", max_ver="2025.99.99")
    async def version_limited_method(self) -> tuple[str, str]:  # noqa: F811
        return ("2025.1.0", "2025.99.99")

    @LimitCvVersion(min_ver=CVAAS_VERSION_STRING, max_ver=CVAAS_VERSION_STRING)
    async def version_limited_method(self) -> tuple[str, str]:  # noqa: F811
        return (CVAAS_VERSION_STRING, CVAAS_VERSION_STRING)

    @GRPCRequestHandler(list_field="field")
    async def msgsize_limited_method(self, field: list, max_accepted_len: int) -> list[bool]:
        # Check if the number of entries is higher than the max accepted length and raise.
        if len(field) > max_accepted_len:
            raise GRPCError(status=Status.RESOURCE_EXHAUSTED, message=f"grpc: received message larger than max ({len(field)} vs. {max_accepted_len})")

        # return list with len of fields for this execution.
        return [len(field)]

    @GRPCRequestHandler()
    async def msgsize_unlimited_grpc_method_success(self) -> str:
        self._grpc_msgsize_unlimited_call_count[self.msgsize_unlimited_grpc_method_success.__name__] += 1
        return "gRPC call succeeded"

    @GRPCRequestHandler()
    async def msgsize_unlimited_grpc_method_exception(self, inner_exception: Exception) -> Exception:
        self._grpc_msgsize_unlimited_call_count[self.msgsize_unlimited_grpc_method_exception.__name__] += 1
        raise inner_exception

    @GRPCRequestHandler()
    async def msgsize_unlimited_grpc_method_failure(self, failures: int = 0) -> Exception | str:
        self._grpc_msgsize_unlimited_call_count[self.msgsize_unlimited_grpc_method_failure.__name__] += 1
        if self._grpc_msgsize_unlimited_call_count[self.msgsize_unlimited_grpc_method_failure.__name__] > failures:
            return "gRPC call succeeded"
        raise GRPCError(Status.UNAVAILABLE)

    def _calculate_list_hash(self, input_list: list) -> str:
        joined = "".join([str(x) for x in input_list if x is not None])
        return sha256(joined.encode("utf-8")).hexdigest()

    @GRPCRequestHandler(list_field="field")
    async def msgsize_limited_grpc_method_success(self, field: list[int] | None = None, max_accepted_size: int = 0) -> list:
        self._grpc_msgsize_limited_call_count[self.msgsize_limited_grpc_method_success.__name__][self._calculate_list_hash(field)] += 1
        if (field_sum := sum(field)) > max_accepted_size:
            raise GRPCError(status=Status.RESOURCE_EXHAUSTED, message=f"grpc: received message larger than max ({field_sum} vs. {max_accepted_size})")
        # return list with len of fields for this execution.
        return [len(field)]

    @GRPCRequestHandler(list_field="field")
    async def msgsize_limited_grpc_method_exception(self, inner_exception: Exception, field: list[int] | None = None) -> list:
        self._grpc_msgsize_limited_call_count[self.msgsize_limited_grpc_method_exception.__name__][self._calculate_list_hash(field)] += 1
        raise inner_exception

    @GRPCRequestHandler(list_field="field")
    async def msgsize_limited_grpc_method_failure(self, failures: int = 0, field: list[int] | None = None, max_accepted_size: int = 0) -> list:
        self._grpc_msgsize_limited_call_count[self.msgsize_limited_grpc_method_failure.__name__][self._calculate_list_hash(field)] += 1
        if self._grpc_msgsize_limited_call_count[self.msgsize_limited_grpc_method_failure.__name__][self._calculate_list_hash(field)] > failures:
            if (field_sum := sum(field)) > max_accepted_size:
                raise GRPCError(status=Status.RESOURCE_EXHAUSTED, message=f"grpc: received message larger than max ({field_sum} vs. {max_accepted_size})")
            # return list with len of fields for this execution.
            return [len(field)]
        raise GRPCError(Status.UNAVAILABLE)


@pytest.mark.asyncio
@pytest.mark.parametrize(("version", "expected_exception"), INVALID_VERSION_TESTS)
async def test_invalid_versions(version: str, expected_exception: Exception) -> None:
    with pytest.raises(type(expected_exception), match=expected_exception.args[0]):
        await CvClass(CvVersion(version)).version_limited_method()


@pytest.mark.asyncio
async def test_invalid_versions_min_max_swapped() -> None:
    with pytest.raises(ValueError, match="Invalid min and max versions passed to 'cv_version' decorator. Min version must be larger than max version"):

        @LimitCvVersion(min_ver="2024.1.99", max_ver="2024.1.0")
        async def version_limited_method() -> None:
            pass


@pytest.mark.asyncio
async def test_invalid_versions_overlapping() -> None:
    with pytest.raises(ValueError, match=r"Overlapping min and max versions.*2024\.1\.0\-2024\.1\.99 overlaps with 2024\.1\.0\-2024\.1\.99\."):  # noqa: PT012

        @LimitCvVersion(min_ver="2024.1.0", max_ver="2024.1.99")
        async def version_limited_method() -> None:
            pass

        @LimitCvVersion(min_ver="2024.1.10", max_ver="2024.1.88")
        async def version_limited_method() -> None:  # noqa: F811
            pass


@pytest.mark.asyncio
@pytest.mark.parametrize(("version", "expected_response"), VALID_VERSION_TESTS)
async def test_valid_versions(version: str, expected_response: tuple[str, str]) -> None:
    resp = await CvClass(CvVersion(version)).version_limited_method()
    assert resp == expected_response


@pytest.mark.asyncio
@pytest.mark.parametrize(("data", "max_len", "expected_response"), MSG_SIZE_HANDLER_TESTS)
async def test_msg_size_handler(data: list, max_len: int, expected_response: list[int]) -> None:
    resp = await CvClass(CvVersion(CVAAS_VERSION_STRING)).msgsize_limited_method(field=data, max_accepted_len=max_len)
    assert resp == expected_response


@pytest.mark.asyncio
async def test_msg_size_handler_invalid_function_return_type() -> None:
    def function_not_returning_list(_field: list) -> str:
        return "foo"

    with pytest.raises(TypeError, match="GRPCRequestHandler decorator is unable to bind to the function .+"):
        await GRPCRequestHandler(list_field="_field")(function_not_returning_list)(["foo", "bar"])


@pytest.mark.asyncio
async def test_msg_size_handler_invalid_function_return_type_union() -> None:
    async def function_returning_union_of_list_and_string(_field: list) -> list | str:
        if len(_field) > 1:
            return _field
        return "foo"

    with pytest.raises(TypeError, match="GRPCRequestHandler decorator is unable to bind to the function .+"):
        await GRPCRequestHandler(list_field="_field")(function_returning_union_of_list_and_string)(["foo", "bar"])


@pytest.mark.asyncio
async def test_msg_size_handler_invalid_function_list_field() -> None:
    def function_with_wrong_arg(_wrong_field: list) -> list:
        return ["foo"]

    with pytest.raises(KeyError, match="GRPCRequestHandler decorator is unable to find the list_field .+"):
        await GRPCRequestHandler(list_field="_field")(function_with_wrong_arg)(["foo", "bar"])


@pytest.mark.asyncio
async def test_msg_size_handler_invalid_function_list_field_annotation_type() -> None:
    def function_with_wrong_arg_type(_field: str) -> list:
        return ["foo"]

    with pytest.raises(TypeError, match="GRPCRequestHandler decorator expected the type of the list_field.*to be defined as a list. Got"):
        await GRPCRequestHandler(list_field="_field")(function_with_wrong_arg_type)(["foo", "bar"])


@pytest.mark.asyncio
async def test_msg_size_handler_invalid_function_list_field_value_type() -> None:
    def function_with_wrong_value_type_of_field(_field: list) -> list:
        return ["foo"]

    with pytest.raises(TypeError, match="GRPCRequestHandler decorator expected the value of the list_field.*to be a list. Got"):
        await GRPCRequestHandler(list_field="_field")(function_with_wrong_value_type_of_field)("foo")


@pytest.mark.asyncio
async def test_msg_size_handler_zero_chunk_size(caplog: pytest.LogCaptureFixture) -> None:
    mocked_cv_client = CvClass(CvVersion(CVAAS_VERSION_STRING))

    with caplog.at_level(logging.DEBUG), pytest.raises(CVMessageSizeExceeded, match=r"Status\.RESOURCE_EXHAUSTED.*message larger than max \(100 vs\. 3\)"):
        await mocked_cv_client.msgsize_limited_grpc_method_success(field=[100, 100], max_accepted_size=3)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    (
        "failures",
        "async_sleep_calls",
        "log_patterns",
        "outer_exception",
    ),
    [
        pytest.param(
            1,
            1,
            [
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s",
            ],
            does_not_raise(),
            id="ONE_GRPC_STATUS_UNAVAILABLE_FAILURE",
        ),
        pytest.param(
            3,
            3,
            [
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
            ],
            does_not_raise(),
            id="THREE_GRPC_STATUS_UNAVAILABLE_FAILURES",
        ),
        pytest.param(
            6,
            5,
            [
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 4/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 5/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
            ],
            pytest.raises(CVGRPCStatusUnavailable, match="Status\\.UNAVAILABLE: 14"),
            id="SIX_GRPC_STATUS_UNAVAILABLE_FAILURES",
        ),
        pytest.param(
            7,
            5,
            [
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 4/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 5/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
            ],
            pytest.raises(CVGRPCStatusUnavailable, match="Status\\.UNAVAILABLE: 14"),
            id="SEVEN_GRPC_STATUS_UNAVAILABLE_FAILURES",
        ),
    ],
)
@pytest.mark.parametrize(
    ("grpc_method", "extra_args"),
    [
        pytest.param("msgsize_unlimited_grpc_method_failure", {}, id="UNLIMITED_SIZE_GRPC_METHOD"),
        pytest.param("msgsize_limited_grpc_method_failure", {"field": [0]}, id="LIMITED_SIZE_GRPC_METHOD"),
    ],
)
async def test_grpc_request_handler_failures(
    caplog: pytest.LogCaptureFixture,
    failures: int,
    async_sleep_calls: int,
    log_patterns: list[str],
    outer_exception: ExpectedExceptionContext,
    grpc_method: str,
    extra_args: dict[str, list[int]],
) -> None:
    with patch("pyavd._cv.client.async_decorators.asyncio_sleep", new_callable=AsyncMock) as sleep_mock:
        mocked_cv_client = CvClass(CvVersion(CVAAS_VERSION_STRING))
        with caplog.at_level(logging.WARNING), outer_exception:
            _ = await getattr(mocked_cv_client, grpc_method)(failures, **extra_args)

        # Assert that log messages match expected log patterns
        for current_pattern, current_record in zip(log_patterns, caplog.records, strict=False):
            assert re.search(re.compile(current_pattern), current_record.message)

        # Assert calls to unlimited function
        assert sleep_mock.call_count == async_sleep_calls

        # Assert usage of exponential backoff mechanism
        delay_pattern = re.compile(r"Retrying in (?P<delay>\d+)s")
        current_call_delays = [int(delay_match.group("delay")) for record in caplog.records if (delay_match := delay_pattern.search(record.message))]
        assert all((y / x == 2) for x, y in pairwise(current_call_delays))


@pytest.mark.asyncio
@pytest.mark.parametrize(
    (
        "function_calls",
        "log_patterns",
        "expected_response",
        "data",
        "max_len",
    ),
    [
        pytest.param(
            8,
            [
                "Preparing call for '.*' for list_field '.*' with 10 item.*",
                "Message size 55 exceeded the max of 15 for '.*' on list_field '.*'\\. Attempting to split 10 items.*",
                "Splitting list_field '.*' for '.*' into 5 calls with up to 2 items each.*",
                "Processing chunk 1/5 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Processing chunk 2/5 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Processing chunk 3/5 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Processing chunk 4/5 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Processing chunk 5/5 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Message size 19 exceeded the max of 15 for '.*' on list_field '.*'\\. Attempting to split 2 items.*",
                "Splitting list_field '.*' for '.*' into 2 calls with up to 1 items each.*",
                "Processing chunk 1/2 for '.*' with 1 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 1 item.*",
                "Processing chunk 2/2 for '.*' with 1 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 1 item.*",
            ],
            [2, 2, 2, 2, 1, 1],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            15,
            id="GRPC_MSG_LIMIT_EXCEEDED",
        ),
    ],
)
async def test_grpc_request_handler_limited_success(
    caplog: pytest.LogCaptureFixture,
    function_calls: int,
    log_patterns: list[str],
    expected_response: Any,
    data: list | None,
    max_len: int | None,
) -> None:
    mocked_cv_client = CvClass(CvVersion(CVAAS_VERSION_STRING))
    with caplog.at_level(logging.DEBUG):
        resp = await mocked_cv_client.msgsize_limited_grpc_method_success(data, max_len)

    # Assert number of method calls
    assert sum(mocked_cv_client._grpc_msgsize_limited_call_count["msgsize_limited_grpc_method_success"].values()) == function_calls

    # Assert that log messages match expected log patterns
    for current_pattern, current_record in zip(log_patterns, caplog.records, strict=False):
        assert re.search(re.compile(current_pattern), current_record.message)

    # Assert that method's return matches expected return
    assert resp == expected_response

    # Assert that for each data payload we used exponential backoff mechanism
    delay_pattern = re.compile(r"Retrying in (?P<delay>\d+)s")
    delay_separator_pattern = re.compile(r"Processing chunk \d+/\d+ for")
    current_call_delays = []
    for record in caplog.records:
        if delay_match := delay_pattern.search(record.message):
            current_call_delays.append(int(delay_match.group("delay")))
        elif delay_separator_pattern.search(record.message):
            # Assert that backoff mechanism used exponential delay
            assert all((y / x == 2) for x, y in pairwise(current_call_delays))
            current_call_delays = []
    if current_call_delays:
        assert all((y / x == 2) for x, y in pairwise(current_call_delays))


@pytest.mark.asyncio
@pytest.mark.parametrize(
    (
        "failures",
        "function_calls",
        "async_sleep_calls",
        "log_patterns",
        "expected_response",
        "data",
        "max_len",
    ),
    [
        pytest.param(
            3,
            44,
            33,
            [
                "Preparing call for '.*' for list_field '.*' with 11 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Message size 70 exceeded the max of 15 for '.*' on list_field '.*'\\. Attempting to split 11 items.*",
                "Splitting list_field '.*' for '.*' into 6 calls with up to 2 items each.*",
                "Processing chunk 1/6 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Processing chunk 2/6 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Processing chunk 3/6 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Message size 20 exceeded the max of 15 for '.*' on list_field '.*'\\. Attempting to split 2 items.*",
                "Splitting list_field '.*' for '.*' into 2 calls with up to 1 items each.*",
                "Processing chunk 1/2 for '.*' with 1 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 1 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Processing chunk 2/2 for '.*' with 1 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 1 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Processing chunk 4/6 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Processing chunk 5/6 for '.*' with 2 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 2 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Message size 17 exceeded the max of 15 for '.*' on list_field '.*'\\. Attempting to split 2 items.*",
                "Splitting list_field '.*' for '.*' into 2 calls with up to 1 items each.*",
                "Processing chunk 1/2 for '.*' with 1 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 1 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Processing chunk 2/2 for '.*' with 1 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 1 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Processing chunk 6/6 for '.*' with 1 item\\(s\\) from list_field '.*'\\..*",
                "Preparing call for '.*' for list_field '.*' with 1 item.*",
                "Attempt 1/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 2/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
                "Attempt 3/6 to execute call '.*' returned '.*'\\. Retrying in [0-9]+s.*",
            ],
            [2, 2, 1, 1, 2, 1, 1, 1],
            [1, 2, 3, 4, 5, 15, 6, 7, 8, 9, 10],
            15,
            id="THREE_GRPC_STATUS_UNAVAILABLE_FAILURES_GRPC_MSG_LIMIT_EXCEEDED",
        ),
    ],
)
async def test_grpc_request_handler_limited_failure_and_success(
    caplog: pytest.LogCaptureFixture,
    failures: int,
    function_calls: int,
    async_sleep_calls: int,
    log_patterns: list[str],
    expected_response: Any,
    data: list | None,
    max_len: int | None,
) -> None:
    with patch("pyavd._cv.client.async_decorators.asyncio_sleep", new_callable=AsyncMock) as sleep_mock:
        mocked_cv_client = CvClass(CvVersion(CVAAS_VERSION_STRING))
        with caplog.at_level(logging.DEBUG):
            resp = await mocked_cv_client.msgsize_limited_grpc_method_failure(failures, data, max_len)

        # Assert number of method calls
        assert sum(mocked_cv_client._grpc_msgsize_limited_call_count["msgsize_limited_grpc_method_failure"].values()) == function_calls

        # Assert number of times when delay was involved due to the received UNAVAILABLE exception
        assert sleep_mock.call_count == async_sleep_calls

        # Assert that log messages match expected log patterns
        for current_pattern, current_record in zip(log_patterns, caplog.records, strict=False):
            assert re.search(re.compile(current_pattern), current_record.message)

        # Assert that method's return matches expected return
        assert resp == expected_response

        # Assert that for each data payload we used exponential backoff mechanism
        delay_pattern = re.compile(r"Retrying in (?P<delay>\d+)s")
        delay_separator_pattern = re.compile(r"Processing chunk \d+/\d+ for")
        current_call_delays = []
        for record in caplog.records:
            if delay_match := delay_pattern.search(record.message):
                current_call_delays.append(int(delay_match.group("delay")))
            elif delay_separator_pattern.search(record.message):
                # Assert that backoff mechanism used exponential delay
                assert all((y / x == 2) for x, y in pairwise(current_call_delays))
                current_call_delays = []
        if current_call_delays:
            assert all((y / x == 2) for x, y in pairwise(current_call_delays))


@pytest.mark.asyncio
async def test_grpc_request_handler_unlimited_success(
    caplog: pytest.LogCaptureFixture,
) -> None:
    mocked_cv_client = CvClass(CvVersion(CVAAS_VERSION_STRING))
    with caplog.at_level(logging.DEBUG):
        result = await mocked_cv_client.msgsize_unlimited_grpc_method_success()

    # Assert number of method calls
    assert sum(mocked_cv_client._grpc_msgsize_unlimited_call_count.values()) == 1

    assert result == "gRPC call succeeded"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    (
        "log_patterns",
        "inner_exception",
        "outer_exception",
    ),
    [
        pytest.param(["Preparing call.*with 1 item"], AsyncioTimeoutError, pytest.raises(CVTimeoutError), id="ASYNCIO_TIMEOUTERROR_CVTIMEOUTERROR"),
        pytest.param(
            ["Preparing call.*with 1 item"],
            AsyncioInvalidStateError,
            pytest.raises(CVClientException),
            id="ASYNCIO_INVALIDSTATEERROR_ASYNCIOINVALIDSTATEERROR",
        ),
        pytest.param(
            ["Preparing call.*with 1 item"],
            GRPCError(Status.NOT_FOUND),
            pytest.raises(CVResourceNotFound, match=r"Status\.NOT_FOUND: 5"),
            id="GRPC_NOT_FOUND_CVRESOURCENOTFOUND",
        ),
        pytest.param(
            ["Preparing call.*with 1 item"],
            GRPCError(Status.CANCELLED),
            pytest.raises(CVTimeoutError, match=r"Status\.CANCELLED: 1"),
            id="GRPC_CANCELLED_CVTIMEOUTERROR",
        ),
        pytest.param(
            ["Preparing call.*with 1 item"],
            GRPCError(Status.DEADLINE_EXCEEDED),
            pytest.raises(CVClientException, match=r"Status\.DEADLINE_EXCEEDED: 4"),
            id="GRPC_DEADLINE_EXCEEDED_DEADLINE_EXCEEDED",
        ),
        pytest.param(
            ["Preparing call.*with 1 item"],
            CVResourceNotFound("Raising the same CV exception."),
            pytest.raises(CVResourceNotFound, match="Raising the same CV exception."),
            id="GRPC_DEADLINE_EXCEEDED_DEADLINE_EXCEEDED",
        ),
    ],
)
@pytest.mark.parametrize(
    ("grpc_method", "extra_args"),
    [
        pytest.param("msgsize_unlimited_grpc_method_exception", {}, id="UNLIMITED_SIZE_GRPC_METHOD"),
        pytest.param("msgsize_limited_grpc_method_exception", {"field": [0]}, id="LIMITED_SIZE_GRPC_METHOD"),
    ],
)
async def test_grpc_request_handler_exceptions(
    caplog: pytest.LogCaptureFixture,
    log_patterns: list[str],
    inner_exception: Exception | None,
    outer_exception: ExpectedExceptionContext,
    grpc_method: str,
    extra_args: dict[str, list[int]],
) -> None:
    mocked_cv_client = CvClass(CvVersion(CVAAS_VERSION_STRING))
    with caplog.at_level(logging.DEBUG), outer_exception:
        _ = await getattr(mocked_cv_client, grpc_method)(inner_exception=inner_exception, **extra_args)

    # Assert that log messages match expected log patterns
    for current_pattern, current_record in zip(log_patterns, caplog.records, strict=False):
        assert re.search(re.compile(current_pattern), current_record.message)


@pytest.mark.asyncio
async def test_grpc_request_handler_negative_max_retries() -> None:
    def basic_function() -> None:
        return

    result = await GRPCRequestHandler(max_retries=-1)(basic_function)()
    assert result is None
