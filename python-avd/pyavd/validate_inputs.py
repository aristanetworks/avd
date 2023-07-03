from .avd_schema_tools import AvdSchemaTools
from .constants import EOS_DESIGNS_SCHEMA_ID
from .vendor.eos_designs.eos_designs_shared_utils import SharedUtils

eos_designs_schema_tools = None


def validate_inputs(inputs: dict) -> dict:
    """
    Validate input variables according to the `eos_designs` schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        inputs: Dictionary with inputs for "eos_designs".

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

    # Initialize a global instance of eos_designs_schema_tools
    global eos_designs_schema_tools
    if eos_designs_schema_tools is None:
        eos_designs_schema_tools = AvdSchemaTools(schema_id=EOS_DESIGNS_SCHEMA_ID)

    # Initialize SharedUtils class to fetch default variables below.
    shared_utils = SharedUtils(hostvars=inputs, templar=None)

    # Insert dynamic keys into the input data if not set.
    # These keys are required by the schema, but the default values are set inside shared_utils.
    inputs.setdefault("node_type_keys", shared_utils.node_type_keys)
    inputs.setdefault("connected_endpoints_keys", shared_utils.connected_endpoints_keys)
    inputs.setdefault("network_services_keys", shared_utils.network_services_keys)

    # Validate input data
    return eos_designs_schema_tools.convert_and_validate_data(inputs)
