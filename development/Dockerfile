FROM centos:7
LABEL maintainer="Arista Ansible Team <ansible@arista.com>"

# Default ARG values
# Default Ansible Version
ARG ANSIBLE=UNSET
# Set some defaults that can be overridden in the build command
ARG UNAME=docker
ARG UPASS=docker
ARG UID=1000
ARG GID=1000

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
   zsh \
   wget \
   git-extras \
   && yum clean all

# Create the /project directory and add it as a mountpoint
WORKDIR /projects
VOLUME ["/projects"]

# Install python modules required by the repo
ADD requirements.txt /tmp/requirements.txt
ADD requirements-dev.txt /tmp/requirements-dev.txt
RUN pip3 install -r /tmp/requirements.txt \
   && pip3 install -r /tmp/requirements-dev.txt \
   && ANSIBLE_VERSION=$(pip3 freeze | grep -e 'ansible==' | awk -F '==' '{print $2}'); \
   if [ "$ANSIBLE" == "UNSET" ] || [ "$ANSIBLE_VERSION" == "$ANSIBLE" ]; \
   then echo "Correct ansible version"; \
   else pip3 install ansible==$ANSIBLE; fi

# Make Python3 default
RUN alternatives --install /usr/bin/python python /usr/bin/python2.7 50 \
   && alternatives --install /usr/bin/python python /usr/bin/python3.6 60

# Create the user/group that will be used in the container
# Create the sudo and UNAME groups and add the sudo group to sudoers
RUN echo "%sudo   ALL=(ALL:ALL) ALL" >> /etc/sudoers
# Create the user, add to the sudo group, and set the password to UPASS
RUN groupadd -r -g 1002 -o sudo \
   && groupadd -r -g $GID -o $UNAME \
   && useradd -r -m -u $UID -g $GID -G sudo -o -s /bin/bash -p $(perl -e 'print crypt($ENV{"UPASS"}, "salt")') $UNAME
# Switch to the new user for when the container is run
USER $UNAME

# Install Oh My ZSH to provide improved shell
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true \
   && echo 'plugins=(ansible common-aliases safe-paste git jsontools history git-extras)' >> $HOME/.zshrc \
   && echo 'eval `ssh-agent -s`' >> $HOME/.zshrc

# Use ZSH as default shell with default oh-my-zsh theme
CMD ["/bin/zsh"]
