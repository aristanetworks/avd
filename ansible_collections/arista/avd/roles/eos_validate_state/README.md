## Overview

This role is used to validate operational states on EOS devices.  

It consumes the same input as the role [eos_cli_config_gen](ansible_collections/arista/avd/roles/eos_cli_config_gen). This input is source of truth (the desired state).  

It connects to EOS devices to collects operational states (actual state). So this role requires an access to the configured devices.   
  
It compares the actual states against the desired state.   

This is the current list of features:  

- Display devices model and EOS release
- Validate environment (fan status) 
- Validate environment (power supplies status) 
- Validate environment (temperature) 
- Validate transceivers manufacturer
- Validate last reload cause
- Validate NTP status
- Validate interfaces admin status
- Validate interfaces op status
- Validate LLDP topology 
- Validate MLAG status
- Validate IP reachability (on directly connected interfaces)
- Validate ArBGP is configured and operating
- Validate BGP sessions state


## Playbook example 

```
---
- name: validate states on EOS devices
  hosts: DC1
  connection: httpapi
  gather_facts: false
  collections:
    - arista.avd

  tasks:

    - name: validate states on EOS devices
      import_role:
         name: arista.avd.eos_validate_state
```
## Input example: 

### inventory/inventory.ini 
```
---
all:
  children:
    DC1:
      children:
        DC1_FABRIC:
          children:
            DC1_SPINES:
              hosts:
                switch2:
                  ansible_host: 10.83.28.190
            DC1_L3LEAFS:
              children:
                DC1_LEAF1:
                  hosts:
                    switch1:
                      ansible_host: 10.83.28.216
                DC1_LEAF2:
                  hosts:
                    switch3:
                      ansible_host: 10.83.28.191
```

### inventory/group_vars/DC1.yml 
```
ansible_user: 'arista'
ansible_password: 'arista'
ansible_network_os: eos
ansible_become: yes
ansible_become_method: enable

validation_mode_loose: true
```

### inventory/intended/structured_configs/switch1.yml
```
router_bgp:
  neighbors:
    10.10.10.1:
      remote_as: 65002
    10.10.10.3:
      remote_as: 65003
  
ethernet_interfaces:
  Ethernet2:
    peer: switch3
    peer_interface: Ethernet4
    ip_address: 10.10.10.2/31
    type: routed
  Ethernet5:
    peer: switch2
    peer_interface: Ethernet5
    ip_address: 10.10.10.0/31
    type: routed
 
mlag_configuration:
  domain_id: MLAG12
  local_interface: Vlan4094
  peer_address: 172.16.12.1
  peer_link: Port-Channel10
  reload_delay_mlag: 300
  reload_delay_non_mlag: 330

ntp_server:
  local_interface:
    vrf: MGMT
    interface: Management1
  nodes:
    - 0.fr.pool.ntp.org
    - 1.fr.pool.ntp.org

dns_domain: lab.local
```

## Usage example

```
ansible-playbook playbooks/pb_validate_yml --skip-tags "hardware, optional" --inventory inventory/inventory.yml
```

## License

Project is published under [Apache 2.0 License](../../LICENSE)