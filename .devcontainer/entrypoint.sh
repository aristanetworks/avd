#!/bin/bash

DOCKER_SOCKET=/var/run/docker.sock
DOCKER_GROUP=docker
USER=avd
HOME_AVD=/home/avd/

# Install specific requirement file
if [ ! -z "${AVD_REQUIREMENTS}" ]; then
  if [ -f ${AVD_REQUIREMENTS} ]; then
    echo "Install new requirements from ${AVD_REQUIREMENTS}"
    sudo -H -u ${USER} pip3 install --upgrade --user -r ${AVD_REQUIREMENTS}
  else
    echo "Requirement file not found, skipping..."
  fi
fi

# Install specific ANSIBLE version
if [ ! -z "${AVD_ANSIBLE}" ]; then
    echo "Install ansible with version ${AVD_ANSIBLE}"
    # Required for migration from 2.9 to 2.10
    sudo -H -u ${USER} pip3 uninstall -y ansible
    sudo -H -u ${USER} pip3 install --upgrade --user ansible==${AVD_ANSIBLE}
fi

# Reconfigure AVD User id if set by user
if [ ! -z "${AVD_UID}" ] && [ "${AVD_UID}" != "`id -u avd`" ] ; then
  echo -n "Update uid for user avd with ${AVD_UID}"
  # Command can take time as it also change permission within the python lib
  usermod -u ${AVD_UID} avd
  # sed -i -e "s/^avd:\([^:]*\):[0-9]*:\([0-9]*\)/avd:\1:${AVD_UID}:\2/" /etc/passwd
  echo "... updated"
else
  echo "skipping UID configuration"
fi

if [ -n "${AVD_GID}" ] && [ "${AVD_GID}" != "`id -g avd`" ] ; then
  echo -n "Update gid for group avd with ${AVD_GID}"
  # Command can take time as it also change permission within the python lib
  usermod -u ${AVD_UID} avd
  # sed -i -e "s/^avd:\([^:]*\):[0-9]*/avd:\1:${AVD_GID}/" /etc/group
  # sed -i -e "s/^avd:\([^:]*\):\([0-9]*\):[0-9]*/avd:\1:\2:${AVD_GID}/" /etc/passwd
  echo "... updated"
else
  echo "skipping GID configuration"
fi

# Update gitconfig with username and email
if [ -n "${AVD_GIT_USER}" ]; then
  echo "Update gitconfig with ${AVD_GIT_USER}"
  sed -i "s/USERNAME/${AVD_GIT_USER}/g" ${HOME_AVD}/.gitconfig
else
  echo "Update gitconfig with default username"
  sed -i "s/USERNAME/AVD Base USER/g" ${HOME_AVD}/.gitconfig
fi
if [ -n "${AVD_GIT_EMAIL}" ]; then
  echo "Update gitconfig with ${AVD_GIT_EMAIL}"
  sed -i "s/USER_EMAIL/${AVD_GIT_EMAIL}/g" ${HOME_AVD}/.gitconfig
else
  echo "Update gitconfig with default email"
  sed -i "s/USER_EMAIL/avd-base@arista.com/g" ${HOME_AVD}/.gitconfig
fi

if [ -S ${DOCKER_SOCKET} ]; then
    sudo chmod 666 /var/run/docker.sock &>/dev/null
fi

export PATH=$PATH:/home/avd/.local/bin
export LC_ALL=C.UTF-8

cd /projects/

# execute command from docker cli if any
if [ ${@+True} ]; then
  sudo -H -u ${USER} "$@"
# otherwise just enter zsh
else
  su - avd -c "cd /projects && export ZSH_DISABLE_COMPFIX=true && /bin/zsh"
fi
