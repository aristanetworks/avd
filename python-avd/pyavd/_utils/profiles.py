# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import functools
from collections import OrderedDict
from typing import TYPE_CHECKING, Generic, Protocol, TypeVar, cast

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._schema.models.type_vars import T_AvdModel

if TYPE_CHECKING:
    from pyavd._schema.models.avd_indexed_list import AvdIndexedList
    from pyavd._schema.models.avd_model import AvdModel


T_ProfileModel = TypeVar("T_ProfileModel", bound="AvdModel")
T_TargetModel = TypeVar("T_TargetModel", bound="AvdModel")


class ProfileModelProtocol(Protocol):
    profile: str
    parent_profile: str


def resolve_profile(
    target_object: T_AvdModel,
    profile_list: AvdIndexedList[str, T_ProfileModel],
    profile_id: str | None,
) -> T_AvdModel:
    """
    Resolve the selected profile into a target input model.

    When no profile is selected, the provided target object is returned unchanged.
    Otherwise, the profile catalog is converted into a graph and the selected profile,
    including any parent profiles, is merged into a copy of the target object.

    Args:
        target_object: Input model receiving the resolved profile values.
        profile_list: Catalog of available profiles.
        profile_id: Selected profile ID to resolve.

    Returns:
        The target object with the selected profile applied.
    """
    if not profile_id:
        return target_object

    graph = _ProfileGraph._from_profile_list(profile_list, target_object)
    return graph._get_profile(profile_id)


class _ProfileGraphNode(Generic[T_AvdModel]):
    def __init__(self, profile_id: str, data: T_AvdModel | None = None) -> None:
        """
        Initialize one profile graph node.

        Args:
            profile_id: Profile ID represented by this node.
            data: Profile or target model data attached to the node.
        """
        self.profile_id: str = profile_id
        self.profile: T_AvdModel | None = data
        self.parent: _ProfileGraphNode[T_AvdModel] | None = None
        self.children: list[_ProfileGraphNode[T_AvdModel]] = []

    @functools.cached_property
    def data(self) -> T_AvdModel:
        """
        Return a deep copy of the node data.

        Access data through this property to avoid overwriting an original data. Also, this
        makes data copy a lazy operation, i.e. it's only executed if that's really needed to
        resolve profile
        """
        # Excluded from the coverage as this won't normally happen. _ProfileGraph._check_all_profiles_resolved
        # would raise an exception before reaching this point
        if self.profile is None:  # pragma: no cover
            msg = f"Profile '{self.profile_id}' is not defined"
            raise AristaAvdInvalidInputsError(msg)
        return self.profile._deepcopy()

    def _as_target_object(self, target_object_cls: type[T_TargetModel]) -> T_TargetModel:
        """
        Cast node data to the target model type.

        Args:
            target_object_cls: Target input model class to cast the profile data into.

        Returns:
            A copy of the node data cast as the target model.
        """
        return self.data._cast_as(target_object_cls, ignore_extra_keys=True)


_UnifiedGraphNode = _ProfileGraphNode[T_AvdModel | T_ProfileModel]


