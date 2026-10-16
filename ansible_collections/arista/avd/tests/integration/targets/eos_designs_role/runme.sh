#!/usr/bin/env bash
# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
set -euxo pipefail
cd "$(dirname "$0")"
# Exercise installed PyAVD, including when running with lowest direct dependencies.
export AVD_NEVER_RUN_FROM_SOURCE=1
# ansible-test isolates its collection path; retain access to the cached role dependencies.
export ANSIBLE_COLLECTIONS_PATH="${ANSIBLE_COLLECTIONS_PATH:-}:$HOME/.ansible/collections"
output_dir=$(mktemp -d)
trap 'rm -rf "$output_dir"' EXIT
ansible-playbook -i hosts.yml playbook.yml -e "root_dir=$output_dir" "$@"
# Every task in both roles must be idempotent on the second invocation.
ansible-playbook -i hosts.yml playbook.yml -e "root_dir=$output_dir" -e '{"expect_changed": false}' "$@" | tee "$output_dir/second-run.log"
if grep -E 'changed=[1-9][0-9]*' "$output_dir/second-run.log"; then
    exit 1
fi
