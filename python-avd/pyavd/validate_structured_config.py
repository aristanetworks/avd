from .avd_schema_tools import AvdSchemaTools
from .constants import EOS_CLI_CONFIG_GEN_SCHEMA_ID

eos_cli_config_gen_schema_tools = None


def validate_structured_config(structured_config: dict) -> dict:
    """
    Validate structured config according the `eos_cli_config_gen` schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        structured_config: Dictionary with structured configuration.

    Returns:
        Dictionary with boolean "failed" and list of "errors" like:
            ```python
            {
                "failed": bool,
                "errors": list[Exception],
            }
            ```

            - "failed" is True if Conversion failed or data is invalid. Otherwise False.
            - "errors" is a list of Exceptions raised during variable conversion and validation containing errors raised as well as data validation issues.
    """

    # Initialize a global instance of eos_cli_config_gen_schema_tools
    global eos_cli_config_gen_schema_tools
    if eos_cli_config_gen_schema_tools is None:
        eos_cli_config_gen_schema_tools = AvdSchemaTools(schema_id=EOS_CLI_CONFIG_GEN_SCHEMA_ID)

    # Validate input data
    return eos_cli_config_gen_schema_tools.convert_and_validate_data(structured_config)
