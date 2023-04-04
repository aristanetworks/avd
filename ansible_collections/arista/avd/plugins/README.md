# Arista AVD Plugins

## Plugin Filters

Arista AVD provides built-in filters to help extend jinja2 templates' functionality and improve code readability.

### list_compress filter

The `arista.avd.list_compress` filter provides the capabilities to compress a list of integers and return it as a string, for example:

```yaml
  - [1,2,3,4,5] -> "1-5"
  - [1,2,3,7,8] -> "1-3,7-8"
```

To use this filter:

```jinja
{{ list_to_compress | arista.avd.list_compress }}
```

### natural_sort filter

The `arista.avd.natural_sort` filter provides the capabilities to sort a list or a dictionary of integers and/or strings that contain alphanumeric characters naturally. When leveraged on a dictionary, only the key value will be returned. An optional `sort_key` can be specified, to sort on content of certain key if the items are dictionaries.

The filter will return an empty list if the value parsed to `arista.avd.natural_sort` is `None` or `undefined`.

To use this filter:

```jinja
{% for item in dictionary_to_natural_sort | arista.avd.natural_sort %}
{{ natural_sorted_item }}
{% endfor %}

{% for item in list_of_dicts_to_natural_sort | arista.avd.natural_sort('name') %}
{{ dict_sorted_on_name }}
{% endfor %}
```

### default filter

The `arista.avd.default` filter can provide the same essential capability as the built-in `default` filter. It will return the input value only if it's valid and, if not, provide a default value instead. Our custom filter requires a value to be `not undefined` and `not None` to pass through. Furthermore, the filter allows multiple default values as arguments, which will undergo the same validation until we find a valid default value. As a last resort, the filter will return None.

To use this filter:

```jinja
{{ variable | arista.avd.default( default_value_1 , default_value_2 ... ) }}
```

### convert_dicts filter

The `arista.avd.convert_dicts` filter will convert a dictionary containing nested dictionaries to a list of dictionaries. It inserts the outer dictionary keys into each list item using the primary_key `name` (the key name is configurable). If there is a non-dictionary value, it inserts this value to a secondary key (the key name is configurable); if a secondary key is provided.

This filter is intended for:

- Seamless data model migration from dictionaries to lists.
- Improve Ansible's processing performance when dealing with large dictionaries by converting them to lists of dictionaries.

!!! note
    If there is a non-dictionary value with no secondary key provided, it will pass through untouched.

To use this filter:

```jinja
{# convert list of dictionary with default `name:` as the primary key and None secondary key #}
{% set example_list = example_dictionary | arista.avd.convert_dicts %}
{% for example_item in example_list %}
item primary key is {{ example_item.name }}
{% endfor %}

{# convert list of dictionary with `id:` set as the primary key and `types:` set as the secondary key #}
{% set example_list = example_dictionary | arista.avd.convert_dicts('id','types') %}
{% for example_item in example_list %}
item primary key is {{ example_item.id }}
item secondary key is {{ example_item.types }}
{% endfor %}
```

### ethernet segment identifiers management filter

To help provide consistency when configuring EVPN A/A ESI values, the `esi_management` filter plugin provides an abstraction in the form of a `short_esi` key. `short_esi` is an abbreviated three octets value to encode Ethernet Segment ID, LACP ID, and route target. The following jinja2 filters manage the transformation from abstraction to network values:

#### generate_esi filter

The `arista.avd.generate_esi` filter transforms short_esi: `0303:0202:0101` with prefix `0000:0000` to EVPN ESI: `0000:0000:0303:0202:0101`

**example:**

```jinja
esi: {{ l2leaf.node_groups[l2leaf_node_group].short_esi | arista.avd.generate_esi }}
```

#### generate_lacp_id filter

The `arista.avd.generate_lacp_id` filter transforms short_esi: `0303:0202:0101` to LACP ID format format: `0303.0202.0101`

**example:**

```jinja
lacp_id: {{ l2leaf.node_groups[l2leaf_node_group].short_esi | arista.avd.generate_lacp_id }}
```

#### generate_route_target filter

The `arista.avd.generate_route_target` filter transforms short_esi: `0303:0202:0101` to route-target format: `03:03:02:02:01:01`

**example:**

```jinja
rt: {{ l2leaf.node_groups[l2leaf_node_group].short_esi | arista.avd.generate_route_target }}
```

