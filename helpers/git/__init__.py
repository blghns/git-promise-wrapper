import helpers.__subprocess as sb
import subprocess
import shlex




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

def current_branch():
    command = "git branch"
    name = next(branch_name for branch_name in sb.call(command).split("\n") if branch_name[0] == "*")
    return name.split(" ")[1]

def is_staged(file_name):
    command = "git diff --name-only --cached"
    staged_files =  sb.call(command).split()
    if file_name in staged_files:
        return True
    return False

def get_lines_edited(promise_commit_hash, file_name):
    command = "ls"
    print sb.call(command)
    command = "git diff --unified=0 %s %s" % (promise_commit_hash, file_name)
    proc1 = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(shlex.split("grep '@@'"), stdin=proc1.stdout, stdout=subprocess.PIPE)
    proc3 = subprocess.Popen(shlex.split("awk '{print $2}'"), stdin=proc2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc4 = subprocess.Popen(shlex.split("tr -d -"), stdin=proc3.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc4.communicate()
    proc1.stdout.close()
    proc2.stdout.close()
    proc3.stdout.close()
    return proc4.split()
