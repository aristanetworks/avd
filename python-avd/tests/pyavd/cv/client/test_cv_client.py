# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from unittest.mock import Mock, patch

import pytest
from requests.exceptions import HTTPError, RequestException

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("cv_token", "exception_to_raise", "expected_cv_exception"),
    [
        pytest.param(
            None,
            HTTPError,
            pytest.raises(CVClientException, match="Unable to get token from CloudVision server due to the following error"),
            id="SET_TOKEN_HTTPERROR",
        ),
        pytest.param(
            None,
            RequestException,
            pytest.raises(CVClientException, match="Unable to get token from CloudVision server due to the following error"),
            id="SET_TOKEN_REQUESTEXCEPTION",
        ),
        pytest.param(
            "cv_token",
            HTTPError,
            pytest.raises(CVClientException, match="Unable to get version from CloudVision server due to the following error"),
            id="SET_VERSION_HTTPERROR",
        ),
        pytest.param(
            "cv_token",
            RequestException,
            pytest.raises(CVClientException, match="Unable to get version from CloudVision server due to the following error"),
            id="SET_VERSION_REQUESTEXCEPTION",
        ),
    ],
)
async def test_cv_client_set_token_set_version_requests_error(
    cv_token: str | None,
    exception_to_raise: Exception,
    expected_cv_exception: ExpectedExceptionContext,
) -> None:
    mocked_response = Mock()
    mocked_response.raise_for_status.side_effect = exception_to_raise

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response),
        patch("pyavd._cv.client.post", return_value=mocked_response),
        expected_cv_exception,
    ):
        async with CVClient(
            servers="127.0.0.1",
            token=cv_token,
            username="avd_user",
            password="avd_password",  # noqa: S106
        ) as cvclient:
            await cvclient.get_inventory_devices([("", "", "spine1")])
