# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from grpclib.const import Status
from grpclib.exceptions import GRPCError


def get_cv_client_exception(exception: Exception, cv_client_details: str | None = None) -> Exception or None:
    if isinstance(exception, GRPCError):
        status, message, details = exception.args
        if status == Status.NOT_FOUND:
            return CVResourceNotFound(cv_client_details, message, details)

    # Last resort return None so calling exception handling can just raise the single error instead of a chain.
    return None


class CVClientException(Exception):
    """Base exception"""


class CVResourceNotFound(CVClientException):
    """CloudVision Resource not found"""


class CVResourceInvalidState(CVClientException):
    """Invalid state for CloudVision Resource"""


class CVWorkspaceBuildTimeout(CVClientException):
    """Build of CloudVision Workspace timed out"""


class CVWorkspaceBuildFailed(CVClientException):
    """Build of CloudVision Workspace failed"""
