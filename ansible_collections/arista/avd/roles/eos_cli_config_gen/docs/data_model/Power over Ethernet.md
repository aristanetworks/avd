---
search:
  boost: 2
---

# Power over Ethernet

## PoE

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>poe</samp>](## "poe") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;reboot</samp>](## "poe.reboot") | Dictionary |  |  |  | Set the global PoE power behavior for PoE ports when the system is rebooted. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "poe.reboot.action") | String |  |  | Valid Values:<br>- power-off<br>- maintain | PoE action for interface. By default in EOS, reboot action is set to power-off. |
    | [<samp>&nbsp;&nbsp;interface_shutdown</samp>](## "poe.interface_shutdown") | Dictionary |  |  |  | Set the global PoE power behavior for PoE ports when ports are admin down |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "poe.interface_shutdown.action") | String |  |  | Valid Values:<br>- power-off<br>- maintain | PoE action for interface. By default in EOS, interface shutdown action is set to maintain. |

=== "YAML"

    ```yaml
    poe:
      reboot:
        action: <str>
      interface_shutdown:
        action: <str>
    ```
