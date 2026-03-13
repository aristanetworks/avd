# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations


class CVClientException(Exception):  # noqa: N818
    """Base exception."""


class CVTimeoutError(CVClientException):
    """API call timed out."""


class CVResourceNotFound(CVClientException):
    """CloudVision Resource not found."""


class CVResourceInvalidState(CVClientException):
    """Invalid state for CloudVision Resource."""


class CVWorkspaceBuildTimeout(CVClientException):
    """Build of CloudVision Workspace timed out."""


class CVWorkspaceBuildFailed(CVClientException):
    """Build of CloudVision Workspace failed."""


class CVWorkspaceSubmitFailed(CVClientException):
    """Failed to submit CloudVision Workspace."""


class CVWorkspaceSubmitFailedInactiveDevices(CVClientException):
    """Failed to submit CloudVision Workspace due to the presence of inactive devices."""


class CVWorkspaceStateTimeout(CVClientException):
    """Timed out waiting for Workspace to get to the expected state."""


class CVChangeControlFailed(CVClientException):
    """CloudVision ChangeControl failed during execution."""


class CVMessageSizeExceeded(CVClientException):
    """GRPC message to CloudVision exceeded the allowed message size."""

    max_size: int
    """Maximum GRPC message size"""
    size: int
    """Actual GRPC message size"""


class CVDuplicatedDevices(CVClientException):
    """Device inputs contain duplicated serial_number or system_mac_address."""


class CVGRPCStatusUnavailable(CVClientException):
    """CloudVision gRPC status is unavailable."""


class CVManifestError(CVClientException):
    """Error while creating a CVManifest instance from a user AvdManifest."""


class CVConfigletCreationFailed(CVClientException):
    """Creation of the CloudVision Static Studio configlet failed."""


class CVClientBulkAPIError(CVClientException):
    """Bulk API call failed due to server-side error(s). See logging for details."""

    cv_client_method_name: str
    """Name of the CVClient method that failed."""
    number_of_errors: int
    """Number of returned errors."""

    def __init__(self, cv_client_method_name: str, number_of_errors: int) -> None:
        self.cv_client_method_name = cv_client_method_name
        self.number_of_errors = number_of_errors
        msg = (
            f"{number_of_errors} server-side error(s) was returned from the '{self.cv_client_method_name}' bulk API call. "
            "Please check logs for the failed items and error messages."
        )
        super().__init__(msg)


class CVGRPCError(CVClientException):
    """GRPC call failed."""
