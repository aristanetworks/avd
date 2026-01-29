# Glossary

## Table of Contents

- [A](#a)

## A

### algorithm

**Type**: String  
**Path**: `fabric_ip_addressing.mlag.algorithm`  
**Default**: `first_id`  
**Valid Values**: `first_id`, `odd_id`, `same_subnet`  

This variable defines the Multi-chassis Link Aggregation (MLAG) algorithm used.
Each MLAG link will have a /31¹ subnet with each subnet allocated from the relevant MLAG pool via a calculated offset.
The offset is calculated using one of the following algorithms:
  - first_id: `(mlag_primary_id - 1) * 2` where `mlag_primary_id` is the ID of the first node defined under the node_group.
    This allocation method will skip every other /31¹ subnet making it less space efficient than `odd_id`.
  - odd_id: `(odd_id - 1) / 2`. Requires the node_group to have a node with an odd ID and a node with an even ID.
  - same_subnet: the offset will always be zero.
    This allocation method will use the first /31¹ subnet from the pool for all MLAG links.
¹ The prefix length is configurable with a default of /31.

---
