from ansible_collections.arista.avd.plugins.plugin_utils.utils import load_python_class

from .avdipaddressing import AvdIpAddressing
from .utils import get_ip_addressing_templates

DEFAULT_AVD_IP_ADDRESSING_PYTHON_MODULE = "ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing"
DEFAULT_AVD_IP_ADDRESSING_PYTHON_CLASS_NAME = "AvdIpAddressing"


def load_ip_addressing(hostvars, templar) -> AvdIpAddressing:
    """
    Load the python_module defined in `templates.ip_addressing.python_module`
    Return the class defined by `templates.ip_addressing.python_class_name`
    """
    ip_addressing_templates = get_ip_addressing_templates(hostvars)

    module_path = ip_addressing_templates.get("python_module", DEFAULT_AVD_IP_ADDRESSING_PYTHON_MODULE)
    class_name = ip_addressing_templates.get("python_class_name", DEFAULT_AVD_IP_ADDRESSING_PYTHON_CLASS_NAME)

    cls = load_python_class(
        module_path,
        class_name,
        AvdIpAddressing,
    )

    return cls(hostvars=hostvars, templar=templar)
