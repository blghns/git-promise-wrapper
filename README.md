# git-promise-wrapper

### Checkout the gui for creating promises
https://github.com/seymourr1/Git-Vow-Electron

## Video
[![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/blghns/git-promise-wrapper/master/images/git-promise-tutorial.png)](https://drive.google.com/open?id=0BxXnQihREm1PVmhsRk41NnluLU0)

## Install
## Windows
clone the repo in your C:/Users/username/git-promise-wrapper folder
copy the wrapper code to your .bash_profile, if you don't have it, you can create it under C:/Users/username/

## Linux
clone the repo in your home folder and paste the wrapper code to your .bash_aliases

### Wrapper code
```bash
. ~/git-promise-wrapper/promise_wrapper.sh
```

## Usage

### git promise

```bash
git promise -f filename [name ...] [-l N [N ...]] [-b N-N [N-N ...]] branchname
```

* -l is for lines
* -b is for lines between: N-N: from-to inclusive.

### git fulfill
```bash
git fulfill branchname --remove
```
merges the promised branch into the parent branch

* checks the promise by default.
* if --remove is included, promise is removed.
