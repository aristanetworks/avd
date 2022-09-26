from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdtodocumentationschemaconverter import AvdToDocumentationSchemaConverter
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdtojsonschemaconverter import AvdToJsonSchemaConverter
from ansible_collections.arista.avd.plugins.plugin_utils.schema.errors import AristaAvdError


def convert_schema(schema: dict, type: str):
    """
    The `arista.avd.convert_schema` filter will convert AVD Schema to a chosen output format.

    Parameters
    ----------
    schema : dict
        Input AVD Schema
    type : str, ["documentation", "jsonschema"]
        Type of schema to convert to

    Returns
    -------
    dict
        Schema of the requested type

    Raises
    ------
    AvdSchemaError, AvdValidationError
        If the input schema is not valid, exceptions will be raised accordingly.
    """
    avdschema = AvdSchema(schema)
    if type == "documentation":
        schemaconverter = AvdToDocumentationSchemaConverter(avdschema)
    elif type == "jsonschema":
        schemaconverter = AvdToJsonSchemaConverter(avdschema)
    else:
        raise AristaAvdError(f"Filter arista.avd.convert_schema requires type 'documentation'. Got {type}")

    return schemaconverter.convert_schema()


class FilterModule(object):
    def filters(self):
        return {
            "convert_schema": convert_schema,
        }
