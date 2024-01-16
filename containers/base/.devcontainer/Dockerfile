ARG FROM_IMAGE
ARG FROM_VARIANT
FROM ${FROM_IMAGE}:${FROM_VARIANT}

# Install essential tools.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    make \
    git \
    # xz-utils required for docker import to work
    xz-utils \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Add entrypoint script.
COPY ./entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
# Use ENTRYPOINT instead of CMD to ensure that entryscript is always executed.
ENTRYPOINT [ "/bin/entrypoint.sh" ]
