# Arista AVD Plugins

**Table of Contents:**

- [Arista AVD Plugins](#arista-avd-plugins)
  - [Plugin Filters](#plugin-filters)
    - [list_compress filter](#list_compress-filter)
    - [natural_sort filter](#natural_sort-filter)
    - [default filter](#default-filter)
  - [Plugin Tests](#plugin-tests)
    - [defined test](#defined-test)
  - [Modules](#modules)
    - [Inventory to CloudVision Containers](#inventory-to-cloudvision-containers)
    - [Add Table Of Contents to existing MarkDown file](#add-table-of-contents-to-existing-markdown-file)
    - [YAML Templates to Facts](#yaml-templates-to-facts)

## Plugin Filters

Arista AVD provides built-in filters to help extend jinja2 templates with functionality and improve code readability.

### list_compress filter

The `arista.avd.list_compress` filter provides the capabilities to compress a list of integers and return as a string for example:

```yaml
  - [1,2,3,4,5] -> "1-5"
  - [1,2,3,7,8] -> "1-3,7-8"
```

To use this filter:

```jinja
{{ list_to_compress | arista.avd.list_compress }}
```

### natural_sort filter

The `arista.avd.natural_sort` filter provides the capabilities to sort a list or a dictionary of integers and/or strings that contain alphanumeric characters naturally. When leveraged on a dictionary, only the key value will be returned.

The filter will return an empty list if the value parsed to `arista.avd.natural_sort` is `none` or `undefined`.

To use this filter:

```jinja
{% for item in dictionary_to_natural_sort | arista.avd.natural_sort %}
{{ natural_sorted_item }}
{% endfor %}
```

### default filter

The `arista.avd.default` filter can provide the same basic capability as the builtin `default` filter. It will return the input value only if it is valid and if not, provide a default value instead. Our custom filter requires a value to be `not undefined` and `not None` to pass through.
Furthermore the filter allows multiple default values as arguments, which will undergo the same validation one after one until we find a valid default value.
As a last resort the filter will return None.

To use this filter:

```jinja
{{ variable | arista.avd.default( default_value_1 , default_value_2 ... ) }}
```

## Plugin Tests

Arista AVD provides built-in test plugins to help verify data efficiently in jinja2 templates

### defined test

The `arista.avd.defined` test will return `False` if the passed value is `Undefined` or `none`. Else it will return `True`.
`arista.avd.defined` test also accepts an optional argument to test if the value equals this argument.

Compared to the builtin `is defined` test, this test will also test for `none` and can even test for a specific value.

To use this test:

```jinja
{% if extremely_long_variable_name is arista.avd.defined %}
text : {{ extremely_long_variable_name }}
{% endif %}
{% if extremely_long_variable_name is arista.avd.defined("something") %}
text : {{ extremely_long_variable_name }}
{% endif %}
Feature is {{ "not " if extremely_long_variable_name is not arista.avd.defined }}configured
```

The `arista.avd.defined` test can be useful as an alternative to:

```jinja
{% if extremely_long_variable_name is defined and extremely_long_variable_name is not none %}
text : {{ extremely_long_variable_name }}
{% endif %}
{% if extremely_long_variable_name is defined and extremely_long_variable_name == "something" %}
text : {{ extremely_long_variable_name }}
{% endif %}
Feature is {{ "not " if extremely_long_variable_name is defined and extremely_long_variable_name is not none }}configured
```

### containing test

The `arista.avd.containing` test will test if a list contains one or more of the supplied value(s).
The test will return `False` if either the passed value or the test_values are `Undefined` or `none`.

The test accepts either a single test_value or a list of test_values.
To use this test:
```jinja
{% if my_list is arista.avd.containing(item) %}Match{% endif %}

{# or #}

{% if my_list is arista.avd.containing(item_list) %}Match{% endif %}
```

**Example**
The `arista.avd.containing` is used in the role `eos_designs` in combination with `selectattr` to parse the `platform_settings` list
for an element where `switch_platform` is contained in the `platforms` attribute.

Without the `selectattr` and `arista.avd.containing` test:
```jinja
switch:
{% set ns = namespace() %}
{% for platform_setting in platform_settings %}
{%     set ns.platform_defined = false %}
{%     if switch_platform in platform_setting.platforms %}
{%         set ns.platform_defined = true ]}
  platform_settings: {{ platform_setting }}
{%         break; %}
{%     endif %}
{% endfor %}
{% for platform_setting in platform_settings if ns.platform_defined == false %}
{%     if 'default' in platform_setting.platforms %}
  platform_settings: {{ platform_setting }}
{%         break; %}
{%     endif %}
{% endfor %}
```
Without the `selectattr` and `arista.avd.containing` test:
```jinja
switch:
  platform_settings: {{ platform_settings | selectattr("platforms", "arista.avd.containing", switch_platform) | first | arista.avd.default(
                        platform_settings | selectattr("platforms", "arista.avd.containing", "default") | first) }}
```

## Modules

### Inventory to CloudVision Containers

The `arista.avd.inventory_to_container` module provides following capabilities:
- Transform inventory groups into CloudVision containers topology.
- Create list of configlets definition.

It saves everything in a `YAML` file using **`destination`** keyword.

It is a module to build structure of data to configure on a CloudVision server. Output is ready to be passed to [`arista.cvp`](https://github.com/aristanetworks/ansible-cvp/) to configure **CloudVision**.

**Example:**

To use this module:

```yaml
tasks:
  - name: generate intended variables
    tags: [always]
    inventory_to_container:
      inventory: '{{ inventory_file }}'
      container_root: '{{ container_root }}'
      configlet_dir: 'intended/configs'
      configlet_prefix: '{{ configlets_prefix }}'
      destination: '{{playbook_dir}}/intended/structured_configs/{{inventory_hostname}}.yml'
```

Inventory example applied to this example:

```yaml
all:
  children:
# DC1_Fabric - EVPN Fabric running in home lab
    DC1:
      children:
        DC1_FABRIC:
          children:
            DC1_SPINES:
              hosts:
                DC1-SPINE1:
                DC1-SPINE2:
            DC1_L3LEAFS:
              children:
                DC1_LEAF1:
                  hosts:
                    DC1-LEAF1A:
                    DC1-LEAF1B:
                DC1_LEAF2:
                  hosts:
                    DC1-LEAF2A:
                    DC1-LEAF2B:
```

Generated output ready to be used by [`arista.cvp`](https://github.com/aristanetworks/ansible-cvp/) collection:

```yaml
---
CVP_DEVICES:
  DC1-SPINE1:
    name: DC1-SPINE1
    parentContainerName: DC1_SPINES
    configlets:
        - DC1-AVD_DC1-SPINE1
    imageBundle: []

CVP_CONTAINERS:
  DC1_LEAF1:
    parent_container: DC1_L3LEAFS
  DC1_FABRIC:
    parent_container: Tenant
  DC1_L3LEAFS:
    parent_container: DC1_FABRIC
  DC1_LEAF2:
    parent_container: DC1_L3LEAFS
  DC1_SPINES:
    parent_container: DC1_FABRIC
```
### Add Table Of Contents to existing MarkDown file

The `arista.avd.add_toc` module provides following capabilities:
  - Wrapper of md-toc python library
  - Produce Table of Contents and add to MD file between markers

The module is used in `eos_designs` to create Table Of Contents for Fabric Documentation.
The module is used in `eos_cli_config_gen` to create Table Of Contents for Device Documentation.

**Example:**

To use this module:

```yaml
tasks:
- name: Generate TOC for fabric documentation
  add_toc:
    md_file: '{{ root_dir }}/documentation/fabric/{{ fabric_name }}-documentation.md'
    skip_lines: 3 #Default is 0
    #toc_levels: 2
    #toc_marker: '<!-- toc -->'
  delegate_to: localhost
  run_once: true
  check_mode: no
  tags: [build, provision]
```

### YAML Templates to Facts

The `arista.avd.yaml_templates_to_facts` module is an Ansible Action Plugin providing the following capabilities:
- Set Facts based on one or more Jinja2 templates producing YAML output.
- Recursively combining output of templates to allow templates to update overlapping parts of the data models.
- Facts set by one template will be accessable by the next templates
- Returned Facts can be set below a specific `root_key`
- Facts returned templates can be stripped for `null` values, to avoid them overwriting previous set facts

The module is used in `eos_designs` first to set facts for devices and then to set the `structured_configuration` variable based on all the `eos_designs` templates.

The module arguments are:

```yaml
- yaml_templates_to_facts:
    root_key: < optional root_key name >
    templates:
        # Path to template file
      - template: < template file >
        options:
          # Merge strategy for lists for Ansible Combine filter. See Ansible Combine filter for details.
          list_merge: < append (default) | replace | keep | prepend | append_rp | prepend_rp >
          # Filter out keys from the generated output if value is null/none/undefined
          strip_empty_keys: < true (default) | false >
```

Example:

```yaml
- name: Set AVD facts
  yaml_templates_to_facts:
    templates: "{{ templates[design.type].facts }}"
  check_mode: no
  changed_when: False
  tags: [build, provision]

- name: Generate device configuration in structured format
  yaml_templates_to_facts:
    root_key: structured_config
    templates: "{{ templates[design.type].structured_config }}"
  check_mode: no
  changed_when: False
  tags: [build, provision]
```

Role default variables applied to this example:

```yaml
# Design variables
design:
  type: "l3ls-evpn"

templates:
  # Templates defined per design
  l3ls-evpn:
    facts:
      # Set general "switch.*" variables
      - template: "facts/main.j2"
      # Set design specific "switch.*" variables
      - template: "designs/l3ls-evpn/facts/main.j2"
    structured_config:
      # Render Strucured Configuration
      # Base features
      - template: "base/main.j2"
      # MLAG feature
      - template: "mlag/main.j2"
      # Underlay feature
      - template: "designs/l3ls-evpn/underlay/main.j2"
      # Overlay feature
      - template: "designs/l3ls-evpn/overlay/main.j2"
      # L3 Edge feature
      - template: "l3_edge/main.j2"
      # Tenants feature
      - template: "designs/l3ls-evpn/tenants/main.j2"
      # Connected Endpoints feature
      - template: "connected_endpoints/main.j2"
      # Merge custom_structured_configuration last
      - template: "custom-structured-configuration-from-var.j2"
        options:
          list_merge: "{{ custom_structured_configuration_list_merge }}"
          strip_empty_keys: false
```
