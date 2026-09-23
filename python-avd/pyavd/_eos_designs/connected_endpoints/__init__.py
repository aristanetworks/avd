# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Connected-endpoints interface builder.

The package separates connected-endpoint and network-port interface generation
from the full structured-config pipeline. Regular builds adapt their full inputs,
facts, shared utilities, existing interface lists, and parent tracker into the
small context and live target exposed here. Isolated builds use the same entry
point and may pre-populate the target lists to reproduce regular-build collision
semantics.

The builder owns no target data and produces no structured config outside
Ethernet and Port-Channel interfaces. ACL and global sFlow needs are reported on
the target for the caller to handle.
"""

from .builder import build_connected_endpoints
from .context import ConnectedEndpointsBuildContext, ConnectedEndpointsDescriptionData, ConnectedEndpointsPlatformFeatures
from .target import ConnectedEndpointsBuildTarget

__all__ = [
    "ConnectedEndpointsBuildContext",
    "ConnectedEndpointsBuildTarget",
    "ConnectedEndpointsDescriptionData",
    "ConnectedEndpointsPlatformFeatures",
    "build_connected_endpoints",
]
