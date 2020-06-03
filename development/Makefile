CONTAINER_NAME = ansible_avd
ANSIBLE_VERSION = 2.9.6
CONTAINER = $(CONTAINER_NAME):$(ANSIBLE_VERSION)
HOME_DIR = $(shell pwd)
HOME_DIR_DOCKER = '/home/docker'
UID = $(shell id -u)
GID = $(shell id -g)

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build a new image of avd container
	#docker build --no-cache -t $(CONTAINER) .
	docker build -t $(CONTAINER) . --build-arg UID=$(UID) --build-arg GID=$(GID)

.PHONY: run
run: ## Run ansible-avd container
	docker run --rm -it --name $(CONTAINER_NAME)_$(ANSIBLE_VERSION) \
		-v $(HOME)/.ssh:$(HOME_DIR_DOCKER)/.ssh \
		-v $(HOME)/.gitconfig:$(HOME_DIR_DOCKER)/.gitconfig \
		-v $(HOME_DIR)/:/projects \
		-v /etc/hosts:/etc/hosts $(CONTAINER)

.PHONY: clean
clean: ## Remove avd image from local repository
	docker rmi $(CONTAINER_NAME):$(ANSIBLE_VERSION)
