FROM centos:7
LABEL maintainer="Arista Ansible Team <ansible@arista.com>"

ENV PS1='avd:\u% '

# Install necessary packages
# Install systemd -- See https://hub.docker.com/_/centos/
RUN yum -y update; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

# Install requirements.
RUN yum makecache fast \
 && yum -y install deltarpm epel-release initscripts \
 && yum -y update \
 && yum -y install \
    findutils \
    git \
    make \
    which \
    python3 \
    python3-pip \
    rpm-build \
    sudo \
 && yum clean all

# Create the /project directory and add it as a mountpoint
WORKDIR /ansible_avd
VOLUME ["/ansible_avd"]

# Install python modules required by the repo
ADD requirements.txt /tmp/requirements.txt
ADD requirements-dev.txt /tmp/requirements-dev.txt
RUN pip3 install -r /tmp/requirements-dev.txt
ARG ANSIBLE=2.9.2
RUN pip3 install ansible==$ANSIBLE

# Clean up
RUN yum clean all

# Make Python3 default
RUN ln -fs /usr/bin/python3 /usr/bin/python

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
