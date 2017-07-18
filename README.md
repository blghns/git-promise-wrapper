# git-promise-wrapper

## Install
## Windows
clone the repo in your C:/Users/username/git-promise-wrapper folder
copy the wrapper code to your .bash_profile, if you don't have it, you can create it under C:/Users/username/

## Linux
clone the repo in your home folder and paste the wrapper code to your .bash_aliases

### Wrapper code
```bash
promise_folder="git-promise-wrapper/"
original_git=`which git`
git() {
  if [ "$1" = "promise" ]; then
    shift
    python -m "${promise_folder}git-promise.py" "$@"
  elif [ "$1" = "commit" ]; then
  	shift
  	python -m "${promise_folder}git-commit.py" "$@"
  elif [ "$1" = "fulfill" ]; then
  	shift
  	python -m "{promise_folder}git-fulfill.py" "$@"
  else
    original_git "$@"
  fi
}
```

## Usage

```bash
git promise -f filename [name ...] [-l N [N ...]] [-b N-N [N-N ...]] branchname
```

* -l is for lines
* -b is for lines between: N-N: from-to inclusive.

