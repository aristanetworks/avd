!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## Default Node Types

### Description

Uses hostname matches against a regular expression to determine the node type.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>default_node_types</samp>](## "default_node_types") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- match_hostnames</samp>](## "default_node_types.[].match_hostnames") | List, items: String | Required |  |  | Regular expressions to match against hostnames |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_node_types.[].match_hostnames.[].&lt;str&gt;") | String | Required |  |  | Regex needs to match full hostname (i.e. is bounded by ^ and $ elements) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_type</samp>](## "default_node_types.[].node_type") | String | Required, Unique |  |  | Resulting node type when regex matches |

### YAML

```yaml
default_node_types:
  - match_hostnames:
      - <str>
    node_type: <str>
```
