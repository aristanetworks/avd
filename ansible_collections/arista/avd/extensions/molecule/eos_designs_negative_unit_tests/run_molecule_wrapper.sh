#!/usr/bin/env bash
# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

# TEMPORARY WORKAROUND for https://github.com/ansible/ansible/issues/83292
# Ansible 2.17+ returns exit code 2 when failures are rescued.
# This wrapper analyzes PLAY RECAP to return exit 0 when all failures were rescued.

set -o pipefail

TEMP_OUTPUT=$(mktemp)
trap 'rm -f "$TEMP_OUTPUT"' EXIT  # Cleanup temp file on script exit

molecule "$@" 2>&1 | tee "$TEMP_OUTPUT"
MOLECULE_EXIT_CODE=${PIPESTATUS[0]}

if [ "$MOLECULE_EXIT_CODE" -eq 0 ]; then
    exit 0
fi

if [ "$MOLECULE_EXIT_CODE" -ne 2 ]; then
    exit "$MOLECULE_EXIT_CODE"
fi

# Exit code 2 - analyze PLAY RECAP to check if all failures were rescued
PLAY_RECAP=$(sed -n '/^PLAY RECAP/,$p' "$TEMP_OUTPUT")

if [ -z "$PLAY_RECAP" ]; then
    exit "$MOLECULE_EXIT_CODE"
fi

REAL_FAILURES=0

while IFS= read -r line; do
    if [[ "$line" =~ ^PLAY\ RECAP ]] || [[ -z "$line" ]]; then
        continue
    fi

    if [[ "$line" =~ failed=([0-9]+) ]]; then
        FAILED="${BASH_REMATCH[1]}"
    else
        FAILED=0
    fi

    if [[ "$line" =~ rescued=([0-9]+) ]]; then
        RESCUED="${BASH_REMATCH[1]}"
    else
        RESCUED=0
    fi

    if [ "$FAILED" -gt 0 ] && [ "$RESCUED" -eq 0 ]; then
        REAL_FAILURES=$((REAL_FAILURES + 1))
    fi
done <<< "$PLAY_RECAP"

if [ $REAL_FAILURES -gt 0 ]; then
    echo "Found $REAL_FAILURES host(s) with unrescued failures. Returning exit code 2."
    exit 2
fi

echo "All failures were successfully rescued. Treating as success (exit code 0)."
echo "Note: This is a workaround for https://github.com/ansible/ansible/issues/83292"
exit 0

