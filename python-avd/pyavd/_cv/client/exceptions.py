# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio.exceptions import TimeoutError

from grpclib.const import Status
from grpclib.exceptions import GRPCError


def get_cv_client_exception(exception: Exception, cv_client_details: str | None = None) -> Exception | None:
    """
    Convert GRPCError or TimeoutError instances to an instance of the relevant subclass of CVClientException.

    Parameters:
        exception: Exception to convert.

    Returns:
        None if If the exception is unmatched, otherwise an instance of the relevant CVClientException subclass.
    """
    if isinstance(exception, GRPCError):
        status = exception.args[0]
        if status == Status.NOT_FOUND:
            return CVResourceNotFound(cv_client_details, *exception.args)
        if status == Status.CANCELLED:
            return CVTimeoutError(cv_client_details, *exception.args)
    if isinstance(exception, TimeoutError):
        return CVTimeoutError(cv_client_details, *exception.args)

    # Last resort return None so calling exception handling can just raise the single error instead of a chain.
    return None


class CVClientException(Exception):
    """Base exception"""


class CVTimeoutError(CVClientException):
    """API call timed out"""


class CVResourceNotFound(CVClientException):
    """CloudVision Resource not found"""


class CVResourceInvalidState(CVClientException):
    """Invalid state for CloudVision Resource"""


class CVWorkspaceBuildTimeout(CVClientException):
    """Build of CloudVision Workspace timed out"""


class CVWorkspaceBuildFailed(CVClientException):
    """Build of CloudVision Workspace failed"""


class CVWorkspaceSubmitFailed(CVClientException):
    """Build of CloudVision Workspace failed"""


class CVWorkspaceStateTimeout(CVClientException):
    """Timed out waiting for Workspace to get to the expected state"""


class CVChangeControlFailed(CVClientException):
    """CloudVision ChangeControl failed during execution"""
