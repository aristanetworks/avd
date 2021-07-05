# Force BASH as default Makefile shell
# Required to use soruce
SHELL := /bin/bash
# AVD Shell container information
CONTAINER_NAME = avdteam/base
DOCKER_TAG ?= 3.6
CONTAINER = $(CONTAINER_NAME):$(DOCKER_TAG)
# Vscode container information
VSCODE_CONTAINER_NAME ?= avdteam/vscode
VSCODE_DOCKER_TAG ?= latest
VSCODE_CONTAINER = $(VSCODE_CONTAINER_NAME):$(VSCODE_DOCKER_TAG)
# VScode listen port exposed on host.
# To change it: make vscode VSCODE_PORT=<port to use>
VSCODE_PORT ?= 8080
# Path to compose stack -- should not be changed
COMPOSE_FILE ?= ansible-avd/development/docker-compose.yml
COMPOSE_ENV_FILE ?= ansible-avd/development/docker-stack.env
# Option to pass custom requirements and custom ansible version to provision in container
PIP_REQ ?=
ANSIBLE_VERSION ?=
# Current position
HOME_DIR = $(shell pwd)
# User ID to allow easy file share between container and host
UID ?= $(shell id -u)
# GID is unset by default as most of users are on Macos with a GID already used in container (20)
# If need to be set: make run GID=< GID of your user >
GID ?=
# User configured on container side
DOCKER_USER ?= avd
# Git Information to use with container to configure remote user
GIT_USERNAME ?= $(shell git config --get user.name)
GIT_EMAIL ?= $(shell git config --get user.email)
MUFFET_TIMEOUT ?= 60
# Container name to
WEBDOC_ID ?= avd

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

###############################################################################
# 			docker containers target									      #
###############################################################################

.PHONY: update
update: ## Get latest version of AVD runner and MKDOCs server
	docker pull $(CONTAINER_NAME):$(DOCKER_TAG) && \
	docker-compose -f ansible-avd/development/docker-compose.yml pull

.PHONY: run
run: ## Run ansible-avd container
	docker pull $(CONTAINER) && \
	docker run --rm -it \
		-e AVD_REQUIREMENTS=$(PIP_REQ) \
		-e AVD_ANSIBLE=$(ANSIBLE_VERSION) \
		-e AVD_UID=$(UID) \
		-e AVD_GID=$(GID) \
		-e AVD_GIT_USER="$(GIT_USERNAME)" \
		-e AVD_GIT_EMAIL="$(GIT_EMAIL)" \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-v $(HOME_DIR)/:/projects \
		-v $(HOME)/.ssh:/home/avd/.ssh/ \
		-v /etc/hosts:/etc/hosts $(CONTAINER)

.PHONY: vscode
vscode: ## Run a VSCODE container
	docker run --rm -it -d \
		-e AVD_GIT_USER="$(GIT_USERNAME)" \
		-e AVD_GIT_EMAIL="$(GIT_EMAIL)" \
		-v ${PWD}/:/home/avd/arista-ansible \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-v $(HOME)/.ssh:/home/avd/.ssh/ \
		-p $(VSCODE_PORT):8080 \
		$(VSCODE_CONTAINER)
	@echo "---------------"
	@echo " INFORMATION"
	@echo "---------------"
	@echo "VScode for AVD: http://127.0.0.1:$(VSCODE_PORT)/?folder=/home/avd/arista-ansible"

.PHONY: clean
clean: ## Remove avd image from local repository
	docker rmi $(CONTAINER_NAME):$(DOCKER_TAG)

.PHONY: start
start: ## Start docker compose stack to develop with AVD and CVP collection
	set -a && \
	source $(COMPOSE_ENV_FILE) && \
	docker-compose -f $(COMPOSE_FILE) pull && \
	docker-compose -f $(COMPOSE_FILE) up -d
	@echo "---------------"
	@echo " INFORMATION"
	@echo "---------------"
	@echo " * Webserver for AVD: http://127.0.0.1:8000"
	@echo " * Webserver for CVP: http://127.0.0.1:8001"
	@echo " * Ansible shell: make shell"
	@echo "---------------"
	docker-compose -f $(COMPOSE_FILE) exec -u $(DOCKER_USER) ansible zsh

.PHONY: stop
stop: ## Stop docker-compose stack
	docker-compose -f $(COMPOSE_FILE) kill && docker-compose -f $(COMPOSE_FILE) rm -f

.PHONY: shell
shell: ## Run a shell attached to ansible container
	docker-compose -f $(COMPOSE_FILE) exec -u $(DOCKER_USER) ansible zsh

.PHONY: ansible-upgrade
ansible-upgrade: ## Run a shell attached to ansible container
	docker-compose -f $(COMPOSE_FILE) exec -u $(DOCKER_USER) ansible pip install --user --upgrade ansible==$(ANSIBLE_VERSION)

.PHONY: restart
restart: stop start  ## Stop and Start docker-compose stack

.PHONY: reload
reload:  ## Reload HTTP container available in docker-compose stack
	docker-compose -f $(COMPOSE_FILE) restart webdoc_$(WEBDOC_ID)

.PHONY: reload-all
reload-all:  ## Reload HTTP container available in docker-compose stack
	docker-compose -f $(COMPOSE_FILE) restart webdoc_avd
	docker-compose -f $(COMPOSE_FILE) restart webdoc_cvp

###############################################################################
# 			Documentation target											  #
###############################################################################

.PHONY: check-404
check-404: check-avd-404 check-cvp-404 ## Check local 404 links in both AVD and CVP documentation

.PHONY: check-avd-404
check-avd-404: ## Check local 404 links for AVD documentation
	docker run --rm --network container:webdoc_avd raviqqe/muffet:1.5.7 http://127.0.0.1:8000 -e ".*fonts.gstatic.com.*" -e ".*edit.*" -f --limit-redirections=3 --timeout=$(MUFFET_TIMEOUT)

.PHONY: check-cvp-404
check-cvp-404: ## Check local 404 links for AVD documentation
	docker run --rm --network container:webdoc_cvp raviqqe/muffet:1.5.7 http://127.0.0.1:8000 -e ".*fonts.gstatic.com.*" -e ".*edit.*" -f --limit-redirections=3 --timeout=$(MUFFET_TIMEOUT)

###############################################################################
# 			Misc Target         											  #
###############################################################################

.PHONY: refresh
refresh: ## Refresh Makefile with new version from AVD
	cp ansible-avd/development/Makefile Makefile
	@echo "Makefile updated from AVD repository"