### add_md_toc filter

The `arista.avd.add_md_toc` filter will parse the input MarkDown and add a TOC between the `toc_markers`.

The module is used in `eos_designs` to create a table of contents for Fabric Documentation. The module is also used in `eos_cli_config_gen` to create a table of contents for Device Documentation.

To use this filter:

```jinja2
{{ markdown string | arista.avd.add_md_toc(skip_lines=0, toc_levels=3, toc_marker='<!-- toc -->') }}
```

| Argument | description | type | optional | default value |
| -------- | ----------- | ---- | -------- | ------------- |
| skip_lines | Skip first x lines when parsing MD file | Integer | True | 0 |
| toc_levels | How many levels of headings will be included in the TOC | Integer | True | 3 |
| toc_marker | TOC will be inserted or updated between two of these markers in the MD file | String | True | `"<!-- toc -->"`

**example:**

To use this module:

```yaml
tasks:
- name: Generate fabric documentation
  tags: [build, provision, documentation]
  run_once: true
  delegate_to: localhost
  check_mode: no
  copy:
    content: "{{ lookup('template','documentation/fabric-documentation.j2') | arista.avd.add_md_toc(skip_lines=3) }}"
    dest: "{{ fabric_dir }}/{{ fabric_name }}-documentation.md"
    mode: 0664
```

### range_expand filter

The `arista.avd.range_expand` filter provides the capabilities to expand a range of interfaces or list of ranges and return as a list for example:

The filter supports VLANs, interfaces, modules, sub-interfaces, and ranges are expanded at all levels. Within a single range, prefixes (ex. Ethernet, Eth, Po) are carried over to items without prefixes (see third example below).

```yaml
  - "Ethernet1"                                   -> ["Ethernet1"]
  - "Ethernet1-2"                                 -> ["Ethernet1", "Ethernet2"]
  - "Eth 3-5,7-8"                                 -> ["Eth 3", "Eth 4", "Eth 5", "Eth 7", "Eth 8"]
  - "et2-6,po1-2"                                 -> ["et2", "et3", "et4", "et5", "et6", "po1", "po2"]
  - ["Ethernet1"]                                 -> ["Ethernet1"]
  - ["Ethernet 1-2", "Eth3-5", "7-8"]             -> ["Ethernet 1", "Ethernet 2", "Eth3", "Eth4", "Eth5", "7", "8"]
  - ["Ethernet2-6", "Port-channel1-2"]            -> ["Ethernet2", "Ethernet3", "Ethernet4", "Ethernet5", "Ethernet6", "Port-channel1", "Port-channel2"]
  - ["Ethernet1/1-2", "Eth1-2/3-5,5/1-2"]         -> ["Ethernet1/1", "Ethernet1/2", "Eth1/3", "Eth1/4", "Eth1/5", "Eth2/3", "Eth2/4", "Eth2/5", "Eth5/1", "Eth5/2"]
  - ["Eth1.1,9-10.1", "Eth2.2-3", "Eth3/1-2.3-4"] -> ["Eth1.1", "Eth9.1", "Eth10.1", "Eth2.2", "Eth2.3", "Eth3/1.3", "Eth3/1.4", "Eth3/2.3", "Eth3/2.4"]
  - "1-3"                                         -> ["1", "2", "3"]
  - ["1", "2", "3"]                               -> ["1", "2", "3"]
  - "vlan1-3"                                     -> ["vlan1", "vlan2", "vlan3"]
  - "Et1-2/3-4/5-6"                               -> ["Et1/3/5", "Et1/3/6", "Et1/4/5", "Et1/4/6", "Et2/3/5", "Et2/3/6", "Et2/4/5", "Et2/4/6"]
```

To use this filter:

```jinja
{{ range_to_expand | arista.avd.range_expand }}
```

!!! note
    This isn't using the same range syntax as EOS for modular or break-out ports. For example, on EOS `et1/1-2/4` gives you `et1/1, et1/2, et1/3, et1/4, et2/1, et2/2, et2/3, et2/4` on a fixed switch, but a different result on a modular switch depending on the module types. In AVD, the same range would be `et1-2/1-4`.

### Password filters

The `arista.avd.encrypt` and `arista.avd.decrypt` filters are used to encrypt or decrypt supported passwords.

