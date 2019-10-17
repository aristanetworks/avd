CONTAINER_NAME = ansible_avd
CONTAINER_TAG = 0.0.1
CONTAINER = $(CONTAINER_NAME):$(CONTAINER_TAG)
HOME_DIR = $(shell pwd)
UID = $(shell id -u)
GID = $(shell id -g)
ANSIBLE_VERSION = 2.8.3

.PHONY: all
all:
	#docker build --no-cache -t $(CONTAINER) .
	docker build -t $(CONTAINER) . --build-arg UID=$(UID) --build-arg GID=$(GID) --build-arg ANSIBLE=$(ANSIBLE_VERSION)
	docker run -t -d --name $(CONTAINER_NAME) -v $(HOME_DIR)/:/ansible_avd $(CONTAINER)
	docker exec -it $(CONTAINER_NAME) /bin/bash

.PHONY: clean
clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)