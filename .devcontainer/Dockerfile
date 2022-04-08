FROM python:3.8-slim as BUILDER

WORKDIR /tmp

RUN useradd -md /home/avd -s /bin/zsh -u 1000 avd && \
    usermod -aG sudo avd && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    sudo \
    wget \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER avd

ENV PATH=$PATH:/home/avd/.local/bin

ADD --chown=avd https://raw.githubusercontent.com/aristanetworks/ansible-avd/devel/ansible_collections/arista/avd/requirements.txt /tmp/requirements.txt
ADD --chown=avd https://raw.githubusercontent.com/aristanetworks/ansible-avd/devel/ansible_collections/arista/avd/requirements-dev.txt /tmp/requirements-dev.txt

RUN pip3 install --upgrade --no-cache-dir pip && \
    pip3 install --disable-pip-version-check --no-cache-dir --user -r /tmp/requirements.txt && \
    pip3 install --disable-pip-version-check --no-cache-dir --user -r /tmp/requirements-dev.txt


FROM python:3.8-slim as BASE

LABEL maintainer="Arista Ansible Team <ansible@arista.com>"
LABEL com.example.version="1.0.4"
LABEL vendor1="Arista"
LABEL com.example.version.is-production="False"

#USER root

# Default ARG values
# Set term option
ARG TERM=xterm

ENV DEBIAN_FRONTEND noninteractive
ENV PROJECT_DIR /projects/

# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    make \
    wget \
    curl \
    less \
    git \
    zsh \
    vim \
    sshpass \
    git-extras \
    openssh-client \
    sudo && \
    apt-get clean && \
    curl -fsSL https://get.docker.com | sh && \
    useradd -md /home/avd -s /bin/zsh -u 1000 avd && \
    usermod -aG docker avd && \
    usermod -aG sudo avd && \
    echo "avd ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm -Rf /usr/share/doc && rm -Rf /usr/share/man

USER avd

# Copy python collection
COPY --from=BUILDER /home/avd/.local/ /home/avd/.local
ENV PATH=$PATH:/home/avd/.local/bin

# Copy gitconfig file
COPY gitconfig /home/avd/.gitconfig

# Install Oh My ZSH to provide improved shell
RUN wget --quiet https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true \
    && echo 'plugins=(ansible common-aliases safe-paste git jsontools history git-extras)' >> $HOME/.zshrc \
    && echo 'eval `ssh-agent -s`' >> $HOME/.zshrc \
    && echo 'export TERM=xterm' >>  $HOME/.zshrc \
    && echo "export LC_ALL=C.UTF-8" >> $HOME/.zshrc \
    && echo "export LANG=C.UTF-8" >> $HOME/.zshrc \
    && echo "export LC_ALL=C.UTF-8" >> $HOME/.zshrc \
    && echo "export LANG=C.UTF-8" >> $HOME/.zshrc \
    && echo 'export PATH=$PATH:/home/avd/.local/bin' >> $HOME/.zshrc

# Set default folder
WORKDIR /projects
VOLUME ["/projects"]

# Use ZSH as default shell with default oh-my-zsh theme
USER root
COPY entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
ENTRYPOINT [ "/bin/entrypoint.sh" ]
