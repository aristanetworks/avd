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
    from typing_extensions import Self

    from pyavd._schema.models.avd_indexed_list import AvdIndexedList
    from pyavd._schema.models.avd_model import AvdModel

T_ProfileModel = TypeVar("T_ProfileModel", bound="AvdModel")


class _ProfileModelProtocol(Protocol):
    """Structural interface for profile catalog entries used by the profile resolver."""

    profile: str
    """Id that is used to reference the profile elsewhere in the models."""
    parent_profile: str | None
    """
    Specifies the profile from the same catalog to inherit the values from. In None, values are
    inherited from the target object to which the profiles are applied to. It can't be empty string.
    """


def resolve_profile(
    target_object: T_AvdModel,
    profile_list: AvdIndexedList[str, T_ProfileModel],
    profile_id: str,
    target_name: str,
) -> T_AvdModel:
    """
    Resolve the selected profile into a target input model.

    The selected profile and its parent profiles are merged into a copy of the target object.

    Args:
        target_object: Input model receiving the resolved profile values.
        profile_list: Catalog of available profiles.
        profile_id: Selected profile ID to resolve.
        target_name: Human-readable name of the target to include in error messages.

    Returns:
        The target object with the selected profile applied.
    """
    resolver = _LazyProfileResolver(target_object, profile_list, target_name=target_name)
    lazy_profile = resolver._get_profile(profile_id)
    return lazy_profile._deepinherit


class _LazyProfile(Generic[T_AvdModel, T_ProfileModel]):
    """Lazy representation of a profile."""

    def __init__(self: Self, profile_id: str, target_cls: type[T_AvdModel], data: T_AvdModel | T_ProfileModel) -> None:
        """
        Initialize lazy profile object.

        It holds references to its parent profile and its raw data. To get a target object with the
        profiles applied, use `_deepinherit` property.

        Args:
            profile_id: Profile ID represented by this entry.
            target_cls: Class of the model that the profile is applied to
            data: Profile or target model data attached to the entry.
        """
        self.profile_id: str = profile_id
        self.profile: T_AvdModel | T_ProfileModel = data
        self.parent: Self | None = None
        self.children: list[Self] = []
        self.target_cls = target_cls

    def _copy_data(self) -> T_AvdModel:
        """Return a deep copy of the profile data, cast to the target model type if needed."""
        data = self.profile._deepcopy()
        if not isinstance(data, self.target_cls):
            data = data._cast_as(self.target_cls, ignore_extra_keys=True)
        return data

    @functools.cached_property
    def _deepinherit(self) -> T_AvdModel:
        """
        Get the target model with the full profile chain applied.

        Profile attributes override the target model (root). Child profile attributes override parent profile attributes.
        """
        data = self._copy_data()
        if self.parent is not None:
            data._deepinherit(self.parent._deepinherit)
        return data


_Profile = _LazyProfile[T_AvdModel, T_ProfileModel]


class _LazyProfileResolver(Generic[T_AvdModel, T_ProfileModel]):
    """
    Resolver that lazily builds a profile tree from given `profile_catalog` to be applied onto `target_object`.

    Validation and profile resolution only happens when the profile is explicitly referenced via `_get_profile(profile_id)` method.
    Profile lookup is performed by matching the given `profile_id` with the `profile` field from `profile_catalog`. Profiles are linked through
    `parent_profile` references, which allows inheriting fields from other profiles in the same `profile_catalog`.
    If `parent_profile` is not set, profile would inherit the `target_object` values.

    Profile models (`T_ProfileModel`) share the same fields with target model (`T_AvdModel`), but they are not subclass to the target model.
    To keep the profile resolution lazy, profile models are only cast to target model when instructed explicitly through `_LazyProfile._deepinherit`.
    """

    # To avoid a slightest chance of naming conflicts we just assume it to be empty string
    ROOT_PROFILE_ID = ""

    def __init__(self, target_object: T_AvdModel, profile_catalog: AvdIndexedList[str, T_ProfileModel], target_name: str = "") -> None:
        """
        Initialize the profile tree.

        Args:
            target_object: Base target model to which profiles are applied to.
            profile_catalog: Profile catalog keyed by profile ID.
            target_name: Human-readable target name used in error messages. Defaults to the target object's class qualified name.
        """
        self._target_object_cls = type(target_object)
        self._profile_mapping: dict[str, _Profile] = {self.ROOT_PROFILE_ID: _Profile(self.ROOT_PROFILE_ID, self._target_object_cls, target_object)}
        self._profile_catalog = profile_catalog
        self._target_name = target_name or self._target_object_cls.__qualname__

    def __lazy_load_profile(self, profile_id: str, visited: OrderedDict[str, Any] | None = None) -> _Profile:
        """
        Lazily add the profile and its parent profiles to the profile tree.

        This method follows the parent chain defined by profile/parent_profile fields and checks that it is valid
        (no circular dependencies, and every profile in the chain is present in the catalog).

        It's meant to be an internal method, use `_get_profile()` instead

        Args:
            profile_id: Profile key to look-up for
            visited: Ordered set populated as the recursion progresses through `parent_profile` refs

        Returns:
            The lazy profile entry for the requested profile.
        """
        if visited is None:
            visited = OrderedDict()

        if profile_id in visited:
            # profile_id appears again in the current chain - cycle detected
            cycle_path = list(visited)
            cycle_path = list(reversed(cycle_path[cycle_path.index(profile_id) :]))
            cycle_path.append(cycle_path[0])

            msg = f"Cycle detected while trying to resolve profiles for '{self._target_name}': " + " -> ".join(cycle_path)
            raise AristaAvdInvalidInputsError(msg)

        visited[profile_id] = True

        # Check if profile is already resolved. This also stops at the synthetic root profile.
        if profile_id in self._profile_mapping:
            return self._profile_mapping[profile_id]

        if profile_id not in self._profile_catalog:
            chain_keys = list(visited.keys())
            # profile_id was added to visited above, so len > 1 means it was reached via a parent chain
            if len(chain_keys) > 1:
                chain_str = " -> ".join(chain_keys)
                msg = f"Unresolved profile '{profile_id}' while trying to resolve profiles for '{self._target_name}': {chain_str}"
            else:
                msg = f"Profile '{profile_id}' is missing while trying to resolve profiles for '{self._target_name}'"
            raise AristaAvdInvalidInputsError(msg)

        profile_data_item = self._profile_catalog[profile_id]

        # The TypeVar cannot express both the AvdModel bound and Profile protocol, so it needs to be cast explicitly
        # to access profile specific fields.
        profile_data = cast("_ProfileModelProtocol", profile_data_item)

        lazy_profile = _Profile(profile_id, self._target_object_cls, profile_data_item)
        self._profile_mapping[profile_id] = lazy_profile

        # If no parent_profile provided, inherit the target model (i.e root profile)
        parent_profile = profile_data.parent_profile or self.ROOT_PROFILE_ID
        # Recursively move up to the parent profile
        parent_lazy_profile = self.__lazy_load_profile(parent_profile, visited=visited)

        parent_lazy_profile.children.append(lazy_profile)
        lazy_profile.parent = parent_lazy_profile
        return lazy_profile

    def _get_profile(self, profile_id: str) -> _Profile:
        """
        Return the lazy profile entry for the given profile.

        Args:
            profile_id: ID of the profile to resolve.

        Returns:
            Profile entry with its parent links set, ready to produce the merged model.
        """
        return self.__lazy_load_profile(profile_id)
