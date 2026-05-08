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
        "cvp.example.com",
        pytest.raises(CVGRPCError),
        id="UNKNOWN_STATUS_ONPREM_FQDN",
    ),
    pytest.param(
        "www.cv-prod-us-central1-a.arista.io",
        pytest.raises(CVGRPCError),
        id="UNKNOWN_STATUS_CVAAS_API_ENDPOINT",
    ),
    pytest.param(
        "cv-prod-us-central1-a.arista.io",
        pytest.raises(
            CVClientException,
            match=(
                r"CVaaS FQDN 'cv-prod-us-central1-a\.arista\.io' is missing the required 'www\.' prefix\. "
                r"Please use 'www\.cv-prod-us-central1-a\.arista\.io' instead\."
            ),
        ),
        id="UNKNOWN_STATUS_CVAAS_BASE_FQDN",
    ),
    pytest.param(
        "apiserver.cv-prod-us-4.arista.io",
        pytest.raises(
            CVClientException,
            match=(
                r"CVaaS FQDN 'apiserver\.cv-prod-us-4\.arista\.io' is pointing to the streaming endpoint\. "
                r"Please use API endpoint 'www\.cv-prod-us-4\.arista\.io' instead\."
            ),
        ),
        id="UNKNOWN_STATUS_CVAAS_STREAMING_ENDPOINT",
    ),
    pytest.param(
        "www.incorrect-cluster.arista.io",
        pytest.raises(
            CVClientException,
            match=r"Provided CVaaS FQDN 'www\.incorrect-cluster\.arista\.io' may be incorrect\.",
        ),
        id="UNKNOWN_STATUS_CVAAS_UNKNOWN_ARISTA_IO_FQDN",
    ),
    # Only the first server is checked.
    pytest.param(
        ["arista.io", "www.cv-prod-us-central1-a.arista.io"],
        pytest.raises(
            CVClientException,
            match=r"CVaaS FQDN 'arista\.io' is missing the required 'www\.' prefix\.",
        ),
        id="UNKNOWN_STATUS_FIRST_SERVER_BASE_FQDN",
    ),
    pytest.param(
        ["www.arista.io", "arista.io"],
        pytest.raises(CVGRPCError),
        id="UNKNOWN_STATUS_FIRST_SERVER_CORRECT_API_ENDPOINT",
    ),
]


@pytest.mark.asyncio
@pytest.mark.parametrize(("servers", "outer_exception"), GRPC_UNKNOWN_STATUS_TESTS)
async def test_grpc_unknown_status_cvaas_fqdn_check(
    servers: str | list[str] | None,
    outer_exception: ExpectedExceptionContext,
) -> None:
    """Test Status.UNKNOWN handling."""
    mocked_cv_client = CvClass(CvVersion(CVAAS_VERSION_STRING), servers=servers)
    with outer_exception:
        await mocked_cv_client.grpc_unknown_status_method()
