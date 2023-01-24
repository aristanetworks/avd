ARG VARIANT="3.8-v2.0"
FROM avdteam/base:${VARIANT}

WORKDIR /workspace
VOLUME ["/workspace"]

USER avd
# ENV DOCKER_HOST=unix:///var/run/user/1000/docker.sock
ENV DOCKER_HOST=unix:///var/run/docker.sock
RUN rm -f /home/avd/.gitconfig
