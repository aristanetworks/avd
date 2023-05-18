from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class StructCfgsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict

    @cached_property
    def struct_cfgs(self) -> list | None:
        """
        Return the combined structured config from VRFs
        """

        if not self.shared_utils.network_services_l3:
            return None

        structured_configs = []

        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if (structured_config := vrf.get("structured_config")) is not None:
                    structured_configs.append(structured_config)

        if structured_configs:
            return structured_configs

        return None
