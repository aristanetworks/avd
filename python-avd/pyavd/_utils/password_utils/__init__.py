# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from .password import (
    bgp_decrypt,
    bgp_encrypt,
    isis_decrypt,
    isis_encrypt,
    ntp_decrypt,
    ntp_encrypt,
    ospf_message_digest_decrypt,
    ospf_message_digest_encrypt,
    ospf_simple_decrypt,
    ospf_simple_encrypt,
    radius_decrypt,
    radius_encrypt,
    tacacs_decrypt,
    tacacs_encrypt,
)

##############
# GENERIC
##############
METHODS_DIR = {
    "bgp": (bgp_encrypt, bgp_decrypt),
    "isis": (isis_encrypt, isis_decrypt),
    "ospf_message_digest": (ospf_message_digest_encrypt, ospf_message_digest_decrypt),
    "ospf_simple": (ospf_simple_encrypt, ospf_simple_decrypt),
    "ntp": (ntp_encrypt, ntp_decrypt),
    "tacacs": (tacacs_encrypt, tacacs_decrypt),
    "radius": (radius_encrypt, radius_decrypt),
}
