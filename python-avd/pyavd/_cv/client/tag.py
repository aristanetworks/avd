# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.tag.v2 import (
    CreatorType,
    ElementType,
    Tag,
    TagAssignment,
    TagAssignmentConfig,
    TagAssignmentConfigServiceStub,
    TagAssignmentConfigSetSomeRequest,
    TagAssignmentConfigStreamRequest,
    TagAssignmentKey,
    TagAssignmentServiceStub,
    TagAssignmentStreamRequest,
    TagConfig,
    TagConfigServiceStub,
    TagConfigSetSomeRequest,
    TagConfigStreamRequest,
    TagKey,
    TagServiceStub,
    TagStreamRequest,
)
from pyavd._cv.api.arista.time import TimeBounds

from .async_decorators import GRPCRequestHandler
from .constants import DEFAULT_API_TIMEOUT

if TYPE_CHECKING:
    from datetime import datetime

    from . import CVClientProtocol
    from .models import CVTag, CVTagAssignment


ELEMENT_TYPE_MAP = {
    "device": ElementType.DEVICE,
    "interface": ElementType.INTERFACE,
    None: ElementType.UNSPECIFIED,
}

CREATOR_TYPE_MAP = {
    "user": CreatorType.USER,
    "system": CreatorType.SYSTEM,
    "external": CreatorType.EXTERNAL,
    None: CreatorType.UNSPECIFIED,
}


class TagMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    tags_api_version: Literal["v2"] = "v2"

    @GRPCRequestHandler()
    async def get_tags(
        self: CVClientProtocol,
        workspace_id: str,
        element_type: Literal["device", "interface"] | None = None,
        creator_type: Literal["user", "system", "external"] | None = None,
        time: datetime | None = None,
        timeout: float = 30.0,
    ) -> list[Tag]:
        """
        Get Tags using arista.tag.v2.TagServiceStub.GetAll arista.tag.v2.TagConfigServiceStub.GetAll APIs.

        The Tags GetAll API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the workspace tags we need to fetch mainline and then "play back" each config change from the workspace.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            element_type: Optionally filter tags on type.
            creator_type: Optionally filter tags on creator type.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            List of Tag objects.
        """
        request = TagStreamRequest(
            partial_eq_filter=Tag(
                # Notice the "" for workspace, since we are fetching mainline.
                key=TagKey(workspace_id="", element_type=ELEMENT_TYPE_MAP[element_type]),
                creator_type=CREATOR_TYPE_MAP[creator_type],
            ),
            time=TimeBounds(start=None, end=time),
        )
        client = TagServiceStub(self._channel)
        responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
        tags = [response.value async for response in responses]

        # Now tags contain all mainline tags.
        if workspace_id == "" or creator_type in ["system", "external"]:
            return tags

        # Next up fetch the tags config from the workspace if workspace is not "".
        request = TagConfigStreamRequest(
            partial_eq_filter=TagConfig(
                # This time fetch for the actual workspace we are interested in.
                key=TagKey(workspace_id=workspace_id, element_type=ELEMENT_TYPE_MAP[element_type]),
            ),
            time=TimeBounds(start=None, end=time),
        )
        client = TagConfigServiceStub(self._channel)
        responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
        async for response in responses:
            tag_config = response.value

            # Recreating a full tag object. Since this was in the workspace, it *must* be a user created tag.
            tag = Tag(key=tag_config.key, creator_type=CreatorType.USER)
            if tag_config.remove:
                self._remove_item_from_list(tag, tags, self._match_tags)
            else:
                self._upsert_item_in_list(tag, tags, self._match_tags)

        return tags

    @GRPCRequestHandler()
    async def set_tags(
        self: CVClientProtocol,
        workspace_id: str,
        tags: set[CVTag],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[TagKey]:
        """
        Set Tags using arista.tag.v2.TagConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            tags: Set of `CVTag` tag objects to be added.
            timeout: Base timeout in seconds. 0.1 second will be added per `CVTag`.

        Returns:
            List of Tag objects after being set including any server-generated values.
        """
        request = TagConfigSetSomeRequest(values=[])
        for tag in tags:
            request.values.append(
                TagConfig(
                    key=TagKey(
                        workspace_id=workspace_id,
                        element_type=tag.get_element_type(),
                        label=tag.label,
                        value=tag.value,
                    ),
                ),
            )

        client = TagConfigServiceStub(self._channel)
        responses = client.set_some(request, metadata=self._metadata, timeout=timeout + len(request.values) * 0.1)

        return [response.key async for response in responses]

    @GRPCRequestHandler()
    async def get_tag_assignments(
        self: CVClientProtocol,
        workspace_id: str,
        element_type: Literal["device", "interface"] | None = None,
        creator_type: Literal["user", "system", "external"] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[TagAssignment]:
        """
        Get Tags using arista.tag.v2.TagAssignmentServiceStub.GetAll arista.tag.v2.TagAssignmentConfigServiceStub.GetAll APIs.

        The TagAssignment GetAll API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the workspace tag assignments we need to fetch mainline and then "play back" each config change from the workspace.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            element_type: Optionally filter tag assignments on tag type.
            creator_type: Optionally filter tag assignments on tag creator type.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Workspace object matching the workspace_id
        """
        request = TagAssignmentStreamRequest(
            partial_eq_filter=TagAssignment(
                # Notice the "" for workspace, since we are fetching mainline.
                key=TagAssignmentKey(workspace_id="", element_type=ELEMENT_TYPE_MAP[element_type]),
                tag_creator_type=CREATOR_TYPE_MAP[creator_type],
            ),
            time=TimeBounds(start=None, end=time),
        )
        client = TagAssignmentServiceStub(self._channel)
        responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
        tag_assignments = [response.value async for response in responses]

        # Now tags contain all mainline tags.
        if workspace_id == "" or creator_type in ["system", "external"]:
            return tag_assignments

        # Next up fetch the tags config from the workspace if workspace is not "".
        request = TagAssignmentConfigStreamRequest(
            partial_eq_filter=TagAssignmentConfig(
                # This time fetch for the actual workspace we are interested in.
                key=TagKey(workspace_id=workspace_id, element_type=ELEMENT_TYPE_MAP[element_type]),
            ),
            time=TimeBounds(start=None, end=time),
        )
        client = TagAssignmentConfigServiceStub(self._channel)
        responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
        async for response in responses:
            tag_assignment_config = response.value

            # Recreating a full tag object. Since this was in the workspace, it *must* be a user created tag assignment.
            tag_assignment = TagAssignment(key=tag_assignment_config.key, tag_creator_type=CreatorType.USER)
            if tag_assignment_config.remove:
                self._remove_item_from_list(tag_assignment, tag_assignments, self._match_tag_assignments)
            else:
                self._upsert_item_in_list(tag_assignment, tag_assignments, self._match_tag_assignments)

        return tag_assignments

    @GRPCRequestHandler()
    async def set_tag_assignments(
        self: CVClientProtocol,
        workspace_id: str,
        tag_assignments: set[CVTagAssignment],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[TagAssignmentKey]:
        """
        Set Tags using arista.tag.v2.TagAssignmentConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            tag_assignments: Set of `CVTagAssignment` tag assignment objects to be added.
            timeout: Base timeout in seconds. 0.1 second will be added per `CVTagAssignment`.

        Returns:
            List of TagAssignmentKey objects after being set including any server-generated values.
        """
        request = TagAssignmentConfigSetSomeRequest(values=[])
        for tag_assignment in tag_assignments:
            request.values.append(
                TagAssignmentConfig(
                    key=TagAssignmentKey(
                        workspace_id=workspace_id,
                        element_type=tag_assignment.get_element_type(),
                        label=tag_assignment.label,
                        value=tag_assignment.value,
                        device_id=tag_assignment.device_id,
                        interface_id=tag_assignment.interface_id,
                    ),
                ),
            )

        client = TagAssignmentConfigServiceStub(self._channel)
        responses = client.set_some(request, metadata=self._metadata, timeout=timeout + len(request.values) * 0.1)

        return [response.key async for response in responses]

    @GRPCRequestHandler()
    async def delete_tag_assignments(
        self: CVClientProtocol,
        workspace_id: str,
        tag_assignments: set[CVTagAssignment],
        timeout: float = 30.0,
    ) -> list[TagAssignmentKey]:
        """
        Set Tags using arista.tag.v2.TagAssignmentConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            tag_assignments: Set of `CVTagAssignment` tag assignment objects to be removed.
            timeout: Base timeout in seconds. 0.1 second will be added per `CVTagAssignment`.

        Returns:
            List of TagAssignmentKey objects after being set including any server-generated values.
        """
        request = TagAssignmentConfigSetSomeRequest(values=[])
        for tag_assignment in tag_assignments:
            request.values.append(
                TagAssignmentConfig(
                    key=TagAssignmentKey(
                        workspace_id=workspace_id,
                        element_type=tag_assignment.get_element_type(),
                        label=tag_assignment.label,
                        value=tag_assignment.value,
                        device_id=tag_assignment.device_id,
                        interface_id=tag_assignment.interface_id,
                    ),
                    remove=True,
                ),
            )

        client = TagAssignmentConfigServiceStub(self._channel)
        responses = client.set_some(request, metadata=self._metadata, timeout=timeout + len(request.values) * 0.1)

        return [response.key async for response in responses]

    @staticmethod
    def _match_tags(a: Tag, b: Tag) -> bool:
        """Match up the properties of two tags without looking at the Workspace and Creator Type fields."""
        return all([a.key.element_type == b.key.element_type, a.key.label == b.key.label, a.key.value == b.key.value])

    @staticmethod
    def _match_tag_assignments(a: TagAssignment, b: TagAssignment) -> bool:
        """Match up the properties of two tag assignments without looking at the Workspace and Creator Type fields."""
        return all(
            [
                a.key.element_type == b.key.element_type,
                a.key.label == b.key.label,
                a.key.value == b.key.value,
                a.key.device_id == b.key.device_id,
                a.key.interface_id == b.key.interface_id,
            ],
        )
