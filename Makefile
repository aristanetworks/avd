CURRENT_DIR = $(shell pwd)
# option to run ansible-test sanity: must be either venv or docker (default is docker)
ANSIBLE_TEST_MODE ?= docker
# Root path for MKDOCS content
WEBDOC_BUILD = ansible_collections/arista/avd/docs/_build
MUFFET_TIMEOUT ?= 60

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#########################################
# Ansible Collection actions		#
#########################################
.PHONY: collection-build
collection-build: ## Build arista.cvp collection locally
	ansible-galaxy collection build --force ansible_collections/arista/avd

#########################################
# pyavd actions                 #
#########################################
.PHONY: pyavd-build
pyavd-build: ## Build pyavd python package locally
	cd python-avd && $(MAKE) clean build

.PHONY: pyavd-test
pyavd-test: ## Test pyavd python code
	cd python-avd && $(MAKE) clean && tox -r

.PHONY: pyavd-publish
pyavd-publish: ## Build and publish pyavd python package
	cd python-avd && $(MAKE) clean build publish

#########################################
# Code Validation using ansible-test 	#
#########################################

.PHONY: sanity
sanity: sanity-info sanity-lint sanity-import ## Run ansible-test sanity validation.

.PHONY: sanity-info
sanity-info: ## Show information about ansible-test
	cd ansible_collections/arista/avd/ ; ansible-test env

.PHONY: sanity-lint
sanity-lint: ## Run ansible-test sanity for code sanity
	cd ansible_collections/arista/avd/ ; \
	ansible-test sanity --requirements --$(ANSIBLE_TEST_MODE) --skip-test import

.PHONY: sanity-import
sanity-import: ## Run ansible-test sanity for code import
	cd ansible_collections/arista/avd/ ; \
	ansible-test sanity --requirements --$(ANSIBLE_TEST_MODE) --test import

.PHONY: galaxy-importer
galaxy-importer:  ## Run galaxy importer tests
	rm -f *.tar.gz && \
	ansible-galaxy collection build --force ansible_collections/arista/avd && \
	python -m galaxy_importer.main *.tar.gz

#############################################
# Run unit test cases using ansible-test    #
#############################################

.PHONY: unit-tests
unit-tests: ## Run unit test cases using ansible-test
	cd ansible_collections/arista/avd/ ; \
	ansible-test units --requirements --$(ANSIBLE_TEST_MODE) -vv

###################################################
# Run integration test cases using ansible-test   #
###################################################

.PHONY: integration-tests
integration-tests: ## Run integration test cases using ansible-test
	cd ansible_collections/arista/avd/ ; \
	ansible-test integration --requirements --$(ANSIBLE_TEST_MODE)

#########################################
# Documentation actions					#
#########################################
.PHONY: webdoc-up
webdoc-up: ## Build documentation to view
	docker-compose -f development/docker-compose.yml up -d webdoc_avd ; \
	docker exec -it webdoc_avd sh

.PHONY: webdoc-down
webdoc-down: ## shutdown docs
	docker-compose -f development/docker-compose.yml down

.PHONY: webdoc-logs
webdoc-logs: ## View logs
	docker logs webdoc_avd

.PHONY: check-avd-404
check-avd-404: ## Check local 404 links for AVD documentation
	docker run --rm --network container:webdoc_avd raviqqe/muffet:2.6.1 http://127.0.0.1:8000/ -e ".*fonts.googleapis.com.*" -e ".*fonts.gstatic.com.*" -e ".*tools.ietf.org.*" -e ".*edit.*" -e ".*docs.github.com.*" -e "twitter.com" -f --max-redirections=3 --timeout=$(MUFFET_TIMEOUT) --rate-limit=1
