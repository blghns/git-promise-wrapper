promise_folder="$HOME/git-promise-wrapper/"
original_git=`which git`
git() {
  if [ "$1" = "promise" ]; then
    shift
    python "${promise_folder}git-promise.py" "$@"
  elif [ "$1" = "commit" ]; then
  	shift
  	python "${promise_folder}git-commit.py" "$@"
  elif [ "$1" = "fulfill" ]; then
  	shift
  	python "${promise_folder}git-fulfill.py" "$@"
  else
    $original_git "$@"
  fi
}