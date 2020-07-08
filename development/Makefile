CONTAINER_NAME = avdteam/base
DOCKER_TAG = 3.6
CONTAINER = $(CONTAINER_NAME):$(DOCKER_TAG)
COMPOSE_FILE ?= ansible-avd/development/docker-compose.yml
PIP_REQ ?=
ANSIBLE_VERSION ?=
HOME_DIR = $(shell pwd)
UID = $(shell id -u)
GID = $(shell id -g)

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: update
update: ## Get latest version of AVD runner and MKDOCs server
	docker pull $(CONTAINER_NAME):$(DOCKER_TAG) && \
	docker-compose -f ansible-avd/development/docker-compose.yml pull

.PHONY: run
run: ## Run ansible-avd container
	docker run --rm -it \
		-e AVD_REQUIREMENTS=$(PIP_REQ) \
		-e AVD_ANSIBLE=$(ANSIBLE_VERSION) \
		-v $(HOME)/.gitconfig:$(HOME_DIR_DOCKER)/.gitconfig \
		-v $(HOME_DIR)/:/projects \
		-v /etc/hosts:/etc/hosts $(CONTAINER)

.PHONY: clean
clean: ## Remove avd image from local repository
	docker rmi $(CONTAINER_NAME):$(DOCKER_TAG)

.PHONY: build
build: ## [DEPRECATED] visit https://github.com/arista-netdevops-community/docker-avd-base to build image
	@echo "!!!!!!!!"
	@echo "Deprecated command -- visit https://github.com/arista-netdevops-community/docker-avd-base to build image"
	@echo "!!!!!!!!"

.PHONY: dev-start
dev-start: ## Start docker compose stack to develop with AVD and CVP collection
	docker-compose -f $(COMPOSE_FILE) up -d
	@echo "---------------"
	@echo " INFORMATION"
	@echo "---------------"
	@echo " * Webserver for AVD: http://127.0.0.1:8000"
	@echo " * Webserver for CVP: http://127.0.0.1:8001"
	@echo " * Ansible shell: make dev-run"
	@echo "---------------"
	docker-compose -f $(COMPOSE_FILE) exec ansible zsh

.PHONY: dev-stop
dev-stop: ## Stop docker compose stack and remove containers
	docker-compose -f $(COMPOSE_FILE) kill && docker-compose -f $(COMPOSE_FILE) rm -f

.PHONY: dev-run
dev-run: ## Run a shell attached to ansible container
	docker-compose -f $(COMPOSE_FILE) exec ansible zsh

.PHONY: shell
shell: ## Run a shell attached to ansible container
	docker-compose -f $(COMPOSE_FILE) exec ansible zsh

.PHONY: ansible-upgrade
ansible-upgrade: ## Run a shell attached to ansible container
	docker-compose -f $(COMPOSE_FILE) exec ansible pip install ansible==$(ANSIBLE_VERSION)

.PHONY: dev-reload
dev-reload: dev-stop dev-start  ## Stop and Start docker-compose stack
