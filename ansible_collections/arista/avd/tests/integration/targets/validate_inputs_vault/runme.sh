#!/usr/bin/env bash

set -eux

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ANSIBLE_PLAYBOOK="${ANSIBLE_PLAYBOOK:-ansible-playbook}"
TEST_DIR="${ANSIBLE_COLLECTIONS_PATH}/ansible_collections/arista/avd/tests"


# Create a temporary directory for test outputs
TEST_TMP_DIR="$TEST_DIR/output/avd_vault_test_$$"
mkdir -p "$TEST_TMP_DIR"

# Test 1: Without vault password
echo "=== Test 1: Without vault password ==="
export AVDTMPDIR="$TEST_TMP_DIR/without_vault"
# Temporarily disable vault by renaming ansible.cfg
if [ -f "$SCRIPT_DIR/ansible.cfg" ]; then
    mv "$SCRIPT_DIR/ansible.cfg" "$SCRIPT_DIR/ansible.cfg.bak"
fi
"$ANSIBLE_PLAYBOOK" -i "$SCRIPT_DIR/hosts.yml" "$SCRIPT_DIR/test_without_vault.yml"
# Restore ansible.cfg
if [ -f "$SCRIPT_DIR/ansible.cfg.bak" ]; then
    mv "$SCRIPT_DIR/ansible.cfg.bak" "$SCRIPT_DIR/ansible.cfg"
fi

# Test 2: With vault password
echo ""
echo "=== Test 2: With vault password ==="
export AVDTMPDIR="$TEST_TMP_DIR/with_vault"
export ANSIBLE_CONFIG="$SCRIPT_DIR/ansible.cfg"
"$ANSIBLE_PLAYBOOK" -i "$SCRIPT_DIR/hosts.yml" "$SCRIPT_DIR/test_with_vault.yml"

# Test 3: Multiple vault identities without avd_vault_id
echo ""
echo "=== Test 3: Multiple vault identities (default behavior) ==="
export AVDTMPDIR="$TEST_TMP_DIR/multi_vault"
export ANSIBLE_CONFIG="$SCRIPT_DIR/ansible_multi_vault.cfg"
"$ANSIBLE_PLAYBOOK" -i "$SCRIPT_DIR/hosts.yml" "$SCRIPT_DIR/test_multi_vault_default.yml"

# Test 4: Multiple vault identities with avd_vault_id='prod'
echo ""
echo "=== Test 4: Multiple vault identities with avd_vault_id='prod' ==="
export AVDTMPDIR="$TEST_TMP_DIR/multi_vault_with_id"
export ANSIBLE_CONFIG="$SCRIPT_DIR/ansible_multi_vault.cfg"
"$ANSIBLE_PLAYBOOK" -i "$SCRIPT_DIR/hosts.yml" "$SCRIPT_DIR/test_multi_vault_with_id.yml"

echo ""
echo "=== All tests passed ==="