class _ProfileGraph(Generic[T_AvdModel, T_ProfileModel]):
    """
    Catalog graph used to resolve selected profiles and their parent profiles once per selector.

    Graph has the single root node, which essentially contains the target model (depicted by `T_AvdModel`)
    to which the profiles are applied, and the nested tree from this root node that contains objects
    of type `T_ProfileModel`.
    While `T_ProfileModel` is duck-typing the target `T_AvdModel`, there's no
    inheritance relationship between them. To keep profile resolution lazy, profile models are not
    cast into `T_AvdModel` during the graph initialization, hence the need to treat them as
    2 different types
    """

    # To avoid a slightest chance of naming conflicts we just assume it to be empty string
    ROOT_NODE_ID = ""

    def __init__(self, target_object_cls: type[T_AvdModel]) -> None:
        """
        Initialize an empty profile graph.

        Args:
            target_object_cls: Target model class used when casting profile models during resolution.
        """
        self.nodes: dict[str, _UnifiedGraphNode] = {}
        # Cache stores resolved profiles and lets later chains reuse cached ancestors.
        self._profile_cache: dict[str, T_AvdModel] = {}
        self._target_object_cls = target_object_cls

    @classmethod
    def _from_profile_list(
        cls,
        catalog_list: AvdIndexedList[str, T_ProfileModel],
        target_object: T_AvdModel,
    ) -> _ProfileGraph[T_AvdModel, T_ProfileModel]:
        """
        Build a profile graph from a profile catalog.

        Args:
            catalog_list: Profile catalog keyed by profile ID.
            target_object: Base target model used as the synthetic root profile.

        Returns:
            A validated profile graph ready for profile resolution.
        """
        target_cls = type(target_object)
        graph = cls(target_cls)

        # Initialize the synthetic root profile. Profiles without parent_profile inherit from this empty root.
        graph.nodes[cls.ROOT_NODE_ID] = _UnifiedGraphNode(cls.ROOT_NODE_ID, target_object)

        for profile_id, profile_data_item in catalog_list.items():
            profile_data = cast("ProfileModelProtocol", profile_data_item)

            # setdefault ensures each profile id gets a single graph node, even if it was referenced as a parent first.
            node = graph.nodes.setdefault(profile_id, _UnifiedGraphNode(profile_id, profile_data_item))
            parent_node = graph.nodes.setdefault(profile_data.parent_profile, _UnifiedGraphNode(profile_data.parent_profile))

            node.profile = profile_data_item
            parent_node.children.append(node)
            node.parent = parent_node

        return graph

    def _get_profile(self, profile_id: str) -> T_AvdModel:
        """
        Get the resolved model by applying the given profile.

        Args:
            profile_id: ID of the profile to apply on the target model.

        Returns:
            Target model after the profile resolution.
        """
        node = self.nodes.get(profile_id)
        if node is None:
            msg = f"Profile '{profile_id}' is missing while trying to resolve profiles for " + self._target_object_cls.__qualname__
            raise AristaAvdInvalidInputsError(msg)

        self._validate_profile_chain(node)
        return self._resolve_profile_chain(node)

    def _validate_profile_chain(self, node: _UnifiedGraphNode) -> None:
        """
        Validate one profile chain before resolving inheritance.

        Args:
            node: First node in the profile chain to validate.

        Raises:
            AristaAvdInvalidInputsError: If the chain contains a cycle or references an undefined parent profile.
        """
        visited_profile_ids: OrderedDict[str, None] = OrderedDict()
        current: _UnifiedGraphNode | None = node
        while current is not None:
            if current.profile_id in self._profile_cache:
                return

            if current.profile_id in visited_profile_ids:
                cycle_path = list(visited_profile_ids)
                cycle_path = list(reversed(cycle_path[cycle_path.index(current.profile_id) :]))
                cycle_path.append(cycle_path[0])

                msg = "Cycle detected while trying to resolve profiles for " + self._target_object_cls.__qualname__ + ": " + " -> ".join(cycle_path)
                raise AristaAvdInvalidInputsError(msg)

            visited_profile_ids[current.profile_id] = None
            if current.profile is None:
                profile_path = list(visited_profile_ids)
                msg = f"Unresolved profile `{current.profile_id}` while trying to resolve profiles for {self._target_object_cls.__qualname__}: " + " -> ".join(
                    profile_path
                )
                raise AristaAvdInvalidInputsError(msg)

            current = current.parent

    def _resolve_profile_chain(self, start_node: _UnifiedGraphNode) -> T_AvdModel:
        """
        Resolve one validated profile chain into the target model type.

        Args:
            start_node: First node in the profile chain to resolve.

        Returns:
            Target model data with parent profiles applied.
        """
        if start_node.profile_id in self._profile_cache:
            return self._profile_cache[start_node.profile_id]

        profile_chain: list[_UnifiedGraphNode] = []
        current = start_node

        while current.parent is not None:
            profile_chain.append(current)
            current = current.parent
            if current.profile_id in self._profile_cache:
                accumulated_data = self._profile_cache[current.profile_id]
                break
        else:
            accumulated_data = current._as_target_object(self._target_object_cls)
            self._profile_cache[current.profile_id] = accumulated_data

        for node in reversed(profile_chain):
            data = node._as_target_object(self._target_object_cls)
            # Current profile values are preferred over parent profile values.
            data._deepinherit(accumulated_data)
            self._profile_cache[node.profile_id] = data
            accumulated_data = data

        return accumulated_data
