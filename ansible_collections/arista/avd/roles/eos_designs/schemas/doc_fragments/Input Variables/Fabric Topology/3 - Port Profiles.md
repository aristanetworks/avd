Optional profiles to share common settings for connected_endpoints and/or network_ports.
Keys are the same as used under endpoint adapters. Keys defined under endpoints adapters take precedence.

A port profile can refer to another port profile using `parent_profile` to inherit settings in up to two levels (adapter->profile->parent_profile).
