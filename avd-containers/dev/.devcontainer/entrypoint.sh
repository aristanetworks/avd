#!/bin/bash

AVD_DEV_REQ_FILE="${HOME}/.ansible/collections/ansible_collections/arista/avd/requirements-dev.txt"
USERNAME=$(whoami)

# install ansible if not yet installed and avd collection is locally mounted
ansible --version &> /dev/null ||  if [ -f $AVD_DEV_REQ_FILE ]; then
  sudo chown -R ${USERNAME} ${HOME}/.ansible
  ANSIBLE_CORE_VERSION=$(cat ${AVD_DEV_REQ_FILE}| grep ansible-core)
  pip3 install "${ANSIBLE_CORE_VERSION}"
  ansible-galaxy collection install -r ${HOME}/.ansible/collections/ansible_collections/arista/avd/collections.yml
  pip3 install -r ${HOME}/.ansible/collections/ansible_collections/arista/avd/requirements.txt
  pip3 install -r ${HOME}/.ansible/collections/ansible_collections/arista/avd/requirements-dev.txt
fi

# install ansible from any AVD git branch (or it's fork)
# the ANSIBLE_INSTALL_LOCATION_FORMAT must be "git+https://github.com/${AVD_GITHUB_REPO}.git#/ansible_collections/arista/avd/,${AVD_BRANCH_NAME}"
# AVD_GITHUB_REPO and AVD_BRANCH_NAME must be defined for ANSIBLE_INSTALL_LOCATION_FORMAT to be crafted successfully
ansible --version &> /dev/null ||  if ! [ -z "${AVD_GITHUB_REPO}" ] && ! [ -z "${AVD_BRANCH_NAME}" ]; then
  ANSIBLE_CORE_VERSION=$(curl -s https://raw.githubusercontent.com/${AVD_GITHUB_REPO}/${AVD_BRANCH_NAME}/ansible_collections/arista/avd/requirements-dev.txt | grep ansible-core)
  pip3 install "${ANSIBLE_CORE_VERSION}"
  ansible-galaxy collection install git+https://github.com/${AVD_GITHUB_REPO}.git#/ansible_collections/arista/avd/,${AVD_BRANCH_NAME}
  pip3 install -r ${HOME}/.ansible/collections/ansible_collections/arista/avd/requirements.txt
  pip3 install -r ${HOME}/.ansible/collections/ansible_collections/arista/avd/requirements-dev.txt
fi

ansible --version &> /dev/null ||  (echo "ERROR: Failed to install Ansible and collections." >&2; exit 1)

# execute command from docker cli if any
if [ ${@+True} ]; then
  exec "$@"
# otherwise just enter sh or zsh
else
  if [ -f "/bin/zsh" ]; then
    exec zsh
  else
    exec sh
  fi
fi