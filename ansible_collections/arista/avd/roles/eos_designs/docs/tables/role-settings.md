<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_6_behaviors</samp>](## "avd_6_behaviors") <span style="color:red">deprecated</span> | Dictionary |  |  |  | Opt-in to AVD 6 behaviors. These behaviors will be the default behaviors in AVD 6.0.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;snmp_settings_vrfs</samp>](## "avd_6_behaviors.snmp_settings_vrfs") | Boolean |  | `False` |  | Opt-in to the new behavior for snmp_settings:<br>- SNMP will only be enabled for VRFs specifically enabled under `snmp_settings.vrfs`.<br>  Note this means SNMP will be disabled for VRF "default" unless it is defined there.<br>- `snmp_settings.hosts[].vrf` defaults to `use_default_mgmt_method_vrf`.<br>  If `default_mgmt_method` is 'none', the VRF must be specified. For VRF default set the string "default". |
    | [<samp>avd_eos_designs_debug</samp>](## "avd_eos_designs_debug") | Boolean |  | `False` |  | Dump all vars and facts per device after generating `avd_switch_facts`. |
    | [<samp>avd_eos_designs_enforce_duplication_checks_across_all_models</samp>](## "avd_eos_designs_enforce_duplication_checks_across_all_models") | Boolean |  | `False` |  | PREVIEW: This option is marked as "preview", while we refactor the code to conform to the described behavior.<br>When this is enabled, the generation of Structured Config in `eos_designs` will prevent duplicate objects generated<br>by different input models. This will also improve performance since `eos_designs` will not maintain separate copied of the Structured Configuration.<br>As an example, if you define an Ethernet interface under `l3_edge` and use the same interface for connectivity under `servers`:<br>- With this option disabled (default), AVD will merge these configurations together for the interface and not raise an error.<br>- With this option enabled, AVD will raise an error about duplicate interface definitions. |
    | [<samp>avd_eos_designs_structured_config</samp>](## "avd_eos_designs_structured_config") | Boolean |  | `True` |  | Generate structured configuration per device. |
    | [<samp>avd_eos_designs_unset_facts</samp>](## "avd_eos_designs_unset_facts") | Boolean |  | `True` |  | Unset `avd_switch_facts` to gain a small performance improvement since Ansible needs to handle fewer variables. |
    | [<samp>eos_designs_documentation</samp>](## "eos_designs_documentation") | Dictionary |  |  |  | Control fabric documentation generation.<br> |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_designs_documentation.enable") | Boolean |  | `True` |  | Generate fabric-wide documentation. |
    | [<samp>&nbsp;&nbsp;connected_endpoints</samp>](## "eos_designs_documentation.connected_endpoints") | Boolean |  | `False` |  | Include connected endpoints in the fabric-wide documentation.<br>This is `false` by default to avoid cluttering documentation for projects with thousands of endpoints. |
    | [<samp>&nbsp;&nbsp;topology_csv</samp>](## "eos_designs_documentation.topology_csv") | Boolean |  | `False` |  | Generate Topology CSV with all interfaces towards other devices. |
    | [<samp>&nbsp;&nbsp;p2p_links_csv</samp>](## "eos_designs_documentation.p2p_links_csv") | Boolean |  | `False` |  | Generate P2P links CSV with all routed point-to-point links between devices. |
    | [<samp>&nbsp;&nbsp;toc</samp>](## "eos_designs_documentation.toc") | Boolean |  | `True` |  | Generate the table of content(TOC) on fabric documentation. |

=== "YAML"

    ```yaml
    # Opt-in to AVD 6 behaviors. These behaviors will be the default behaviors in AVD 6.0.
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    avd_6_behaviors:

      # Opt-in to the new behavior for snmp_settings:
      # - SNMP will only be enabled for VRFs specifically enabled under `snmp_settings.vrfs`.
      #   Note this means SNMP will be disabled for VRF "default" unless it is defined there.
      # - `snmp_settings.hosts[].vrf` defaults to `use_default_mgmt_method_vrf`.
      #   If `default_mgmt_method` is 'none', the VRF must be specified. For VRF default set the string "default".
      snmp_settings_vrfs: <bool; default=False>

    # Dump all vars and facts per device after generating `avd_switch_facts`.
    avd_eos_designs_debug: <bool; default=False>

    # PREVIEW: This option is marked as "preview", while we refactor the code to conform to the described behavior.
    # When this is enabled, the generation of Structured Config in `eos_designs` will prevent duplicate objects generated
    # by different input models. This will also improve performance since `eos_designs` will not maintain separate copied of the Structured Configuration.
    # As an example, if you define an Ethernet interface under `l3_edge` and use the same interface for connectivity under `servers`:
    # - With this option disabled (default), AVD will merge these configurations together for the interface and not raise an error.
    # - With this option enabled, AVD will raise an error about duplicate interface definitions.
    avd_eos_designs_enforce_duplication_checks_across_all_models: <bool; default=False>

    # Generate structured configuration per device.
    avd_eos_designs_structured_config: <bool; default=True>

    # Unset `avd_switch_facts` to gain a small performance improvement since Ansible needs to handle fewer variables.
    avd_eos_designs_unset_facts: <bool; default=True>

    # Control fabric documentation generation.
    eos_designs_documentation:

      # Generate fabric-wide documentation.
      enable: <bool; default=True>

      # Include connected endpoints in the fabric-wide documentation.
      # This is `false` by default to avoid cluttering documentation for projects with thousands of endpoints.
      connected_endpoints: <bool; default=False>

      # Generate Topology CSV with all interfaces towards other devices.
      topology_csv: <bool; default=False>

      # Generate P2P links CSV with all routed point-to-point links between devices.
      p2p_links_csv: <bool; default=False>

      # Generate the table of content(TOC) on fabric documentation.
      toc: <bool; default=True>
    ```
