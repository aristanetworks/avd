# .yaml_templates_to_facts

Set facts from YAML via Jinja2 templates

## Synopsis

Set facts from YAML produced by Jinja2 templates

## Parameters

  root_key (False, str, None)
    Root key under which the facts will be defined\. If not set the facts well be set directly on root level\.

  schema (False, dict, None)
    Schema conforming to \"AVD Meta Schema\"\. Either schema or schema\_id must be set\.

  schema_id (False, str, None)
    ID of Schema conforming to \"AVD Meta Schema\"\.  Either schema or schema\_id must be set\.

  templates (True, list, None)
    List of dicts for Jinja templates to be run\.

    template (False, str, None)
      Template file\.
Either template or python\_module must be set\.

    python_module (False, str, None)
      Python module to import
Either template or python\_module must be set\.

    python_class_name (False, str, AvdStructuredConfig)
      Name of Python Class to import


    options (False, dict, None)
      Template options

      list_merge (False, str, append)
        Merge strategy for lists

      strip_empty_keys (False, bool, True)
        Filter out keys from the generated output if value is null/none/undefined
Only applies to templates\.

  debug (False, bool, None)
    Output list \'avd\_yaml\_templates\_to\_facts\_debug\' with timestamps of each performed action\.

  dest (False, str, None)
    Destination path\. If set\, the output facts will also be written to this path\.
Autodetects data format based on file suffix\. \'\.yml\'\, \'\.yaml\' \-\> YAML\, default \-\> JSON

  mode (False, str, None)
    File mode \(ex\. 0664\) for dest file\. See \'ansible\.builtin\.copy\' module for details\.

  template_output (False, bool, None)
    If true the output data will be run through another jinja2 rendering before returning\.
This is to resolve any input values with inline jinja using variables/facts set by the input templates\.

  conversion_mode (False, str, debug)
    Run data conversion in either \"error\"\, \"warning\"\, \"info\"\, \"debug\"\, \"quiet\" or \"disabled\" mode\.
    Conversion will perform type conversion of input variables as defined in the schema\.
    Conversion is intended to help the user to identify minor issues with the input data\, while still allowing the data to be validated\.
    During conversion\, messages will be generated with information about the host\(s\) and key\(s\) which required conversion\.
    conversion\_mode\:disabled means that conversion will not run\.
    conversion\_mode\:error will produce error messages and fail the task\.
    conversion\_mode\:warning will produce warning messages\.
    conversion\_mode\:info will produce regular log messages\.
    conversion\_mode\:debug will produce hidden messages viewable with \-v\.
    conversion\_mode\:quiet will not produce any messages\.

  validation_mode (False, str, warning)
    Run validation in either \"error\"\, \"warning\"\, \"info\"\, \"debug\" or \"disabled\" mode\.
    Validation will validate the input variables according to the schema\.
    During validation\, messages will be generated with information about the host\(s\) and key\(s\) which failed validation\.
    validation\_mode\:disabled means that validation will not run\.
    validation\_mode\:error will produce error messages and fail the task\.
    validation\_mode\:warning will produce warning messages\.
    validation\_mode\:info will produce regular log messages\.
    validation\_mode\:debug will produce hidden messages viewable with \-v\.

  output_schema (False, dict, None)
    AVD Schema for output data\. Used for automatic merge of data\.

  output_schema_id (False, str, None)
    ID of AVD Schema for output data\. Used for automatic merge of data\.

  set_switch_fact (False, bool, True)
    Set \"switch\" fact from on \"avd\_switch\_facts\.\<inventory\_hostname\>\.switch\"

## Examples

```yaml

    - name: Generate device configuration in structured format
      arista.avd.yaml_templates_to_facts:
        root_key: structured_config
        templates:
          - python_module: "ansible_collections.arista.avd.roles.eos_designs.python_modules.base"
            python_class_name: "AvdStructuredConfig"
          - template: "mlag/main.j2"
          - template: "designs/underlay/main.j2"
          - template: "designs/overlay/main.j2"
          - template: "l3_edge/main.j2"
          - template: "designs/network_services/main.j2"
          - template: "connected_endpoints/main.j2"
          - template: "custom-structured-configuration-from-var.j2"
            options:
              list_merge: "{{ custom_structured_configuration_list_merge }}"
              strip_empty_keys: false
        schema_id: eos_designs
        output_schema_id: eos_cli_config_gen
      check_mode: no
      changed_when: False

```

## Status

## Authors

- EMEA AS Team (@aristanetworks)