To use these filters:

```jinja
{{ <var_with_clear_text_password> | arista.avd.encrypt(passwd_type=<type>, key=<encryption_key>) }}
{{ <var_with_encrypted_password> | arista.avd.decrypt(passwd_type=<type>, key=<encryption_key>) }}
```

Supported types:

- bgp
- ospf_simple
- ospf_message_digest

!!! Note
For now this filter only supports encryption and decryption to type `7` and not type `8a` for OSPF and BGP passwords

#### BGP passwords

BGP passwords are encrypted/decrypted based on the Neighbor IP or the BGP Peer Group Name in EOS.

Example usage for `arista.avd.encrypt` filter for BGP is to use it in conjunction with Ansible Vault to be able to load a password and have it encrypted on the fly by AVD in `eos_designs`.

**example:**

```jinja
bgp_peer_groups:
  ipv4_underlay_peers:
    name: IPv4-UNDERLAY-PEERS
      password: "{{ bgp_vault_password | arista.avd.encrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"
```

#### OSPF passwords

OSPF passwords are encrypted/decrypted based on the interface name (e.g., Ethernet1), and for message-digest-key, the hash algorithm (in the list [md5, sha1, sha256, sha384, sha512]) and the key ID (between 1 and 255).

The filter provides two types for OSPF:

- `ospf_simple` for simple authentication, which requires only the password and the interface name as key inputs.
- `ospf_message_digest` for message digest keys which requires the password, the interface name as the key, the hash algorithm, and the key id as input.

Example usage for `arista.avd.encrypt` filter for OSPF is to use it in conjunction with Ansible Vault to be able to load a password and have it encrypted on the fly by AVD in `eos_designs`.

**examples:**

- Simple authentication

    ```jinja
    ethernet_interfaces:
      - name: Ethernet1:
        ospf_authentication: simple
        ospf_authentication_key: "{{ ospf_vault_password | arista.avd.encrypt(passwd_type='ospf_simple', key='Ethernet1') }}"
    ```

- Message Digest Keys

    ```jinja
    ethernet_interfaces:
      - name: Ethernet1:
        ospf_authentication: message-digest
        ospf_message_digest_keys:
          - id: 1
            hash_algorithm: md5
            key: "{{ ospf_vault_password | arista.avd.encrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"
    ```

## Plugin Tests

Arista AVD provides built-in test plugins to help verify data efficiently in jinja2 templates.

### defined test

The `arista.avd.defined` test will return `False` if the passed value is `Undefined` or `None`. Else it will return `True`. `arista.avd.defined` test also accepts an optional `test_value` argument to test if the value equals this. The optional `var_type` argument can also be used to test if the variable is of the expected type.

Optionally the test can emit warnings or errors if the test fails.

Compared to the builtin `is defined` test, this test will also test for `None` and can even test for a specific value or class.

Syntax:

```jinja
{% <value> is arista.avd.defined(test_value=<test_value>,
                                 var_type=['float', 'int', 'str', 'list', 'dict', 'tuple', 'bool'],
                                 fail_action=['warning','error'],
                                 var_name=<string representing name of value>) %}
```

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

Warnings or Errors can be emitted with the optional arguments `fail_action` and `var_name`:

```jinja
{% if my_dict.my_list[12].my_var is arista.avd.defined(fail_action='warning', var_name='my_dict.my_list[12].my_var') %}
>>> [WARNING]: my_dict.my_list[12].my_var was expected but not set. Output may be incorrect or incomplete!

{% if my_dict.my_list[12].my_var is arista.avd.defined(fail_action='error', var_name='my_dict.my_list[12].my_var') %}
>>> fatal: [DC2-RS1]: FAILED! => {"msg": "my_dict.my_list[12].my_var was expected but not set!"}

{% set my_dict.my_list[12].my_var = 'not_my_value' %}

{% if my_dict.my_list[12].my_var is arista.avd.defined('my_value', fail_action='warning', var_name='my_dict.my_list[12].my_var') %}
>>> [WARNING]: my_dict.my_list[12].my_var was set to not_my_value but we expected my_value. Output may be incorrect or incomplete!

{% if my_dict.my_list[12].my_var is arista.avd.defined('my_value', fail_action='error', var_name='my_dict.my_list[12].my_var') %}
>>> fatal: [DC2-RS1]: FAILED! => {"msg": "my_dict.my_list[12].my_var was set to not_my_value but we expected my_value!"}
```

