from .constants import JINJA2_CONFIG_TEMPLATE
from .templater import Templar


def get_device_config(structured_config: dict) -> str:
    """
    Render and return the device configuration using AVD eos_cli_config_gen templates.

    Args:
        structured_config: Dictionary with structured configuration.
            Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.

    Returns:
        Device configuration in EOS CLI format.
    """

    templar = Templar()
    return templar.render_template_from_file(JINJA2_CONFIG_TEMPLATE, structured_config)
