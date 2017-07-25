import helpers.__subprocess as sb


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


def current_branch():
    command = "git branch"
    name = next(branch_name for branch_name in sb.call(command).split("\n") if branch_name[0] == "*")
    return name.split(" ")[1]
