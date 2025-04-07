#!/bin/bash
#
# Purpose: Molecule runner for github-action
# Author: @titom73
# Date: 2020-12-16
# Version: 1.1
# License: APACHE
# --------------------------------------

echo "Script running from ${PWD}"

# Set default values
INPUT_CHECK_GIT="${INPUT_CHECK_GIT:-true}"
INPUT_CHECK_GIT_ENFORCED="${INPUT_CHECK_GIT_ENFORCED:-true}"

if [ ${INPUT_CHECK_GIT} = "true" ]; then
    git config core.fileMode false
    echo "  * Run Git Verifier because CHECK_GIT is set to ${INPUT_CHECK_GIT}"
    # if git diff-index --quiet HEAD --; then
    GIT_STATUS="$(git status --porcelain)"
    if  [ "$?" -ne "0" ]; then
        echo "'git status --porcelain' failed to run - something is wrong"
        exit 1
    fi
    if [ -n "$GIT_STATUS" ]; then
        # Some changes
        echo 'Some changes'
        echo '------------'
        git --no-pager status --short
        echo ''
        echo 'Diffs are:'
        echo '------------'
        git --no-pager diff
        if [ ${INPUT_CHECK_GIT_ENFORCED} = "true" ]; then
            exit 1
        else
            exit 0
        fi
    else
        # No Changes
        echo '    - No change found after running Molecule'
        exit 0
    fi
    exit 0
else
    echo "  * Git verifier skipped as not set to true"
fi
