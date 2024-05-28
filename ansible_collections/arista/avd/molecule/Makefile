
MOLECULE ?= eos_cli_config_gen
ANSIBLE_OPTIONS ?=

.PHONY: help
help: ## Display help message.
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

###############################################################################
# 			Molecule Execution and Git Helpers  						      #
###############################################################################

.PHONY: test
test: ## Execute molecule "test" sequence. Specify scenario name (default: eos_cli_config_gen) with MOLECULE= and Ansible options (default none) with ANSIBLE_OPTIONS=.
	cd .. && \
	molecule test --scenario-name $(MOLECULE) -- $(ANSIBLE_OPTIONS)

.PHONY: converge
converge: ## Execute molecule "converge" sequence. Specify scenario name (default: eos_cli_config_gen) with MOLECULE= and Ansible options (default none) with ANSIBLE_OPTIONS=.
	cd .. && \
	molecule converge --scenario-name $(MOLECULE) -- $(ANSIBLE_OPTIONS)

.PHONY: refresh-facts
refresh-facts: ## Run all "eos_designs" and "eos_cli_config_gen" molecule scenarios.
	@while read -r MOLECULE_SCENARIO; do \
		if [ -d "$$MOLECULE_SCENARIO" ]; then\
			echo "Run scenario for "$$MOLECULE_SCENARIO && \
			cd .. ; \
			molecule converge --scenario-name $$MOLECULE_SCENARIO -- $(ANSIBLE_OPTIONS); \
			cd ./molecule ; \
		fi \
	done <MOLECULE_SCENARIOS.txt

.PHONY: commit-facts
commit-facts: ## Commit updated facts for CI with the following message: 'CI(molecule): Update Molecule artifacts'.
	git status --short
	git add .
	git commit --no-verify -m 'CI(molecule): Update Molecule artifacts' ./

.PHONY: sync-facts
sync-facts: refresh-facts commit-facts ## Run refresh-facts and commit-facts to update all CI artifacts.

.PHONY: cleanup
cleanup: ## Execute molecule "cleanup" sequence on all scenarios located in the molecule directory.
	@for MOLECULE_SCENARIO in * ; do \
        if [ -d "$$MOLECULE_SCENARIO" ]; then\
        echo "Run scenario for "$$MOLECULE_SCENARIO && \
		cd .. ; \
		molecule cleanup --scenario-name $$MOLECULE_SCENARIO -- $(ANSIBLE_OPTIONS); \
		cd ./molecule ; \
        fi \
    done
