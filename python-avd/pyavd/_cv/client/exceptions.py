# Copyright (c) 2023-2025 Arista Networks, Inc.
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
    """Build of CloudVision Workspace failed."""


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
