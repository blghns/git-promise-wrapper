import os
import subprocess


def branch_exists(branch_name):
    git_exists_with_name = "git rev-parse --verify --quiet " + branch_name
    output = __subprocess(git_exists_with_name)
    if output == "":
        return False
    else:
        return True


def branch(branch_name):
    git_branch_with_name = "git branch " + branch_name
    __subprocess(git_branch_with_name)


def add(file_name):
    git_add_with_name = "git add " + file_name
    __subprocess(git_add_with_name)


def commit(commit_message):
    git_commit_with_message = "git commit -m \"" + commit_message + "\""
    __subprocess(git_commit_with_message)


def __subprocess(process_string):
    process = subprocess.Popen(process_string,
                               cwd=os.getcwd(),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        raise error
    return output
