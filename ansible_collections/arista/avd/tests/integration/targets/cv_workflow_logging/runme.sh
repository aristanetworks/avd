#!/usr/bin/env bash
# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
set -euo pipefail
cd "$(dirname "$0")"

export ANSIBLE_ACTION_PLUGINS="${PWD}/action_plugins"
export ANSIBLE_NOCOLOR=1
export ANSIBLE_ACTION_WARNINGS=true
export ANSIBLE_STDOUT_CALLBACK=default

output_file=$(mktemp)
trap 'rm -f "$output_file"' EXIT
ansible-playbook -i localhost, -c local playbook.yml "$@" 2>&1 | tee "$output_file"

# Registered-result assertions live in the playbook. Check screen deduplication here.
for case in success-summary success-details failure-summary failure-details; do
    for source in pyavd urllib3; do
        warning="[WARNING]: CV_LOGGING_PROBE_${source}_${case}"
        count=$(grep -Fc "$warning" "$output_file" || true)
        if [ "$count" -ne 1 ]; then
            printf 'Expected one screen warning, found %s: %s\n' "$count" "$warning" >&2
            exit 1
        fi
    done
done
