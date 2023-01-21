---
search:
  boost: 2
---

# Banners
## Banners

=== "Banners"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>banners</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;login</samp> | String |  |  |  | Multiline string ending with EOF on the last line |
    | <samp>&nbsp;&nbsp;motd</samp> | String |  |  |  | Multiline string ending with EOF on the last line |

=== "YAML"

    ```yaml
    banners:
      login: <str>
      motd: <str>
    ```
