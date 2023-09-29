ARG FROM_IMAGE
ARG FROM_VARIANT

FROM ${FROM_IMAGE}:${FROM_VARIANT}

ARG ANSIBLE_CORE_VERSION
ARG ANSIBLE_INSTALL_LOCATION
ARG USERNAME

# switch user to vscode otherwise Ansible will be installed as root
USER ${USERNAME}
ENV PATH=$PATH:/home/${USERNAME}/.local/bin
# install Ansible AVD collection
RUN pip3 install "${ANSIBLE_CORE_VERSION}" \
    && ansible-galaxy collection install ${ANSIBLE_INSTALL_LOCATION} \
    && pip3 install -r /home/${USERNAME}/.ansible/collections/ansible_collections/arista/avd/requirements.txt
