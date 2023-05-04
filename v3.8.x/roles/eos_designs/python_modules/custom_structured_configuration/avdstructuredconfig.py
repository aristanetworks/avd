from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

CUSTOM_STRUCTURED_CONFIGURATION_EXEMPT_KEYS = ["custom_structured_configuration_prefix", "custom_structured_configuration_list_merge"]


class AvdStructuredConfig(AvdFacts):
    """
    The AvdStructuredConfig Class is imported by "yaml_templates_to_facts" to render parts of the structured config.

    "yaml_templates_to_facts" imports, instantiates and run the .render() method on the class.

    The Class uses AvdFacts, as the base class, to inherit _hostvars other attributes.
    """

    @cached_property
    def _custom_structured_configuration_prefix(self) -> list:
        """
        Reads custom_structured_configuration_prefix from hostvars and converts to list if necessary
        """
        custom_structured_configuration_prefix = get(self._hostvars, "custom_structured_configuration_prefix", default=[])
        if not isinstance(custom_structured_configuration_prefix, list):
            return [custom_structured_configuration_prefix]

        return custom_structured_configuration_prefix

    @cached_property
    def _router_bgp(self) -> dict | None:
        return get(self._hostvars, "router_bgp")

    def _extract_struct_cfg_from_dict_of_dicts(self, data: dict, varname: str) -> dict | None:
        # TODO: Handle AVD4.0 data models. For now this is only handling dicts
        dict_of_dicts = get(data, varname)
        if not dict_of_dicts:
            return None

        struct_cfgs = {key: dict_of_dicts[key].pop("struct_cfg") for key in natural_sort(dict_of_dicts) if "struct_cfg" in dict_of_dicts[key]}
        if not struct_cfgs:
            return None

        return {varname: struct_cfgs}

    def _struct_cfg(self) -> dict | None:
        return self._hostvars.pop("struct_cfg", None)

    def _ethernet_interfaces(self) -> dict | None:
        return self._extract_struct_cfg_from_dict_of_dicts(self._hostvars, "ethernet_interfaces")

    def _port_channel_interfaces(self) -> dict | None:
        return self._extract_struct_cfg_from_dict_of_dicts(self._hostvars, "port_channel_interfaces")

    def _vlan_interfaces(self) -> dict | None:
        return self._extract_struct_cfg_from_dict_of_dicts(self._hostvars, "vlan_interfaces")

    def _router_bgp_peer_groups(self) -> dict | None:
        if self._router_bgp is None:
            return None

        if (struct_cfgs := self._extract_struct_cfg_from_dict_of_dicts(self._router_bgp, "peer_groups")) is None:
            return None

        return {"router_bgp": struct_cfgs}

    def _router_bgp_vrfs(self) -> dict | None:
        if self._router_bgp is None:
            return None

        if (struct_cfgs := self._extract_struct_cfg_from_dict_of_dicts(self._router_bgp, "vrfs")) is None:
            return None

        return {"router_bgp": struct_cfgs}

    def _router_bgp_vlans(self) -> dict | None:
        if self._router_bgp is None:
            return None

        if (struct_cfgs := self._extract_struct_cfg_from_dict_of_dicts(self._router_bgp, "vlans")) is None:
            return None

        return {"router_bgp": struct_cfgs}

    def _custom_structured_configurations(self) -> list[dict]:
        if not self._custom_structured_configuration_prefix:
            return []

        return [
            {
                str(key)[len(prefix) :]: self._hostvars[key]
                for key in self._hostvars
                if str(key).startswith(prefix) and key not in CUSTOM_STRUCTURED_CONFIGURATION_EXEMPT_KEYS
            }
            for prefix in self._custom_structured_configuration_prefix
        ]

    def render(self) -> list[dict]:
        """
        Custom Structured Configuration can contain any key, so we cannot use the regular render method.

        This method returns a list of dicts with structured_configuration.

        yaml_templates_to_facts will merge this list into a single dict.
        """

        struct_cfgs = [
            self._struct_cfg(),
            self._ethernet_interfaces(),
            self._port_channel_interfaces(),
            self._vlan_interfaces(),
            self._router_bgp_peer_groups(),
            self._router_bgp_vrfs(),
            self._router_bgp_vlans(),
        ]
        struct_cfgs = [struct_cfg for struct_cfg in struct_cfgs if struct_cfg is not None]
        struct_cfgs.extend(self._custom_structured_configurations())

        return struct_cfgs
