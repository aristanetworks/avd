# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations


class CVClientException(Exception):  # noqa: N818
    """Base exception."""


class CVClientGRPCException(CVClientException):
    """API call failed due to a gRPC error."""


class CVTimeoutError(CVClientGRPCException):
    """API call timed out."""


class CVResourceNotFound(CVClientGRPCException):
    """CloudVision Resource not found."""


class CVResourceInvalidState(CVClientGRPCException):
    """Invalid state for CloudVision Resource."""


class CVWorkspaceBuildTimeout(CVClientGRPCException):
    """Build of CloudVision Workspace timed out."""


class CVWorkspaceBuildFailed(CVClientGRPCException):
    """Build of CloudVision Workspace failed."""


class CVWorkspaceSubmitFailed(CVClientGRPCException):
    """Failed to submit CloudVision Workspace."""


class CVWorkspaceSubmitFailedInactiveDevices(CVClientGRPCException):
    """Failed to submit CloudVision Workspace due to the presence of inactive devices."""


class CVWorkspaceStateTimeout(CVClientGRPCException):
    """Timed out waiting for Workspace to get to the expected state."""


class CVChangeControlFailed(CVClientGRPCException):
    """CloudVision ChangeControl failed during execution."""


class CVMessageSizeExceeded(CVClientGRPCException):
    """GRPC message to CloudVision exceeded the allowed message size."""

    max_size: int
    """Maximum GRPC message size"""
    size: int
    """Actual GRPC message size"""


class CVDuplicatedDevices(CVClientException):
    """Device inputs contain duplicated serial_number or system_mac_address."""


class CVGRPCStatusUnavailable(CVClientGRPCException):
    """CloudVision gRPC status is unavailable."""


class CVManifestError(CVClientException):
    """Error while creating a CVManifest instance from a user AvdManifest."""


class CVConfigletCreationFailed(CVClientGRPCException):
    """Creation of the CloudVision Static Studio configlet failed."""
