ARG FROM_IMAGE
ARG FROM_VARIANT

FROM ${FROM_IMAGE}:${FROM_VARIANT}

ARG USERNAME

# Add entrypoint script.
COPY ./entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
# Use ENTRYPOINT instead of CMD to ensure that entryscript is always executed.
ENTRYPOINT [ "/bin/entrypoint.sh" ]

# Switch user to given USERNAME otherwise Ansible will be installed as root.
USER ${USERNAME}
ENV PATH=$PATH:/home/${USERNAME}/.local/bin