### contains test

The `arista.avd.contains` test will test if a list contains one or more of the supplied values. The test will return `False` if either the passed value or the test_values are `Undefined` or `none`.

The test accepts either a single test_value or a list of test_values.

To use this test:

```jinja
{% if my_list is arista.avd.contains(item) %}Match{% endif %}

{# or #}

{% if my_list is arista.avd.contains(item_list) %}Match{% endif %}
```

**example:**

The `arista.avd.contains` is used in the role `eos_designs` in combination with `selectattr` to parse the `platform_settings` list for an element where `switch_platform` is contained in the `platforms` attribute.

Data model:

```yaml
platform_settings:
  - platforms: [default]
    reload_delay:
      mlag: 300
      non_mlag: 330
  - platforms: [ 7280R, 7280R2, 7500R, 7500R2, 7020R ]
    tcam_profile: vxlan-routing
    lag_hardware_only: true
    reload_delay:
      mlag: 900
      non_mlag: 1020
  - platforms: [ 7280R3, 7500R3, 7800R3 ]
    reload_delay:
      mlag: 900
      non_mlag: 1020
```

Jinja template without the `selectattr` and `arista.avd.contains` test:

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

Jinja template with the `selectattr` and `arista.avd.contains` test:

```jinja
switch:
  platform_settings: {{ platform_settings | selectattr("platforms", "arista.avd.contains", switch_platform) | first | arista.avd.default(
                        platform_settings | selectattr("platforms", "arista.avd.contains", "default") | first) }}
```

## Modules

### Inventory to CloudVision Containers

The `arista.avd.inventory_to_container` module provides following capabilities:

- Transform inventory groups into CloudVision containers topology.
- Create a list of configlet definitions.

It saves everything in a `YAML` file using the **`destination`** keyword.

It's a module to build a data structure to configure a CloudVision server. Output is ready to be passed to [`arista.cvp`](https://github.com/aristanetworks/ansible-cvp/) to configure **CloudVision**.

**example:**

To use this module:

```yaml
tasks:
  - name: generate intended variables
    tags: [always]
    arista.avd.inventory_to_container:
      inventory: "{{ inventory_file }}"
      container_root: "{{ container_root }}"
      configlet_dir: "intended/configs"
      configlet_prefix: "{{ configlets_prefix }}"
      destination: "{{ playbook_dir }}/intended/structured_configs/{{ inventory_hostname }}.yml"
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
cvp_devices:
  DC1-SPINE1:
    name: DC1-SPINE1
    parentContainerName: DC1_SPINES
    configlets:
        - DC1-AVD_DC1-SPINE1
    imageBundle: []

cvp_containers:
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

### Build Configuration to publish configlets to CloudVision

The `arista.avd.configlet_build_config` module provides the following capabilities:

- Build arista.cvp.configlet configuration.
- Build configuration to publish configlets to CloudVision.

**options:**

```yaml
- arista.avd.configlet_build_config:
    configlet_dir:  "< Directory where configlets are located | Required >"
    configlet_prefix: "< Prefix to append on configlet | Required >"
    destination: "< File where to save information | Optional >"
    configlet_extension: "< File extension to look for | Default 'conf' >"
```

**example:**

```yaml
# tasks file for configlet_build_config
- name: generate intended variables
  tags: [build, provision]
  arista.avd.configlet_build_config:
    configlet_dir: "/path/to/configlets/folder/"
    configlet_prefix: "AVD_"
    configlet_extension: "cfg"
