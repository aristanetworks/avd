FROM centos:8
LABEL maintainer="Arista Ansible Team <ansible@arista.com>"

ENV PS1='avd:\u% '

# Install necessary packages
RUN dnf -y install \
    findutils \
    git \
    make \
    python3-pip \
    rpm-build \
    sudo

# Create the /project directory and add it as a mountpoint
WORKDIR /ansible_avd
VOLUME ["/ansible_avd"]

# Install python modules required by the repo
RUN pip3 install --upgrade pip
ADD requirements.txt /tmp/requirements.txt
ADD requirements-dev.txt /tmp/requirements-dev.txt
RUN pip3 install --trusted-host pypi.python.org -r /tmp/requirements-dev.txt
ARG ANSIBLE=2.8.5
RUN pip3 install ansible==$ANSIBLE

# Clean up
RUN dnf clean all

# Create the user/group that will be used in the container
# Set some defaults that can be overridden in the build command
ARG UNAME=docker
ARG UPASS=docker
ARG UID
ARG GID
# Create the sudo and UNAME groups and add the sudo group to sudoers
RUN echo "%sudo   ALL=(ALL:ALL) ALL" >> /etc/sudoers
RUN groupadd -r -g 1002 -o sudo
RUN groupadd -r -g $GID -o $UNAME
# Create the user, add to the sudo group, and set the password to UPASS
RUN useradd -r -m -u $UID -g $GID -G sudo -o -s /bin/bash -p $(perl -e 'print crypt($ENV{"UPASS"}, "salt")') $UNAME
# Switch to the new user for when the container is run
USER $UNAME

CMD ["/bin/sh"]
