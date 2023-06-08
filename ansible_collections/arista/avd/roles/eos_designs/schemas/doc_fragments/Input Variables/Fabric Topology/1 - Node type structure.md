All node types have the same structure based on `defaults`, `node_group`, `node` and all variables can be defined in any section and support inheritance like this:

Under `node_type_keys.key:`

```bash
defaults <- node_group <- node_group.node <- node
```

### Node Type Structure

```yaml
---
<node_type_keys.key>:
  defaults:
    # Define vars for all nodes of this type
  node_groups:
    - group: <node group name>
    # Vars related to all nodes part of this group
      nodes:
        - name: <node inventory hostname>
          # Vars defined per node
  nodes:
    - name: <node inventory hostname>
      # Vars defined per node
```
