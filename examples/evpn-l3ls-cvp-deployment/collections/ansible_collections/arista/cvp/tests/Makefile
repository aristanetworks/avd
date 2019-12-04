# option to run ansible-test sanity: must be either venv or docker (default is docker)
ANSIBLE_TARGET ?= cvp_2018
ANSIBLE_TAG ?= configlet

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: run
run: ## Run set of testing from playbook.build.topology.yml
	ansible-playbook playbook.build.topology.yml --limit ${ANSIBLE_TARGET}

.PHONY: unit
unit: ## Run Unit test for one of the list container, configlet, device using ANSIBLE_TAG
	ansible-playbook playbook.build.topology.yml --tags ${ANSIBLE_TAG} --limit ${ANSIBLE_TARGET}

.PHONY: reset
reset: ## Reset topology with playbook.reset.topology.yml
	ansible-playbook playbook.reset.topology.yml --limit ${ANSIBLE_TARGET}