from collections import ChainMap

from .constants import JINJA2_DOCUMENTAITON_TEMPLATE
from .templater import Templar


def get_device_doc(
    hostname: str,
    hostvars: dict,
) -> str:
    """
    Render and return the device documentation using AVD eos_cli_config_gen templates.

    Args:
        hostname: Hostname of device.
        hostvars: Dictionary of variables applied to template.
            Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_inputs`.

    Returns:
        Device documentation in Markdown format.
    """

    # Set 'inventory_hostname' on the input hostvars, to keep compatability with Ansible focused code.
    mapped_hostvars = ChainMap({"inventory_hostname": hostname}, hostvars)

    templar = Templar()
    return templar.render_template_from_file(JINJA2_DOCUMENTAITON_TEMPLATE, mapped_hostvars)
