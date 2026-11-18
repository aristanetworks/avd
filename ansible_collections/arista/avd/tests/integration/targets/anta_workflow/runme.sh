#!/usr/bin/env bash
# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
set -euo pipefail
cd "$(dirname "$0")"

export ANSIBLE_NOCOLOR=1
export ANSIBLE_ACTION_WARNINGS=true
export ANSIBLE_STDOUT_CALLBACK=default

output_file=$(mktemp)
trap 'rm -f "$output_file"' EXIT
ansible-playbook -i localhost, -c local playbook.yml "$@" 2>&1 | tee "$output_file"

# Registered-result assertions live in the playbook. Check the warning only
# when the unreachable-device task is included in the selected test cases.
if grep -Eq '^TASK \[.*Test unreachable device without dry-run\]' "$output_file"; then
    warning="An error occurred while attempting to connect to device anta-leaf1:"
    if ! grep -Fq "$warning" "$output_file"; then
        printf 'Expected an ANTA connection-failure warning: %s\n' "$warning" >&2
        exit 1
    fi
fi
