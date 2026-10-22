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
log_file=$(mktemp)
trap 'rm -f "$output_file" "$log_file"' EXIT
export ANSIBLE_LOG_PATH="$log_file"
ansible-playbook -i localhost, -c local playbook.yml "$@" 2>&1 | tee "$output_file"

# Registered-result assertions live in the playbook. Check live display and Ansible file logging here.
for case in success-summary success-details failure-summary failure-details; do
    for message in "CV_LOGGING_PROBE_pyavd_${case}" "CV_LOGGING_PROBE_urllib3_${case}" "CV_WORKFLOW_WARNING_${case}"; do
        warning="[WARNING]: ${message}"
        count=$(grep -Fc "$warning" "$output_file" || true)
        if [ "$count" -ne 1 ]; then
            printf 'Expected one screen warning, found %s: %s\n' "$count" "$warning" >&2
            exit 1
        fi
    done
done

# ERROR/CRITICAL diagnostics remain visible and reach Ansible's log file without result log saving.
for case in success-summary success-details failure-summary failure-details; do
    for message in "CV_LOGGING_PROBE_ERROR_${case}" "CV_LOGGING_PROBE_CRITICAL_${case}"; do
        for captured_file in "$output_file" "$log_file"; do
            count=$(grep -Fc "$message" "$captured_file" || true)
            if [ "$count" -ne 1 ]; then
                printf 'Expected one captured diagnostic, found %s: %s in %s\n' "$count" "$message" "$captured_file" >&2
                exit 1
            fi
        done
    done
done
