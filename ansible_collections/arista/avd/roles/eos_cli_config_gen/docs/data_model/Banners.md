---
search:
  boost: 2
---

# Banners

## Banners

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>banners</samp>](## "banners") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;login</samp>](## "banners.login") | String |  |  |  | Multiline string ending with EOF on the last line |
    | [<samp>&nbsp;&nbsp;motd</samp>](## "banners.motd") | String |  |  |  | Multiline string ending with EOF on the last line |

=== "YAML"

    ```yaml
    banners:
      login: <str>
      motd: <str>
    ```
