from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, load_python_class
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing.avdipaddressing import AvdIpAddressing

DEFAULT_AVD_IP_ADDRESSING_PYTHON_MODULE = "ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing"
DEFAULT_AVD_IP_ADDRESSING_PYTHON_CLASS_NAME = "AvdIpAddressing"


class IpAddressingMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    """

    node_type_key_data: dict
    hostvars: dict

    @cached_property
    def ip_addressing(self) -> AvdIpAddressing:
        """
        Load the python_module defined in `templates.ip_addressing.python_module`
        Return an instance of the class defined by `templates.ip_addressing.python_class_name` as cached_property
        """
        module_path = self.ip_addressing_templates.get("python_module", DEFAULT_AVD_IP_ADDRESSING_PYTHON_MODULE)
        class_name = self.ip_addressing_templates.get("python_class_name", DEFAULT_AVD_IP_ADDRESSING_PYTHON_CLASS_NAME)

        cls = load_python_class(
            module_path,
            class_name,
            AvdIpAddressing,
        )

        return cls(hostvars=self.hostvars, shared_utils=self)

    @cached_property
    def ip_addressing_templates(self) -> dict:
        """
        Return dict with ip_addressing templates set based on
        templates.ip_addressing.* combined with (overridden by)
        node_type_keys.<node_type_key>.ip_addressing.*
        """
        hostvar_templates = get(self.hostvars, "templates.ip_addressing", default={})
        node_type_templates = get(self.node_type_key_data, "ip_addressing", default={})
        if hostvar_templates or node_type_templates:
            return merge(hostvar_templates, node_type_templates, list_merge="replace", destructive_merge=False)
        else:
            return {}
