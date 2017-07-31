import helpers.__subprocess as sb


def current_hash():
    hash_command = "git rev-parse HEAD"
    hash_str = sb.call(hash_command).split("\n")[0]
    return hash_str


def branch_exists(branch_name):
    git_exists_with_name = "git rev-parse --verify --quiet " + branch_name
    output = sb.call(git_exists_with_name)
    if output == "":
        return False
    else:
        return True


def branch(branch_name):
    command = "git branch " + branch_name
    sb.call(command)


def init():
    command = "git init"
    sb.call(command)


def add(file_name):
    command = "git add " + file_name
    sb.call(command)


def commit(commit_message):
    command = "git commit -m".split() + ["\"" + commit_message + "\""]
    sb.call(command)


def commit_with_args(args):
    command = ["git"] + ["commit"] + args
    sb.call(command)


def current_branch():
    command = "git branch"
    name = next(branch_name for branch_name in sb.call(command).split("\n") if branch_name[0] == "*")
    return name.split(" ")[1]


def is_staged(file_name):
    command = "git diff --name-only --cached"
    staged_files = sb.call(command).split()
    if file_name in staged_files:
        return True
    return False


def get_lines_edited(promise_commit_hash, file_name):
    command = "git diff --staged --unified=0 %s %s" % (promise_commit_hash, file_name)
    output = sb.call(command).split('\n')
    a1 = [el.split() for el in output if el[:2] == "@@"]
    a2 = [el[1][1:] for el in a1]
    return a2


def merge(branch_name):
    command = "git merge " + branch_name
    sb.call(command)


def delete_branch(branch_name):
    command ="git branch -D " + branch_name
    sb.call(branch)
