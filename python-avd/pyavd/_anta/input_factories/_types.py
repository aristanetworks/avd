# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Protocol


class Metadata(Protocol):
    peer: str
    peer_interface: str


class ValidatedEthernetInterfacesItem(Protocol):
    name: str
    metadata: Metadata
