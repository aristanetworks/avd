from __future__ import absolute_import, annotations, division, print_function

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.key_to_display_name import key_to_display_name

__metaclass__ = type

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema

# The DEFAULT_TABLE value is only used a dummy value for unset "table" value.
DEFAULT_TABLE = "_default_table_value_if_not_set"


def get_deprecation(schema: dict) -> tuple[str, str]:
    """
    Build deprecation details for documentation if deprecation is set on the schema element.

    This function is also imported into avdtojsonschemaconverter

    Returns
    -------
    deprecation_label : str | None
        If deprecated or removed this is "removed" or "deprecated". Should be added as label
        on the key by the calling function.
    deprecation : str | None
        Deprecation or removal message which should be added to the key comment field by the calling function.
    """
    if (deprecation := schema.get("deprecation")) is None:
        return None, None

    if removed := deprecation.get("removed"):
        removed_verb = "was"
        state_verb = "was"
        state = "removed"
    else:
        removed_verb = "will be"
        state_verb = "is"
        state = "deprecated"

    output = [f"This key {state_verb} {state}."]

    if (remove_in_version := deprecation.get("remove_in_version")) is not None:
        output.append(f"Support {removed_verb} removed in AVD version {remove_in_version}.")
    elif (remove_after_date := deprecation.get("remove_after_date")) is not None:
        output.append(f"Support {removed_verb} removed in the first major AVD version released after {remove_after_date}.")
    elif removed:
        output.append(f"Support {removed_verb} removed in AVD.")

    if (new_key := deprecation.get("new_key")) is not None:
        output.append(f"Use <samp>{new_key}</samp> instead.")

    if (url := deprecation.get("url")) is not None:
        output.append(f"See [here]({url}) for details.")

    return state, " ".join(output)


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
    "myfile":
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
        documentation_options_schema = meta_schema["$defs"]["documentation_options"]
        self._default_filename = documentation_options_schema["properties"]["filename"]["default"]

    def convert_schema(self):
        schema = {}
        output = {}

        # Get fully resolved schema (where all $ref has been expanded recursively)
        schema = self._avdschema.resolved_schema

        filenames = self._get_filenames(schema)

        for filename in filenames:
            output[filename] = {"tables": self.build_tables(schema=schema, filter_filename=filename)}

        return output

    def build_tables(self, schema: dict, filter_filename: str = None):
        tables = self._get_tables(schema)

        # Skip the default table, since we want a unique table per root key if table is not set.
        if DEFAULT_TABLE in tables:
            tables.remove(DEFAULT_TABLE)

        output = []
        # Build tables for keys where "documentation_options.table" is set in their schema
        for table in tables:
            built_table = self.build_table(table=table, schema=schema, filter_filename=filter_filename)
            # Only append if the table contain rows
            if built_table["table"]:
                output.append(built_table)

        # Build tables for all root keys if "documentation_options.table" is not set in their schema
        schema_keys = self._get_keys(schema)
        for key, childschema in schema_keys.items():
            table_schema = {"keys": {key: childschema}}
            built_table = self.build_table(table=DEFAULT_TABLE, schema=table_schema, filter_filename=filter_filename)
            # Only append if the table contain rows
            if built_table["table"]:
                output.append(built_table)

        return output

    def build_table(self, table: str, schema: dict, filter_filename: str = None):
        built_table = {}

        if table == DEFAULT_TABLE:
            # Single key table
            main_key = list(schema["keys"].keys())[0]
            main_key_schema = schema["keys"][main_key]
            built_table["display_name"] = main_key_schema.get("display_name", key_to_display_name(main_key))
            built_table["description"] = main_key_schema.get("description")
        else:
            # Combined table
            built_table["display_name"] = table

        schema_keys = self._get_keys(schema)

        built_table["table"] = []
        built_table["yaml"] = []
        for key, childschema in schema_keys.items():
            if filter_filename is not None and filter_filename not in self._get_filenames(childschema):
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

        deprecation_label, deprecation = get_deprecation(schema)
        if deprecation is not None:
            row["deprecation_label"] = deprecation_label
            row["deprecation"] = deprecation

        output.append(row)

        if schema.get("keys") or schema.get("dynamic_keys"):
            output.extend(self.keys(schema, indentation, var_path + [var_name], table))
        elif schema.get("items"):
            output.extend(self.items(schema, indentation, var_path + [var_name], table))

        return output

    def build_yaml_row(self, var_name: str, schema: dict, indentation: int, table: str, first_list_item_key: bool = False):
        output = []

        deprecation_label = get_deprecation(schema)[0]
        if deprecation_label == "removed":
            return output

        row_indentation = " " * indentation
        if first_list_item_key:
            # Make an indentation of "    " into "  - " to show this is a list item in YAML format
            row_indentation = f"{row_indentation[:-2]}- "

        row = f"{row_indentation}{var_name}:"
        var_type = schema.get("type")

        if var_type == "dict" and (schema_keys := self._get_keys(schema)):
            output.append(row)
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
        elif var_type == "list" and (schema_items := schema.get("items")):
            output.append(row)
            schema_items_type = schema_items.get("type")
            if schema_items_type == "dict" and "keys" in schema_items:
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
        else:
            row = f"{row} <{var_type}>"
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
        if schema.get("convert_to_lower_case"):
            restrictions.append("Value is converted to lower case")
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
            if valid_value not in schema["valid_values"]:
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

    def _get_tables(self, schema: dict, parent_table: str = DEFAULT_TABLE):
        """
        Get list of tables recursively for this schema and all childschemas.
        Handles inheritance by accepting the parent_table argument which will be used as the default table.
        """
        table = schema.setdefault("documentation_options", {}).setdefault("table", parent_table)
        tables = {table}

        if "keys" in schema:
            for key, childschema in schema["keys"].items():
                tables.update(self._get_tables(childschema, parent_table=table))

        if "dynamic_keys" in schema:
            for key, childschema in schema["dynamic_keys"].items():
                tables.update(self._get_tables(childschema, parent_table=table))

        if "items" in schema:
            tables.update(self._get_tables(schema["items"], parent_table=table))

        # Return sorted list of unique tables
        return sorted(tables)

    def _get_filenames(self, schema: dict, parent_filename: str = None):
        if parent_filename is None:
            parent_filename = self._default_filename

        filename = schema.setdefault("documentation_options", {}).setdefault("filename", parent_filename)
        filenames = {filename}

        if "keys" in schema:
            for key, childschema in schema["keys"].items():
                filenames.update(self._get_filenames(childschema, parent_filename=filename))

        if "dynamic_keys" in schema:
            for key, childschema in schema["dynamic_keys"].items():
                filenames.update(self._get_filenames(childschema, parent_filename=filename))

        if "items" in schema:
            filenames.update(self._get_filenames(schema["items"], parent_filename=filename))

        # Return sorted list of unique filenames
        return sorted(filenames)

    def _get_keys(self, schema: dict):
        keys = schema.get("keys", {})
        dynamic_keys = schema.get("dynamic_keys", {})
        keys.update({f"<{dynamic_key}>": subschema for dynamic_key, subschema in dynamic_keys.items()})
        return keys
