from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class StructCfgMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict

    @cached_property
    def struct_cfg(self) -> dict | None:
        """
        Return the combined structured config from VRFs
        """

        if not self._network_services_l3:
            return None

        structured_configs = []

        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if (structured_config := vrf.get("structured_config")) is not None:
                    structured_configs.append(structured_config)

        if structured_configs:
            list_merge = get(self._hostvars, "custom_structured_configuration_list_merge", required=True)
            return merge({}, *structured_configs, recursive=True, list_merge=list_merge)

        return None