```

### YAML Templates to Facts

The `arista.avd.yaml_templates_to_facts` module is an Ansible Action Plugin providing the following capabilities:

- Set Facts based on one or more Jinja2 templates producing YAML output.
- Recursively combining templates' output to allow templates to update overlapping parts of the data models.
- Facts set by one template will be accessible by the following templates.
- Returned facts can be set below a specific `root_key`.
- Facts returned templates can be stripped for `null` values to avoid overwriting previous set facts.

The module is used in `eos_designs` to generate the `structured_configuration` based on all the `eos_designs` templates.

The module arguments are:

```yaml
- arista.avd.yaml_templates_to_facts:
    root_key: < optional root_key name >
    templates:
        # Path to template file
      - template: "< template file >"
        options:

          # Merge strategy for lists for Ansible Combine filter. See Ansible Combine filter for details.
          list_merge: < append (default) | replace | keep | prepend | append_rp | prepend_rp >

          # Filter out keys from the generated output if value is null/none/undefined
          strip_empty_keys: < true (default) | false >

    # Output list 'avd_yaml_templates_to_facts_debug' with timestamps of each performed action.
    debug: < true | false (default) >

    # Destination path. If set, the output facts will also be written to this path.
    # Autodetects data format based on file suffix. '.yml', '.yaml' -> YAML, default -> JSON
    dest: < path >

    # If true the output data will be run through another jinja2 rendering before returning.
    # This is to resolve any input values with inline jinja using variables/facts set by the input templates.
    template_output: < true | false (default) >

    # Export cProfile data to a file ex. "eos_designs_structured_config-{{inventory_hostname}}"
    cprofile_file: < filename >
```

**example:**

```yaml
- name: Set AVD facts
  tags: [build, provision]
  arista.avd.yaml_templates_to_facts:
    templates: "{{ templates.facts }}"
  delegate_to: localhost
  check_mode: no
  changed_when: False

- name: Generate device configuration in structured format
  tags: [build, provision]
  arista.avd.yaml_templates_to_facts:
    templates: "{{ templates.structured_config }}"
    dest: "{{ structured_dir }}/{{ inventory_hostname }}.{{ avd_structured_config_file_format }}"
    template_output: True
  delegate_to: localhost
  check_mode: no
  register: structured_config
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
      - template: "facts/main.j2"
    structured_config:
      # Render Structured Configuration
      # Base features
      - template: "base/main.j2"
      # MLAG feature
      - template: "mlag/main.j2"
      # Underlay feature
      - template: "underlay/main.j2"
      # Overlay feature
      - template: "overlay/main.j2"
      # L3 Edge feature
      - template: "l3_edge/main.j2"
      # Tenants feature
      - template: "network_services/main.j2"
      # Connected Endpoints feature
      - template: "connected_endpoints/main.j2"
      # Merge custom_structured_configuration last
      - template: "custom-structured-configuration-from-var.j2"
        options:
          list_merge: "{{ custom_structured_configuration_list_merge }}"
          strip_empty_keys: false
```

### EOS Designs Facts

The `arista.avd.eos_designs_facts` module is an Ansible Action Plugin providing the following capabilities:

- Set `avd_switch_facts` fact containing both `switch` facts per host.
- Set `avd_topology_peers` fact containing a list of downlink switches per host. This list is built based on the `uplink_switches` from all other hosts.
- Set `avd_overlay_peers` fact containing a list of EVPN or MPLS overlay peers per host. This list is built based on the `evpn_route_servers` and `mpls_route_reflectors` from all other hosts.
- The plugin is designed to `run_once`. With this, Ansible will set the same facts on all devices, so all devices can lookup values of any other device without using the slower `hostvars`.
- The facts can also be copied to the "root" `switch` in a task run per device (see example below).

The module is used in `arista.avd.eos_designs` to set facts for devices, which are then used by Jinja templates in `arista.avd.eos_designs` to generate the `structured_configuration`.

The module arguments are:

```yaml
- eos_designs_facts:
    # Calculate and set 'avd_switch_facts.<devices>.switch', 'avd_overlay_peers' and 'avd_topology_peers' facts
    avd_switch_facts: < True | False >

    # Export cProfile data to a file ex. "eos_designs_facts-{{inventory_hostname}}.prof"
    cprofile_file: < filename >
```

The output data model is:

```yaml
ansible_facts:
  avd_switch_facts:
    <switch_1>:
      switch:
        < switch.* facts used by eos_designs >
    <switch_2>:
      ...
  avd_topology_peers:
    <uplink_switch_1>:
      - <downlink_switch_1>
      - <downlink_switch_2>
      - <downlink_switch_3>
    <uplink_switch_1>:
      ...
  avd_overlay_peers:
    <route_server_1>:
      - <route_server_client_1>
      - <route_server_client_2>
      - <route_server_client_3>
    <route_server_2>:
      - <route_server_client_1>
      - <route_server_client_2>
      - <route_server_client_3>
