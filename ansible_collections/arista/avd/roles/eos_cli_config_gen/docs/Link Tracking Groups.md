# Link Tracking Groups

## Link Tracking Groups

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>link_tracking_groups</samp>](## "link_tracking_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "link_tracking_groups.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "link_tracking_groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "link_tracking_groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 |  |

### YAML

```yaml
link_tracking_groups:
  - name: <str>
    links_minimum: <int>
    recovery_delay: <int>
```
