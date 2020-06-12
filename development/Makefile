CONTAINER_NAME = avdteam/base
DOCKER_TAG = centos-8
CONTAINER = $(CONTAINER_NAME):$(DOCKER_TAG)
HOME_DIR = $(shell pwd)
HOME_DIR_DOCKER = '/home/docker'
UID = $(shell id -u)
GID = $(shell id -g)

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: run
run: ## Run ansible-avd container
	docker run --rm -it \
		-v $(HOME)/.ssh:$(HOME_DIR_DOCKER)/.ssh \
		-v $(HOME)/.gitconfig:$(HOME_DIR_DOCKER)/.gitconfig \
		-v $(HOME_DIR)/:/projects \
		-v /etc/hosts:/etc/hosts $(CONTAINER)

.PHONY: clean
clean: ## Remove avd image from local repository
	docker rmi $(CONTAINER_NAME):$(DOCKER_TAG)

.PHONY: build
build: ## [DEPRECATED] visit https://github.com/arista-netdevops-community/docker-avd-base to build image
	#docker build --no-cache -t $(CONTAINER) .
	echo ''; echo 'Deprecated command -- visit https://github.com/arista-netdevops-community/docker-avd-base to build image'; echo ''
