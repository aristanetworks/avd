#!/bin/bash

USERNAME=$(whoami)
AVD_COLLECTION_PATH="${HOME}/.ansible/collections/ansible_collections/arista/avd"
CONTAINER_WORKSPACE=$(git rev-parse --show-toplevel)
CONTAINER_WSF_AVD_PATH=${CONTAINER_WORKSPACE}/ansible_collections/arista/avd

# if collection is already mounted, it will be used to install the requirements
# there is no need to install AVD collection for this case as it's already mounted to the correct location
if [ -f ${AVD_COLLECTION_PATH}/requirements.txt ] && [ -f ${AVD_COLLECTION_PATH}/requirements-dev.txt ] ; then
  sudo chown -R ${USERNAME} ${HOME}/.ansible  # make sure mounted path is owned by container user and not root
  ANSIBLE_CORE_VERSION=$(cat ${AVD_COLLECTION_PATH}/requirements-dev.txt | grep ansible-core)
# if env variables are set - use git
elif ! [ -z "${AVD_GITHUB_REPO}" ] && ! [ -z "${AVD_BRANCH_NAME}" ]; then
  ANSIBLE_CORE_VERSION=$(curl -s https://raw.githubusercontent.com/${AVD_GITHUB_REPO}/${AVD_BRANCH_NAME}/ansible_collections/arista/avd/requirements-dev.txt | grep ansible-core)
  AVD_INSTALL_PATH="git+https://github.com/${AVD_GITHUB_REPO}.git#/ansible_collections/arista/avd/,${AVD_BRANCH_NAME}"
# In some cases AVD can not be correctly mounted, for ex. when running dev container as Codespace
# In that case if collection is available in the container workspace, it will be installed from there
elif [ -f ${CONTAINER_WSF_AVD_PATH}/requirements.txt ] && [ -f ${CONTAINER_WSF_AVD_PATH}/requirements-dev.txt ] ; then
  ANSIBLE_CORE_VERSION=$(cat ${CONTAINER_WSF_AVD_PATH}/requirements-dev.txt | grep ansible-core)
  AVD_INSTALL_PATH="${CONTAINER_WSF_AVD_PATH}/"
fi

# install ansible core and requirements
if ! [ -z "${ANSIBLE_CORE_VERSION}" ]; then
  pip3 install "${ANSIBLE_CORE_VERSION}"
  if ! [ -z "${AVD_INSTALL_PATH}" ]; then
    ansible-galaxy collection install ${AVD_INSTALL_PATH}
  fi
  ansible-galaxy collection install -r ${AVD_COLLECTION_PATH}/collections.yml
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
