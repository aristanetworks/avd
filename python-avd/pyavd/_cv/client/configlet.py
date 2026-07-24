# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather, to_thread
from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.configlet.v1 import (
    Configlet,
    ConfigletAssignment,
    ConfigletAssignmentConfig,
    ConfigletAssignmentConfigServiceStub,
    ConfigletAssignmentConfigSetRequest,
    ConfigletAssignmentConfigSetSomeRequest,
    ConfigletAssignmentKey,
    ConfigletAssignmentServiceStub,
    ConfigletAssignmentStreamRequest,
    ConfigletConfig,
    ConfigletConfigServiceStub,
    ConfigletConfigSetRequest,
    ConfigletConfigSetSomeRequest,
    ConfigletKey,
    ConfigletServiceStub,
    ConfigletStreamRequest,
    MatchPolicy,
)
from pyavd._cv.api.arista.time import TimeBounds
from pyavd._cv.api.fmp import RepeatedString
from pyavd._utils import batch

from .async_decorators import GRPCRequestHandler, LimitCvVersion
from .constants import DEFAULT_API_TIMEOUT
from .exceptions import CVGRPCError, CVGRPCStatusUnavailable, CVMessageSizeExceeded, CVResourceNotFound, CVTimeoutError
from .models import get_required_field, get_required_fields

if TYPE_CHECKING:
    from datetime import datetime

    from . import CVClientProtocol


ASSIGNMENT_MATCH_POLICY_MAP: dict[Literal["match_first", "match_all"] | None, MatchPolicy] = {
    "match_first": MatchPolicy.MATCH_FIRST,
    "match_all": MatchPolicy.MATCH_ALL,
    None: MatchPolicy.UNSPECIFIED,
}
PARALLEL_COROUTINES = 20

LOGGER = getLogger(__name__)


class ConfigletMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    configlet_api_version: Literal["v1"] = "v1"

    @GRPCRequestHandler(retry_on_stream_reset=True)
    async def get_configlet_containers(
        self: CVClientProtocol,
        workspace_id: str,
        container_ids: list[str] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletAssignment]:
        """
        Get Configlet Containers (a.k.a. Assignments) using arista.configlet.v1.ConfigletAssignmentServiceStub.GetAll API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            container_ids: Unique identifiers for Containers/Assignments.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignment objects.
        """
        request = ConfigletAssignmentStreamRequest(partial_eq_filter=[], time=TimeBounds(start=None, end=time) if time else None)
        if container_ids:
            for container_id in container_ids:
                request.partial_eq_filter.append(
                    ConfigletAssignment(key=ConfigletAssignmentKey(workspace_id=workspace_id, configlet_assignment_id=container_id)),
                )
        else:
            request.partial_eq_filter.append(ConfigletAssignment(key=ConfigletAssignmentKey(workspace_id=workspace_id)))

        client = self.new_stub(ConfigletAssignmentServiceStub)
        responses = client.get_all(request, timeout=timeout)

        return [get_required_field(response, "value", response.value) async for response in responses]

    @GRPCRequestHandler()
    async def set_configlet_container(
        self: CVClientProtocol,
        workspace_id: str,
        container_id: str,
        display_name: str | None = None,
        description: str | None = None,
        configlet_ids: list[str] | None = None,
        query: str | None = None,
        child_assignment_ids: list[str] | None = None,
        match_policy: Literal["match_first", "match_all"] = "match_all",
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ConfigletAssignmentConfig:
        """
        Create/update a Configlet Container (a.k.a. Assignment) using arista.configlet.v1.ConfigletAssignmentConfigServiceStub.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            container_id: Unique identifier for Container/Assignment.
            display_name: Container/Assignment Name.
            description: Container/Assignment description.
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignmentConfig object after being set including any server-generated values.
        """
        request = ConfigletAssignmentConfigSetRequest(
            value=ConfigletAssignmentConfig(
                key=ConfigletAssignmentKey(workspace_id=workspace_id, configlet_assignment_id=container_id),
                display_name=display_name,
                description=description,
                configlet_ids=RepeatedString(values=configlet_ids or []),
                query=query,
                child_assignment_ids=RepeatedString(values=child_assignment_ids) if child_assignment_ids else None,
                match_policy=ASSIGNMENT_MATCH_POLICY_MAP[match_policy],
            ),
        )
        client = self.new_stub(ConfigletAssignmentConfigServiceStub)
        response = await client.set(request, timeout=timeout)

        return get_required_field(response, "value", response.value)

    @LimitCvVersion(min_ver="2024.2.0")
    @GRPCRequestHandler(list_field="containers")
    async def set_configlet_containers(  # pyright: ignore[reportRedeclaration]
        self: CVClientProtocol,
        workspace_id: str,
        containers: list[tuple[str, str | None, str | None, list[str] | None, str | None, list[str] | None, Literal["match_first", "match_all"] | None]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletAssignmentKey]:
        """
        Create/update a Configlet Container (a.k.a. Assignment) using arista.configlet.v1.ConfigletAssignmentConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            containers: List of Tuples with the format\
                (container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy).
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignmentKey objects after being set including any server-generated values.
        """
        request = ConfigletAssignmentConfigSetSomeRequest(
            values=[
                ConfigletAssignmentConfig(
                    key=ConfigletAssignmentKey(workspace_id=workspace_id, configlet_assignment_id=container_id),
                    display_name=display_name,
                    description=description,
                    configlet_ids=RepeatedString(values=configlet_ids or []),
                    query=query,
                    child_assignment_ids=RepeatedString(values=child_assignment_ids or []),
                    match_policy=ASSIGNMENT_MATCH_POLICY_MAP[match_policy or "match_all"],
                )
                for container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy in containers
            ],
        )
        client = self.new_stub(ConfigletAssignmentConfigServiceStub)
        responses = client.set_some(request, timeout=timeout)

        return [get_required_field(response, "key", response.key) async for response in responses]

    # Use this variant for versions below 2024.2.0 (still respecting overall min version)
    @LimitCvVersion(max_ver="2024.1.99")
    @GRPCRequestHandler()
    async def set_configlet_containers(  # noqa: F811 - Redefining with decorator.
        self: CVClientProtocol,
        workspace_id: str,
        containers: list[tuple[str, str | None, str | None, list[str] | None, str | None, list[str] | None, Literal["match_first", "match_all"] | None]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletAssignmentConfig]:
        """
        Create batches of containers and do parallel calls to set_configlet_container for each batch.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            containers: List of Tuples with the format\
                (container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy).
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignmentKey objects after being set including any server-generated values.
        """
        coroutines = [
            self.set_configlet_container(
                workspace_id=workspace_id,
                container_id=container_id,
                display_name=display_name,
                description=description,
                configlet_ids=configlet_ids,
                query=query,
                child_assignment_ids=child_assignment_ids,
                match_policy=match_policy or "match_all",
                timeout=timeout,
            )
            for container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy in containers
        ]

        configlet_configs = []

        LOGGER.info("set_configlet_containers: Deploying %s configlet assignments / containers in batches of %s.", len(coroutines), PARALLEL_COROUTINES)
        for index, batch_coroutines in enumerate(batch(coroutines, PARALLEL_COROUTINES), start=1):
            LOGGER.info("set_configlet_containers: Batch %s", index)
            configlet_configs.extend(await gather(*batch_coroutines))

        # TODO: This fallback ignores the batched results above and calls the API a second time.
        # It also returns ConfigletAssignmentConfig objects despite the annotated ConfigletAssignmentKey return type.
        return [
            await self.set_configlet_container(
                workspace_id, container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy or "match_all", timeout
            )
            for container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy in containers
        ]

    @GRPCRequestHandler()
    async def delete_configlet_container(
        self: CVClientProtocol,
        workspace_id: str,
        assignment_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ConfigletAssignmentConfig:
        """
        Delete a Configlet Container (a.k.a. Assignment) using arista.configlet.v1.ConfigletAssignmentConfigServiceStub.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            assignment_id: Unique identifier for Container/Assignment.

        Returns:
            ConfigletAssignmentConfig object after being set including any server-generated values.
        """
        request = ConfigletAssignmentConfigSetRequest(
            value=ConfigletAssignmentConfig(
                key=ConfigletAssignmentKey(workspace_id=workspace_id, configlet_assignment_id=assignment_id),
                remove=True,
            ),
        )
        client = self.new_stub(ConfigletAssignmentConfigServiceStub)
        response = await client.set(request, timeout=timeout)

        return get_required_field(response, "value", response.value)

    @GRPCRequestHandler(list_field="configlet_ids", retry_on_stream_reset=True)
    async def get_configlets(
        self: CVClientProtocol,
        workspace_id: str,
        configlet_ids: list[str] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[Configlet]:
        """
        Get Configlets using arista.configlet.v1.ConfigletServiceStub.GetAll API.

        Missing objects will not produce an error.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            configlet_ids: Unique identifiers for Configlets. If not set the function will return all configlets.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            List of matching Configlet objects.
        """
        request = ConfigletStreamRequest(partial_eq_filter=[], time=TimeBounds(start=None, end=time) if time else None)
        if configlet_ids:
            for configlet_id in configlet_ids:
                request.partial_eq_filter.append(Configlet(key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id)))
        else:
            request.partial_eq_filter.append(Configlet(key=ConfigletKey(workspace_id=workspace_id)))

        client = self.new_stub(ConfigletServiceStub)

        responses = client.get_all(request, timeout=timeout)

        return [get_required_field(response, "value", response.value) async for response in responses]

    @GRPCRequestHandler()
    async def set_configlet(
        self: CVClientProtocol,
        workspace_id: str,
        configlet_id: str,
        display_name: str | None = None,
        description: str | None = None,
        body: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ConfigletConfig:
        """
        Create/update a Configlet using arista.configlet.v1.ConfigletConfigServiceStub.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlet_id: Unique identifier for Configlet.
            display_name: Configlet Name.
            description: Configlet description.
            body: EOS Configuration.
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignment object after being set including any server-generated values.
        """
        request = ConfigletConfigSetRequest(
            value=ConfigletConfig(
                key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                display_name=display_name,
                description=description,
                body=body,
            ),
        )
        client = self.new_stub(ConfigletConfigServiceStub)
        response = await client.set(request, timeout=timeout)

        return get_required_field(response, "value", response.value)

    @GRPCRequestHandler()
    async def set_configlet_from_file(
        self: CVClientProtocol,
        workspace_id: str,
        configlet_id: str,
        file: str,
        display_name: str | None = None,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ConfigletConfig:
        """
        Create/update a Configlet using arista.configlet.v1.ConfigletConfigServiceStub.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlet_id: Unique identifier for Configlet.
            file: Path to file containing EOS Configuration.
            display_name: Configlet Name.
            description: Configlet description.
            timeout: Timeout in seconds.

        Returns:
            ConfigletConfig object after being set including any server-generated values.
        """
        request = ConfigletConfigSetRequest(
            value=ConfigletConfig(
                key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                display_name=display_name,
                description=description,
                body=await to_thread(Path.read_text, Path(file), encoding="UTF-8"),
            ),
        )
        client = self.new_stub(ConfigletConfigServiceStub)
        response = await client.set(request, timeout=timeout)

        return get_required_field(response, "value", response.value)

    @LimitCvVersion(min_ver="2024.2.0")
    @GRPCRequestHandler(list_field="configlets", check_bulk_response_errors=True)
    async def set_configlets_from_files(  # pyright: ignore[reportRedeclaration]
        self: CVClientProtocol,
        workspace_id: str,
        configlets: list[tuple[str, str, str, str]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[tuple[ConfigletKey, str]]:
        """
        Create/update multiple Configlets using arista.configlet.v1.ConfigletConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlets: List of Tuples with the format `(configlet_id, display_name, description, path_to_config_file)`.
            timeout: Timeout in seconds.

        Returns:
            List of (<ConfigletKey>, <gRPC error message>) tuples for Configlets that failed to be created/updated due to encountered gRPC error.
        """
        request = ConfigletConfigSetSomeRequest(values=[])
        for configlet in configlets:
            configlet_id, display_name, description, file = configlet
            request.values.append(
                ConfigletConfig(
                    key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                    display_name=display_name,
                    description=description,
                    body=await to_thread(Path.read_text, Path(file), encoding="UTF-8"),
                )
            )
        client = self.new_stub(ConfigletConfigServiceStub)

        responses = client.set_some(request, timeout=timeout)

        return [get_required_fields(response, ("key", "error"), (response.key, response.error)) async for response in responses]

    # Use this variant for versions below 2024.2.0 (still respecting overall min version)
    @LimitCvVersion(max_ver="2024.1.99")
    @GRPCRequestHandler(check_bulk_response_errors=True)
    async def set_configlets_from_files(  # noqa: F811 - Redefining with decorator.
        self: CVClientProtocol,
        workspace_id: str,
        configlets: list[tuple[str, str, str, str]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[tuple[ConfigletKey, str]]:
        """
        Create batches of configlets and do parallel calls to set_configlet_from_file for each batch.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlets: List of Tuples with the format `(configlet_id, display_name, description, path_to_config_file)`.
            timeout: Timeout in seconds.

        Returns:
            List of (<ConfigletKey>, <gRPC error message>) tuples for Configlets that failed to be created/updated due to encountered gRPC error.
        """
        responses_with_errors: list[tuple[ConfigletKey, str]] = []

        coroutines = [
            self.set_configlet_from_file(
                workspace_id=workspace_id,
                configlet_id=configlet_id,
                file=file,
                display_name=display_name,
                description=description,
                timeout=timeout,
            )
            for configlet_id, display_name, description, file in configlets
        ]

        LOGGER.info("set_configlets_from_files: Deploying %s configlets in batches of %s.", len(coroutines), PARALLEL_COROUTINES)
        batch_offset = 0
        for index, batch_coroutines in enumerate(batch(coroutines, PARALLEL_COROUTINES), start=1):
            LOGGER.info("set_configlets_from_files: Batch %s", index)

            # Pre work for mapping configlet tuples to coroutines.
            batch_size = len(batch_coroutines)
            batch_configlets = configlets[batch_offset : batch_offset + batch_size]
            batch_offset += batch_size

            # Results are returned in the same order as the coroutines.
            # Coroutines will either return a ConfigletConfig object (for successful deployment) or an Exception (for a failed deployment).
            configlet_configs = await gather(*batch_coroutines, return_exceptions=True)

            # Process results of each batch. Collect all Cloudvision/GRPC-related exceptions. Raise for any other type of Exception.
            for (configlet_id, _, _, _), configlet_config in zip(batch_configlets, configlet_configs, strict=False):
                # Append all Cloudvision/GRPC-related errors to the list of responses_with_errors.
                if isinstance(
                    configlet_config,
                    (
                        CVTimeoutError,
                        CVResourceNotFound,
                        CVGRPCStatusUnavailable,
                        CVMessageSizeExceeded,
                        CVGRPCError,
                    ),
                ):
                    # Attempt to fetch reason of the original gRPC exception.
                    try:
                        error_message = (
                            f"{configlet_config.args[0]}: {configlet_config.args[1]}"
                            if len(configlet_config.args) > 1 and isinstance(configlet_config.args[1], str)
                            else str(configlet_config.args[0])  # pyright: ignore[reportGeneralTypeIssues]
                        )
                    # fall back to the full error if not possible
                    except (AttributeError, IndexError):
                        error_message = str(configlet_config)
                    responses_with_errors.append(
                        (
                            ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                            error_message,
                        )
                    )
                # Raise immediately for any other type of Exception (FileNotFound, etc.).
                elif isinstance(configlet_config, Exception):
                    raise configlet_config
                # configlet_config is not an Exception and is a ConfigletConfig object, meaning the Configlet was successfully deployed.
                else:
                    # We do not return anything here to have a consistent behavior with 2024.2.0+ implementation of the 'set_configlets_from_files' method.
                    pass

        return responses_with_errors

    @GRPCRequestHandler(list_field="configlet_ids")
    async def delete_configlets(
        self: CVClientProtocol,
        workspace_id: str,
        configlet_ids: list[str],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletKey]:
        """
        Delete a Configlet using arista.configlet.v1.ConfigletConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlet_ids: List of unique identifiers for Configlets to delete.
            timeout: Timeout in seconds.

        Returns:
            List of ConfigletKey objects after being deleted including any server-generated values.
        """
        request = ConfigletConfigSetSomeRequest(values=[])
        for configlet_id in configlet_ids:
            request.values.append(
                ConfigletConfig(
                    key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                    remove=True,
                ),
            )
        client = self.new_stub(ConfigletConfigServiceStub)

        responses = client.set_some(request, timeout=timeout)

        return [get_required_field(response, "key", response.key) async for response in responses]