```

The facts can be inspected in a file per device by running the `arista.avd.eos_designs` role with `--tags facts,debug`.

**example playbook:**

```yaml
- name: Set eos_designs facts
  tags: [build, provision, facts]
  arista.avd.eos_designs_facts:
    avd_switch_facts: True
  check_mode: False
  run_once: True

- name: Set eos_designs facts per device
  tags: [build, provision, facts]
  ansible.builtin.set_fact:
    switch: "{{ avd_switch_facts[inventory_hostname].switch }}"
  delegate_to: localhost
  changed_when: False
```

### Validate and Template

The `arista.avd.validate_and_template` Action Plugin performs data conversions and validation according to the supplied Schema.
The converted data is then used to render a Jinja2 template and writing the result to a file.

The Action Plugin supports different modes for conversion and validation, to either block the playbook or just warn the user if
the input data is not valid.

For Markdown files the plugin can also run `md_toc` on the output before writing to the file.

The module is used in `eos_cli_config_gen` for generating configuration and documentation outputs. By combining conversion, validation
and template generation in a single tasks, we can avoid Ansible's variable precendence from interfering with the converted vars.

If `dest` is not set, the template output will be returned under the `output` key in the result.

The module arguments are:

```yaml
  # Path to Jinja2 Template file | Required
  ansible.builtin.template: <str>

  # Destination path. The rendered template will be written to this file | Optional
  dest: <str>

  # File mode for dest file | Optional
  mode: <str>

  # Schema conforming to "AVD Meta Schema" | Required
  schema: <dict>

  # Run md_toc on the output before writing to the file | Optional
  add_md_toc: <bool>

  # Pass this value as skip_lines to add_md_toc | Optional, default: 0
  md_toc_skip_lines: <int>

  # Run data conversion in either "warning", "info", "debug", "quiet" or "disabled" mode | Optional, default: "debug"
  # Conversion will perform type conversion of input variables as defined in the schema.
  # Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
  # During conversion, messages will generated with information about the host(s) and key(s) which required conversion.
  # conversion_mode:disabled means that conversion will not run.
  # conversion_mode:error will produce error messages and fail the task.
  # conversion_mode:warning will produce warning messages.
  # conversion_mode:info will produce regular log messages.
  # conversion_mode:debug will produce hidden messages viewable with -v.
  # conversion_mode:quiet will not produce any messages
  conversion_mode: <str>

  # Run validation in either "error", "warning", "info", "debug" or "disabled" mode | Optional, default: "warning"
  # Validation will validate the input variables according to the schema.
  # During validation, messages will generated with information about the host(s) and key(s) which failed validation.
  # validation_mode:disabled means that validation will not run.
  # validation_mode:error will produce error messages and fail the task.
  # validation_mode:warning will produce warning messages.
  # validation_mode:info will produce regular log messages.
  # validation_mode:debug will produce hidden messages viewable with -v.
  validation_mode: <str>
```

Example:

```yaml
- name: Generate device documentation
  tags: [build, provision, documentation]
  arista.avd.validate_and_template:
    template: "eos-device-documentation.j2"
    dest: "{{ devices_dir }}/{{ inventory_hostname }}.md"
    mode: 0664
    schema: "{{ lookup('ansible.builtin.file', role_schema_path) | from_yaml }}"
    conversion_mode: "{{ avd_data_conversion_mode }}"
    validation_mode: "{{ avd_data_validation_mode }}"
    add_md_toc: true
    md_toc_skip_lines: 3
  delegate_to: localhost
  when: generate_device_documentation | arista.avd.default(true)
```

### Batch Template

The `arista.avd.batch_template`  Action Plugin performs templating of one template for multiple "items".

Results are written to individual files named using format string passed to the plugin. Destination file mode is hardcoded to 0o664.

```yaml
options:
  template:
    description: Path to Jinja2 Template file
    required: true
    type: str
  dest_format_str:
    description: Format string used to specify target file for each item. 'item' is the current item from 'items'. Like "mypath/{item}.md"
    required: true
    type: str
  items:
    description: List of strings. Each list item is passed to 'dest_format_str' as 'item' and passed to templater as 'item'
    required: true
    type: list
    elements: str

Example:

