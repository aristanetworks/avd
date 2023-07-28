# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdtodocumentationschemaconverter import AvdToDocumentationSchemaConverter
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdtojsonschemaconverter import AvdToJsonSchemaConverter

DOCUMENTATION = r"""
---
name: convert_schema
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.8"
short_description: Convert AVD Schema to a chosen output format.
description: Only for internal use.
positional: _input
options:
  _input:
    type: string
    description: ID of AVD Schema.
    required: true
    choices: ["eos_cli_config_gen" , "eos_designs"]
  type:
    type: string
    description: Type of schema to convert to.
    required: true
    choices: ["documentation_tables", "jsonschema"]
"""

RETURN = r"""
---
_value:
  description: Schema of the requested type.
  type: any
"""


def convert_schema(schema_id: str, type: str):
    """
    The `arista.avd.convert_schema` filter will convert AVD Schema to a chosen output format.

    TODO: Split into separate filters or lookups for each type.

    Parameters
    ----------
    schema_id : str, ["eos_cli_config_gen" , "eos_designs"]
        ID of AVD Schema
    type : str, ["documentation_tables", "jsonschema"]
        Type of schema to convert to

    Returns
    -------
    dict | list
        Schema of the requested type

    Raises
    ------
    AvdSchemaError, AvdValidationError
        If the input schema is not valid, exceptions will be raised accordingly.
    """
    avdschema = AvdSchema(schema_id=schema_id)

    # Validate that the loaded schema follows the meta schema
    avdschematools = AvdSchemaTools(
        hostname="schema converter", ansible_display=Display(), schema_id=schema_id, conversion_mode="disabled", validation_mode="error"
    )
    validation_results = avdschematools.validate_schema()
    if validation_results:
        raise AnsibleFilterError("Invalid schema!")

    if type == "documentation_tables":
        return AvdToDocumentationSchemaConverter(avdschema).convert_schema_to_tables()

    elif type == "jsonschema":
        return AvdToJsonSchemaConverter(avdschema).convert_schema()

    else:
        raise AristaAvdError(f"Filter arista.avd.convert_schema requires type 'documentation_tables' or 'jsonschema'. Got {type}")


class FilterModule(object):
    def filters(self):
        return {
            "convert_schema": convert_schema,
        }
