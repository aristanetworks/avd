ARG FROM_IMAGE
ARG FROM_VARIANT

FROM ${FROM_IMAGE}:${FROM_VARIANT}

ARG USERNAME

# add entrypoint script
COPY ./entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
# use ENTRYPOINT instead of CMD to ensure that entryscript is always executed
ENTRYPOINT [ "/bin/entrypoint.sh" ]

# switch user to vscode otherwise Ansible will be installed as root
USER ${USERNAME}
ENV PATH=$PATH:/home/${USERNAME}/.local/bin