```yaml
- name: Output eos_cli_config_gen Documentation
  tags: [eos_cli_config_gen]
  delegate_to: localhost
  run_once: true
  arista.avd.batch_template:
    template: avd_schema_documentation.j2
    dest_format_str: "{{ role_documentation_dir }}/{item}.md"
    items: "{{ documentation_schema | list }}"
  vars:
    documentation_schema: "{{ role_name | arista.avd.convert_schema(type='documentation') }}"
```

### Verify Requirements

The `arista.avd.verify_requirements` module is an Ansible Action Plugin providing the following capabilities:

- Display the current running version of the collection.
- Given a list of python requirements, verify if the installed libraries match these requirements.
- Validate the ansible version against collection requirements.
- Validate the collection requirements against the collection requirements.
- Validate the running python version.

A task is added to every `eos_*` role in the collection but the Verify Requirement task will run only once per playbook when multiple roles are used.

Added in: version 4.0.0 of arista.avd

Module options (= is mandatory):

```yaml
# Boolean, if set to True, the play does not stop if any requirement error is detected | Optional
avd_ignore_requirements: <bool | default false>

# List of strings of python requirements with pip file syntax | Required
requirements: <list of str>
```

Example:

```yaml
- name: Verify collection requirements
  arista.avd.verify_requirements:
    requirements:
      - Jinja2 >= 2.9
      - paramiko == 2.7.1
  check_mode: false
  run_once: true
```

Example output (with debug):

```text
TASK [arista.avd.eos_designs : Verify Requirements] ********************************************************************************************************************************
AVD version v4.0.0-dev5-25-g0233492b5
{
    "ansible": {
        "collection": {
            "name": "arista.avd",
            "path": "/tmp/ansible-avd/ansible_collections",
            "version": "v4.0.0-dev5-25-g0233492b5"
        },
        "ansible_version": "2.14.2",
        "requires_ansible": "!=2.13.0,<2.15.0,>=2.12.6",
        "collection_requirements": {
            "not_found": {},
            "valid": {
                "arista.cvp": {
                    "installed": "3.3.1",
                    "required_version": null
                },
                "arista.eos": {
                    "installed": "4.1.1",
                    "required_version": null
                },
                "ansible.netcommon": {
                    "installed": "3.0.1",
                    "required_version": "!=2.6.0,>=2.4.0"
                }
            },
            "mismatched": {},
            "parsing_failed": []
        }
    },
    "python": {
        "python_version_info": {
            "major": 3,
            "minor": 10,
            "micro": 3,
            "releaselevel": "final",
            "serial": 0
        },
        "python_path": [
            "/tmp/.pyenv/versions/3.10.3/envs/ansible-avd/bin",
            "/tmp/.pyenv/versions/3.10.3/lib/python310.zip",
            "/tmp/.pyenv/versions/3.10.3/lib/python3.10",
            "/tmp/.pyenv/versions/3.10.3/lib/python3.10/lib-dynload",
            "/tmp/.pyenv/versions/3.10.3/envs/ansible-avd/lib/python3.10/site-packages"
        ],
        "python_requirements": {
            "not_found": {},
            "valid": {
                "netaddr": {
                    "installed": "0.8.0",
                    "required_version": ">=0.7.19"
                },
                "Jinja2": {
                    "installed": "3.1.2",
                    "required_version": ">=2.11.3"
                },
                "treelib": {
                    "installed": "1.6.1",
                    "required_version": ">=1.5.5"
                },
                "cvprac": {
                    "installed": "1.2.2",
                    "required_version": ">=1.0.7"
                },
                "paramiko": {
                    "installed": "3.0.0",
                    "required_version": ">=2.7.1"
                },
                "jsonschema": {
                    "installed": "4.17.3",
                    "required_version": ">=4.5.1"
                },
                "requests": {
                    "installed": "2.28.2",
                    "required_version": ">=2.25.1"
                },
                "PyYAML": {
                    "installed": "5.4.1",
                    "required_version": ">=5.4.1"
                },
                "md-toc": {
                    "installed": "8.1.8",
                    "required_version": ">=7.1.0"
                },
                "deepmerge": {
                    "installed": "1.1.0",
                    "required_version": ">=1.1.0"
                },
                "cryptography": {
                    "installed": "39.0.0",
                    "required_version": ">=38.0.4"
                },
                "packaging": {
                    "installed": "23.0",
                    "required_version": ">=21.3"
                }
            },
            "mismatched": {},
            "parsing_failed": []
        }
    }
}
```
