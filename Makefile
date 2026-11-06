CURRENT_DIR = $(shell pwd)
# option to run ansible-test sanity: must be either venv or docker (default is venv)
ANSIBLE_TEST_MODE ?= venv
MUFFET_TIMEOUT ?= 60

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#########################################
# Ansible Collection actions            #
#########################################
.PHONY: collection-build
collection-build: ## Build arista.avd collection locally.
	ansible-galaxy collection build --force ansible_collections/arista/avd

#########################################
# pyavd actions                         #
#########################################
.PHONY: pyavd-build
pyavd-build: ## Build PyAVD Python package locally.
	cd python-avd && $(MAKE) build

.PHONY: uv-pyavd-build
uv-pyavd-build: ## Build PyAVD Python package locally.
	cd python-avd && $(MAKE) uv-build

.PHONY: pyavd-test
pyavd-test: ## Test PyAVD Python code with tox.
	tox run -r

.PHONY: pyavd-publish
pyavd-publish: ## Build and publish PyAVD Python package.
	cd python-avd && $(MAKE) build publish

.PHONY: uv-pyavd-publish
uv-pyavd-publish: ## Build and publish PyAVD Python package.
	cd python-avd && $(MAKE) uv-build uv-publish

.PHONY: pyavd-install
pyavd-install: pyavd-build ## Build and install PyAVD Python package.
	pip install python-avd/dist/* --force-reinstall

# The editable_mode=compat is required for pylance to pick up the editable install.
.PHONY: pyavd-editable-install
pyavd-editable-install: ## Build and install PyAVD as editable
	pip install -e python-avd --config-settings editable_mode=compat --force-reinstall

.PHONY: uv-pyavd-install
uv-pyavd-install: pyavd-build ## Build and install PyAVD Python package.
	uv pip install python-avd/dist/* --force-reinstall

# The editable_mode=compat is required for pylance to pick up the editable install.
.PHONY: uv-pyavd-editable-install
uv-pyavd-editable-install: ## Build and install PyAVD as editable
	uv pip install -e python-avd --config-settings editable_mode=compat --force-reinstall

#########################################
# Dependency lock files                 #
#########################################

.PHONY: lock
lock: ## Update uv lock files.
	uv lock --project . --python 3.10 --fork-strategy requires-python
	uv lock --project python-avd --python 3.10 --fork-strategy requires-python

.PHONY: lock-check-exists
lock-check-exists: ## Check uv lock files exist.
	uv lock --project . --python 3.10 --fork-strategy requires-python --check-exists
	uv lock --project python-avd --python 3.10 --fork-strategy requires-python --check-exists

.PHONY: lock-check
lock-check: ## Check uv lock files are fresh.
	uv lock --project . --python 3.10 --fork-strategy requires-python --check
	uv lock --project python-avd --python 3.10 --fork-strategy requires-python --check

#########################################
# Code Validation using ansible-test 	#
#########################################

.PHONY: sanity
sanity: sanity-info sanity-lint sanity-import ## Run ansible-test sanity validation.

.PHONY: sanity-info
sanity-info: ## Show information about ansible-test.
	cd ansible_collections/arista/avd/ ; ansible-test env

.PHONY: sanity-lint
sanity-lint: ## Run ansible-test sanity for code sanity. Specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
	cd ansible_collections/arista/avd/ ; \
	ansible-test sanity --requirements --$(ANSIBLE_TEST_MODE) --skip-test import

.PHONY: sanity-import
sanity-import: ## Run ansible-test sanity for code import. Specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
	cd ansible_collections/arista/avd/ ; \
	ansible-test sanity --requirements --$(ANSIBLE_TEST_MODE) --test import

.PHONY: galaxy-importer
galaxy-importer:  ## Run galaxy importer tests.
	rm -f *.tar.gz && \
	ansible-galaxy collection build --force ansible_collections/arista/avd && \
	python -m galaxy_importer.main *.tar.gz

#############################################
# Run unit test cases using ansible-test    #
#############################################

.PHONY: unit-tests
unit-tests: ## Run unit test cases using ansible-test. Specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
	cd ansible_collections/arista/avd/ ; \
	ansible-test units --requirements --$(ANSIBLE_TEST_MODE) -vv

###################################################
# Run integration test cases using ansible-test   #
###################################################

.PHONY: integration-tests
integration-tests: ## Run integration test cases using ansible-test. Specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
	cd ansible_collections/arista/avd/ ; \
	ansible-test integration --requirements --$(ANSIBLE_TEST_MODE)

################
# Bump version #
################

.PHONY: bump-dev
bump-dev: ## Bump dev release. 6.0.0-dev0 -> 6.0.0-dev1
	bump-my-version bump pre_n

.PHONY: bump-release
bump-release: ## Bump from dev to final release. 6.2.0-dev2 -> 6.2.0
	bump-my-version bump pre_l

.PHONY: bump-minor
bump-minor: ## Bump minor release. 6.1.4 -> 6.2.0-dev0
	bump-my-version bump minor

.PHONY: bump-major
bump-major: ## Bump major release. 6.2.4 -> 7.0.0-dev0
	bump-my-version bump major

.PHONY: bump-patch
bump-patch: ## Bump patch release. 6.2.4 -> 6.2.5-dev0
	bump-my-version bump patch

####################
# Random shortcuts #
####################

.PHONY: config-diff
config-diff: ## Run git diff comparing molecule configs with 'devel' using our special config diff ignoring reordering of config lines.
	@GIT_EXTERNAL_DIFF=development/compare.py git diff devel --ext-diff -- **/configs/*.cfg

#########################################
# Documentation                         #
#########################################

SCHEMA_EXPLORER_SRC   = tools/schema-explorer
SCHEMA_EXPLORER_BUILD = tools/schema-explorer/build

.PHONY: schema-explorer-build
schema-explorer-build: ## Build the Schema Explorer (static assets + SQLite) into tools/schema-explorer/build/ for local inspection.
	uv run --group doc python $(SCHEMA_EXPLORER_SRC)/generate.py \
		--avd-root . --site-dir $(SCHEMA_EXPLORER_BUILD)

.PHONY: docs-serve
docs-serve: ## Run `mkdocs serve` on http://127.0.0.1:8000. The Schema Explorer hook builds its own cache outside the watched repo tree.
	uv run --group doc mkdocs serve --dev-addr=127.0.0.1:8000 -f mkdocs.yml

.PHONY: docs-serve-docker
docs-serve-docker: ## Same as docs-serve, but inside the webdoc_avd container (no host deps required).
	docker compose -f development/docker-compose.yml up


##########################
# Run End-to-end tests #
##########################

.PHONY: e2e
e2e: ## Run end-to-end tests, regenerating all outputs and capturing errors to files.
	@uv run --no-project tools/e2e-test-avd.py $$(find . -type f -name e2e-test.toml -print | sort)

# Find all e2e-test.toml files recursively
# NOTE we only look under ansible_collections for now to avoid other local paths which might contain such files.
ALL_CONFIGS := $(shell find ansible_collections -type f -name e2e-test.toml -print)

# For each config, extract the last 2 directories and prefix with "e2e-"
TARGET_MAPPINGS := $(shell for f in $(ALL_CONFIGS); do \
    dir=$$(dirname "$$f"); \
    last2=$$(echo "$$dir" | awk -F/ '{print $$(NF-1)"/"$$NF}'); \
    echo "e2e-$$last2:$$f"; \
done)

# 3. Extract just the target names to register them as .PHONY targets
SHORT_TARGETS := $(foreach pair,$(TARGET_MAPPINGS),$(word 1,$(subst :, ,$(pair))))
.PHONY: $(SHORT_TARGETS)

$(SHORT_TARGETS):
	@$(eval MATCHED_PAIRS := $(filter $@%,$(TARGET_MAPPINGS))) \
	if [ -z "$(MATCHED_PAIRS)" ]; then \
		echo "Error: Target $@ does not match any configurations."; \
		exit 1; \
	fi; \
	$(eval ACTUAL_FILES := $(foreach pair,$(MATCHED_PAIRS),$(word 2,$(subst :, ,$(pair))))) \
	uv run --no-project tools/e2e-test-avd.py $(ACTUAL_FILES)
