#!/bin/bash
#
# Purpose: Check Git status and exit with status code 0 if no change, 1 if change
# Author: @titom73
# Date: 2020-11-13
# Version: 0.1
# License: BSD
# --------------------------------------

GIT_CHANGES=$(git status --short | wc -l | awk -F " " "{print $1}")

if [[ $(echo ${GIT_CHANGES}| tr -d ' ') == *'0' ]]; then
    echo 'No change in GIT'
    exit 0
else
    echo 'Has unexpected changes'
    echo '----------------------'
    echo $(git status --short)
    exit 1
fi
