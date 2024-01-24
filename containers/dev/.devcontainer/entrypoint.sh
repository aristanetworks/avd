#!/bin/bash

USERNAME=$(whoami)
AVD_COLLECTION_PATH="${HOME}/.ansible/collections/ansible_collections/arista/avd"
CONTAINER_WORKSPACE=$(git rev-parse --show-toplevel)
CONTAINER_WSF_AVD_PATH=${CONTAINER_WORKSPACE}/ansible_collections/arista/avd

# if env variables are set - install collection from git
if ! [ -z "${AVD_GITHUB_REPO}" ] && ! [ -z "${AVD_BRANCH_NAME}" ]; then
  ANSIBLE_CORE_VERSION=$(curl -s https://raw.githubusercontent.com/${AVD_GITHUB_REPO}/${AVD_BRANCH_NAME}/ansible_collections/arista/avd/requirements-dev.txt | grep ansible-core)
  AVD_INSTALL_PATH="git+https://github.com/${AVD_GITHUB_REPO}.git#/ansible_collections/arista/avd/,${AVD_BRANCH_NAME}"
# install collection from the workspace if no env variables defined
else [ -f ${CONTAINER_WSF_AVD_PATH}/requirements.txt ] && [ -f ${CONTAINER_WSF_AVD_PATH}/requirements-dev.txt ] ; then
  ANSIBLE_CORE_VERSION=$(cat ${CONTAINER_WSF_AVD_PATH}/requirements-dev.txt | grep ansible-core)
  AVD_INSTALL_PATH="${CONTAINER_WSF_AVD_PATH}/"
fi

# install ansible core and requirements
if ! [ -z "${ANSIBLE_CORE_VERSION}" ]; then
  pip3 install "${ANSIBLE_CORE_VERSION}"
  ansible-galaxy collection install --force ${AVD_INSTALL_PATH}
  pip3 install -r ${AVD_COLLECTION_PATH}/requirements.txt -r ${AVD_COLLECTION_PATH}/requirements-dev.txt
fi

# if ansible installation failed for whatever reason - raise an error
ansible --version &> /dev/null ||  (echo "ERROR: Failed to install Ansible and collections." >&2; exit 1)

# Execute command from docker cli if any.
if [ ${@+True} ]; then
  exec "$@"
# Otherwise just enter sh or zsh.
else
  if [ -f "/bin/zsh" ]; then
    exec zsh
  else
    exec sh
  fi
fi
