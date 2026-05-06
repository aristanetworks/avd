# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from contextlib import AbstractContextManager

import pytest
from test_async_decorators import CvClass

from pyavd._cv.client.exceptions import CVClientException, CVGRPCError
from pyavd._cv.client.versioning import CVAAS_VERSION_STRING, CvVersion

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]

GRPC_UNKNOWN_STATUS_TESTS = [
    # Format: servers, outer_exception
    pytest.param(
        None,
        pytest.raises(CVGRPCError),
        id="UNKNOWN_STATUS_NO_SERVERS",
    ),
    pytest.param(
        "staging.arista.io",
        pytest.raises(
            CVClientException,
            match=r"CVaaS FQDN 'staging\.arista\.io' is missing the required 'www\.' prefix\. Please use 'www\.staging\.arista\.io' instead\.",
        ),
        id="UNKNOWN_STATUS_CVAAS_MISSING_WWW_PREFIX",
    ),
    pytest.param(
        "www.staging.arista.io",
        pytest.raises(CVGRPCError),
        id="UNKNOWN_STATUS_CVAAS_WITH_WWW_PREFIX",
    ),
    pytest.param(
        "cvp.example.com",
        pytest.raises(CVGRPCError),
        id="UNKNOWN_STATUS_NON_CVAAS_FQDN",
    ),
    pytest.param(
        ["prod.arista.io", "www.prod2.arista.io"],
        pytest.raises(
            CVClientException,
            match=r"CVaaS FQDN 'prod\.arista\.io' is missing the required 'www\.' prefix\. Please use 'www\.prod\.arista\.io' instead\.",
        ),
        id="UNKNOWN_STATUS_FIRST_SERVER_MISSING_WWW",
    ),
    pytest.param(
        ["www.prod.arista.io", "prod2.arista.io"],
        pytest.raises(CVGRPCError),
        id="UNKNOWN_STATUS_FIRST_SERVER_WITH_WWW",
    ),
]


@pytest.mark.asyncio
@pytest.mark.parametrize(("servers", "outer_exception"), GRPC_UNKNOWN_STATUS_TESTS)
async def test_grpc_unknown_status_www_prefix_check(
    servers: str | list[str] | None,
    outer_exception: ExpectedExceptionContext,
) -> None:
    """Test Status.UNKNOWN raising CVClientException with a hint when a CVaaS FQDN is missing the 'www.' prefix. Falls back to CVGRPCError otherwise."""
    mocked_cv_client = CvClass(CvVersion(CVAAS_VERSION_STRING), servers=servers)
    with outer_exception:
        await mocked_cv_client.grpc_unknown_status_method()
