ARG FROM_IMAGE
ARG FROM_VARIANT

FROM ${FROM_IMAGE}:${FROM_VARIANT}

ARG PYAVD_INSTALL_LOCATION
ARG ANSIBLE_INSTALL_LOCATION
ARG USERNAME

# Switch user to given USERNAME otherwise Ansible will be installed as root.
USER ${USERNAME}
ENV PATH=$PATH:/home/${USERNAME}/.local/bin
# Install Ansible AVD collection.
RUN pip install "pyavd[ansible] @ ${PYAVD_INSTALL_LOCATION}" \
    && ansible-galaxy collection install ${ANSIBLE_INSTALL_LOCATION} \
    # install community.general to support callback plugins in ansible.cfg, etc.
    && ansible-galaxy collection install community.general
