from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, load_python_class

from .avdinterfacedescriptions import AvdInterfaceDescriptions

DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_MODULE = "ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions"
DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_CLASS_NAME = "AvdInterfaceDescriptions"


def load_interfacedescriptions(hostvars, templar) -> AvdInterfaceDescriptions:
    """
    Load the python_module defined in `templates.interface_descriptions.python_module`
    Return the class defined by `templates.interface_descriptions.python_class_name`
    """
    module_path = get(
        hostvars,
        "switch.interface_descriptions.python_module",
        default=DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_MODULE,
    )
    class_name = get(
        hostvars,
        "switch.interface_descriptions.python_class_name",
        default=DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_CLASS_NAME,
    )

    cls = load_python_class(
        module_path,
        class_name,
        AvdInterfaceDescriptions,
    )

    return cls(hostvars=hostvars, templar=templar)
