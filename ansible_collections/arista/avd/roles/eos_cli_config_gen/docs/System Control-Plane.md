# System Control-Plane

## System

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>system</samp>](## "system") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;control_plane</samp>](## "system.control_plane") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss</samp>](## "system.control_plane.tcp_mss") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "system.control_plane.tcp_mss.ipv4") | Integer |  |  |  | Segment size |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "system.control_plane.tcp_mss.ipv6") | Integer |  |  |  | Segment size |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_access_groups</samp>](## "system.control_plane.ipv4_access_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- acl_name</samp>](## "system.control_plane.ipv4_access_groups.[].acl_name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "system.control_plane.ipv4_access_groups.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_groups</samp>](## "system.control_plane.ipv6_access_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- acl_name</samp>](## "system.control_plane.ipv6_access_groups.[].acl_name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "system.control_plane.ipv6_access_groups.[].vrf") | String |  |  |  |  |

### YAML

```yaml
system:
  control_plane:
    tcp_mss:
      ipv4: <int>
      ipv6: <int>
    ipv4_access_groups:
      - acl_name: <str>
        vrf: <str>
    ipv6_access_groups:
      - acl_name: <str>
        vrf: <str>
```

## VMTracer Sessions

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vmtracer_sessions</samp>](## "vmtracer_sessions") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "vmtracer_sessions.[].name") | String | Required, Unique |  |  | Vmtracer Session Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "vmtracer_sessions.[].url") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "vmtracer_sessions.[].username") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "vmtracer_sessions.[].password") | String |  |  |  | Type 7 Password Hash |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;autovlan_disable</samp>](## "vmtracer_sessions.[].autovlan_disable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "vmtracer_sessions.[].source_interface") | String |  |  |  |  |

### YAML

```yaml
vmtracer_sessions:
  - name: <str>
    url: <str>
    username: <str>
    password: <str>
    autovlan_disable: <bool>
    source_interface: <str>
```
