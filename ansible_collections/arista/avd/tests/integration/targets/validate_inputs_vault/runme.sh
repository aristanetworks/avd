#!/usr/bin/env bash

set -eux

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Use the correct ansible-playbook from pyenv
ANSIBLE_PLAYBOOK="${ANSIBLE_PLAYBOOK:-ansible-playbook}"

# Set up test tmp directory
TEST_TMP_DIR="/tmp/avd_vault_test_$$"
mkdir -p "$TEST_TMP_DIR"

# Test 1: Without vault - verify files are NOT encrypted
echo "=== Test 1: Without vault password ==="
export AVDTMPDIR="$TEST_TMP_DIR/without_vault"

# Temporarily rename ansible.cfg to disable vault
if [ -f "$SCRIPT_DIR/ansible.cfg" ]; then
    mv "$SCRIPT_DIR/ansible.cfg" "$SCRIPT_DIR/ansible.cfg.bak"
fi

"$ANSIBLE_PLAYBOOK" -i "$SCRIPT_DIR/hosts.yml" "$SCRIPT_DIR/playbook_without_vault.yml"

# Restore ansible.cfg
if [ -f "$SCRIPT_DIR/ansible.cfg.bak" ]; then
    mv "$SCRIPT_DIR/ansible.cfg.bak" "$SCRIPT_DIR/ansible.cfg"
fi

# Note: The plugin appends "/arista_avd" to AVDTMPDIR if it's not already in the path
TEMPLATED_FILE="$TEST_TMP_DIR/without_vault/arista_avd/eos_cli_config_gen/templated/testhost.json"
VALIDATED_FILE="$TEST_TMP_DIR/without_vault/arista_avd/eos_cli_config_gen/validated/testhost.json"

if [ ! -f "$TEMPLATED_FILE" ]; then
    echo "ERROR: Templated file not found: $TEMPLATED_FILE"
    exit 1
fi

if [ ! -f "$VALIDATED_FILE" ]; then
    echo "ERROR: Validated file not found: $VALIDATED_FILE"
    exit 1
fi

# Check that files are plain JSON (start with '{')
if ! head -1 "$TEMPLATED_FILE" | grep -q '^{'; then
    echo "ERROR: Templated file should be plain JSON"
    exit 1
fi

if ! head -1 "$VALIDATED_FILE" | grep -q '^{'; then
    echo "ERROR: Validated file should be plain JSON"
    exit 1
fi

echo "✓ Files are plain JSON (not encrypted)"

# Test 2: With vault - verify files ARE encrypted
echo "=== Test 2: With vault password ==="
export AVDTMPDIR="$TEST_TMP_DIR/with_vault"
"$ANSIBLE_PLAYBOOK" -i "$SCRIPT_DIR/hosts.yml" --vault-password-file="$SCRIPT_DIR/.vault_password" "$SCRIPT_DIR/playbook_with_vault.yml"

# Note: The plugin appends "/arista_avd" to AVDTMPDIR if it's not already in the path
TEMPLATED_FILE="$TEST_TMP_DIR/with_vault/arista_avd/eos_cli_config_gen/templated/testhost.json"
VALIDATED_FILE="$TEST_TMP_DIR/with_vault/arista_avd/eos_cli_config_gen/validated/testhost.json"

if [ ! -f "$TEMPLATED_FILE" ]; then
    echo "ERROR: Templated file not found: $TEMPLATED_FILE"
    exit 1
fi

if [ ! -f "$VALIDATED_FILE" ]; then
    echo "ERROR: Validated file not found: $VALIDATED_FILE"
    exit 1
fi

# Check that files are encrypted (start with '$ANSIBLE_VAULT;')
if ! head -1 "$TEMPLATED_FILE" | grep -q '^\$ANSIBLE_VAULT;'; then
    echo "ERROR: Templated file should be encrypted"
    cat "$TEMPLATED_FILE" | head -5
    exit 1
fi

if ! head -1 "$VALIDATED_FILE" | grep -q '^\$ANSIBLE_VAULT;'; then
    echo "ERROR: Validated file should be encrypted"
    cat "$VALIDATED_FILE" | head -5
    exit 1
fi

echo "✓ Files are encrypted with Ansible Vault"

# Clean up
rm -rf "$TEST_TMP_DIR"

echo ""
echo "=== All tests passed ==="

