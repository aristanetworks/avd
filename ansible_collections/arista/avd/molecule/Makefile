
MOLECULE ?= eos_cli_config_gen

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

###############################################################################
# 			docker containers target									      #
###############################################################################

.PHONY: run
run: ## Execute molecule test. By default eos_cli_config_gen. Can be set with MOLECULE=
	cd .. && \
	molecule test --scenario-name $(MOLECULE)

.PHONY: refresh-facts
refresh-facts: ## Run all molecule scenario and commit changes
	cd .. && \
	molecule test --scenario-name eos_cli_config_gen && \
	molecule test --scenario-name evpn_underlay_ebgp_overlay_ebgp && \
	molecule test --scenario-name evpn_underlay_isis_overlay_ibgp && \
	molecule test --scenario-name evpn_underlay_ospf_overlay_ebgp && \
	molecule test --scenario-name upgrade_v1.0_to_v1.1 && \
	molecule test --scenario-name evpn_l3leaf_no_mlag && \
	cd molecule

.PHONY: commit-facts
commit-facts: ## Commit updated facts for CI
	git status --short
	git add .
	git commit --no-verify -m 'Update CI artifacts' ./

.PHONY: test-git-status
test-git-status: ## Run post molecule script to check git status
	sh ../../../../.github/git-repo-state-monitor.sh

.PHONY: sync-facts
sync-facts: refresh-facts commit-facts ## Refresh and commit CI artifacts
