from ansible_collections.arista.avd.plugins.plugin_utils.utils import load_python_class

from .avdinterfacedescriptions import AvdInterfaceDescriptions
from .utils import get_interface_descriptions_templates

DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_MODULE = "ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions"
DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_CLASS_NAME = "AvdInterfaceDescriptions"


def load_interfacedescriptions(hostvars, templar) -> AvdInterfaceDescriptions:
    """
    Load the python_module defined in `templates.interface_descriptions.python_module`
    Return the class defined by `templates.interface_descriptions.python_class_name`
    """
    interface_descriptions_templates = get_interface_descriptions_templates(hostvars)

    module_path = interface_descriptions_templates.get("python_module", DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_MODULE)
    class_name = interface_descriptions_templates.get("python_class_name", DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_CLASS_NAME)

    cls = load_python_class(
        module_path,
        class_name,
        AvdInterfaceDescriptions,
    )

    return cls(hostvars=hostvars, templar=templar)
