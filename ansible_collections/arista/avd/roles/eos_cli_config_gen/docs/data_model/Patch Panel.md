---
search:
  boost: 2
---

# Patch Panel

## Patch Panel

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>patch_panel</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;patches</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connectors</samp> | List, items: Dictionary |  |  | Min Length: 2<br>Max Length: 2 | Must have exactly two connectors to a patch of which at least one must be of type "interface" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String | Required |  | Valid Values:<br>- interface<br>- pseudowire |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint</samp> | String | Required |  |  | String with relevant endpoint depending on type.<br>Examples:<br>- "Ethernet1"<br>- "Ethernet1 dot1q vlan 123"<br>- "bgp vpws TENANT_A pseudowire VPWS_PW_1"<br>- "ldp LDP_PW_1"<br> |

=== "YAML"

    ```yaml
    patch_panel:
      patches:
        - name: <str>
          enabled: <bool>
          connectors:
            - id: <str>
              type: <str>
              endpoint: <str>
    ```
