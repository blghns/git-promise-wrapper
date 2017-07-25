#!/usr/bin/env bash
promise_folder="$HOME/git-promise-wrapper/"
original_git=`which git`
git() {
  if [ "$1" = "promise" ]; then
    shift
    python "${promise_folder}promise.py" "$@"
  elif [ "$1" = "commit" ]; then
  	shift
  	python "${promise_folder}commit.py" "$@"
  elif [ "$1" = "fulfill" ]; then
  	shift
  	python "${promise_folder}fulfill.py" "$@"
  else
    ${original_git} "$@"
  fi
}