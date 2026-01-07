# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible.release import __version__ as ansible_version

ANSIBLE_ABOVE_2_19 = ansible_version.startswith(("2.2", "2.19"))
"""Bool to signal if we are running on Ansible 2.19 or above."""
# TODO: Remove this once we no longer support <2.19. Note it does not cover version 2.3x so hopefully we will cut the old stuff before then :)
