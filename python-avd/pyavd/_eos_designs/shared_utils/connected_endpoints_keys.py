# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ..._utils import get
from ...j2filters import convert_dicts

if TYPE_CHECKING:
    from . import SharedUtils

# NOTE: there is a static list of default endpoint keys in the fabric connected endpoints documentation templates.
DEFAULT_CONNECTED_ENDPOINTS_KEYS = [
    {"key": "servers", "type": "server", "description": "Server"},
    {"key": "firewalls", "type": "firewall", "description": "Firewall"},
    {"key": "routers", "type": "router", "description": "Router"},
    {"key": "load_balancers", "type": "load_balancer", "description": "Load Balancer"},
    {"key": "storage_arrays", "type": "storage_array", "description": "Storage Array"},
    {"key": "cpes", "type": "cpe", "description": "CPE"},
    {"key": "workstations", "type": "workstation", "description": "Workstation"},
    {"key": "access_points", "type": "access_point", "description": "Access Point"},
    {"key": "phones", "type": "phone", "description": "Phone"},
    {"key": "printers", "type": "printer", "description": "Printer"},
    {"key": "cameras", "type": "camera", "description": "Camera"},
    {"key": "generic_devices", "type": "generic_device", "description": "Generic Device"},
]


class ConnectedEndpointsKeysMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def connected_endpoints_keys(self: SharedUtils) -> list:
        """
        Return connected_endpoints_keys filtered for invalid entries and unused keys

        NOTE: This method is called _before_ any schema validation, since we need to resolve connected_endpoints_keys dynamically
        """
        connected_endpoints_keys = []
        # Support legacy data model by converting nested dict to list of dict
        connected_endpoints_keys = convert_dicts(get(self.hostvars, "connected_endpoints_keys", default=DEFAULT_CONNECTED_ENDPOINTS_KEYS), "key")
        connected_endpoints_keys = [entry for entry in connected_endpoints_keys if entry.get("key") is not None and self.hostvars.get(entry["key"]) is not None]
        return connected_endpoints_keys
