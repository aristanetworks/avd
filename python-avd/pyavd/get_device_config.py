from collections import ChainMap

from .constants import JINJA2_CONFIG_TEMPLATE
from .templater import Templar


def get_device_config(hostname: str, hostvars: dict) -> str:
    """
    Render and return the device configuration using AVD eos_cli_config_gen templates.

    Args:
        hostname: Hostname of device.
        hostvars: Dictionary of variables applied to template.
            Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_inputs`.

    Returns:
        Device configuration in EOS CLI format.
    """

    # Set 'inventory_hostname' on the input hostvars, to keep compatability with Ansible focused code.
    mapped_vars = ChainMap({"inventory_hostname": hostname}, hostvars)

    templar = Templar()
    return templar.render_template_from_file(JINJA2_CONFIG_TEMPLATE, mapped_vars)
