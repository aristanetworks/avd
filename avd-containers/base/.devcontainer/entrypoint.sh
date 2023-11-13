#!/bin/bash

# Execute command from docker cli if any.
if [ ${@+True} ]; then
  exec "$@"
# Otherwise just enter sh or zsh.
else
  if [ -f "/bin/zsh" ]; then
    exec zsh
  else
    exec sh
  fi
fi
