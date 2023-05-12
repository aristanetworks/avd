#!/usr/bin/env bash

set -eux

# Testing with ansible.cfg
export ANSIBLE_CONFIG=./ansible.cfg
ansible-playbook -i hosts.yml playbook.yml
unset ANSIBLE_CONFIG

# Testing with env variable
export ANSIBLE_VARS_ENABLED=arista.avd.global_vars,host_group_vars
export ARISTA_AVD_GLOBAL_VARS_PATHS=./global_vars.yml,./zz_global_vars
ansible-playbook -i hosts.yml playbook.yml
