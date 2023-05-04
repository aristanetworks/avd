from __future__ import absolute_import, division, print_function

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.key_to_display_name import key_to_display_name

__metaclass__ = type

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema

# The DEFAULT_TABLE value is only used a dummy value for unset "table" value.
DEFAULT_TABLE = "_default_table_value_if_not_set"


class AvdToDocumentationSchemaConverter:
    """
    This converter will convert a regular avdschema to a documentation schema.

    The documentation schema is a flatter representation of the AVD schema
    more suited for creating tables in markdown documentation

    By default all keys will be documented in a single file using the default filename from the meta-schema
    By default a table will be created per root-key, containing all keys below.
    These default behaviors can be overridden by setting "documentation_options.filename" and "documentation_options.table"
    in the schema. See the schema documentation for details.

    Example:
    - filename: myfile
      tables:
        - display_name: Foo
          description: "foo is an example of a schema key"
          table:
            - variable: "foo"
              type: "List, Items: Dictionary"
            - variable: "  - bar"
              type: "String"
              required: "Yes, Unique"
              description: "Description of foo.bar"
          yaml:
            - 'foo:'
            - '  - bar: "<str>"'
    """

    def __init__(self, avdschema: AvdSchema):
        self._avdschema = avdschema
        meta_schema = self._avdschema._validator.META_SCHEMA
        documentation_options_schema = meta_schema["$def"]["documentation_options"]
        self._default_filename = documentation_options_schema["properties"]["filename"]["default"]

    def convert_schema(self):
        schema = {}
        output = []

        # Get fully resolved schema (where all $ref has been expanded recursively)
        # Performs inplace update of the argument so we give an empty dict.
        # By default it will resolve the full schema
        resolve_errors = self._avdschema.resolve(schema)
        for resolve_error in resolve_errors:
            if isinstance(resolve_error, Exception):
                raise AristaAvdError(resolve_error)

        filenames = self._get_filenames(schema)

        for filename in filenames:
            output.append({"filename": filename, "tables": self.build_tables(filename, schema)})

        return output

    def build_tables(self, filename: str, schema: dict):
        tables = self._get_tables(schema)

        # Skip the default table, since we want a unique table per root key if table is not set.
        if DEFAULT_TABLE in tables:
            tables.remove(DEFAULT_TABLE)

        output = []
        # Build tables for keys where "documentation_options.table" is set in their schema
        for table in tables:
            built_table = self.build_table(table, filename, schema)
            # Only append if the table contain rows
            if built_table["table"]:
                output.append(built_table)

        # Build tables for all root keys if "documentation_options.table" is not set in their schema
        schema_keys = self._get_keys(schema)
        for key, childschema in schema_keys.items():
            table_schema = {"keys": {key: childschema}}
            built_table = self.build_table(DEFAULT_TABLE, filename, table_schema)
            # Only append if the table contain rows
            if built_table["table"]:
                output.append(built_table)

        return output

    def build_table(self, table: str, filename: str, schema: dict):
        built_table = {}

        if table == DEFAULT_TABLE:
            # Single key table
            main_key = list(schema["keys"].keys())[0]
            main_key_schema = schema["keys"][main_key]
            built_table["display_name"] = main_key_schema.get("display_name", key_to_display_name(main_key))
            built_table["description"] = main_key_schema.get("description")
        else:
            # Combined table
            built_table["display_name"] = key_to_display_name(table)

        schema_keys = self._get_keys(schema)

        built_table["table"] = []
        built_table["yaml"] = []
        for key, childschema in schema_keys.items():
            if filename not in self._get_filenames(childschema):
                # Skip key if none of the underlying keys have the relevant filename
                continue
            if table not in self._get_tables(childschema):
                # Skip key if none of the underlying keys have the relevant table
                continue
            built_table["table"].extend(self.build_table_row(var_name=key, schema=childschema, indentation=0, var_path=[], table=table))
            built_table["yaml"].extend(self.build_yaml_row(var_name=key, schema=childschema, indentation=0, table=table))

        return built_table

    def build_table_row(
        self, var_name: str, schema: dict, indentation: int, var_path: list, table: str, parent_schema: dict = None, first_list_item_key: bool = False
    ):
        output = []

        row_indentation = " " * indentation
        if first_list_item_key:
            # Make an indentation of "    " into "  - " to show this is a list item in YAML format
            row_indentation = f"{row_indentation[:-2]}- "

        row = {}
        row["var_path"] = ".".join(var_path + [var_name])
        row["variable"] = f"{row_indentation}{var_name}"
        row["type"] = self.type(schema)
        required = self.required(schema, var_name, parent_schema)
        if required is not None:
            row["required"] = required

        default = self.default(schema)
        if default is not None:
            row["default"] = default

        restrictions = self.restrictions(schema)
        if restrictions is not None:
            row["restrictions"] = restrictions

        description = self.description(schema, indentation, table)
        if description is not None:
            row["description"] = description

        output.append(row)

        if schema.get("keys") or schema.get("dynamic_keys"):
            output.extend(self.keys(schema, indentation, var_path + [var_name], table))
        elif schema.get("items"):
            output.extend(self.items(schema, indentation, var_path + [var_name], table))

        return output

    def build_yaml_row(self, var_name: str, schema: dict, indentation: int, table: str, first_list_item_key: bool = False):
        output = []

        row_indentation = " " * indentation
        if first_list_item_key:
            # Make an indentation of "    " into "  - " to show this is a list item in YAML format
            row_indentation = f"{row_indentation[:-2]}- "

        row = f"{row_indentation}{var_name}:"
        var_type = schema.get("type")
        if var_type not in ["list", "dict"]:
            row = f"{row} <{var_type}>"

        output.append(row)

        schema_keys = self._get_keys(schema)
        schema_items = schema.get("items")

        if schema_keys:
            for key, childschema in schema_keys.items():
                if table not in self._get_tables(childschema):
                    # Skip key if none of the underlying keys have the relevant table
                    continue

                rows = self.build_yaml_row(
                    var_name=key,
                    schema=childschema,
                    indentation=indentation + 2,
                    table=table,
                )
                output.extend(rows)
        elif schema_items:
            schema_items_type = schema_items.get("type")
            if schema_items_type == "dict":
                schema_keys = self._get_keys(schema_items)
                first = True
                for key, childschema in schema_keys.items():
                    if table not in self._get_tables(childschema):
                        # Skip key if none of the underlying keys have the relevant table
                        continue

                    rows = self.build_yaml_row(
                        var_name=key,
                        schema=childschema,
                        indentation=indentation + 4,
                        table=table,
                        first_list_item_key=first,
                    )
                    output.extend(rows)
                    first = False
            else:
                row_indentation = " " * indentation
                row = f"{row_indentation}  - <{schema_items_type}>"
                output.append(row)

        return output

    def type(self, schema: dict):
        if "$ref" in schema:
            # TODO: Expand references and generate full documentation
            # Add a guard for $ref in the other functions later.
            return "$ref"

        type_converters = {
            "str": "String",
            "int": "Integer",
            "bool": "Boolean",
            "dict": "Dictionary",
            "list": "List",
        }
        schema_type = schema.get("type")
        if not schema_type:
            raise AristaAvdError(f"'type' key not defined in schema: {schema}")

        output = type_converters.get(schema_type)
        if not output:
            raise AristaAvdError(f"Unknown 'type': {schema_type}")

        if schema_type == "list":
            schema_items_type = schema.get("items", {}).get("type")
            if not schema_items_type:
                return output
            items_type = type_converters.get(schema_items_type)
            if not items_type:
                return output
            output = f"{output}, items: {items_type}"

        return output

    def keys(self, schema: dict, indentation: int, var_path: list, table: str):
        output = []
        schema_keys = self._get_keys(schema)

        for key, childschema in schema_keys.items():
            if table not in self._get_tables(childschema):
                # Skip key if none of the underlying keys have the relevant table
                continue
            rows = self.build_table_row(
                var_name=key,
                schema=childschema,
                indentation=indentation + 2,
                var_path=var_path,
                table=table,
                parent_schema=schema,
            )
            output.extend(rows)
        return output

    def items(self, schema: dict, indentation: int, var_path: list, table: str):
        output = []
        schema_items = schema.get("items", {})
        schema_items_type = schema_items.get("type")
        if schema_items_type == "dict":
            schema_keys = self._get_keys(schema_items)
            first = True
            for key, childschema in schema_keys.items():
                if table not in self._get_tables(childschema):
                    # Skip key if none of the underlying keys have the relevant table
                    continue

                rows = self.build_table_row(
                    var_name=key,
                    schema=childschema,
                    indentation=indentation + 4,
                    var_path=(var_path + ["[]"]),
                    table=table,
                    parent_schema=schema,
                    first_list_item_key=first,
                )
                output.extend(rows)
                first = False
        else:
            output = self.build_table_row(
                var_name=f"<{schema_items_type}>",
                schema=schema_items,
                indentation=indentation + 4,
                var_path=(var_path + ["[]"]),
                table=table,
                parent_schema=schema,
                first_list_item_key=True,
            )
        return output

    def required(self, schema: dict, var_name: str, parent_schema: dict):
        output = None
        if parent_schema and parent_schema.get("primary_key") == var_name:
            output = "Required, Unique"
        elif schema.get("required"):
            output = "Required"
        return output

    def default(self, schema: dict):
        return schema.get("default")

    def restrictions(self, schema: dict):
        restrictions = []
        if schema.get("min") is not None:
            restrictions.append(f"Min: {schema['min']}")
        if schema.get("max") is not None:
            restrictions.append(f"Max: {schema['max']}")
        if schema.get("min_length") is not None:
            restrictions.append(f"Min Length: {schema['min_length']}")
        if schema.get("max_length") is not None:
            restrictions.append(f"Max Length: {schema['max_length']}")
        if schema.get("format") is not None:
            restrictions.append(f"Format: {schema['format']}")
        if schema.get("dynamic_valid_values") is not None:
            schema.setdefault("valid_values", [])
            valid_value = f"<value(s) of {schema['dynamic_valid_values']}>"
            schema["valid_values"].append(valid_value)
        if schema.get("valid_values") is not None:
            restrictions.append("Valid Values:")
            for valid_value in schema["valid_values"]:
                restrictions.append(f"- {valid_value}")
        if schema.get("pattern") is not None:
            restrictions.append(f"Pattern: {schema['pattern']}")

        if restrictions:
            return "<br>".join(restrictions)
        return None

    def description(self, schema: dict, indentation: str, table: str):
        descriptions = []
        if schema.get("description"):
            # Only append schema description field to the description if this is a combined table or if it is not the first row
            # For the first row in a single-key table / DEFAULT_TABLE we will print the description as the table description.
            if indentation or table != DEFAULT_TABLE:
                descriptions.append(str(schema["description"]).replace("\n", "<br>"))

        if descriptions:
            return "<br>".join(descriptions)
        return None

    def _get_tables(self, schema: dict):
        table = schema.get("documentation_options", {}).get("table", DEFAULT_TABLE)
        tables = [table]

        # Only check for table on childschemas if the parent is set to default.
        # This ensures that all keys below will inherit the parent setting
        if table == DEFAULT_TABLE:
            if "keys" in schema:
                for key, childschema in schema["keys"].items():
                    # tables.extend(self._get_tables(childschema, default_table))
                    tables.extend(self._get_tables(childschema))

            if "dynamic_keys" in schema:
                for key, childschema in schema["dynamic_keys"].items():
                    # tables.extend(self._get_tables(childschema, default_table))
                    tables.extend(self._get_tables(childschema))

            if "items" in schema:
                # tables.extend(self._get_tables(schema["items"], default_table))
                tables.extend(self._get_tables(schema["items"]))

        # Return list of unique tables
        return list(set(tables))

    def _get_filenames(self, schema: dict):
        filename = schema.get("documentation_options", {}).get("filename", self._default_filename)
        filenames = [filename]

        # Only check for filename on childschemas if the parent is set to default.
        # This ensures that all keys below will inherit the parent setting
        if filename == self._default_filename:
            if "keys" in schema:
                for key, childschema in schema["keys"].items():
                    filenames.extend(self._get_filenames(childschema))

            if "dynamic_keys" in schema:
                for key, childschema in schema["dynamic_keys"].items():
                    filenames.extend(self._get_filenames(childschema))

            if "items" in schema:
                filenames.extend(self._get_filenames(schema["items"]))

        # Return list of unique tables
        return list(set(filenames))

    def _get_keys(self, schema: dict):
        keys = schema.get("keys", {})
        dynamic_keys = schema.get("dynamic_keys", {})
        keys.update({f"<{dynamic_key}>": subschema for dynamic_key, subschema in dynamic_keys.items()})
        return keys
