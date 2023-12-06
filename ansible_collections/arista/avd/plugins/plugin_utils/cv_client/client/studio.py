# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Literal

from ..api.arista.studio.v1 import Studio, StudioKey, StudioRequest, StudioServiceStub

if TYPE_CHECKING:
    from .cv_client import CVClient


class StudioMixin:
    """
    Only to be used as mixin on CVClient class.
    """

    studio_api_version: Literal["v1"] = "v1"

    async def get_studio(
        self: CVClient,
        studio_id: str,
        workspace_id: str,
        time: datetime = None,
        timeout: float = 10.0,
    ) -> Studio:
        """
        Get Studio using arista.studio.v1.StudioService.GetOne API

        Parameters:
            studio_id: Unique identifier for the studio in the workspace indicated by workspace_id.
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Studio object matching the studio_id and workspace_id
        """
        request = StudioRequest(
            key=StudioKey(
                studio_id=studio_id,
                workspace_id=workspace_id,
            ),
            time=time,
        )
        client = StudioServiceStub(self._channel)
        response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
        return response.value
