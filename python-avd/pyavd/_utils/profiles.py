# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import functools
from collections import OrderedDict
from typing import TYPE_CHECKING, Any, Generic, Protocol, TypeVar, cast

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._schema.models.type_vars import T_AvdModel

if TYPE_CHECKING:
    from pyavd._schema.models.avd_indexed_list import AvdIndexedList
    from pyavd._schema.models.avd_model import AvdModel


T_ProfileModel = TypeVar("T_ProfileModel", bound="AvdModel")


class _ProfileModelProtocol(Protocol):
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

    graph = _ProfileGraph(target_object, profile_list)
    graph_node = graph._get_profile(profile_id)
    return graph_node._deepinherit


class _ProfileGraphNode(Generic[T_AvdModel, T_ProfileModel]):
    """Lazy object to work with the target models and profiles applied to it."""

    def __init__(self, profile_id: str, target_cls: type[T_AvdModel], data: T_AvdModel | T_ProfileModel) -> None:
        """
        Initialize one profile graph node.

        Args:
            profile_id: Profile ID represented by this node.
            target_cls: Class of the model that the profile is applied to
            data: Profile or target model data attached to the node.
        """
        self.profile_id: str = profile_id
        self.profile: T_AvdModel | T_ProfileModel = data
        self.parent: _ProfileGraphNode[T_AvdModel, T_ProfileModel] | None = None
        self.children: list[_ProfileGraphNode[T_AvdModel, T_ProfileModel]] = []
        self.target_cls = target_cls

    def copy_data(self) -> T_AvdModel:
        """
        Return a deep copy of the node data.

        Access data through this property to avoid overwriting an original data. Also, this
        makes data copy a lazy operation, i.e. it's only executed if that's really needed to
        resolve profile
        """
        data = self.profile._deepcopy()
        if not isinstance(data, self.target_cls):
            data = data._cast_as(self.target_cls, ignore_extra_keys=True)
        return data

    @functools.cached_property
    def _deepinherit(self) -> T_AvdModel:
        """
        Get the target model with all profile chain applied to it.

        Child profile attributes take precedence over parent profile. Target model's attributes take precedence
        over profile's attributes.
        """
        data = self.copy_data()
        if self.parent is not None:
            data._deepinherit(self.parent._deepinherit)
        return data


_UnifiedGraphNode = _ProfileGraphNode[T_AvdModel, T_ProfileModel]


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

    def __init__(self, target_object: T_AvdModel, profile_catalog: AvdIndexedList[str, T_ProfileModel]) -> None:
        """
        Initialize an empty profile graph.

        Args:
            target_object_cls: Target model class used when casting profile models during resolution.
            profile_catalog: Profile catalog keyed by profile ID.
            target_object: Base target model used as the synthetic root profile.
        """
        self._target_object_cls = type(target_object)

        self.nodes: dict[str, _UnifiedGraphNode] = {self.ROOT_NODE_ID: _UnifiedGraphNode(self.ROOT_NODE_ID, self._target_object_cls, target_object)}

        self._profiles_mapping = profile_catalog

    def __get_profile_node(self, profile_id: str, visited: OrderedDict[str, Any] | None = None) -> _UnifiedGraphNode:
        """
        Lazily resolve the profile chain into graph.

        This method traverses the parent chain defined by profile/parent_profile fields and checks if it is valid
        (no circular dependencies between profiles and all profiles in the chain must be present in the catalog).

        It's meant to be an internal method, use `_get_profile()` instead

        Args:
            profile_id: Profile key to look-up for
            visited: Ordered set populated as the recursion progresses through `parent_profile` refs

        Returns:
            Profile graph branch represented by the profile key.
        """
        if visited is None:
            visited = OrderedDict()

        # O(1) check for cycles
        if profile_id in visited:
            cycle_path = list(visited)
            cycle_path = list(reversed(cycle_path[cycle_path.index(profile_id) :]))
            cycle_path.append(cycle_path[0])

            msg = "Cycle detected while trying to resolve profiles for " + self._target_object_cls.__qualname__ + ": " + " -> ".join(cycle_path)
            raise AristaAvdInvalidInputsError(msg)

        visited[profile_id] = True

        # Check if profile is already resolved. Will stop when reaching the root node
        if profile_id in self.nodes:
            return self.nodes[profile_id]

        if profile_id not in self._profiles_mapping:
            chain_keys = list(visited.keys())
            if len(chain_keys) > 1:
                # profile_id is already in visited; len > 1 means there's a parent chain
                chain_str = " -> ".join(chain_keys)
                msg = f"Unresolved profile `{profile_id}` while trying to resolve profiles for {self._target_object_cls.__qualname__}: {chain_str}"
            else:
                msg = f"Profile '{profile_id}' is missing while trying to resolve profiles for {self._target_object_cls.__qualname__}"
            raise AristaAvdInvalidInputsError(msg)

        profile_data_item = self._profiles_mapping[profile_id]

        profile_data = cast("_ProfileModelProtocol", profile_data_item)

        node = _UnifiedGraphNode(profile_id, self._target_object_cls, profile_data_item)
        self.nodes[profile_id] = node

        # Recursively move up to the parent profile
        parent_node = self.__get_profile_node(profile_data.parent_profile, visited=visited)

        parent_node.children.append(node)
        node.parent = parent_node
        return node

    def _get_profile(self, profile_id: str) -> _UnifiedGraphNode:
        """
        Get the lazy object associated with the target object and the profile applied to it.

        Args:
            profile_id: ID of the profile to apply on the target model.

        Returns:
            Lazy object representation with the profile applied based on profile key
        """
        return self.__get_profile_node(profile_id)
