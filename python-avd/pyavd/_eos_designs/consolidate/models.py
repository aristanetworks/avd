# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import ClassVar

from pyavd._eos_designs.schema import EosDesigns as AVDDesign
from pyavd._schema.models.avd_indexed_list import AvdIndexedList
from pyavd._schema.models.avd_list import AvdList
from pyavd._schema.models.avd_model import AvdModel


class ConsolidatedConnectedEndpoint(AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem):
    """Connected endpoint with source indices aligned with the filtered adapters."""

    _fields: ClassVar[dict] = {
        **AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem._fields,
        "_adapter_indices": {"type": list},
    }
    _adapter_indices: list[int]


class ConsolidatedConnectedEndpoints(AvdIndexedList[str, ConsolidatedConnectedEndpoint]):
    """Connected endpoints indexed by name."""

    _primary_key: ClassVar[str] = "name"


ConsolidatedConnectedEndpoints._item_type = ConsolidatedConnectedEndpoint


class ConsolidatedConnectedEndpointsItem(AvdModel):
    """Device-local connected endpoints retaining their source key metadata."""

    _fields: ClassVar[dict] = {
        "key": {"type": str},
        "type": {"type": str},
        "description": {"type": str},
        "value": {"type": ConsolidatedConnectedEndpoints},
    }
    key: str
    type: str | None
    description: str | None
    value: ConsolidatedConnectedEndpoints


class ConsolidatedConnectedEndpointGroups(AvdIndexedList[str, ConsolidatedConnectedEndpointsItem]):
    """Device-local connected endpoint groups indexed by their source key."""

    _primary_key: ClassVar[str] = "key"


ConsolidatedConnectedEndpointGroups._item_type = ConsolidatedConnectedEndpointsItem


class ConsolidatedNetworkPort(AVDDesign.NetworkPortsItem):
    """Device-local network port candidate retaining its original list index."""

    _fields: ClassVar[dict] = {**AVDDesign.NetworkPortsItem._fields, "_source_index": {"type": int}}
    _source_index: int


class ConsolidatedNetworkPorts(AvdList[ConsolidatedNetworkPort]):
    """Device-local network port candidates."""


ConsolidatedNetworkPorts._item_type = ConsolidatedNetworkPort


class ConsolidatedPortProfileName(AvdModel):
    """Minimal port profile metadata retained for fabric documentation."""

    _fields: ClassVar[dict] = {"profile": {"type": str}, "parent_profile": {"type": str}}
    profile: str
    parent_profile: str | None


class ConsolidatedPortProfileNames(AvdList[ConsolidatedPortProfileName]):
    """Configured port profile names and their parent profiles."""


ConsolidatedPortProfileNames._item_type = ConsolidatedPortProfileName
