from .avd_schema_tools import AvdSchemaTools
from .constants import EOS_CLI_CONFIG_GEN_SCHEMA_ID, EOS_DESIGNS_SCHEMA_ID
from .vendor.eos_designs.eos_designs_shared_utils import SharedUtils
from .vendor.errors import AristaAvdError


def validate_inputs(
    all_hostvars: dict[str, dict],
    eos_designs: bool = True,
    eos_cli_config_gen: bool = True,
) -> None:
    """
    Validate input variables according to AVD the `eos_designs` schema and/or the `eos_cli_config_gen` schema.
    as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        all_hostvars: A dictionary where keys are hostnames and values are dictionaries of all variables per devices.
            ```python
            {
                "<hostname1>": dict,
                "<hostname2>": dict,
                ...
            }
            ```
        eos_designs: Validate variables according to the `eos_designs` schema.
        eos_cli_config_gen: Validate variables according to the `eos_cli_config_gen` schema.

    Raises:
        AristaAvdError: List of validation errors across all devices.
    """
    if eos_designs:
        eos_designs_schema_tools = AvdSchemaTools(schema_id=EOS_DESIGNS_SCHEMA_ID)

    if eos_cli_config_gen:
        eos_cli_config_gen_schema_tools = AvdSchemaTools(schema_id=EOS_CLI_CONFIG_GEN_SCHEMA_ID)

    error_messages = []
    for hostname, hostvars in all_hostvars.items():
        if eos_designs:
            # Initialize SharedUtils class to fetch default variables below.
            shared_utils = SharedUtils(hostvars=hostvars, templar=None)

            # Insert dynamic keys into the input data if not set.
            # These keys are required by the schema, but the default values are set inside shared_utils.
            hostvars.setdefault("node_type_keys", shared_utils.node_type_keys)
            hostvars.setdefault("connected_endpoints_keys", shared_utils.connected_endpoints_keys)
            hostvars.setdefault("network_services_keys", shared_utils.network_services_keys)

            # Validate input data
            result = eos_designs_schema_tools.convert_and_validate_data(hostvars)
            if result.get("failed"):
                error_messages.extend([f"[{hostname}]: {str(error)}" for error in result["errors"]])

        if eos_cli_config_gen:
            # Validate input data
            result = eos_cli_config_gen_schema_tools.convert_and_validate_data(hostvars)
            if result.get("failed"):
                error_messages.extend([f"[{hostname}]: {str(error)}" for error in result["errors"]])

    if error_messages:
        raise AristaAvdError(f"{error_messages}")

    return
