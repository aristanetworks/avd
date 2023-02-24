from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.plugins.lookup import LookupBase

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdtodocumentationschemaconverter import AvdToDocumentationSchemaConverter

DOCUMENTATION = r"""
  name: convert_to_documentation_schema
  author: Arista
  version_added: "4.0.0"
  short_description: convert a built-in AVD Schema to a chosen output format
  description:
    - This lookup module will convert a built-in AVD Schema to a chosen output format.
  options:
    _terms:
      description: ID of built-in schema to convert
      options:
        - eos_cli_config_gen
        - eos_designs
      required: True
"""


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        """
        The `arista.avd.convert_to_documentation_schema` lookup module will convert a built-in AVD Schema to
        documentation_schema used to generate role documentation.

        Parameters
        ----------
        terms : list[str]
            ID of built-in schema ('eos_cli_config_gen' or 'eos_designs') to use as source

        Returns
        -------
        dict
            Documentation Schema

        Raises
        ------
        AvdSchemaError, AvdValidationError
            If the input schema is not valid, exceptions will be raised accordingly.
        """
        schema_id = terms[0]
        avdschema = AvdSchema(schema_id=schema_id)
        schemaconverter = AvdToDocumentationSchemaConverter(avdschema)
        return schemaconverter.convert_schema()
