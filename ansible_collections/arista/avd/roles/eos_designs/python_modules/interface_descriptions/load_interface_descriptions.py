iimport importlib

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

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
    try:
        cls = getattr(importlib.import_module(module_path), class_name)
    except ImportError as imp_exc:
        raise AristaAvdError(imp_exc) from imp_exc

    # if not isinstance(cls, AvdInterfaceDescriptions):
    if not issubclass(cls, AvdInterfaceDescriptions):
        raise AristaAvdError(f"{cls} is not a subclass of AvdInterfaceDescriptions class")

    return cls(hostvars=hostvars, templar=templar)
