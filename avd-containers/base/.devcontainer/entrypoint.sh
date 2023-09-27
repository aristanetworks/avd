#!/bin/bash

# execute command from docker cli if any
if [ ${@+True} ]; then
  exec "$@"
# otherwise just enter sh or zsh
else
  if [ -f "/bin/zsh" ]; then
    exec zsh
  else
    exec sh
  fi
fi