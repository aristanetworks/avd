# Arista AVD Plugins

**Table of Contents:**

- [Arista AVD Plugins](#arista-avd-plugins)
  - [Plugin Filters](#plugin-filters)
    - [**list_compress filter**](#listcompress-filter)
    - [**natural_sort filter**](#naturalsort-filter)

## Plugin Filters

Arista AVD provides built-in filters to help extend jinja2 templates

### **list_compress filter**

The `list_compress` filter provides the capabilities to compress a list of integers and return as a string for example:

```yaml
  - [1,2,3,4,5] -> "1-5"
  - [1,2,3,7,8] -> "1-3,7-8"
```

To use this filter:

```jinja
{{ list_to_compress | arista.avd.list_compress }}
```

### **natural_sort filter**

The `natural_sort` filter provides the capabilities to sort a list or a dictionary of integers and/or strings that contain alphanumeric characters naturally. When leveraged on a dictionary, only the key value will be returned.

The filter will return an empty list if the value parsed to `natural_sort` is `none` or `undefined`.

To use this filter:

```jinja
{% for item in dictionary_to_natural_sort | arista.avd.natural_sort %}
{{ natural_sorted_item }}
{% endfor %}
```

### **default filter**

The `default` filter can provide the same basic capability as the builtin `default` filter. It will return the input value only if it is valid and if not, provide a default value instead. Our custom filter requires a value to be `not undefined` and `not None` to pass through.
Furthermore the filter allows multiple default values as arguments, which will undergo the same validation one after one until we find a valid default value.
As a last resort the filter will return None.

To use this filter:

```jinja
{{ variable | arista.avd.default( default_value_1 , default_value_2 ... ) }}
```

## Plugin Tests

Arista AVD provides built-in test plugins to help verify data efficiently in jinja2 templates

### **defined test**

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
## Modules

### **Inventory to CloudVision Containers**

The `inventory_to_container` module provides following capabilities:
- Transform inventory groups into CloudVision containers topology.
- Create list of configlets definition.

It saves everything in a `YAML` file using **`destination`** keyword.

It is a module to build structure of data to configure on a CloudVision server. Output is ready to be passed to [`arista.cvp`](https://github.com/aristanetworks/ansible-cvp/) to configure **CloudVision**.

**Example:**

To use this module:

```yaml
tasks:
  - name: generate intented variables
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
