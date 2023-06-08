# CloudVision Portal Tags

## Table of Contents

- [CVP Tags for dc1-super-spine1](#cvp-tags-for-dc1-super-spine1)
- [CVP Tags for dc1-super-spine2](#cvp-tags-for-dc1-super-spine2)
- [CVP Tags for dc1-pod1-spine1](#cvp-tags-for-dc1-pod1-spine1)
- [CVP Tags for dc1-pod1-spine2](#cvp-tags-for-dc1-pod1-spine2)
- [CVP Tags for dc1-pod1-leaf1a](#cvp-tags-for-dc1-pod1-leaf1a)
- [CVP Tags for dc1-pod1-leaf1b](#cvp-tags-for-dc1-pod1-leaf1b)
- [CVP Tags for dc1-pod1-leaf2a](#cvp-tags-for-dc1-pod1-leaf2a)
- [CVP Tags for dc1-pod1-leaf2b](#cvp-tags-for-dc1-pod1-leaf2b)
- [CVP Tags for dc1-pod1-leaf1c](#cvp-tags-for-dc1-pod1-leaf1c)
- [CVP Tags for dc1-pod1-leaf2c](#cvp-tags-for-dc1-pod1-leaf2c)
- [CVP Tags for dc1-pod2-spine1](#cvp-tags-for-dc1-pod2-spine1)
- [CVP Tags for dc1-pod2-spine2](#cvp-tags-for-dc1-pod2-spine2)
- [CVP Tags for dc1-pod2-leaf1a](#cvp-tags-for-dc1-pod2-leaf1a)
- [CVP Tags for dc1-pod2-leaf1b](#cvp-tags-for-dc1-pod2-leaf1b)

## CVP Tags for dc1-super-spine1

### dc1-super-spine1 Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | core |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | superspines |
| topology_hint_datacenter | DC1 |

## CVP Tags for dc1-super-spine2

### dc1-super-spine2 Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | core |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | superspines |
| topology_hint_datacenter | DC1 |

## CVP Tags for dc1-pod1-spine1

### dc1-pod1-spine1 Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | spine |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod1 |
| topology_hint_datacenter | DC1 |

### dc1-pod1-spine1 Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-leaf1a |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet1 |
| Ethernet1 | peer_int | Ethernet1 |
| Ethernet1 | interface_peer | dc1-pod2-leaf1a |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet1 |
| Ethernet1 | peer_int | Ethernet1 |
| Ethernet2 | interface_peer | dc1-pod1-leaf1b |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet1 |
| Ethernet2 | peer_int | Ethernet1 |
| Ethernet2 | interface_peer | dc1-pod2-leaf1b |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet1 |
| Ethernet2 | peer_int | Ethernet1 |
| Ethernet3 | interface_peer | dc1-pod1-leaf2a |
| Ethernet3 | interface_desc | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet1 |
| Ethernet3 | peer_int | Ethernet1 |
| Ethernet4 | interface_peer | dc1-pod1-leaf2b |
| Ethernet4 | interface_desc | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet1 |
| Ethernet4 | peer_int | Ethernet1 |

## CVP Tags for dc1-pod1-spine2

### dc1-pod1-spine2 Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | spine |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod1 |
| topology_hint_datacenter | DC1 |

### dc1-pod1-spine2 Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-leaf1a |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet2 |
| Ethernet1 | peer_int | Ethernet2 |
| Ethernet1 | interface_peer | dc1-pod2-leaf1a |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet2 |
| Ethernet1 | peer_int | Ethernet2 |
| Ethernet2 | interface_peer | dc1-pod1-leaf1b |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet2 |
| Ethernet2 | peer_int | Ethernet2 |
| Ethernet2 | interface_peer | dc1-pod2-leaf1b |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet2 |
| Ethernet2 | peer_int | Ethernet2 |
| Ethernet3 | interface_peer | dc1-pod1-leaf2a |
| Ethernet3 | interface_desc | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet2 |
| Ethernet3 | peer_int | Ethernet2 |
| Ethernet4 | interface_peer | dc1-pod1-leaf2b |
| Ethernet4 | interface_desc | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet2 |
| Ethernet4 | peer_int | Ethernet2 |

## CVP Tags for dc1-pod1-leaf1a

### dc1-pod1-leaf1a Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | leaf |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod1 |
| topology_hint_datacenter | DC1 |
| custom_tag | custom_value |

### dc1-pod1-leaf1a Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-spine1 |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet1 |
| Ethernet1 | peer_int | Ethernet1 |
| Ethernet2 | interface_peer | dc1-pod1-spine2 |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet1 |
| Ethernet2 | peer_int | Ethernet1 |
| Ethernet8 | interface_peer | dc1-pod1-leaf1c |
| Ethernet8 | interface_desc | DC1-POD1-LEAF1C_Ethernet1 |
| Ethernet8 | peer_int | Ethernet1 |

## CVP Tags for dc1-pod1-leaf1b

### dc1-pod1-leaf1b Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | leaf |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod1 |
| topology_hint_datacenter | DC1 |

### dc1-pod1-leaf1b Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-spine1 |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet2 |
| Ethernet1 | peer_int | Ethernet2 |
| Ethernet2 | interface_peer | dc1-pod1-spine2 |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet2 |
| Ethernet2 | peer_int | Ethernet2 |

## CVP Tags for dc1-pod1-leaf2a

### dc1-pod1-leaf2a Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | leaf |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod1 |
| topology_hint_datacenter | DC1 |

### dc1-pod1-leaf2a Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-spine1 |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet3 |
| Ethernet1 | peer_int | Ethernet3 |
| Ethernet2 | interface_peer | dc1-pod1-spine2 |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet3 |
| Ethernet2 | peer_int | Ethernet3 |
| Ethernet8 | interface_peer | dc1-pod1-leaf2c |
| Ethernet8 | interface_desc | DC1-POD1-LEAF2C_Ethernet1 |
| Ethernet8 | peer_int | Ethernet1 |

## CVP Tags for dc1-pod1-leaf2b

### dc1-pod1-leaf2b Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | leaf |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod1 |
| topology_hint_datacenter | DC1 |

### dc1-pod1-leaf2b Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-spine1 |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet4 |
| Ethernet1 | peer_int | Ethernet4 |
| Ethernet2 | interface_peer | dc1-pod1-spine2 |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet4 |
| Ethernet2 | peer_int | Ethernet4 |

## CVP Tags for dc1-pod1-leaf1c

### dc1-pod1-leaf1c Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | leaf |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod1 |
| topology_hint_rack | rack-1c |
| topology_hint_datacenter | DC1 |
| custom_tag | custom_value |

### dc1-pod1-leaf1c Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-leaf1a |
| Ethernet1 | interface_desc | DC1-POD1-LEAF1A_Ethernet8 |
| Ethernet1 | peer_int | Ethernet8 |

## CVP Tags for dc1-pod1-leaf2c

### dc1-pod1-leaf2c Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | edge |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod1 |
| topology_hint_rack | rack-2c |
| topology_hint_datacenter | DC1 |

### dc1-pod1-leaf2c Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-leaf2a |
| Ethernet1 | interface_desc | DC1-POD1-LEAF2A_Ethernet8 |
| Ethernet1 | peer_int | Ethernet8 |

## CVP Tags for dc1-pod2-spine1

### dc1-pod2-spine1 Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | spine |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod2 |
| topology_hint_datacenter | DC1 |

## CVP Tags for dc1-pod2-spine2

### dc1-pod2-spine2 Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | spine |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod2 |
| topology_hint_datacenter | DC1 |

## CVP Tags for dc1-pod2-leaf1a

### dc1-pod2-leaf1a Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | leaf |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod2 |
| topology_hint_datacenter | DC1 |
| custom_tag | custom_value |

### dc1-pod2-leaf1a Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-spine1 |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet1 |
| Ethernet1 | peer_int | Ethernet1 |
| Ethernet2 | interface_peer | dc1-pod1-spine2 |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet1 |
| Ethernet2 | peer_int | Ethernet1 |

## CVP Tags for dc1-pod2-leaf1b

### dc1-pod2-leaf1b Device Tags

| Tag Name | Tag Value |
| -------- | --------- |
| topology_hint_type | leaf |
| topology_hint_fabric | FABRIC |
| topology_hint_pod | pod2 |
| topology_hint_datacenter | DC1 |

### dc1-pod2-leaf1b Interface Tags

| Interface | Tag Name | Tag Value |
| --------- |-------- | --------- |
| Ethernet1 | interface_peer | dc1-pod1-spine1 |
| Ethernet1 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet2 |
| Ethernet1 | peer_int | Ethernet2 |
| Ethernet2 | interface_peer | dc1-pod1-spine2 |
| Ethernet2 | interface_desc | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet2 |
| Ethernet2 | peer_int | Ethernet2 |
