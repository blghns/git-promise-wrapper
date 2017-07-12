# git-promise-wrapper

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

