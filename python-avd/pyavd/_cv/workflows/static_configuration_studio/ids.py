# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import lru_cache
from uuid import NAMESPACE_DNS, uuid5


class AvdId:
    """Namespace for AVD-managed entity IDs."""

    NAMESPACE = uuid5(NAMESPACE_DNS, "avd.arista.com")
    PREFIX = "avd_"

    @staticmethod
    def is_managed(entity_id: str) -> bool:
        """Return True if the given entity ID belongs to the AVD-managed namespace."""
        return entity_id.startswith(AvdId.PREFIX)

    @staticmethod
    @lru_cache(maxsize=1024)
    def generate(key: str) -> str:
        """Generate a deterministic ID from the AVD namespace and the provided key."""
        return f"{AvdId.PREFIX}{uuid5(AvdId.NAMESPACE, key)}"
