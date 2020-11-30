## Configure management network

Because we want to be generic, let's configure a DHCP server on NAT gateway to provide fixed DHCP address to your devices. Thus you will be able to get access to them easily. To support that, we can leverage `arista.cvp.dhcp_configuration` to install and configure a DHCP server.

This role requires a set of information related to your own setup:

For your out of band management network:

- Subnet your are using to allocate your devices IP
- Name server to send to your DHCP client
- Default scope for unknown devices.

For every devices:

- EOS device hostname you want to configure.
- Mac address to use to identify request from your device.
- IP address to allocate.
- An optional URI for ZTP registration.

### Create an inventory file

Inventory contains information related to your nat-gateway:

```yaml
# inventory.yml
---
all:
  children:
    DCHP:
      hosts:
        nat_gateway:
          ansible_host: < YOUR RUNNER NETWORK>
          ansible_user: < USERNAME >
          ansible_password: < PASSWORD >
```

### Create host variables

Host variables for your NAT-GATEWAY should be defined like this:

```yaml
---
ztp:
  default:
    registration: '< Optional ZTP registration URL >'
    gateway: < OOB DEFAULT GATEWAY >
    nameservers:
      - < DNS >
  general:
    subnets:
      - network: < OOB SUBNET >
        netmask: < OOB NETMASK >
        gateway: < OOB DEFAULT GATEWAY >
        nameservers:
          - < DNS >
        start: < FIRST LEASE IP >
        end: < LAST LEASE IP >
        lease_time: 300
  clients:
  # AVD/CVP Integration
    - name: DC1-SPINE1
      mac: 0c:1d:c0:1d:62:01
      ip4: 10.73.1.11
    - name: DC1-SPINE2
      mac: 0c:1d:c0:1d:62:02
      ip4: 10.73.1.12
```

### Playbook to configure DHCP

Playbok is fairly simple:

```yaml
---
- name: Configure DHCP Service for ZTP
  hosts: DHCP
  gather_facts: true
  tasks:
    - name: 'Execute DHCP configuration role'
      import_role:
        name: arista.cvp.dhcp_configuration
```
