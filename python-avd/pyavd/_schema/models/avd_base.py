# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING, ClassVar, Literal, Protocol

from .type_vars import T_AvdDataClass, T_LoadDumpType

if TYPE_CHECKING:
    from typing_extensions import Self


class InternalData:
    __slots__ = (
        "campus_link_type",
        "context",
        "description",
        "evpn_l3_multicast_enabled",
        "evpn_l3_multicast_evpn_peg_transit",
        "evpn_l3_multicast_group_ip",
        "interface",
        "interfaces",
        "pim_rp_addresses",
        "type",
    )

    campus_link_type: list[str]
    context: str
    description: str | None
    evpn_l3_multicast_enabled: bool | None
    evpn_l3_multicast_evpn_peg_transit: bool | None
    evpn_l3_multicast_group_ip: str | None
    interface: str
    interfaces: list
    pim_rp_addresses: list[dict]
    type: str | None


class AvdBaseProtocol(Protocol[T_LoadDumpType, T_AvdDataClass]):
    """Base protocol used for schema-based data classes holding data loaded from AVD inputs."""

    _created_from_null: bool
    """
    Flag to say if this data was loaded from a '<key>: null' value in YAML.

    This is used to handle inheritance and merging correctly.
    When _created_from_null we inherit nothing (we win!).
    When _created_from_null we take anything in when merging and clear the flag.
    TODO: Stop changing data in-place.

    The flag is not carried across between classes, so it should not affect anything outside the loaded inputs.
    Only exception is on _cast_as, where the flag is carried over.
    """

    _block_inheritance: bool
    """Flag to block inheriting further if we at some point inherited from a class with _created_from_null set."""

    _internal_data_instance: InternalData
    """Placeholder for Internal data used for storing internal context on data objects, without affecting other logic."""

    _is_avd_data_class: ClassVar[bool]
    """Flag to enable easy detection of fields with AVD data classes."""

    @property
    def _internal_data(self) -> InternalData:
        """Internal data used for storing internal context on data objects, without affecting other logic."""
        ...  # pylint: disable=unnecessary-ellipsis

    @classmethod
    def _load(cls, data: T_LoadDumpType) -> Self:
        """Returns a new instance loaded with the given data."""
        ...  # pylint: disable=unnecessary-ellipsis

    @classmethod
    def _from_null(cls) -> Self:
        """Returns a new instance with all attributes set to None. This represents the YAML input '<key>: null'."""
        ...  # pylint: disable=unnecessary-ellipsis

    def _strip_empties(self) -> None:
        """In-place update the instance to remove data matching the given strip_values."""
        ...  # pylint: disable=unnecessary-ellipsis

    def _dump(self, include_default_values: bool = False) -> T_LoadDumpType:
        """Dump data into native Python types with or without default values."""
        ...  # pylint: disable=unnecessary-ellipsis

    def _cast_as(self, new_type: type[T_AvdDataClass], ignore_extra_keys: bool = False) -> T_AvdDataClass:
        """Recast a class instance as another similar subclass if they are compatible."""
        ...  # pylint: disable=unnecessary-ellipsis

    def _deepmerge(self, other: Self, list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"] = "append_unique") -> None:
        """
        Update instance by deepmerging the other instance in.

        Args:
            other: The other instance of the same type to merge on this instance.
            list_merge: Merge strategy used on any nested lists.

        List merge strategies:
        - "append_unique" will first try to deep merge on the primary key, and if not found it will append non-existing items.
        - "append" will first try to deep merge on the primary key, and if not found it will append all other items (including duplicates).\
            (For AvdIndexedList this works the same as append_unique)
        - "replace" will replace the full list.
        - "keep" will only use the new list if there is no existing list or existing list is `None`.
        - "prepend_unique" will first try to deep merge on the primary key, and if not found it will prepend non-existing items.
        - "prepend" will first try to deep merge on the primary key, and if not found it will prepend all other items (including duplicates).\
            (For AvdIndexedList this works the same as prepend_unique)
        """
        ...  # pylint: disable=unnecessary-ellipsis

    def _compare(self, other: Self) -> bool:
        """Compare two instances. Optionally ignoring fields for the outermost AvdModel."""
        ...  # pylint: disable=unnecessary-ellipsis

    def _deepmerged(
        self, other: Self, list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"] = "append_unique"
    ) -> Self:
        """
        Return new instance with the result of the deepmerge of "other" on this instance.

        Args:
            other: The other instance of the same type to merge on this instance.
            list_merge: Merge strategy used on any nested lists.

        List merge strategies:
        - "append_unique" will first try to deep merge on the primary key, and if not found it will append non-existing items.
        - "append" will first try to deep merge on the primary key, and if not found it will append all other items (including duplicates).\
            (For AvdIndexedList this works the same as append_unique)
        - "replace" will replace the full list.
        - "keep" will only use the new list if there is no existing list or existing list is `None`.
        - "prepend_unique" will first try to deep merge on the primary key, and if not found it will prepend non-existing items.
        - "prepend" will first try to deep merge on the primary key, and if not found it will prepend all other items (including duplicates).\
            (For AvdIndexedList this works the same as prepend_unique)
        """
        ...  # pylint: disable=unnecessary-ellipsis

    def _combine(self, other: Self) -> None:
        """
        Update instance by combining the other instance in.

        Combining is different from merging in the sense that it will raise if there is a conflict
        between one of our elements and the other elements.

        Args:
            other: The other instance of the same type to combine into this instance.

        Raises:
            AristaAvdDuplicateDataError: When conflicting information is found when combining.
        """
        ...  # pylint: disable=unnecessary-ellipsis


class AvdBase(AvdBaseProtocol):
    """Base class used for schema-based data classes holding data loaded from AVD inputs."""

    __slots__ = ("_block_inheritance", "_created_from_null", "_internal_data_instance")

    _is_avd_data_class: ClassVar[bool] = True

    def __init__(self) -> None:
        self._created_from_null = False
        self._block_inheritance = False

    @property
    def _internal_data(self) -> InternalData:
        # Creating the instance on first access to avoid creating unused instances of this class.
        try:
            return self._internal_data_instance
        except AttributeError:
            self._internal_data_instance = InternalData()
            return self._internal_data_instance

    def _deepcopy(self) -> Self:
        return deepcopy(self)

    @classmethod
    def _from_null(cls) -> Self:
        new_instance = cls()
        new_instance._created_from_null = True
        return new_instance

    def _deepmerged(
        self, other: Self, list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"] = "append_unique"
    ) -> Self:
        new_instance = deepcopy(self)
        new_instance._deepmerge(other=other, list_merge=list_merge)
        return new_instance
