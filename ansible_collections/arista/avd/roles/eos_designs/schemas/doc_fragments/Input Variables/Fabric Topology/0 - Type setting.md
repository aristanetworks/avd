- The `type:` variable needs to be defined for each device in the fabric.
- This is leveraged to load the appropriate template to generate the configuration.

### Variables and Options

As explained above, you can defined your own types of devices. CLI only provides default node types.

```yaml
# define the layer type
type: < spine | l3leaf | l2leaf | super-spine | overlay-controller >
```

#### Example

```yaml
# Defined in SPINE.yml file
# Can also be set directly in your inventory file under spine group
type: spine

# Defined in L3LEAFS.yml
# Can also be set directly in your inventory file under l3leaf group
type: l3leaf

# Defined in L2LEAFS.yml
# Can also be set directly in your inventory file under l2leaf group
type: l2leaf

# Defined in SUPER-SPINES.yml
# Can also be set directly in your inventory file under super-spine group
type: super-spine

# Defined in ROUTE-SERVERS.yml
# Can also be set directly in your inventory file under route-server group
type: overlay-controller
```
