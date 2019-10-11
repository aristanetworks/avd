CONTAINER_NAME = ansible_avd
CONTAINER_TAG = 0.0.1
CONTAINER = $(CONTAINER_NAME):$(CONTAINER_TAG)
HOME_DIR = $(shell pwd)

.PHONY: all
all:
	#docker build --no-cache -t $(CONTAINER) .
	docker build -t $(CONTAINER) .
	docker run -t -d --name $(CONTAINER_NAME) -v $(HOME_DIR)/:/usr/ansible_avd $(CONTAINER)
	docker exec -it $(CONTAINER_NAME) /bin/bash

.PHONY: clean
clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)