FROM centos:7

LABEL maintainer="ansible@arista.com"

WORKDIR /usr/ansible-avd


RUN yum makecache fast \
 && yum -y install deltarpm epel-release initscripts \
 && yum -y update \
 && yum -y install \
      sudo \
      which \
      python-pip \
      python-devel \
      @development \
 && yum clean all

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#VOLUME ["/usr/ansible-avd"]

# Create the user/group that will be used in the container
# Set some defaults that can be overridden in the build command
#ARG UNAME=docker
#ARG UPASS=docker
#ARG UID
#ARG GID
# Create the sudo and UNAME groups and add the sudo group to sudoers
#RUN echo "%sudo   ALL=(ALL:ALL) ALL" >> /etc/sudoers
#RUN groupadd -r -g 1002 -o sudo
#RUN groupadd -r -g $GID -o $UNAME
# Create the user, add to the sudo group, and set the password to UPASS
#RUN useradd -r -m -u $UID -g $GID -G sudo -o -s /bin/bash -p $(perl -e 'print crypt($ENV{"UPASS"}, "salt")') $UNAME
# Switch to the new user for when the container is run
#USER $UNAME

CMD ["/bin/sh"]

# For initial container debugging, it can start a shell
# WORKDIR /usr/share/ztpserver
# CMD [ "python", "./myscript.py" ]
# CMD sh

# docker run -it -rm --name ansible-avd --volume `pwd`:/home/ansible-avd ansible-avd:0.0.1
# NOTE: the '-d', above, gets passed to the ztps process
#ENTRYPOINT /usr/local/bin/ztps