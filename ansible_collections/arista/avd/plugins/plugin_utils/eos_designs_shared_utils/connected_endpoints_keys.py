from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils

DEFAULT_CONNECTED_ENDPOINTS_KEYS = [
    "servers",
    "firewalls",
    "load_balancers",
    "storage_arrays",
    "routers",
    "cpes",
    "workstations",
    "access_points",
    "phones",
    "printers",
    "cameras",
    "generic_devices",
]


class ConnectedEndpointsKeysMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    def get_default_connected_endpoints_keys(self: SharedUtils) -> list:
        result = []
        for key in DEFAULT_CONNECTED_ENDPOINTS_KEYS:
            singular_key = key.removesuffix("s")
            description = singular_key.replace("_", " ").title()
            result.append(
                {
                    "key": key,
                    "type": singular_key,
                    "description": description,
                }
            )

        return result

    @cached_property
    def connected_endpoints_keys(self: SharedUtils) -> list:
        """
        Return connected_endpoints_keys filtered for invalid entries and unused keys

        NOTE: This method is called _before_ any schema validation, since we need to resolve connected_endpoints_keys dynamically
        """
        connected_endpoints_keys = []
        # Support legacy data model by converting nested dict to list of dict
        connected_endpoints_keys = convert_dicts(get(self.hostvars, "connected_endpoints_keys", default=self.get_default_connected_endpoints_keys()), "key")
        connected_endpoints_keys = [entry for entry in connected_endpoints_keys if entry.get("key") is not None and self.hostvars.get(entry["key"]) is not None]
        return connected_endpoints_keys
