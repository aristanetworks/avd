#!/usr/bin/env bash
# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
set -eux
cd "$(dirname "$0")"
# Disable source-checkout detection so schema_tools (and its 'referencing' dep) are not imported.
# This test targets requirement validation, not schema recompilation.
export AVD_NEVER_RUN_FROM_SOURCE=1
ansible-playbook -i hosts.yml playbook.yml "$@"
