# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Callable, Literal

from ..api.arista.tag.v2 import (
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
from .exceptions import get_cv_client_exception

if TYPE_CHECKING:
    from .cv_client import CVClient

ELEMENT_TYPE_MAP = {
    "device": ElementType.ELEMENT_TYPE_DEVICE,
    "interface": ElementType.ELEMENT_TYPE_INTERFACE,
    None: ElementType.ELEMENT_TYPE_UNSPECIFIED,
}

CREATOR_TYPE_MAP = {
    "user": CreatorType.CREATOR_TYPE_USER,
    "system": CreatorType.CREATOR_TYPE_SYSTEM,
    "external": CreatorType.CREATOR_TYPE_EXTERNAL,
    None: CreatorType.CREATOR_TYPE_UNSPECIFIED,
}


class TagMixin:
    tags_api_version: Literal["v2"] = "v2"
    # TODO: Ensure the to document that we only support v2 of this api - hence only the CV versions supporting that.

    async def get_tags(
        self: CVClient,
        workspace_id: str,
        element_type: Literal["device", "interface"] | None = None,
        creator_type: Literal["user", "system", "external"] | None = None,
        time: datetime = None,
        timeout: float = 10.0,
    ) -> list[Tag]:
        """
        Get Tags using arista.tag.v2.TagServiceStub.GetAll arista.tag.v2.TagConfigServiceStub.GetAll APIs.

        The Tags GetAll API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the workspace tags we need to fetch mainline and then "play back" each config change from the workspace.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        TODO: Consider if we should add sub_type.

        Returns:
            Workspace object matching the workspace_id
        """
        tags = []

        request = TagStreamRequest(
            partial_eq_filter=Tag(
                # Notice the "" for workspace, since we are fetching mainline.
                key=TagKey(workspace_id="", element_type=ELEMENT_TYPE_MAP[element_type]),
                creator_type=CREATOR_TYPE_MAP[creator_type],
            ),
            time=time,
        )
        client = TagServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                tags.append(response.value)

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '' (main), Element Type '{element_type}', Creator Type '{creator_type}'") or e

        # Now tags contain all mainline tags.
        if workspace_id == "" or creator_type in ["system", "external"]:
            return tags

        # Next up fetch the tags config from the workspace if workspace is not "".
        request = TagConfigStreamRequest(
            partial_eq_filter=TagConfig(
                # This time fetch for the actual workspace we are interested in.
                key=TagKey(workspace_id=workspace_id, element_type=ELEMENT_TYPE_MAP[element_type]),
            ),
            time=time,
        )
        client = TagConfigServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                tag_config = response.value

                # Recreating a full tag object. Since this was in the workspace, it *must* be a user created tag.
                tag = Tag(key=tag_config.key, creator_type=CreatorType.CREATOR_TYPE_USER)
                if tag_config.remove:
                    self._remove_item_from_list(tag, tags, self._match_tags)
                else:
                    self._upsert_item_in_list(tag, tags, self._match_tags)
            return tags

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}', Creator Type '{creator_type}'") or e

    async def set_tags(
        self: CVClient,
        workspace_id: str,
        tags: list[tuple[str, str]],
        element_type: Literal["device", "interface"] | None = None,
        timeout: float = 10.0,
    ) -> list[Tag]:
        """
        Set Tags using arista.tag.v2.TagConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            tags: List of tuples where each tuple is in the format (<tag_label>, <tag_value>).
            timeout: Timeout in seconds.

        TODO: Consider if we should add sub_type.

        Returns:
            Workspace object matching the workspace_id
        """
        request = TagConfigSetSomeRequest(values=[])
        for label, value in tags:
            request.values.append(
                TagConfig(
                    key=TagKey(
                        workspace_id=workspace_id,
                        element_type=ELEMENT_TYPE_MAP[element_type],
                        label=label,
                        value=value,
                    )
                )
            )

        return_tags = []
        client = TagConfigServiceStub(self._channel)
        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                # Recreating a full tag object. Since we just created it, it *must* be a user created tag.
                return_tags.append(Tag(key=response.key, creator_type=CreatorType.CREATOR_TYPE_USER))
            return return_tags

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}'") or e

    async def get_tag_assignments(
        self: CVClient,
        workspace_id: str,
        element_type: Literal["device", "interface"] | None = None,
        creator_type: Literal["user", "system", "external"] | None = None,
        time: datetime = None,
        timeout: float = 10.0,
    ) -> list[TagAssignment]:
        """
        Get Tags using arista.tag.v2.TagAssignmentServiceStub.GetAll arista.tag.v2.TagAssignmentConfigServiceStub.GetAll APIs.

        The TagAssignment GetAll API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the workspace tag assignments we need to fetch mainline and then "play back" each config change from the workspace.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        TODO: Consider if we should add sub_type.

        Returns:
            Workspace object matching the workspace_id
        """
        tag_assignments = []

        request = TagAssignmentStreamRequest(
            partial_eq_filter=TagAssignment(
                # Notice the "" for workspace, since we are fetching mainline.
                key=TagAssignmentKey(workspace_id="", element_type=ELEMENT_TYPE_MAP[element_type]),
                tag_creator_type=CREATOR_TYPE_MAP[creator_type],
            ),
            time=time,
        )
        client = TagAssignmentServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                tag_assignments.append(response.value)

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '' (main), Element Type '{element_type}', Creator Type '{creator_type}'") or e

        # Now tags contain all mainline tags.
        if workspace_id == "" or creator_type in ["system", "external"]:
            return tag_assignments

        # Next up fetch the tags config from the workspace if workspace is not "".
        request = TagAssignmentConfigStreamRequest(
            partial_eq_filter=TagAssignmentConfig(
                # This time fetch for the actual workspace we are interested in.
                key=TagKey(workspace_id=workspace_id, element_type=ELEMENT_TYPE_MAP[element_type]),
            ),
            time=time,
        )
        client = TagAssignmentConfigServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                tag_assignment_config = response.value

                # Recreating a full tag object. Since this was in the workspace, it *must* be a user created tag assignment.
                tag_assignment = TagAssignment(key=tag_assignment_config.key, tag_creator_type=CreatorType.CREATOR_TYPE_USER)
                if tag_assignment_config.remove:
                    self._remove_item_from_list(tag_assignment, tag_assignments, self._match_tag_assignments)
                else:
                    self._upsert_item_in_list(tag_assignment, tag_assignments, self._match_tag_assignments)
            return tag_assignments

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}', Creator Type '{creator_type}'") or e

    async def set_tag_assignments(
        self: CVClient,
        workspace_id: str,
        tag_assignments: list[tuple[str, str, str, str | None]],
        element_type: Literal["device", "interface"] | None = None,
        timeout: float = 10.0,
    ) -> list[TagAssignment]:
        """
        Set Tags using arista.tag.v2.TagConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            tag_assignments: List of tuples where each tuple is in the format (<tag_label>, <tag_value>, <device_id/serial_number>, <interface_name | None>).
            timeout: Timeout in seconds.

        TODO: Consider if we should add sub_type.

        Returns:
            Workspace object matching the workspace_id
        """
        request = TagAssignmentConfigSetSomeRequest(values=[])
        for label, value, device_id, interface_id in tag_assignments:
            request.values.append(
                TagAssignmentConfig(
                    key=TagAssignmentKey(
                        workspace_id=workspace_id,
                        element_type=ELEMENT_TYPE_MAP[element_type],
                        label=label,
                        value=value,
                        device_id=device_id,
                        interface_id=interface_id,
                    )
                )
            )

        return_tag_assignments = []
        client = TagAssignmentConfigServiceStub(self._channel)
        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                # Recreating a full tag object. Since we just created it, it *must* be a user created tag assignment.
                return_tag_assignments.append(TagAssignment(key=response.key, creator_type=CreatorType.CREATOR_TYPE_USER))
            return return_tag_assignments

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}'") or e

    @staticmethod
    def _match_tags(a: Tag, b: Tag) -> bool:
        """
        Match up the properties of two tags without looking at the Workspace and Creator Type fields.
        """
        return all([a.key.element_type == b.key.element_type, a.key.label == b.key.label, a.key.value == b.key.value])

    @staticmethod
    def _match_tag_assignments(a: TagAssignment, b: TagAssignment) -> bool:
        """
        Match up the properties of two tag assignments without looking at the Workspace and Creator Type fields.
        """
        return all(
            [
                a.key.element_type == b.key.element_type,
                a.key.label == b.key.label,
                a.key.value == b.key.value,
                a.key.device_id == b.key.device_id,
                a.key.interface_id == b.key.interface_id,
            ]
        )

    @staticmethod
    def _remove_item_from_list(itm, lst: list, matcher: Callable) -> None:
        """
        Remove one item from the given list.

        Used for Tags and TagAssignments.

        Ignore if we are told to remove an item that is not present.
        This happens if you add a tag in a workspace and then remove it again.
        """
        for index in range(len(lst)):
            if matcher(lst[index], itm):
                lst.pop(index)
                return

    @staticmethod
    def _upsert_item_in_list(itm, lst: list, matcher: Callable) -> None:
        """
        Update or append one item from the given list.

        Used for Tags and TagAssignments.
        """
        for index in range(len(lst)):
            if matcher(lst[index], itm):
                lst[index] = itm
                return

        lst.append(itm)
