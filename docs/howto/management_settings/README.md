<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Management Settings

## Introduction

**Management settings** define how network devices are accessed and managed out-of-band. AVD configures a dedicated management VRF, interface, DNS, NTP, and local user accounts consistently across every device in the fabric from a single set of variables.

This guide explains how to define management settings and demonstrates the resulting device configuration.

### When to Use Management Settings

- Configuring out-of-band management access for all fabric devices
- Standardising NTP and DNS across the fabric
- Defining local user accounts for emergency access
- Setting management gateway and routing

## Concepts

**Management VRF**: A dedicated VRF (typically named `MGMT`) that isolates management traffic from production traffic. All management protocols (NTP, DNS, SSH) source from this VRF.

**mgmt_interface**: The physical interface connected to the out-of-band management network (typically `Management1`).

**mgmt_gateway**: The default gateway for the management VRF, used to reach NTP servers, DNS resolvers, and management systems.

**dns_settings**: Configures DNS name servers used by all devices in the fabric.

**ntp_settings**: Configures NTP servers and the VRF from which NTP traffic is sourced. Using `server_vrf: use_mgmt_interface_vrf` automatically sources NTP from whatever VRF `mgmt_interface_vrf` is set to.

**aaa_settings**: Configures local user accounts. These provide emergency access when AAA servers are unreachable.

## Fabric-wide Management Configuration

Management settings are defined at the fabric level so they apply to every device uniformly. The example below shows a complete management configuration:

```yaml title="group_vars/FABRIC/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTMS/fabric.yml
--8<--
```

1. `fabric_name` must match the top-level inventory group that covers all fabric devices.
2. The management interface name — `Management1` on most EOS platforms.
3. The VRF for management traffic — separates out-of-band traffic from the production network.
4. Default gateway for the management VRF. Set this to the management network gateway.
5. DNS servers applied to all devices, sourced from the management VRF.
6. NTP server list. All devices sync to these servers.
7. `use_mgmt_interface_vrf` automatically uses the VRF defined by `mgmt_interface_vrf` — no need to hardcode the VRF name in two places.
8. Local user accounts for emergency access. Always define at least one user with a strong, known password.

### Generated Configuration

AVD generates a consistent management VRF and interface configuration on every fabric device:

```cli title="Management VRF and interface on htms-spine1"
--8<--
docs/howto/management_settings/artifacts/htms-spine1-mgmt.cfg
--8<--
```

AVD also generates the DNS, NTP, management routing, and user configuration as global commands on each device:

```cli title="Global management commands on htms-spine1"
hostname htms-spine1
ip domain lookup vrf MGMT source-interface Management1
ip name-server vrf MGMT 8.8.8.8
ip name-server vrf MGMT 192.168.1.1
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 0.pool.ntp.org prefer
!
ip route vrf MGMT 0.0.0.0/0 172.16.4.1
```

## Per-node Management IP

Each node defines its own management IP address within the node definition. These are set in the spine and leaf group_vars:

```yaml title="group_vars/SPINES/spines.yml (excerpt)"
spine:
  nodes:
    - name: htms-spine1
      id: 1
      mgmt_ip: 172.16.4.11/24
    - name: htms-spine2
      id: 2
      mgmt_ip: 172.16.4.12/24
```

```yaml title="group_vars/L3_LEAFS/l3_leafs.yml (excerpt)"
l3leaf:
  node_groups:
    - group: HTMS_LEAF1
      nodes:
        - name: htms-leaf1a
          id: 1
          mgmt_ip: 172.16.4.101/24
        - name: htms-leaf1b
          id: 2
          mgmt_ip: 172.16.4.102/24
```

## Best Practices

1. **Define management settings at the fabric group level**: All management variables (`mgmt_interface`, `mgmt_interface_vrf`, `dns_settings`, `ntp_settings`) should go in the group that covers all fabric devices. Avoid setting them per-node or per-subgroup.

2. **Use `use_mgmt_interface_vrf` for NTP**: This keeps the NTP VRF in sync with `mgmt_interface_vrf` automatically — changing the VRF name in one place updates NTP as well.

3. **Always define a local fallback user**: In production, primary authentication may rely on AAA servers. A local user with emergency access prevents lockouts if those servers become unreachable.

4. **Define `mgmt_ip` for each node**: Every device requires a unique management IP. Set `mgmt_ip` in the node definition inside your group_vars.

5. **Keep the management VRF name consistent**: Use the same VRF name (`MGMT`) across all management-related variables. AVD uses `mgmt_interface_vrf` to automatically set the VRF on the management interface, DNS lookups, and NTP source.

## Troubleshooting

### Device not reachable after provisioning

**Issue**: The device is unreachable on its management IP after the configuration is applied.

**Solution**:

- Verify `mgmt_ip` is set correctly for the node in the group_vars.
- Confirm `mgmt_gateway` is reachable from the management network.
- Check that `ip route vrf MGMT 0.0.0.0/0 {mgmt_gateway}` is present in the generated config.

### NTP not synchronising

**Issue**: Devices show unsynchronised NTP status.

**Solution**:

- Verify the NTP server names/IPs are reachable from the management VRF.
- Confirm `ntp_settings.server_vrf` is set to `use_mgmt_interface_vrf` or the correct VRF name.
- Check that `ntp local-interface vrf MGMT Management1` appears in the generated config.

### DNS resolution failing on device

**Issue**: Hostname resolution fails on the device.

**Solution**:

- Verify `dns_settings.servers` contains valid, reachable DNS server IPs.
- Confirm `ip domain lookup vrf MGMT source-interface Management1` is in the generated config.
- Check that the DNS servers are accessible from the management VRF.

## Reference

For complete details on all available properties, see:

- [Management Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#management-settings)
- [Node Management Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-management-configuration)
