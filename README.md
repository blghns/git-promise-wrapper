# git-promise-wrapper

## Install
## Linux
download git-promise.py to your home folder and add following code to your .bash_aliases
```bash
git() {
  if [ "$1" = "promise" ]; then
    shift
    python -m git-promise.py "$@"
  else
    /usr/bin/git "$@"
  fi
}
```

## Usage

```bash
git promise -f filename [name ...] [-l N [N ...]] [-b N-N [N-N ...]] branchname
```

* -l is for lines
* -b is for lines between: N-N: from-to inclusive.

