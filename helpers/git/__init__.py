import helpers.__subprocess as sb


def branch_exists(branch_name):
    git_exists_with_name = "git rev-parse --verify --quiet " + branch_name
    output = sb.make_call(git_exists_with_name)
    if output == "":
        return False
    else:
        return True


def branch(branch_name):
    git_branch_with_name = "git branch " + branch_name
    sb.make_call(git_branch_with_name)


def add(file_name):
    git_add_with_name = "git add " + file_name
    sb.make_call(git_add_with_name)


def commit(commit_message):
    git_commit_with_message = "git commit -m".split() + ["\"" + commit_message + "\""]
    sb.make_call(git_commit_with_message)


def current_branch():
    git_branch_name = "git branch"
    name = next(branch_name for branch_name in sb.make_call(git_branch_name).split("\n") if branch_name[0] == "*")
    return name.split(" ")[1]
