<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Validation of Input Variables

!!! NOTE
    - Some schema validations are not implemented yet.

`eos_designs` and `eos_cli_config_gen` support a wide range of input variables described under the role documentation sections.

Internally the supported data models are described in the proprietary "AVD Schema" format, which is used to perform validation of
the input variables at run-time. The same schema is also used to generate the role documentation describing the supported data
models.

For details on the schema format see the [Schema Details](#schema-details) section below.

## Automatic Type Conversion

The validation of input variables is performed in most AVD Action Plugins. The validation also supports automatic conversion of
variable types, if configured in the schema. The supported types that can be converted from depends on the type to be converted to.
The current implementation supports the automatic conversions listed below.

| From (`convert_types`) | To (`type`) |
| ---------------------- | ----------- |
| `bool`, `str` | `int` |
| `int`, `str` | `bool` |
| `bool`, `int` | `str` |
| `dict`*, `list`** | `list` |

\* If `primary_key` is set on the `list` schema, conversion from `dict`-of-`dicts` to `list`-of-`dicts` will insert the `primary_key`
with the value of the outer dictionary key in each `dict`. If `primary_key` is *not* set on the `list` schema, only the input `dict`
keys are returned as `list` items (any input `dict` values are lost).
\*\* If `primary_key` is set on the `list` schema, conversion from `list` to `list`-of-`dicts` will insert the `primary_key` with the
value of the input `list` items in each `dict`.

An example of input variable conversion is `bgp_as`. `bgp_as` is expected as a string (`str`) since 32-bit AS numbers can be
written with dot-notation such as `"65001.10000"`. Most deployments use 16-bit AS numbers, where the setting `bgp_as: 65001` will be interpreted as an integer in YAML, unless it is enclosed in quotes `bgp_as: "65001"`. In the schema for `bgp_as` the `convert_types` option is configured to `['int']` which means AVD Action Plugins will automatically convert
`bgp_as: 65001` to `bgp_as: "65001"`.

Type conversion is also used for introducing changes to the data models without affecting existing deployments. For example,
in AVD 4.0, the data models using "Dictionaries with wildcard keys" has been be changed to lists.
Ex. the old data model:

```yaml
tenants:
  mytenant:
    vrfs:
      myvrf:
        ...
```

has been be changed to:

```yaml
tenants:
  - name: mytenant
    vrfs:
      - name: myvrf
        ...
```

The input data will be converted automatically and validated according to the new model to allow for a gracious introduction of this data-model changes in late 3.x versions.

Type conversion is turned on by default.

!!! CAUTION
    Although conversion can be disabled, this is **not** recommended, and will most likely lead to issues with AVD or the generated
    configuration. Data conversion also handles data deprecation and upgrades.

## Validation Options

Schema validation is built in to the central Action plugins used in AVD. Each plugin runs variable type conversion first and then
performs validation of the converted data.

By default the data conversions are logged with `-v` and data validation issues will trigger warnings - not blocking further processing.
This behavior can be adjusted by setting the variables described below.

```yaml
# Conversion Mode for AVD input data conversion | Optional
# During conversion, messages will generated with information about the host(s) and key(s) which required conversion.
# "disabled" means that conversion will not run - avoid this since conversion is also handling data deprecation and upgrade.
# "error" will produce error messages and fail the task.
# "warning" will produce warning messages.
# "info" will produce regular log messages.
# "debug" will produce hidden debug messages viewable with -v.
# "quiet" will not produce any messages
avd_data_conversion_mode: < "disabled" | "error" | "warning" | "info" | "debug" | "quiet" | default -> "debug" >

# Validation Mode for AVD input data validation | Optional
# During validation, messages will generated with information about the host(s) and key(s) which failed validation.
# "disabled" means that validation will not run.
# "error" will produce error messages and fail the task.
# "warning" will produce warning messages.
# "info" will produce regular log messages.
# "debug" will produce hidden debug messages viewable with -v.
avd_data_validation_mode: < "disabled" | "error" | "warning" | "info" | "debug" | default -> "warning" >
```

## Schema Details

The AVD Schema format is a proprietary schema inspired by JSON Schema, Ansible Argument Specification and Arista
CloudVision Studios formats.

The AVD Schema has unique features which are not supported or possible with any of the mentioned schema formats.
Schema converters can be developed as needed.

Here is an example of a schema fragment for `bgp_as`:

```yaml
type: dict
allow_other_keys: true
keys:
  bgp_as:
    display_name: BGP AS
    description: AS number to use to configure overlay when "overlay_routing_protocol" == IBGP
    type: str
    convert_types:
      - int
```

This fragment will be merged with other fragments during development, to form the complete role schema.

For reference, the full Role Schemas can be found here:

- [`eos_designs` AVD Schema, not ready yet](../../roles/eos_designs/schemas/eos_designs.schema.yml)
- [`eos_cli_config_gen` AVD Schema](../../roles/eos_cli_config_gen/schemas/eos_cli_config_gen.schema.yml)

The supported schema options depend on the type of variable that is described. The supported types are `int`, `bool`, `str`,
`dict` and `list`. The schema does not support mixed types for the same variable, but the automatic type conversion mentioned
above can address the usability aspect by helping the user with common mistakes.

The supported schema options for AVD Schema are described in a meta-schema using JSON Schema Draft-7 format. The meta-schema
can be seen [here](../../plugins/plugin_utils/schema/avd_meta_schema.json). In addition, below is a more detailed description of the supported
schema options per variable type.

All schema options (ex. `type`, `max`, `valid_values`) are validated individually, and to pass the validation, the data must
conform to all the rules given by the schema options.
This means that the validator may report multiple errors about the same piece of data if it violates more than on rule.
This also means that a poorly written schema could have conflicting schema options, which may not allow any value. For example `type: str` schema with `min_length: 10` and `max_length: 5` would never be satisfied.

### Schema Options for type `int` (Integer)

| Key | Type | Required | Default | Value Restrictions | Description |
| ----| ---- | -------- | ------- | ------------------ | ----------- |
| <samp>type</samp> | String | True | | Valid Values:<br>- `"int"` | Type of variable using the Python short names for each type.<br>`int` for Integer |
| <samp>convert_types</samp> | List, items: String | | | | List of types to auto-convert from.<br>For type `int`, auto-conversion is supported from `bool` and `str` |
| <samp>&nbsp;&nbsp;- \<str\></samp> | String | | | Valid Values:<br>- `"bool"`<br>- `"str"` | |
| <samp>default</samp> | Integer | | | | Default value |
| <samp>max</samp> | Integer | | | | Maximum value |
| <samp>min</samp> | Integer | | | | Minimum value |
| <samp>valid_values</samp> | List, items: Integer | | | | List of valid values |
| <samp>&nbsp;&nbsp;- \<int\></samp> | Integer | | | | |
| <samp>dynamic_valid_values</samp> | String | | | | Path to variable under the parent dictionary containing valid values.<br>Variable path use dot-notation and variable path must be relative to the parent dictionary.<br>If an element of the variable path is a list, every list item will unpacked.<br>**Note that this is building the schema from values in the *data* being validated!** |
| <samp>display_name</samp> | String | | | Regex Pattern: `"^[^\n]+$"` | Free text display name for forms and documentation (single line) |
| <samp>description</samp> | String | | | Minimum Length: 1 | Free text description for forms and documentation (multi line) |
| <samp>required</samp> | Boolean | | | | Set if variable is required |
| <samp>deprecation</samp> | Dictionary | | | | Deprecation Settings |
| <samp>&nbsp;&nbsp;warning</samp> | Boolean | True | True | | Emit deprecation warning if key is set |
| <samp>&nbsp;&nbsp;new_key</samp> | String | | | | Relative path to new key |
| <samp>&nbsp;&nbsp;remove_in_version</samp> | String | | | | Version in which the key will be removed |
| <samp>&nbsp;&nbsp;remove_after_date</samp> | String | | | | Date after which the key will be removed |
| <samp>$ref</samp> | String | | | | Reference to Sub Schema using JSON Schema resolver<br>Example '#/keys/mykey' will resolve the schema for 'mykey' under the root dictionary of the current schema |
| <samp>documentation_options</samp> | Dictionary | | | | Special options used for generating documentation |
| <samp>&nbsp;&nbsp;table</samp> | String | | | | Setting 'table' will allow for custom grouping of schema fields in the documentation.<br>By default each root key has it's own table. By setting the same table-value on multiple keys, they will be merged to a single table.<br>If 'table' is set on a 'child' key, all "ancestor" keys are automatically included in the table so the full path is visible.<br>The 'table' option is inherited to all child keys, unless specifically set on the child. |

The meta-schema does not allow for other keys to be set in the schema.

### Schema Options for type `bool` (Boolean)

| Key | Type | Required | Default | Value Restrictions | Description |
| ----| ---- | -------- | ------- | ------------------ | ----------- |
| <samp>type</samp> | String | True | | Valid Values:<br>- `"bool"` | Type of variable using the Python short names for each type.<br>`bool` for Boolean |
| <samp>convert_types</samp> | List, items: String | | | | List of types to auto-convert from.<br>For type `bool`, auto-conversion is supported from `int` and `str` |
| <samp>&nbsp;&nbsp;- \<str\></samp> | String | | | Valid Values:<br>- `"int"`<br>- `"str"` | |
| <samp>default</samp> | Boolean | | | | Default value |
| <samp>valid_values</samp> | List, items: Boolean | | | | List of valid values |
| <samp>&nbsp;&nbsp;- \<int\></samp> | Boolean | | | | |
| <samp>dynamic_valid_values</samp> | String | | | | Path to variable under the parent dictionary containing valid values.<br>Variable path use dot-notation and variable path must be relative to the parent dictionary.<br>If an element of the variable path is a list, every list item will unpacked.<br>**Note that this is building the schema from values in the *data* being validated!** |
| <samp>display_name</samp> | String | | | Regex Pattern: `"^[^\n]+$"` | Free text display name for forms and documentation (single line) |
| <samp>description</samp> | String | | | Minimum Length: 1 | Free text description for forms and documentation (multi line) |
| <samp>required</samp> | Boolean | | | | Set if variable is required |
| <samp>deprecation</samp> | Dictionary | | | | Deprecation Settings |
| <samp>&nbsp;&nbsp;warning</samp> | Boolean | True | True | | Emit deprecation warning if key is set |
| <samp>&nbsp;&nbsp;new_key</samp> | String | | | | Relative path to new key |
| <samp>&nbsp;&nbsp;remove_in_version</samp> | String | | | | Version in which the key will be removed |
| <samp>&nbsp;&nbsp;remove_after_date</samp> | String | | | | Date after which the key will be removed |
| <samp>$ref</samp> | String | | | | Reference to Sub Schema using JSON Schema resolver<br>Example '#/keys/mykey' will resolve the schema for 'mykey' under the root dictionary of the current schema |
| <samp>documentation_options</samp> | Dictionary | | | | Special options used for generating documentation |
| <samp>&nbsp;&nbsp;table</samp> | String | | | | Setting 'table' will allow for custom grouping of schema fields in the documentation.<br>By default each root key has it's own table. By setting the same table-value on multiple keys, they will be merged to a single table.<br>If 'table' is set on a 'child' key, all "ancestor" keys are automatically included in the table so the full path is visible.<br>The 'table' option is inherited to all child keys, unless specifically set on the child. |

The meta-schema does not allow for other keys to be set in the schema.

### Schema Options for type `str` (String)

| Key | Type | Required | Default | Value Restrictions | Description |
| ----| ---- | -------- | ------- | ------------------ | ----------- |
| <samp>type</samp> | String | True | | Valid Values:<br>- `"str"` | Type of variable using the Python short names for each type.<br>`str` for String |
| <samp>convert_to_lower_case</samp> | Boolean | | False | | Convert string value to lower case before performing validation |
| <samp>convert_types</samp> | List, items: String | | | | List of types to auto-convert from.<br>For type `str`, auto-conversion is supported from `bool` and `int` |
| <samp>default</samp> | String | | | | Default value |
| <samp>&nbsp;&nbsp;- \<str\></samp> | String | | | Valid Values:<br>- `"bool"`<br>- `"int"` | |
| <samp>format</samp> | String | | | Valid Values:<br>- `"ipv4"`<br>- `"ipv4_cidr"`<br>- `"ipv6"`<br>- `"ipv6_cidr"`<br>- `"ip"`<br>- `"cidr"`<br>- `"mac"` | Expected format of the string value.<br>`ipv4` accepts a single IPv4 address (`x.x.x.x`)<br>`ipv4_cidr` accepts an IPv4 CIDR (`x.x.x.x/x`)<br>`ipv6` accepts a single IPv6 address (`x:x::x:x`)<br>`ipv6_cidr` accepts an IPv6 CIDR (`x:x::x:x/x`)<br>`ip` accepts a single IPv4 or IPv6 address<br>`cidr` accepts an IPv4 or IPv6 CIDR<br>`mac` accepts a MAC address (`xx:xx:xx:xx:xx:xx`) |
| <samp>max_length</samp> | Integer | | | | Maximum length |
| <samp>min_length</samp> | Integer | | | | Minimum length |
| <samp>pattern</samp> | String | | | Format: Regex | A regular expression which will be matched on the variable value.<br>The regular expression should follow the syntax of [JSON Schema Regular Expressions](https://json-schema.org/understanding-json-schema/reference/regular_expressions.html)<br>Remember to use double escapes |
| <samp>valid_values</samp> | List, items: String | | | | List of valid values |
| <samp>&nbsp;&nbsp;- \<str\></samp> | String | | | | |
| <samp>dynamic_valid_values</samp> | String | | | | Path to variable under the parent dictionary containing valid values.<br>Variable path use dot-notation and variable path must be relative to the parent dictionary.<br>If an element of the variable path is a list, every list item will unpacked.<br>**Note that this is building the schema from values in the *data* being validated!** |
| <samp>display_name</samp> | String | | | Regex Pattern: `"^[^\n]+$"` | Free text display name for forms and documentation (single line) |
| <samp>description</samp> | String | | | Minimum Length: 1 | Free text description for forms and documentation (multi line) |
| <samp>required</samp> | Boolean | | | | Set if variable is required |
| <samp>deprecation</samp> | Dictionary | | | | Deprecation Settings |
| <samp>&nbsp;&nbsp;warning</samp> | Boolean | True | True | | Emit deprecation warning if key is set |
| <samp>&nbsp;&nbsp;new_key</samp> | String | | | | Relative path to new key |
| <samp>&nbsp;&nbsp;remove_in_version</samp> | String | | | | Version in which the key will be removed |
| <samp>&nbsp;&nbsp;remove_after_date</samp> | String | | | | Date after which the key will be removed |
| <samp>$ref</samp> | String | | | | Reference to Sub Schema using JSON Schema resolver<br>Example '#/keys/mykey' will resolve the schema for 'mykey' under the root dictionary of the current schema |
| <samp>documentation_options</samp> | Dictionary | | | | Special options used for generating documentation |
| <samp>&nbsp;&nbsp;table</samp> | String | | | | Setting 'table' will allow for custom grouping of schema fields in the documentation.<br>By default each root key has it's own table. By setting the same table-value on multiple keys, they will be merged to a single table.<br>If 'table' is set on a 'child' key, all "ancestor" keys are automatically included in the table so the full path is visible.<br>The 'table' option is inherited to all child keys, unless specifically set on the child. |

The meta-schema does not allow for other keys to be set in the schema.

### Schema Options for type `list` (List)

| Key | Type | Required | Default | Value Restrictions | Description |
| ----| ---- | -------- | ------- | ------------------ | ----------- |
| <samp>type</samp> | String | True | | Valid Values:<br>- `"list"` | Type of variable using the Python short names for each type.<br>`list` for List |
| <samp>convert_types</samp> | List, items: String | | | | List of types to auto-convert from.<br>For `list` auto-conversion is supported from `dict` if `primary_key` is set on the list schema |
| <samp>default</samp> | List | | | | Default value |
| <samp>items</samp> | Dict | | | | Dictionary describing the schema of each list item. This is a recursive schema, so the value must conform to AVD Schema |
| <samp>max_length</samp> | Integer | | | | Maximum length |
| <samp>min_length</samp> | Integer | | | | Minimum length |
| <samp>primary_key</samp> | String | | | Pattern: `^[a-z][a-z0-9_]*$` | Name of a primary key in a list of dictionaries.<br>The configured key is implicitly required and must have unique values between the list elements |
| <samp>secondary_key</samp> | String | | | Pattern: `^[a-z][a-z0-9_]*$` | Name of a secondary key, which is used with `convert_types:['dict']` in case of values not being dictionaries |
| <samp>display_name</samp> | String | | | Regex Pattern: `"^[^\n]+$"` | Free text display name for forms and documentation (single line) |
| <samp>description</samp> | String | | | Minimum Length: 1 | Free text description for forms and documentation (multi line) |
| <samp>required</samp> | Boolean | | | | Set if variable is required |
| <samp>deprecation</samp> | Dictionary | | | | Deprecation Settings |
| <samp>&nbsp;&nbsp;warning</samp> | Boolean | True | True | | Emit deprecation warning if key is set |
| <samp>&nbsp;&nbsp;new_key</samp> | String | | | | Relative path to new key |
| <samp>&nbsp;&nbsp;remove_in_version</samp> | String | | | | Version in which the key will be removed |
| <samp>&nbsp;&nbsp;remove_after_date</samp> | String | | | | Date after which the key will be removed |
| <samp>$ref</samp> | String | | | | Reference to Sub Schema using JSON Schema resolver<br>Example '#/keys/mykey' will resolve the schema for 'mykey' under the root dictionary of the current schema |
| <samp>documentation_options</samp> | Dictionary | | | | Special options used for generating documentation |
| <samp>&nbsp;&nbsp;table</samp> | String | | | | Setting 'table' will allow for custom grouping of schema fields in the documentation.<br>By default each root key has it's own table. By setting the same table-value on multiple keys, they will be merged to a single table.<br>If 'table' is set on a 'child' key, all "ancestor" keys are automatically included in the table so the full path is visible.<br>The 'table' option is inherited to all child keys, unless specifically set on the child. |

The meta-schema does not allow for other keys to be set in the schema.

### Schema Options for type `dict` (Dictionary)

| Key | Type | Required | Default | Value Restrictions | Description |
| ----| ---- | -------- | ------- | ------------------ | ----------- |
| <samp>type</samp> | String | True | | Valid Values:<br>- `"dict"` | Type of variable using the Python short names for each type.<br>`dict` for Dictionary |
| <samp>default</samp> | Dict | | | | Default value |
| <samp>keys</samp> | Dictionary | | | Key Pattern: `^[a-z][a-z0-9_]*$` | Dictionary of dictionary-keys in the format `{<keyname>: {<schema>}}`.<br>`keyname` must use snake_case.<br>`schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema |
| <samp>dynamic_keys</samp> | Dictionary | | | Pattern: `^[a-z][a-z0-9_]*$` | Dictionary of dynamic dictionary-keys in the format `{<variable.path>: {<schema>}}`.<br>`variable.path` is a variable path using dot-notation and pointing to a variable under the parent dictionary containing dictionary-keys.<br>If an element of the variable path is a list, every list item will unpacked.<br>`schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema<br>**Note that this is building the schema from values in the *data* being validated!** |
| <samp>allow_other_keys</samp> | Boolean | | False | | Allow keys in the dictionary which are not defined in the schema. Custom keys starting with an underscore, like `_mycustomkey` are exempt from this validation |
| <samp>display_name</samp> | String | | | Regex Pattern: `"^[^\n]+$"` | Free text display name for forms and documentation (single line) |
| <samp>description</samp> | String | | | Minimum Length: 1 | Free text description for forms and documentation (multi line) |
| <samp>required</samp> | Boolean | | | | Set if variable is required |
| <samp>deprecation</samp> | Dictionary | | | | Deprecation Settings |
| <samp>&nbsp;&nbsp;warning</samp> | Boolean | True | True | | Emit deprecation warning if key is set |
| <samp>&nbsp;&nbsp;new_key</samp> | String | | | | Relative path to new key |
| <samp>&nbsp;&nbsp;remove_in_version</samp> | String | | | | Version in which the key will be removed |
| <samp>&nbsp;&nbsp;remove_after_date</samp> | String | | | | Date after which the key will be removed |
| <samp>$ref</samp> | String | | | | Reference to Sub Schema using JSON Schema resolver<br>Allows for easy reuse of schema definitions.<br>Example '#/keys/mykey' will resolve the schema for 'mykey' under the root dictionary of the current schema |
| <samp>documentation_options</samp> | Dictionary | | | | Special options used for generating documentation |
| <samp>&nbsp;&nbsp;table</samp> | String | | | | Setting 'table' will allow for custom grouping of schema fields in the documentation.<br>By default each root key has it's own table. By setting the same table-value on multiple keys, they will be merged to a single table.<br>If 'table' is set on a 'child' key, all "ancestor" keys are automatically included in the table so the full path is visible.<br>The 'table' option is inherited to all child keys, unless specifically set on the child. |

The meta-schema does not allow for other keys to be set in the schema.
