#!/usr/bin/env bash
# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
set -eux
cd "$(dirname "$0")"
# The default ansible-test role harness injects output_dir as an extra variable,
# which would mask the role's default and overridden output directory paths.
ansible-playbook -i hosts.yml playbook.yml "$@"
