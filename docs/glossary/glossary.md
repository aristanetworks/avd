# Glossary

### Aaa Settings

Arista EOS AAA (Authentication, Authorization, and Accounting) settings provide secure network access control via local user databases, RADIUS, or TACACS+ servers.
Core configuration involves enabling AAA, defining server groups, and applying methods to console or VTY lines. Key commands include aaa authentication, aaa authorization, and aaa accounting

### Mgmt Interface Description

Management interface description.


### Svi Profiles

Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
Keys are the same used under SVIs. Keys defined under SVIs take precedence.
Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
1. svi.nodes[inventory_hostname].structured_config
2. svi_profile.nodes[inventory_hostname].structured_config
3. svi_parent_profile.nodes[inventory_hostname].structured_config
4. svi.structured_config
5. svi_profile.structured_config
6. svi_parent_profile.structured_config


### Update Default Result Permit

Accept the packets when access-list is being updated.
